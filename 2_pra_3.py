#!/usr/bin/env python3

'''
This module scrapes entries from StudentNews.  Each entry is a dictionary containing 'from_addr', 'from_name', 'subject', and 'entry'
'''

import requests
from bs4 import BeautifulSoup, NavigableString, Comment
import re
import time
from datetime import datetime
import json

def report(text):
    print(datetime.now(), ' | ', text)

def get_soup(url=''):
    'return the BeautifulSoup of a path at StudentNews. Does retries.'
    try:
        html = requests.get("http://www.calvin.edu/archive/student-news/" + url).content
    except Exception as e:
        report(e)
        time.sleep(10)
        return get_soup(url)
    return BeautifulSoup(html, "lxml") #lxml doesn't allow nested <p> tags, so it closes them when necessary.  This is important.

## find all message_urls
def get_month_urls():
    soup = get_soup()
    return (a.attrs['href'] for a in soup.select('a'))
def get_message_urls(month):
    report('getting month {}'.format(month))
    soup = get_soup(month)
    anchors = soup.select('div.messages-list a[href]')
    return (month+a.attrs['href'] for a in anchors)
def get_all_message_urls():
    return (url for month in get_month_urls() for url in get_message_urls(month))

## parse each message into entries
def get_text_from_soup(soup):
    return ' '.join(child for child in soup.children if isinstance(child, NavigableString) and not isinstance(child, Comment)).replace('\n \n', '\n')
def parse_message(url):
    soup = get_soup(url)
    entries = [[]]
    paras = soup.select('div.mail p')
    paras = (get_text_from_soup(para) for para in paras)
    for para in paras:
        if para == '----------------------------------------------------------------------\n': #start parsing entries
            entries = [[]]
        elif para == '------------------------------\n': #next entry
            entries.append([])
        else: #add to current entry
            entries[-1].append(para)
    entries.pop(-1) #last one was the footer
    for i,entry in enumerate(entries):
        from_field = re.search('From: (.*)\n', entry[0]).group(1)
        try:
            from_addr = re.search('<(.*?)>', from_field).group(1)
            from_name = re.search('(.*?) <', from_field).group(1)
        except:
            from_addr = from_name = from_field
        subject = re.search('Subject: (.*)\n', entry[0]).group(1)
        entry = '\n'.join(entry[1:])
        entries[i] = dict(from_addr=from_addr,
                          from_name=from_name,
                          subject=subject,
                          entry=entry)
    return entries

if __name__ == '__main__':
    entries = []
    try:
        for message_url in get_all_message_urls():
            entries += parse_message(message_url)
    finally:
        with open('SN.json', 'w') as f:
            json.dump(entries, f, sort_keys=True, indent=2)
    

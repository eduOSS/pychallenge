#!/usr/bin/python2
from itertools import takewhile, dropwhile
from bs4 import BeautifulSoup, Tag, NavigableString, Comment, Doctype
from sys import stdin, stdout
import json
import codecs


SINGLE_LINE_COMMENT_THRESHOLD = 1
STRIP_WRAPPING_EMPTY_LINES = True
INDENT_UNIT = '  '


stdout = codecs.getwriter('utf8')(stdout)


def prints(indent, lines, prefix='', mapper=lambda x: x):
    if isinstance(lines, basestring):
        lines = lines.splitlines()
    for line in lines:
        stdout.write(INDENT_UNIT * indent + prefix + mapper(line) + '\n')


def strip_wrapping_empty_lines(lines):
    return list(takewhile(lambda l: l, dropwhile(lambda l: not l, lines)))


def tojade(indent, obj):
    if isinstance(obj, Doctype):
        stdout.write(obj.output_ready())
    elif isinstance(obj, NavigableString):
        lines = unicode(obj).splitlines()
        lines = [line.lstrip() for line in lines]
        if STRIP_WRAPPING_EMPTY_LINES:
            lines = strip_wrapping_empty_lines(lines)
        if isinstance(obj, Comment):
            if len(lines) > SINGLE_LINE_COMMENT_THRESHOLD:
                prints(indent, '//')
                prints(indent + 1, lines, mapper=lambda x: x.lstrip())
            else:
                for line in lines:
                    prints(indent, '// ' + line.lstrip())
        else:
            prints(indent, lines, '| ')
    elif isinstance(obj, Tag):
        if isinstance(obj, BeautifulSoup):
            stdout.write('!!! xml\n')
        else:
            attrs = []
            for k, v in obj.attrs.iteritems():
                attrs.append('%s=%s' % (k, json.dumps(v)))
            tag_header = obj.name
            if attrs:
                tag_header += '(%s)' % ', '.join(attrs)
            prints(indent, tag_header)
            indent += 1
        for child in obj.children:
            tojade(indent, child)


def main():
    soup = BeautifulSoup(stdin.read(), 'xml')
    tojade(0, soup)

if __name__ == '__main__':
    main()

from multiprocessing import Process, Manager

def dosomething(mlist):
    mlist.append((4,5,6))

def main():
    manager = Manager()
    L = manager.list((1,2,3,4))

    p = Process(target=dosomething, args=(L,))
    p.start()
    p.join()

    print L

if __name__ == '__main__':
    main()

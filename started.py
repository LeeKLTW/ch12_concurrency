# encoding: utf-8
from threading import Thread, Event
import time


def countdown(n, started_evt=None):
    print('count down starting')
    if started_evt != None:
        started_evt.set()
    while n > 0:
        print('T - minus', n)
        n -= 1
        time.sleep(0.5)


print('Lauching countdown')
started_evt = Event()
threads = []
for i in range(4):
    threads.append(Thread(target=countdown, args=(5, started_evt)))

for thread in threads:
    thread.start()
    started_evt.wait()

for thread in threads:
    thread.join()

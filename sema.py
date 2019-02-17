# encoding: utf-8
import threading


def worker(n, sema):
    sema.acquire()
    print('working', n)

sema = threading.Semaphore(0)
nworkers = 10

for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n ,sema,))
    t.start()

# nothing will happend now

# semaphore release:
# >>
for i in range(nworkers):
    sema.release()
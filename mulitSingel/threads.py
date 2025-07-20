import time 

def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} completed")

def singel_threaded():
    start = time.time()
    task("A")
    task("B")
    task("C")
    end = time.time()
    print(f"Singel-threaded total time: {end - start:.2f} seconds")

singel_threaded()

import threading


def multi_threading():
    start = time.time()

    threads = []
    for name in ["A", "B", "C"]:
        t = threading.Thread(target=task, args=(name,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()
    print(f"Multi-threded total time: {end - start:.2f} seconds")

multi_threading()

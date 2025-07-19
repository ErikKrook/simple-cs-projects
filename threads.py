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
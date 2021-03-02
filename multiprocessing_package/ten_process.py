import multiprocessing
import time

start = time.perf_counter()

def do_something():
        print('sleeping 1 second...')
        time.sleep(1)
        print('done sleeping')
lst = []
if __name__ == '__main__':                          #it is always good to use this in all calling statements
    for _ in range(10):
        p =multiprocessing.Process(target=do_something)
        p.start()
        lst.append(p)

for i in lst:
    i.join()

finish = time.perf_counter()
print(f'finishes in {round(finish - start)} second(s)')


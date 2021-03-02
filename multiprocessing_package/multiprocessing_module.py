import multiprocessing
import time

start = time.perf_counter()

def do_something():
        print('sleeping 1 second...')
        time.sleep(1)
        print('done sleeping')

if __name__ == '__main__':                          #it is always good to use this in all calling statements
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

finish = time.perf_counter()
print(f'finishes in {round(finish - start)} second(s)')


import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'sleeping {seconds} second...')
    time.sleep(seconds)
    return f'done sleeping...{seconds}'

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as ex:
       lst = [5,4,3,2,1]
       results = ex.map(do_something,lst)

       for i in results:
            print(i)


finish = time.perf_counter()
print(f'finishes in {round(finish - start)} second(s)')



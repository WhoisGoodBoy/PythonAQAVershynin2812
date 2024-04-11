import time
import concurrent.futures


def sleepy_function(name):
    print(f'we`re entered {name} func congratulations with this win')
    time.sleep(4)
    print(f'we`re exited {name} func, what a shame')



with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(sleepy_function, range(30))
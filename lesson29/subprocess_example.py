import subprocess
import datetime
import concurrent.futures
'''
print(datetime.datetime.now())
result = subprocess.run(['pytest', 'test_cat.py', '--pytest-html=result.html'], shell=True, capture_output=True, text=True)
print(result.stdout)

print(datetime.datetime.now())
'''

def threads_subporocess(name):
    print(f'we`re entered {name} file rn')
    result = subprocess.run(['python', name], shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(f'we`re exited {name} file, what a shame')


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(threads_subporocess, ['threads1.py', 'threads2.py', 'threads1.py', 'threads2.py'])

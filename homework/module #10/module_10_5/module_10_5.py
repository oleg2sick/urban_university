import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, mode='r', encoding='UTF-8') as file:
        for string in file:
            if len(string) > 0:
                all_data.append(string)
            else:
                break


start_time = datetime.datetime.now()

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
"""for name in files:
    read_info(name)

time_spent = datetime.datetime.now() - start_time
print(f'Времени затрачено линейно {time_spent}')"""

if __name__ == '__main__':
    start_time_with_mproc = datetime.datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    time_spent_with_mproc = datetime.datetime.now() - start_time_with_mproc
    print(f'Времени затрачено с multiprocessing {time_spent_with_mproc}')

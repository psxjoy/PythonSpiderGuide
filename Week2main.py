from multiprocessing import Pool
from Week2_3 import channel_list
from Week2_3_1 import get_links_from


def get_all_links_from(channel):
    for num in range(1, 101):
        get_links_from(channel, num)


# c创建进程池
if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from, channel_list.split())

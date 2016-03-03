from multiprocessing import Pool
from Week2T1 import channel_list
from Week2T2 import get_item_links
import time


def get_all_links_from(channel):
    for num in range(1, 101):
        time.sleep(2)
        get_item_links(channel, num)


if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from, channel_list.split())

from multiprocessing import Pool
from Week2T1 import channel_list
from Week2T2 import get_item_links


def get_all_links_from(channel):
    for num in range(1, 101):
        get_item_links(channel, num)


if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from, channel_list.split())

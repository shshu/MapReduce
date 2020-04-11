import random
import time

from collections import Counter
from functools import reduce
from multiprocessing import Pool

URLS = 'A aB bC cD dE eF fG gH hI iJ jK kL lM mN nO oP pQ qR rS sT tU V W X Y Z '.split(
    ' ')
URL_ACSEESS = [random.choice(URLS) for _ in range(1000000)]


def chunks(lst, number_of_chunks):
    """Yield successive chunk from lst."""
    size = len(lst)
    num = int(size / number_of_chunks)
    for i in range(0, size, num):
        yield lst[i:i + num]


def mapper(text):
    return Counter([text])


def reducer(cnt1, cnt2):
    cnt1.update(cnt2)
    return cnt1


def mapper_chunk(chunk):
    mapped_chunk = map(mapper, chunk)
    return reduce(reducer, mapped_chunk)


def main():
    data_chunks = chunks(URL_ACSEESS, number_of_chunks=30)
    pool = Pool(8)
    reduced = pool.map(mapper_chunk, data_chunks)
    reduced = reduce(reducer, reduced)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print('running time: {}'.format(time.time() - start_time))

import random
import time

from collections import Counter
from functools import reduce

URLS = 'A aB bC cD dE eF fG gH hI iJ jK kL lM mN nO oP pQ qR rS sT tU uV vW wX xY yZ z'.split(
    ' ')
URL_ACSEESS = [random.choice(URLS) for _ in range(1000000)]


def chunks(lst, number_of_chunks):
    size = len(lst)
    num = int(size / number_of_chunks)
    for i in range(0, size, num):
        yield lst[i:i + num]


def mapper(text):
    return Counter([text])


def reducer(cnt1, cnt2):
    cnt1.update(cnt2)
    return cnt1


def main():
    data_chunks = chunks(URL_ACSEESS, number_of_chunks=30)
    reduced = []
    for chunk in data_chunks:
        mapped_chunk = map(mapper, chunk)
        reduced_chunk = reduce(reducer, mapped_chunk)
        reduced.append(reduced_chunk)

    reduced = reduce(reducer, reduced)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print('running time: {}'.format(time.time() - start_time))

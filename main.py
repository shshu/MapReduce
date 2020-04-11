import random
import time

from collections import Counter
from functools import reduce
from multiprocessing import Pool

URLS = 'A aB bC cD dE eF fG gH hI iJ jK kL lM mN nO oP pQ qR rS sT tU V W X Y Z '.split(
    ' ')
URL_ACSEESS = [random.choice(URLS) for _ in range(10000000)]


def main():
    cnt = Counter()
    for url in URL_ACSEESS:
        cnt.update([url])


if __name__ == "__main__":
    start_time = time.time()
    main()
    print('running time: {}'.format(time.time() - start_time))

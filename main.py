"""
https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf
Count of URL Access Frequency: The map function processes logs of web page requests and outputs
hURL, 1i. The reduce function adds together all values
for the same URL and emits a hURL, total count i pair.
"""
import random
from collections import Counter
from functools import reduce

URLS = 'A aB bC cD dE eF fG gH hI iJ jK kL lM mN nO oP pQ qR rS sT tU uV vW wX xY yZ z'.split(' ')
URL_ACSEESS = [random.choice(URLS) for _ in range(1000000)]

def chunks(lst, number_of_chunks):
    """Yield successive chunk from lst."""
    size = len(lst)
    num = int(size/number_of_chunks)
    for i in range(0, size, num):
        yield lst[i:i + num]

def mapper(text):
    return Counter([text])

def reducer(cnt1, cnt2):
    cnt1.update(cnt2)
    return cnt1

data_chunks = chunks(URL_ACSEESS, number_of_chunks=30)
import time
t = time.time()
reduced = []
for chunk in data_chunks:
    mapped_chunk = map(mapper, chunk)
    mapped_chunk = list(mapped_chunk)
    reduced_chunk = reduce(reducer, mapped_chunk)
    reduced.append(reduced_chunk)

reduced = reduce(reducer, reduced)
print(time.time()-t)

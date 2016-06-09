#!/usr/bin/python3

LIST_COUNT = 1000;
LOOP_COUNT = 1000;
MAX_NUM = 1000;

def data_generate():
    import random
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]

def quick_sort(data, start, end):
    pivot = data[0]
    i = start
    j = end
    while 

def make_pivot(data, start, end):

if __name__ == '__main__':
    import time
    import sys

    start = time.time()
    for _ in range(LOOP_COUNT):
        data = data_generate()

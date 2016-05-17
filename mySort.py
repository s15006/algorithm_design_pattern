def quick_sort(data):
    import random

    if len(data) < 1:
        return data

    """
    基準値をランダムに選択
    pivot = random.choice(data)
    """

    """
    左の２つを比べて大きい方を選択
    pivot = data[0] if data[0] > data[1] else data[1]
    """

    "最初の値を選択"
    pivot = data[0]


    left = []
    right = []

    for x in range(1, len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right

if __name__ == '__main__':
    import time
    import sys
    
    start = time.time()
    for _ in range(LOOP_COUNT):
        data = data_generate()
        quick_sort(data)
        print('.', end='')
        sys.stdout.flush()

    end = time.time()
    print()
    print('経過時間:', (end - start))
    print('平均時間:', (end - start) / LOOP_COUNT)


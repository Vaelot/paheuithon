from multiprocessing import Pool, Queue, Lock
from random import choice

db = {
    2: ('박', '반', '밧'),
    3: ('받', '밪', '밬'),
    4: ('밤', '밥', '밫', '밭', '밮', '밖', '밗', '밨'),
    5: ('발', '밙', '밚'),
    6: ('밦'),
    7: ('밝', '밠'),
    8: ('밣'),
    9: ('밞', '밟', '밡', '밢'),
}
rdb = {v: k for k, v in db.items()}
dp = {}
    
def IDS_bottomup(pack):
    result, string, depth = pack
    if result == limit:
        finished.put((string, chr(result)))
    elif depth == 0 or result > limit or result < 1:
        pass
    else:
        if result > 1:
            IDS_bottomup((result * result, string + '빠따', depth - 1))
        for i in range(9, 1, -1):
            IDS_bottomup((result * i, string + db[i][0] + '따', depth - 1))
            IDS_bottomup((result + i, string + db[i][0] + '다', depth - 1))


def IDS(limit, finished):
    cnt = 6
    with Pool(4, initializer=init, initargs=(limit, finished)) as p:
        while True:
            start = []
            for i in range(9, 1, -1):
                start.append((i, db[i][0], cnt))
            cnt += 1
            p.map(IDS_bottomup, start, chunksize=1)
            if not finished.empty():
                break
            print(f"depth {cnt} has no answer.")
    print(f"{cnt} has the answer.")
    result = []
    while not finished.empty():
        result.append(finished.get())
    result.sort()

    return result[0]


def init(l, f):
    global limit, finished
    limit = l
    finished = f


if __name__ == '__main__':
    finq = Queue()

    # expand once for waiting
    print('start multiprocessing!')
    for i in input('input: '):
        num = ord(i)
        print(IDS(num, finq))
    """
    for num in range(ord('가'), ord('힣') + 1):
        result = IDS(num, finq)

        print(result)
    """
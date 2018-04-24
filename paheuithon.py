from random import choice
from queue import Queue

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


def IDS_bottomup(limit, finished, result, string, depth):
    global dp
    if result == limit:
        finished.put((string, chr(result)))
    elif depth == 0 or result > limit or result < 1:
        pass
    else:
        if result > 1:
            if result * result not in dp:
                dp[result * result] = f'{string}빠다'
                IDS_bottomup(limit, finished, result * result, dp[result * result], depth - 1)
            else:
                pass
        for i in range(9, 1, -1):
            if result * i not in dp:
                dp[result * i] = f'{string}{choice(db[i])}따'
                IDS_bottomup(limit, finished, result * i, dp[result * i], depth - 1)
            else:
                pass
            if result + i not in dp:
                dp[result + i] = f'{string}{choice(db[i])}다'
                IDS_bottomup(limit, finished, result + i, dp[result + i], depth - 1)
            else:
                pass


def IDS(limit, finished):
    global dp
    cnt = 0
    while True:
        dp = {}
        for i in range(9, 1, -1):
            IDS_bottomup(limit, finished, i, choice(db[i]), cnt)
        cnt += 1
        if not finished.empty():
            break
        print(f"depth {cnt} has no answer.")
    print(f"{cnt} has the answer.")
    result = []
    while not finished.empty():
        result.append(finished.get())
    result.sort()

    return result


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
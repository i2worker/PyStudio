import concurrent.futures
import multiprocessing
import queue
import itertools
import signal
import time

BOUND = 10**5

in_queue = multiprocessing.Queue(100)
exit_event = multiprocessing.Event()


def exit_handler(signum, frame):
    exit_event.set()


signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler)


def collatz(n):
    steps = 0
    while n > 1:
        if n % 2:
            n = n * 3 + 1
        else:
            n = n // 2
        steps += 1
    return steps


def collatz_consumer(target):
    count = 0
    while True:
        if not in_queue.empty():
            try:
                n = in_queue.get(timeout=1)
            except queue.Empty:
                return count

            if collatz(n) == target:
                count += 1

        if exit_event.is_set():
            return count


def range_producer():
    for n in range(2, BOUND):
        if exit_event.is_set():
            return
        try:
            in_queue.put(n, timeout=1)
        except queue.Full:
            exit_event.set()
            return

    while True:
        time.sleep(0.05)
        if in_queue.empty():
            exit_event.set()
            return


def length_counter(target):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(range_producer)
        results = executor.map(
            collatz_consumer,
            itertools.repeat(target, 4)
        )

    return sum(results)


def get_input(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
        except ValueError:
            print("请输入一个整数")
            continue
        if value <= 0:
            print("请输入一个大于0的整数")
        else:
            return value


def main():
    target = get_input("请输入Collatz序列的计算步数：")

    with concurrent.futures.ThreadPoolExecutor() as executor:  # 通过线程启动
        future = executor.submit(get_input, "请输入你猜的Collatz序列的个数：")
        count = length_counter(target)
        guess = future.result()

    if guess == count:
        print("恭喜你猜对了！")
    else:
        print(f"很遗憾，你猜错了。实际的数是{count}")

if __name__ == "__main__":
    main()

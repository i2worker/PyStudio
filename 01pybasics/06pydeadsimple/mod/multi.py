import concurrent.futures

BOUND = 10**5

def collatz_process(n):
    steps = 0
    while n > 1:
        if n % 2:
            n = n * 3 + 1
        else:
            n //= 2
        steps += 1
    return steps

def length_counter_process(target):
    count = 0
    with concurrent.futures.ProcessPoolExecutor() as executor:  # 创建进程池
        for result in executor.map(collatz_process, range(2, BOUND), chunksize=BOUND//4):  # 批量提交任务，通过chunksize指定每个进程处理的任务数量
            if result == target:
                count += 1
    return count

def get_input_process(prompt):
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

def main_process():
    target = get_input_process("请输入Collatz序列的计算步数：")

    with concurrent.futures.ThreadPoolExecutor() as executor:  # 通过线程启动
        future = executor.submit(get_input_process, "请输入你猜的Collatz序列的个数：")
        count = length_counter_process(target)
        guess = future.result()

    if guess == count:
        print("恭喜你猜对了！")
    else:
        print(f"很遗憾，你猜错了。实际的数是{count}")

if __name__ == "__main__":
    main_process()

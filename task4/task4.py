import sys


def read_file(path):
    with open(path, encoding='utf-8') as f:
         values = f.read().split()
    for i in range(len(values)):
        values[i] = int(values[i])
    return values


def min_steps(nums):
    median = sorted(nums)[len(nums) // 2]
    result = (sum(abs(v - median) for v in nums))
    return result


if __name__ == '__main__':
    nums = read_file(sys.argv[1])
    res = min_steps(nums)
    print(res)

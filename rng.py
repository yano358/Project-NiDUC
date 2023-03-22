import time


def random_value(x):
    random_int = int(time.time() * 10000000)
    random_int %= x
    return random_int


print("Please enter an upper limit:")
limit = int(input()) + 1

print("Please enter the number of desired random integers:")
number = int(input())

for i in range(number):
    print(random_value(limit), end=' ')
    time.sleep(time.time() % 5)

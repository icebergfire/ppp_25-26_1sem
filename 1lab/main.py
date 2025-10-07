

if __name__ == "__main__":
import random
def my_shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
counts = [[0] * 5 for _ in range(5)]
for i in range(1000):
    numbers = [1, 2, 3, 4, 5]
    my_shuffle(numbers) 
    for j in range(5):
        num = numbers[j]
        counts[num - 1][j] += 1
for i in range(5):
    print(counts[i])
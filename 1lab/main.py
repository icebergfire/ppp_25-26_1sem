

if __name__ == "__main__":
import random
counts = [[0]*5 for _ in range(5)]
for i in range(1000):
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)  
for j in range(5):
    num = numbers[j]
    counts[num - 1][j] += 1
for i in range(5):
    print(counts[i])
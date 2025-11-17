steps = []

def permute(current, remaining):
    steps.append((current.copy(), remaining.copy()))
    if not remaining:
        print("Готовая перестановка:", current)
        return
    for i in range(len(remaining)):
        permute(current + [remaining[i]], remaining[:i] + remaining[i+1:])

permute([], [1, 2, 3])
print("История шагов:")
for step in steps:
    print(step)


if __name__ == "__main__":
def check_brackets(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for i, ch in enumerate(s, start=1):
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return f"Ошибка на позиции {i}"
            stack.pop()
    if stack:
        return "Ошибка: не все скобки закрыты"
    return "ok"

print(check_brackets("(a)(b(c[d{e{r}f{g}s}w]r)tasd)"))        
 
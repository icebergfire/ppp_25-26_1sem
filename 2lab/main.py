

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


#Проверка
print(check_brackets("()"))        # ok
print(check_brackets("(]"))        # Ошибка на позиции 2
print(check_brackets("("))         # Ошибка: не все скобки закрыты
print(check_brackets(")"))         # Ошибка на позиции 1
print(check_brackets("([])"))      # ok
print(check_brackets("([)]"))      # Ошибка на позиции 3
print(check_brackets("{[()]}"))    # ok
print(check_brackets("{[(])}"))    # Ошибка на позиции 5
print(check_brackets("(((())))"))  # ok
print(check_brackets("((())"))     # Ошибка: не все скобки закрыты
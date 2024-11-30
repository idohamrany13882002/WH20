def is_valid_brackets(s: str):
    brackets: dict[str, str] = {')': '(', ']': '[', '}': '{'}
    results: list[str] = []

    for char in s:
        if char in brackets.values():
            results.append(char)
        elif char in brackets.keys():
            if results[-1] == brackets[char]:
                results.pop()
            else:
                return False

    return len(results) == 0


print(is_valid_brackets("{[()]}"))  # to check

def rot13(s: str) -> str:
    result = ""
    for char in s:
        const = 97 if ord(char) >= 97 else 65
        if char.isalpha():
            result += chr((ord(char) - const + 13) % 26 + const)
        else:
            result += char
    return result

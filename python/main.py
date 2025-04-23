# prg = "L"+"O"*100+"V"
# prg = "LLLOO[ROOOOOR-]E[ROOOOOOOR-]EV"
prg = "".join(["L"+"O"*i+"V" for i in [72, 101, 108, 108, 111]])


def parser(prg: str) -> list[str]:
    prg = prg.replace("\n", "")
    prg = prg.replace("\t", "")
    prg = prg.replace(" ", "")
    tokens = [i for i in prg]
    return tokens

def execute(tokens: list[str], ptr: int, stack:list[int]) -> None:
    if ptr >= len(tokens):
        if DEBUG:
            print(f"Pointer: {ptr}, Stack: {stack}")
        print("End of program")
        return
    
    token = tokens[ptr]
    if DEBUG:
        print(f"Pointer: {ptr}, Stack: {stack}, Token: {tokens[ptr]}")
    
    
    if token == "L":
        stack.append(0)
        execute(tokens, ptr+1, stack)
    elif token == "O":
        stack[-1] += 1
        execute(tokens, ptr+1, stack)
    elif token == "V":
        data = stack.pop()
        print(chr(data), end=" ")
        print(data)
        execute(tokens, ptr+1, stack)
    elif token == "E":
        stack.pop()    
        execute(tokens, ptr+1, stack)
    elif token == "[":
        if stack[-1] == 0:
            while tokens[ptr] != "]":
                ptr += 1
        execute(tokens, ptr+1, stack)
    elif token == "]":
        if stack[-1] != 0:
            while tokens[ptr] != "[":
                ptr -= 1
        execute(tokens, ptr+1, stack)
    elif token == "R":
        a = stack.pop()
        b = stack.pop()
        stack.append(a)
        stack.append(b)
        execute(tokens, ptr+1, stack)
    elif token == "-":
        stack[-1] -= 1
        execute(tokens, ptr+1, stack)
    elif token == "C":
        stack.append(stack[-1])
        execute(tokens, ptr+1, stack)
    else:
        print("Error: Unknown token")
        return
    

if __name__ == "__main__":
    DEBUG = True
    tokens = parser(prg)
    if DEBUG:
        print("Tokens:")
        print(tokens)
    execute(tokens, 0, [])
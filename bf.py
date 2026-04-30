import sys

code = sys.stdin.read()
cells = [0] * 30000
ptr = 0
i = 0

# build bracket map
stack = []
brackets = {}
for pos, cmd in enumerate(code):
    if cmd == "[":
        stack.append(pos)
    elif cmd == "]":
        start = stack.pop()
        brackets[start] = pos
        brackets[pos] = start

while i < len(code):
    cmd = code[i]

    if cmd == ">": ptr += 1
    elif cmd == "<": ptr -= 1
    elif cmd == "+": cells[ptr] = (cells[ptr] + 1) % 256
    elif cmd == "-": cells[ptr] = (cells[ptr] - 1) % 256
    elif cmd == ".": print(chr(cells[ptr]), end="")
    elif cmd == ",":
        cells[ptr] = ord(sys.stdin.read(1))
    elif cmd == "[" and cells[ptr] == 0:
        i = brackets[i]
    elif cmd == "]" and cells[ptr] != 0:
        i = brackets[i]

    i += 1
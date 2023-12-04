with open('input.txt', 'r') as f:
    contents = f.read().replace('\n', '')

LINE_LEN = 140
SPEC_CHARS = '*%@+-=/&$#'
ADJ_MATRIX = [
    -(LINE_LEN - 1), -(LINE_LEN), -(LINE_LEN+1),
    -1, 1,
    LINE_LEN-1, LINE_LEN, LINE_LEN+1
]

def special_char_adj(idx) -> bool:
    for offset in ADJ_MATRIX:
        new_idx = min(idx+offset, len(contents) - 1)
        if contents[new_idx] in SPEC_CHARS:
            return True
        
    return False

i = 0
sum = 0
while i < len(contents):
    num_str = ''
    j = 0
    while contents[i+j].isnumeric() and j <= 2:
        num_str += contents[i+j]
        j += 1
    else:
        if len(num_str) > 0:
            for idx in range(i, i+j):
                if special_char_adj(idx):
                    print(f"Include: {num_str}")
                    sum += int(num_str)
                    break
            else:
                print(f"NOT: {num_str}")

    i += j + 1

print(sum)

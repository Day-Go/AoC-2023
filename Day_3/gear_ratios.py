with open('input.txt', 'r') as f:
    contents = f.read().replace('\n', '')

LINE_LEN = 140
SPEC_CHARS = '*%@+-=/&$#'
ADJ_MATRIX = [
    -(LINE_LEN - 1), -(LINE_LEN), -(LINE_LEN+1),
    -1, 0, 1,
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
                    sum += int(num_str)
                    break

            j -= 1

    i += j + 1

print(sum)

# Part 2
from operator import mul
from functools import reduce 

def get_whole_number(idx: int, num_str: str, go_to_start: bool):
    '''
    go_to_start = true -> Go left
    '''
    if not contents[idx].isnumeric() and not go_to_start:
        return num_str

    if contents[idx].isnumeric():
        if go_to_start:
            num_str = get_whole_number(idx-1, '', True)
            return num_str
            
        else:
            num_str += contents[idx]
            num_str = get_whole_number(idx+1, num_str, False)
            return num_str
    else:
        num_str = get_whole_number(idx+1, '', False)
        return num_str

def numeric_char_adj(idx) -> str:
    if contents[idx].isnumeric():
        num_str = ''
        number = get_whole_number(idx, num_str, True)
        return number
    return ''

i = 0
sum = 0
while i < len(contents):
    nums = []
    
    if contents[i] == "*":
        j = 0

        while j < len(ADJ_MATRIX):
            val = ADJ_MATRIX[j]
            num_str = numeric_char_adj(i+val)

            if num_str and not int(num_str) in nums:
                nums.append(int(num_str))

            j += 1
                
        if len(nums) >= 2:
            print(nums)
            sum += reduce(mul, nums, 1)

    i += 1

print(sum)


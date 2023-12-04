with open('input.txt', 'r') as f:
    contents = f.read().replace('\n', '')

# 2 passes
# Pass 1:
#   - Get location of all symbols (r, c)
#
# Pass 2:
#   - Get location of all digits, group into numbers
#     i.e. d[r, c-1] + d[r, c] + d[r, c+1] = number
#
#   - Check for adjacency


# OR
# - iterate through each char like its a flat list
# - Store starting idx, len and value in a dict
# - Store loc of all symbols 

def find_digit(idx: int, num_str: str, msb: bool) -> int:
    '''
    Given an index in the string, check if the value contained is a digit.
    If it is, search for other characters in digit and return value as int. 
    '''
    print(contents[idx]) 
    if contents[idx].isnumeric():
        if msb == None:
            pass
        elif msb == True:
            num_str = contents[idx] + num_str
            find_digit(idx-1, num_str)
        else:
            num_str += contents[idx]
            find_digit(idx+1, num_str)

    print(num_str)
    return int(num_str)

ROW_LEN = 1
SPECIAL_SYMBOLS = "\"!@#$%^&*()-+?_=,<>/\'"

print(contents[4])
print(contents[5+2*ROW_LEN])

i = 0
while i < len(contents):
    v = contents[i]
    if v in SPECIAL_SYMBOLS:
        find_digit(i, '', None)
    i += 1 
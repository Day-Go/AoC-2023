import argparse

parser = argparse.ArgumentParser(
    prog='Trebutchet',
    description='AoC day 1'
)
parser.add_argument('--strs', action='store_true', 
                    help='include strings as valid numbers')

DIGIT_STRINGS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def kmp_precompute(word: str) -> list[int]:
    lsp_table = [0] * len(word)

    j = 0
    i = 1
    while i < len(word):
        if word[j] == word[i]:
            lsp_table[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            lsp_table[i] = 0
            i += 1
        else:
            j = lsp_table[j - 1]

    return lsp_table

if __name__ == '__main__':
    args = parser.parse_args()
    print(args.strs)

    # # KMP doesn't give any advantage over naive approach except in the case of 'nine'.
    # # Not going to use it
    # lsp_tables = [kmp_precompute(d_str) for d_str in DIGIT_STRINGS]
    # print(lsp_tables)

    with open("input.txt", "r") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        num_str = ''
        i = 0
        while i < len(line): 
            if line[i].isdigit():
                num_str += line[i]
            elif args.strs:
                for v, digit in enumerate(DIGIT_STRINGS):
                    if digit == line[i:i+len(digit)]:
                        num_str += str(v + 1)
                        break

            i += 1    
            if len(num_str) == 1: break
            

        j = len(line) - 1
        while j >= 0:
            if line[j].isdigit():
                num_str += line[j]
                break
            elif args.strs:
                for v, digit in enumerate(DIGIT_STRINGS):
                    if digit == line[j-len(digit)+1:j+1]:
                        num_str += str(v + 1)
                        break
            
            j -= 1
            if len(num_str) == 2: break

        sum += int(num_str)

    print(sum)


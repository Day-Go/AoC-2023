with open('input.txt', 'r') as f:
    lines = f.readlines()

# dest, src, range

lines.append('\n')
# print(lines)
seeds = ''.join(lines[0].split(':')[-1]).strip().split(' ')
# print(seeds)

locs = []
for seed in seeds:
    i = 2
    next_src = int(seed)
    print(next_src)
    while i < len(lines):

        if 'map' in lines[i]:
            i += 1
        elif len(lines[i]) == 1:
            i += 1
            # break
        else:
            line = lines[i].strip().split()
            dest = int(line[0])
            src = int(line[1])
            range = int(line[2])
            # print(f"ns: {next_src}")
            # print(f"src: {src}")
            # print(f"range: {range}")
            # print(f"dest: {dest}")
            # print('')

            if next_src >= src and next_src <= (src + range):
                next_src = dest
                j = 0
                while len(lines[i+j]) > 1:
                    j += 1
                i += j
                print(lines[i-1])
                
            i += 1

    locs.append(next_src)
    print(next_src)
    print('')
    # break

print(locs)  
print(min(locs))


# for i, line in enumerate(lines[2:]):
#     if 'map' in line:
#         j = 0
#         while len(line[i+j+1]) > 0:
            
with open('input.txt', 'r') as f:
    lines = f.readlines()

def calc_distance(vel: int, t_remaining: int):
    return vel * t_remaining

times = [int(time) for time in lines[0].split()[1:]]
dists = [int(dist) for dist in lines[1].split()[1:]]

print(times)
print(dists)

w_mult = 1
for time, w_dist in zip(times, dists):
    print(time, w_dist)
    w_sum = 0
    for i in range(time):
        d = i * (time - i)
        if d > w_dist:
            w_sum += 1

    w_mult *= w_sum

print(w_mult)
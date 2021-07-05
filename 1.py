def solution(init,power_bonus):
    power_bonus.sort(key = lambda item: item[0])
    count = 0
    for power,bonus in power_bonus:
        if power>init:
            return count
        count+=1
        init+=bonus
    return count

def main():
    n = int(input().rstrip())
    init = int(input().rstrip())
    power_bonus =[]
    for _ in range(n):
        power_bonus.append([int(input().rstrip())])
    for i in range(n):
        power_bonus[i].append(int(input().rstrip()))
    print(solution(init,power_bonus))

main()

"""
input 1:
3
100
101
100
304
100
1
524
answer = 2

input 2:
2
123
78
130
10 
0
answer = 2
"""
def solution(array):
    curr = max(array[0])
    sum = curr
    for i in range(1,len(array)):
        curr_next = max(array[i])
        if curr>=curr_next:
            break
        sum+=curr_next
        curr = curr_next
    return sum%1000000007

def main():
    n = int(input().rstrip())
    array = []
    for _ in range(n):
        ip = input().split()
        array.append([int(ip[0]),int(ip[1])])
    print(solution(array))

main()

"""
input 1:
2
1 2 
3 4 
answer=6

input 2:
2
7 8
5 5
answer=8

input 3:
3
1 1
2 2
3 3
answer=6
"""
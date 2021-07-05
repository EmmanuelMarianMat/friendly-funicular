def solution(array):
    n = len(array)
    subseq = [[num] for num in array]
    pos = 0
    for i in range(1,n):
        for j in range(i):
            if array[j]<array[i] and 2*(array[j]&array[i])<(array[j]|array[i]) and len(subseq[j])+1>len(subseq[i]):
                subseq[i] = subseq[j] + [array[i]]
        if len(subseq[pos])<len(subseq[i]):
            pos = i
    # print(subseq[pos])
    return len(subseq[pos])

def main():
    n = int(input().rstrip())
    array = []
    for _ in range(n):
        array.append(int(input().rstrip()))
    print(solution(array))

main()

"""
input 1:
5
15
6
5
12
1
answer=2

input 2:
6
9
17
2
15
5
2
answer=2

input 3:
7
17
16
12
2
8
17
17
answer=3
"""
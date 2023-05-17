n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count = 0
pointer1 = 0
pointer2 = 0
result = []


while pointer1 < n and pointer2 < m:
    if arr1[pointer1] < arr2[pointer2]:
        count += 1
        pointer1 += 1
    else:
        result.append(count)
        pointer2 += 1

while pointer2 < m:
    result.append(count)
    pointer2 += 1

for num in result:
    print(num, end=' ')

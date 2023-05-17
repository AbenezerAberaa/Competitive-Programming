n, k = map(int, input().split())
sequence = list(map(int, input().split()))
 
sequence.sort()
 
left = 1
right = 10**9
result = -1
 
while left <= right:
    mid = (left + right) // 2
    count = 0
 
    
    for num in sequence:
        if num <= mid:
            count += 1
 
    
    if count == k:
        result = mid
        break
    elif count < k:
        left = mid + 1
    else:
        right = mid - 1
 
print(result)

n, m = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

merged_array = []
i, j = 0, 0

while i < n and j < m:
    if array1[i] <= array2[j]:
        merged_array.append(array1[i])
        i += 1
    else:
        merged_array.append(array2[j])
        j += 1

# Append the remaining elements from the arrays
while i < n:
    merged_array.append(array1[i])
    i += 1

while j < m:
    merged_array.append(array2[j])
    j += 1

print(*merged_array)

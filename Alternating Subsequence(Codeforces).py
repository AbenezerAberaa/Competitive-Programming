t = int(input())

for _ in range(t):
    n = int(input())
    sequence = list(map(int, input().split()))

    max_sum = 0
    current_sum = sequence[0]
    current_sign = sequence[0] // abs(sequence[0])

    for i in range(1, n):
        if sequence[i] // abs(sequence[i]) == current_sign:
            current_sum = max(current_sum, sequence[i])
        else:
            max_sum += current_sum
            current_sum = sequence[i]
            current_sign = sequence[i] // abs(sequence[i])

    max_sum += current_sum

    print(max_sum)

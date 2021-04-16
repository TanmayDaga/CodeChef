lst = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

for _ in range(int(input())):
    p = int(input())
    final_val = 0
    for i in lst:
        if p == 1:
            final_val += 1
        elif p >= 2048:
            p -= 2048
            final_val += 1
        elif p >= i:
            p -= i
            final_val += 1

    print(final_val)

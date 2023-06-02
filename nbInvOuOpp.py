def sontInvOuOpp(a, b):
    if a + b == 0 or a * b == 1:
        print("Vrai")
    else:
        print("Faux")

def nb(T):
    count = 0
    n = len(T)

    for i in range(n):
        for j in range(i+1, n):
            if (T[i] + T[j] == 0) or (T[i] * T[j] == 1):
                count += 1

    return count

T = [1, 2, -1, -2, 0, 3]
sontInvOuOpp(1, 2)
result = nb(T)
print(result)

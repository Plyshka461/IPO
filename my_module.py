def suma_delit(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum
def poisk_druzei(N):
    friendly_numbers = []
    for i in range(1, N):
        a = suma_delit(i)
        b = suma_delit(a)
        if i == b and i != a:
            friendly_numbers.append((i, a))
    return friendly_numbers
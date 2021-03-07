import sympy

def get_factors(num):
    factors = []
    if not sympy.isprime(num):
        for m in range(1, num+1):
            if num % m == 0 and m != num and m != 1:
                factors.append(m)
    return factors


if __name__ == "__main__":

    max_checked = 0
    for i in range(110880, 1200000000):
        # print(i)
        f = get_factors(i)
        if len(f) > max_checked:
            max_checked = len(f)
            print(max_checked, i, f)

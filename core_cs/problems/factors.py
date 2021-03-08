import sympy

def get_factors(num):
    factors = []
    if not sympy.isprime(num):
        for m in range(1, num+1):
            if num % m == 0 and m != num and m != 1:
                factors.append(m)
    return factors


if __name__ == "__main__":

    with open("numbers.txt", "a") as fi:
        max_checked = 0
        for i in range(1443960, 1200000000):
            f = get_factors(i)
            fi.write(f"{i}, {len(f)}, {f} \n")

            if len(f) > max_checked:
                max_checked = len(f)
                print(max_checked, i, f)
            if len(f) == 237:
                print(i, f)
                fi.write(f"!!!!! - {i}, {len(f)}, {f} \n")

import sympy


def get_factors(num):
    factors = [1, num]
    if not sympy.isprime(num):
        for m in range(1, num+1):
            if num % m == 0 and m != num and m != 1:
                factors.append(m)
    return factors


if __name__ == "__main__":
    with open("numbers3.txt", "a") as fi:
        max_checked = 0
        perfect_squares = []

        for i in range(2738, 1443960):
            n = i*i
            print(n)
            perfect_squares.append((i, i*i))

        for i, perfect_square in perfect_squares:
            f = get_factors(perfect_square)
            # print(perfect_square)
            fi.write(f"{i}, {perfect_square},  {f} \n")
            print("", end="!")

            if len(f) > max_checked:
                print("")
                max_checked = len(f)
                print(max_checked, i, perfect_square, f )

            if len(f) == 237:
                print("")
                print("+++++++++++", i, perfect_square,"+++++++++++", f)
                fi.write(f"!!!!! - {max_checked}, {i}, {perfect_square}, {f} \n")




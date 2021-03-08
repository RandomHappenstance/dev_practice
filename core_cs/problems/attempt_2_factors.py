import sympy


def get_factors(num):
    factors = []
    if not sympy.isprime(num):
        for m in range(1, num+1):
            if num % m == 0 and m != num and m != 1:
                factors.append(m)
    return factors


if __name__ == "__main__":

    with open("numbers3.txt", "a") as fi:
        max_checked = 0
        perfect_squares = []

        for i in range(0, 1443960):
            n = i*i
            print(n)
            perfect_squares.append((i, i*i))

        for i, perfect_square in perfect_squares:
            f = get_factors(perfect_square)
            # print(perfect_square)
            fi.write(f"{i}, {perfect_square},  {f} \n")

            if len(f) > max_checked:
                max_checked = len(f)
                print(max_checked, i, f)

            if len(f) == 237:
                print(i, f)
                fi.write(f"!!!!! - {i}, {f} \n")



            # f = get_factors(perfect_square)
            # fi.write(f"{i}, {len(f)}, {f} \n")
            #
            # if len(f) > max_checked:
            #     max_checked = len(f)
            #     print(max_checked, i, f)
            # if len(f) == 237:
            #     print(i, f)
            #     fi.write(f"!!!!! - {i}, {len(f)}, {f} \n")

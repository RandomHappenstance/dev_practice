
def recursive_string_reverse(value):
    if len(value) == 1:
        return list(value)
    else:
        last = [value[-1]]
        fe = value[:-1]
        last.extend(recursive_string_reverse(fe))
        return "".join(last)

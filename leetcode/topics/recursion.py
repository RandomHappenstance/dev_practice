

def recursive_string_reverse(value: str) -> str:
    """ This function starts from the back of the array and works itself forward.
        It takes the last element, then passes the 0,..., n - 1 elements to the recursive function
        and keeps doing that until it reaches the end. """

    if len(value) == 1:
        return value
    else:
        last = [value[-1]]
        fe = value[:-1]
        last.extend(recursive_string_reverse(fe))
        return "".join(last)


def reverse_in_place(value: str, pos: int = 0) -> str:
    """ Requirement: Do not allocate extra space for another array, you must do this
                     by modifying the input array in-place with O(1) extra memory.

        My approach here is going to be to start in the middle and work my way out. That
        way I only need a variable to hold one of the values while the values switch places.

        The algorithm is going to start on the outside, recursively go inward towards the middle.
        """
    # Break condition
    if len(value) == 1:
        return value
    elif len(value) == 2:
        last_elem = value[-(pos+1)]
        value[-(pos+1)] = value[pos]
        value[pos] = last_elem
        return value
    # recursive condition
    else:
        last_elem = value[-(pos+1)]
        value[-(pos+1)] = value[pos]
        value[pos] = last_elem
        pos += 1
        if pos < int(len(value))/2:
            reverse_in_place(value, pos)
        return value

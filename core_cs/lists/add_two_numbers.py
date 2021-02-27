# You are given two non-empty linked lists representing two
# non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two
# numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

# src: https://leetcode.com/problems/add-two-numbers/

# input
# l1 = [2, 4, 3]
# l2 = [5, 6, 4]


def add_two_numbers(l1: list=[], l2: list=[]):
    # first pass
    # the runtime is len(l2) + 1

    l2_len = len(l2)-1
    final_list = []
    carry = 0
    for pos in range(len(l1)):
        if pos <= l2_len:
            num_sum = l1[pos] + l2[pos] + carry
            final_list.append(num_sum % 10)
            if num_sum >= 10:
                carry = 1
            else:
                carry = 0
        else:
            num_sum = l1[pos] + carry
            final_list.append(num_sum % 10)
            if num_sum >= 10:
                carry = 1
            else:
                carry = 0

        if pos == len(l1)-1 and carry == 1:
            final_list.append(1)

    return final_list


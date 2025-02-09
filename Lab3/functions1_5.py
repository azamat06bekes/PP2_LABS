# 5th Task

import itertools
def print_permuts():
    s = input("Enter a string: ")
    permutations = itertools.permutations(s)
    for perm in permutations:
        print(''.join(perm))

print_permuts()


# 6th Task

def func_reverse():
    s = list(map(str, input("Enter a string: ").split()))
    s.reverse()
    rev_sentence = ' '.join(s)
    return rev_sentence
print(func_reverse())

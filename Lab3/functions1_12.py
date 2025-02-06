# 12th Task

m_list = list(map(int, input(" Enter a numbers: ").split()))
def histogram(m_list):
    for num in m_list:
        print("*" * num)

print(histogram(m_list))


# 3rd Task

def func_3(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if(2 * chickens + 4 * rabbits == legs):
            return chickens, rabbits
    return "There are no solutions"
cnt_chickens, cnt_rab = func_3(35, 94)
print(f"Chickens: {cnt_chickens} \n Rabbits: {cnt_rab}")
    

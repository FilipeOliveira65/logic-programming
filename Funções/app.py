# FUNÇÃO QUE RETORNA VALOR

# def sum_num (a, b):
#     return a + b

# soma = sum_num(2, 5)

# print(soma + 3)
# =====================================

# FUNÇÃO QUE NÃO RETORNA VALOR

# def display_sum (a, b):
#     print(a + b)

# soma = display_sum(2, 5)

# print(soma + 3)

n1 = 10
n2 = 5

if n1 % 11 == 1:
    if n1 % 2 == 1: 
        n1 = n2 + 10
    else:
        n2 = n1 + 10.5
else:
    n1 = n1 % 11

    if n1 % 2 == 0 and n1 % 2 == 1: 
        n2 = n1 + 5 

n2 = n2 // 2 + 5 * n2 // 3

print(n1 + n2 % 2)
print(f"{n1}, {n2}")
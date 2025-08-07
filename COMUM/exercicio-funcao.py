# def numeros(a, b, c):
#     if a > b and a > c:
#         #print(f"O número {a} é o maior")
#         return f"O maior número é: {a}"
#     elif b > a and b > c:
#         #print(f"O número {b} é o maior")
#         return f"O maior número é: {b}"
#     else:
#         #print(f"O número {c} é o maior")
#         return f"O maior número é: {c}"
#     #return numeros(a, b, c)

# print(numeros(20, 10, 30))

def maior(primeiro, *restantes):
    return max(primeiro, *restantes)

print(maior(10, 7, 4, 22, 13, 17))
print(maior(5, 5, 5))

    
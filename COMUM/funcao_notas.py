def classificar_nota(nota):
    
    if nota > 70:
        return f"A nota {nota} é suficiente: aprovado."
    
    elif nota < 0:
        return f"A nota {nota} é inválida."
    
    elif nota < 50:
        return f"A nota {nota} não é suficiente: reprovado."

    elif nota >= 50 and nota < 70:
        return f"A nota {nota} não é suficiente: recuperação."
    
    else:
        return f"Não foi possíve realizar a operação."

nota = float(input("Digite a sua nota por favor: "))
print(classificar_nota(nota))
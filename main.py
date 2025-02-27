def karatsuba(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2

    n = max(len(str(num1)), len(str(num2)))
    m = n // 2
    
    high1 = num1 // 10**m  # Parte mais significativa de num1
    low1 = num1 % 10**m    # Parte menos significativa de num1

    high2 = num2 // 10**m  # Parte mais significativa de num2
    low2 = num2 % 10**m    # Parte menos significativa de num2

    # efetuando as multiplicações recursivamente
    lowProduct = karatsuba(low1, low2) # multiplicação da parte menos significativa
    sumProduct = karatsuba((low1 + high1), (low2 + high2)) # multiplicação da soma das partes menos e mais significativas
    highProduct = karatsuba(high1, high2) # multiplicação da parte mais significativa

    # Juntando os resultados
    return (highProduct * 10**(2*m)) + ((sumProduct - highProduct - lowProduct) * 10**m) + lowProduct

#Validando a funcao
num1 = 11111
num2 = 22222
result = karatsuba(num1, num2) 
print(f" {num1} x {num2} = {result}")
print(f" {num1} x {num2} = {num1*num2}")

num1 = 5634
num2 = 96374
result = karatsuba(num1, num2)
print(f" {num1} x {num2} = {result}")
print(f" {num1} x {num2} = {num1*num2}")

num1 = 50
num2 = 5
result = karatsuba(num1, num2)
print(f" {num1} x {num2} = {result}")
print(f" {num1} x {num2} = {num1*num2}")




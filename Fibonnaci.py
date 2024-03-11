
def fibonacci(n):

    a, b = 0, 1

   
    if n == a or n == b:
        return f"↪ {n} pertence à sequência de Fibonacci."

    
    while b < n:
        a, b = b, a + b

    
    if b == n:
        return f"↪ {n} pertence à sequência de Fibonacci."
    else:
        return f"↪ {n} não pertence à sequência de Fibonacci."

i = True
print("Teste:")

while i == True:

    numero = int(input("Informe um valor:"))
    
    print("-------------------------")
    print(fibonacci(numero))
    print("-------------------------")
    
           
    while True:
        Option = input("Desejar testar novamente ? S/N : ").capitalize()
    
        if Option == 'S':
            print('------▼▼▼-------')
            print("Refazer Teste")
            break 
        elif Option == 'N':
            print("Teste Finalizado")
            i = False
            break
        else:
            print("Por favor! Digite 'S' ou 'N'")
            continue
        


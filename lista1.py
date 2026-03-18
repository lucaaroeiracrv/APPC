# Lista de Exercícios (Python) – if e try


# 1.
# Faça uma função em Python que solicite a digitação de dois valores quaisquer,
# informando-os em seguida em ordem crescente.

def ordenar2NumerosEmCrescente():
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    if num1 <= num2:
        print(f"Valores em ordem crescente: {num1}, {num2}")
    else:
        print(f"Valores em ordem crescente: {num2}, {num1}")
              

# 2.
# Faça uma função em Python que solicite a digitação de três valores quaisquer,
# informando-os em seguida em ordem crescente.
#Usando apenas if e elif, sem usar listas, tuplas ou funções prontas de ordenação.
def ordenar3NumerosEmCrescente():
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    num3 = float(input("Digite o terceiro valor: "))
    if num1 <= num2 <= num3:
        print(f"Valores em ordem crescente: {num1}, {num2}, {num3}")
    elif num1 <= num3 <= num2:
        print(f"Valores em ordem crescente: {num1}, {num3}, {num2}")
    elif num2 <=num1 <= num3:
        print(f"Valores em ordem crescente: {num2}, {num1}, {num3}")
    elif num2 <= num3 <= num1:
        print(f"Valores em ordem crescente: {num2}, {num3}, {num1}")
    elif num3 <= num1 <= num2:
        print(f"Valores em ordem crescente: {num3}, {num1}, {num2}")
    else:        
        print(f"Valores em ordem crescente: {num3}, {num2}, {num1}")

    
# 3.
# Faça uma função em Python que solicite a digitação de quatro valores quaisquer,
# informando-os em seguida em ordem crescente.
def ordenadr4NumerosEmCrescente():
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    num3 = float(input("Digite o terceiro valor: "))
    num4 = float(input("Digite o quarto valor: "))
    if num1 <= num2 <= num3 <= num4:
        print(f"Valores em ordem crescente: {num1}, {num2}, {num3}, {num4}")
    elif num1 <= num2 <= num4 <= num3:
        print(f"Valores em ordem crescente: {num1}, {num2}, {num4}, {num3}")
    elif num1 <= num3 <= num2 <= num4:
        print(f"Valores em ordem crescente: {num1}, {num3}, {num2}, {num4}")
    elif num1 <= num3 <= num4 <= num2:
        print(f"Valores em ordem crescente: {num1}, {num3}, {num4}, {num2}")
    elif num1 <= num4 <= num2 <= num3:
        print(f"Valores em ordem crescente: {num1}, {num4}, {num2}, {num3}")
    elif num1 <= num4 <= num3 <= num2:
        print(f"Valores em ordem crescente: {num1}, {num4}, {num3}, {num2}")
    elif num2 <= num1 <= num3 <= num4:
        print(f"Valores em ordem crescente: {num2}, {num1}, {num3}, {num4}")
    elif num2 <= num1 <= num4 <= num3:
        print(f"Valores em ordem crescente: {num2}, {num1}, {num4}, {num3}")
    elif num2 <= num3 <= num1 <= num4:
        print(f"Valores em ordem crescente: {num2}, {num3}, {num1}, {num4}")
    elif num2 <= num3 <= num4 <= num1:
        print(f"Valores em ordem crescente: {num2}, {num3}, {num4}, {num1}")
    elif num2 <= num4 <= num1 <= num3:
        print(f"Valores em ordem crescente: {num2}, {num4}, {num1}, {num3}")
    elif num2 <= num4 <= num3 <= num1:
        print(f"Valores em ordem crescente: {num2}, {num4}, {num3}, {num1}")
    elif num3 <= num1 <= num2 <= num4:
        print(f"Valores em ordem crescente: {num3}, {num1}, {num2}, {num4}")
    elif num3 <= num1 <= num4 <= num2:
        print(f"Valores em ordem crescente: {num3}, {num1}, {num4}, {num2}")
    elif num3 <= num2 <= num1 <= num4:
        print(f"Valores em ordem crescente: {num3}, {num2}, {num1}, {num4}")
    elif num3 <= num2 <= num4 <= num1:
        print(f"Valores em ordem crescente: {num3}, {num2}, {num4}, {num1}")
    elif num3 <= num4 <= num1 <= num2:
        print(f"Valores em ordem crescente: {num3}, {num4}, {num1}, {num2}")
    elif num3 <= num4 <= num2 <= num1:
        print(f"Valores em ordem crescente: {num3}, {num4}, {num2}, {num1}")
    elif num4 <= num1 <= num2 <= num3:
        print(f"Valores em ordem crescente: {num4}, {num1}, {num2}, {num3}")
    elif num4 <= num1 <= num3 <= num2:
        print(f"Valores em ordem crescente: {num4}, {num1}, {num3}, {num2}")
    elif num4 <= num2 <= num1 <= num3:
        print(f"Valores em ordem crescente: {num4}, {num2}, {num1}, {num3}")
    elif num4 <= num2 <= num3 <= num1:
        print(f"Valores em ordem crescente: {num4}, {num2}, {num3}, {num1}")
    elif num4 <= num3 <= num1 <= num2:
        print(f"Valores em ordem crescente: {num4}, {num3}, {num1}, {num2}")
    else:        
        print(f"Valores em ordem crescente: {num4}, {num3}, {num2}, {num1}")

#Usando listas e a função sorted:
def ordenar4NumerosEmCrescenteComSorted():
    numeros = [
        float(input("Digite o primeiro valor: ")),
        float(input("Digite o segundo valor: ")),
        float(input("Digite o terceiro valor: ")),
        float(input("Digite o quarto valor: "))
    ]
    ordenados = sorted(numeros)
    print("Valores em ordem crescente:", ordenados)
#Com for
def ordenar4NumerosEmCrescenteComFor():
    print(sorted([float(input(f"Digite o {i}º valor: ")) for i in range(1, 5)])) #pq se nao fica "Digite o 0º valor: "

# Conversões de temperatura

# 4.
# Faça uma função em Python que converta temperaturas de Celsius para Fahrenheit.
# A função deve solicitar o valor em Celsius (C).
# Fórmula:
# F = C / 1.8 + 32
# Menor temperatura possível em Celsius: -273.15
def celciusToFahrenheit():
    try:
        c = float(input("Digite a temperatura em Celsius: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return 
    if c < -273.15:
        print("Temperatura inválida. A menor temperatura possível em Celsius é -273.15.")
    else: #dava pra usar return no if e nao colocar o else, mas fica mais organizado assim
        f = c / 1.8 + 32
        print(f"{c}°C é igual a {f}°F.")

# 5.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Celsius.
# A função deve solicitar o valor em Fahrenheit (F).
# Fórmula:
# C = 1.8 × (F − 32)
# Menor temperatura possível em Fahrenheit: -459.67
def fahrenheitToCelcius():
    try:
        f = float(input("Digite a temperatura em Fahrenheit: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if f < -459.67:
        print("Temperatura inválida. A menor temperatura possível em Fahrenheit é -459.67.")
    else:
        c = 1.8 * (f - 32)
        print(f"{f}°F é igual a {c}°C.")


# 6.
# Faça uma função em Python que converta temperaturas de Celsius para Kelvin.
# Fórmula:
# K = C + 273.15
# Menor temperatura possível em Celsius: -273.15
def celciusToKelvin():
    try:
        c = float(input("Digite a temperatura em Celsius: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if c < -273.15:
        print("Temperatura inválida. A menor temperatura possível em Celsius é -273.15.")
    else:
        k = c + 273.15
        print(f"{c}°C é igual a {k}K.")

# 7.
# Faça uma função em Python que converta temperaturas de Kelvin para Celsius.
# Fórmula:
# C = K − 273.15
# Menor temperatura possível em Kelvin: 0
def kelvinToCelcius():
    try:
        k = float(input("Digite a temperatura em Kelvin: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if k < 0:
        print("Temperatura inválida. A menor temperatura possível em Kelvin é 0.")
    else:
        c = k - 273.15
        print(f"{k}K é igual a {c}°C.")
# 8. 
# Faça uma função em Python que converta temperaturas de Celsius para Rankine.
# Fórmula:
# R = (C + 491.67) × 1.8
# Menor temperatura possível em Celsius: -273.15
def celciusToRankine():
    try:
        c = float(input("Digite a temperatura em Celsius: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if c < -273.15:
        print("Temperatura inválida. A menor temperatura possível em Celsius é -273.15.")
    else:
        r = (c + 491.67) * 1.8
        print(f"{c}°C é igual a {r}°R.")

# 9.
# Faça uma função em Python que converta temperaturas de Rankine para Celsius.
# Fórmula:
# C = (R / 1.8) − 491.67
# Menor temperatura possível em Rankine: 0
def rankineToCelcius():
    try:
        r = float(input("Digite a temperatura em Rankine: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if r < 0:
        print("Temperatura inválida. A menor temperatura possível em Rankine é 0.")
    else:
        c = (r / 1.8) - 491.67
        print(f"{r}°R é igual a {c}°C.")
# 10.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Kelvin.
# Menor temperatura possível em Fahrenheit: -459.67
def fahrenheitToKelvin():
    try:
        f = float(input("Digite a temperatura em Fahrenheit: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if f < -459.67:
        print("Temperatura inválida. A menor temperatura possível em Fahrenheit é -459.67.")
    else:
        k = (f - 32) / 1.8 + 273.15  
        print(f"{f}°F é igual a {k}K.")

# 11.
# Faça uma função em Python que converta temperaturas de Kelvin para Fahrenheit.
# Menor temperatura possível em Kelvin: 0
def kelvinToFahrenheit():
    try:
        k = float(input("Digite a temperatura em Kelvin: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if k < 0:
        print("Temperatura inválida. A menor temperatura possível em Kelvin é 0.")
    else:
        f = (k - 273.15) * 1.8 + 32 
        print(f"{k}K é igual a {f}°F.")

# 12.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Rankine.
# Menor temperatura possível em Fahrenheit: -459.67
def fahrenheitToRankine():
    try:
        f = float(input("Digite a temperatura em Fahrenheit: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if f < -459.67:
        print("Temperatura inválida. A menor temperatura possível em Fahrenheit é -459.67.")
    else:
        r = f + 459.67
        print(f"{f}°F é igual a {r}°R.")

# 13.
# Faça uma função em Python que converta temperaturas de Rankine para Fahrenheit.
# Menor temperatura possível em Rankine: 0
def rankineToFahrenheit():
    try:
        r = float(input("Digite a temperatura em Rankine: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if r < 0:
        print("Temperatura inválida. A menor temperatura possível em Rankine é 0.")
    else:
        f = r - 459.67
        print(f"{r}°R é igual a {f}°F.")
# 14.
# Faça uma função em Python que converta temperaturas de Kelvin para Rankine.
# Menor temperatura possível em Kelvin: 0
def kelvinToRankine():
    try:
        k = float(input("Digite a temperatura em Kelvin: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if k < 0:
        print("Temperatura inválida. A menor temperatura possível em Kelvin é 0.")
    else:
        r = k * 1.8
        print(f"{k}K é igual a {r}°R.")

# 15.
# Faça uma função em Python que converta temperaturas de Rankine para Kelvin.
# Menor temperatura possível em Rankine: 0
def rankineToKelvin():
    try:
        r = float(input("Digite a temperatura em Rankine: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        return

    if r < 0:
        print("Temperatura inválida. A menor temperatura possível em Rankine é 0.")
    else:
        k = r / 1.8
        print(f"{r}°R é igual a {k}K.")


# Perímetros

# 16.
# Faça uma função em Python que calcule o perímetro de um triângulo.
# Entradas: lado A, lado B, lado C
def perimetroTriangulo():
    a = float(input("Digite o lado A do triângulo: "))
    b = float(input("Digite o lado B do triângulo: "))
    c = float(input("Digite o lado C do triângulo: "))
    if a <= 0 or b <= 0 or c <= 0:
        print("Os lados do triângulo devem ser valores positivos.")
    else:
        perimetro = a + b + c
        print(f"O perímetro do triângulo é: {perimetro}")

# 17.
# Faça uma função em Python que calcule o perímetro de um quadrado/losango.
# Entrada: lado L
def perimetroQuadrado():
    lado = float(input("Digite o lado do quadrado/losango: "))
    if lado <= 0:
        print("O lado do quadrado/losango deve ser um valor positivo.")
    else:
        perimetro = 4 * lado
        print(f"O perímetro do quadrado/losango é: {perimetro}")

# 18.
# Faça uma função em Python que calcule o perímetro de um retângulo/paralelogramo.
# Entradas: lado menor (m) e lado maior (M)
def perimetroRetanguloOuParalelogramo():
    m = float(input("Digite o lado menor do retângulo/paralelogramo: "))
    M = float(input("Digite o lado maior do retângulo/paralelogramo: "))
    if m > M or m <= 0 or M <= 0 or m == 0 or M == 0:
        print("Valores inválidos. Os lados devem ser positivos e o lado menor não pode ser maior que o lado maior. E os lados nao podem ser iguais") 
    #especificamente nesse caso o tudo bem o lado menor ser maior que o lado maior, mas melhor fazer direito né
    else:
        perimetro = 2 * (m + M)
        print(f"O perímetro do retângulo/paralelogramo é: {perimetro}")

# 19.
# Faça uma função em Python que calcule o perímetro de um trapézio.
# Entradas: lado paralelo menor (m), lado paralelo maior (M) e outro lado (O) 
#Se for um trapézio isósceles, os outros dois lados são iguais, ou seja, O = O2. 
def perimetroTrapezioIsoseleces():
    m = float(input("Digite o lado paralelo menor do trapézio: "))
    M = float(input("Digite o lado paralelo maior do trapézio: "))
    o = float(input("Digite o outro lado do trapézio: "))
    if m <= 0 or M <= 0 or o <= 0 or M <= m or m == o or M == o:
        print("Valores inválidos. Os lados devem ser positivos, o lado paralelo maior deve ser maior que o lado paralelo menor, e os lados nao podem ser iguais.")
    else:
        perimetro = m + M + 2 * o
        print(f"O perímetro do trapézio é: {perimetro}")

#Se for um trapézio escaleno, os outros dois lados são diferentes
def perimetroTrapezioEscaleno():
    m = float(input("Informe a base menor (m): "))
    M = float(input("Informe a base maior (M): "))
    o1 = float(input("Informe o lado não paralelo 1 (o1): "))
    o2 = float(input("Informe o lado não paralelo 2 (o2): "))
    
    if m <= 0 or M <= 0 or o1 <= 0 or o2 <= 0 or M <= m or m == o1 or m == o2 or M == o1 or M == o2 or o1 == o2:
        print("Valores inválidos. Os lados devem ser positivos, o lado paralelo maior deve ser maior que o lado paralelo menor, e os lados nao podem ser iguais.")
    else:
        perimetro = m + M + o1 + o2
        print(f"O perímetro do trapézio é: {perimetro}")



# 20.
# Faça uma função em Python que calcule o perímetro de um polígono regular.
# Entradas: quantidade de lados (Q) e tamanho do lado
def perimetroPoligonoRegular():
    Q = int(input("Digite a quantidade de lados do polígono regular: "))
    tamanho = float(input("Digite o tamanho do lado do polígono regular: "))
    if Q < 3:
        print("Um polígono regular deve ter pelo menos 3 lados.")
    elif tamanho <= 0:
        print("O tamanho do lado deve ser um valor positivo.")
    else:
        perimetro = Q * tamanho
        print(f"O perímetro do polígono regular é: {perimetro}")

# 21.
# Faça uma função em Python que calcule o perímetro de um círculo.
# Entrada: raio (R)
# Fórmula: Perímetro = 2 × π × R
# π ≈ 3.1415
def perimetroCirculo():
    R = float(input("Digite o raio do círculo: "))
    if R <= 0:
        print("O raio do círculo deve ser um valor positivo.")
    else:
        perimetro = 2 * 3.1415 * R
        print(f"O perímetro do círculo é: {perimetro}")

# Áreas

# 22.
# Área de um triângulo
# Entradas: base (B) e altura (A)
# Fórmula: Área = (B × A) / 2
def areaTriangulo():
    B = float(input("Digite a base do triângulo: "))
    A = float(input("Digite a altura do triângulo: "))
    if B <= 0 or A <= 0:
        print("A base e a altura do triângulo devem ser valores positivos.")
    else:
        area = (B * A) / 2
        print(f"A área do triângulo é: {area}")

# 23.
# Área de um quadrado
# Entrada: lado (L)
# Fórmula: Área = L²
def areaQuadrado():
    L = float(input("Digite o lado do quadrado: "))
    if L <= 0:
        print("O lado do quadrado deve ser um valor positivo.")
    else:
        area = L ** 2 #Ou area = L * L
        print(f"A área do quadrado é: {area}")

# 24.
# Área de um retângulo
# Entradas: lado menor (m) e lado maior (M)
# Fórmula: Área = m × M
def areaRetangulo():
    m = float(input("Digite o lado menor do retângulo: "))
    M = float(input("Digite o lado maior do retângulo: "))
    if m <= 0 or M <= 0 or M <= m:
        print("Valores inválidos. Os lados devem ser positivos e o lado maior deve ser maior que o lado menor.")
    else:
        area = m * M
        print(f"A área do retângulo é: {area}")

# 25.
# Área de um losango
# Entradas: diagonal menor (d) e diagonal maior (D)
# Fórmula: Área = (d × D) / 2
def areaLosango():
    d = float(input("Digite a diagonal menor do losango: "))
    D = float(input("Digite a diagonal maior do losango: "))
    if d <= 0 or D <= 0 or D <= d:
        print("Valores inválidos. As diagonais devem ser positivas e a diagonal maior deve ser maior que a diagonal menor.")
    else:
        area = (d * D) / 2
        print(f"A área do losango é: {area}")

# 26.
# Área de um trapézio
# Entradas: base menor (b), base maior (B) e altura (A)
# Fórmula: Área = ((b + B) × A) / 2
def areaTrapezio():
    b = float(input("Digite a base menor do trapézio: "))
    B = float(input("Digite a base maior do trapézio: "))
    A = float(input("Digite a altura do trapézio: "))
    if b <= 0 or B <= 0 or A <= 0 or B <= b:
        print("Valores inválidos. As bases e a altura devem ser positivas, e a base maior deve ser maior que a base menor.")
    else:
        area = ((b + B) * A) / 2
        print(f"A área do trapézio é: {area}")

# 27.
# Área de um polígono regular
# Entradas: número de lados (Q), base (B) e apótema (A)
# Fórmula: Área = (Q × B × A) / 2
def areaPoligonoRegular():
    Q = int(input("Digite o número de lados do polígono regular: "))
    B = float(input("Digite a base do polígono regular: "))
    A = float(input("Digite a apótema do polígono regular: "))
    if Q < 3:
        print("Um polígono regular deve ter pelo menos 3 lados.")
    elif B <= 0 or A <= 0:
        print("A base e a apótema do polígono regular devem ser valores positivos.")
    else:
        area = (Q * B * A) / 2
        print(f"A área do polígono regular é: {area}")

# 28.
# Área de um círculo
# Entrada: raio (R)
# Fórmula: Área = π × R²
def areaCirculo():
    R = float(input("Digite o raio do círculo: "))
    if R <= 0:
        print("O raio do círculo deve ser um valor positivo.")
    else:
        area = 3.1415 * (R ** 2)
        print(f"A área do círculo é: {area}")



# 29.
# Faça uma função que calcule o IMC (Índice de Massa Corporal).
# Entradas: peso (kg) e altura (m)
# Fórmula: IMC = peso / altura²
def calcularIMC():
    peso = float(input("Digite o peso em kg: "))
    altura = float(input("Digite a altura em metros: "))
    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser valores positivos.")
    else:
        imc = peso / (altura ** 2)
        print(f"O IMC é: {imc}")


# 30.
# Faça uma função que resolva uma equação do 1º grau.
# Forma: AX + B = 0
# Entradas: A e B
def resolverEquacaoPrimeiroGrau():
    A = float(input("Digite o valor de A: "))
    B = float(input("Digite o valor de B: "))
    if A == 0:
        if B == 0:
            print("A equação tem infinitas soluções.") #qlquer numero vezes 0 = 0
        else:
            print("A equação não tem solução.")#0 + qualquer numero diferente de 0 vai ser != 0, entao nao tem soluca
    else:
        X = -B / A
        print(f"X é igual a: {X}")

#EXTRAS - EU(Luca) QUE FIZ :)
#30.1
#Faça uma função que calcula quantos litros de água uma pessoa deveria berer por dia de acordo com a sua massa corporal. 
# A fórmula é: P * 0.035 = L (Litros de água por dia)
#Entradas: P (peso em kg)
def calcularLitrosAguaPorDia():
    P = float(input("Digite o peso em kg: "))
    if P <= 0:
        print("O peso deve ser um valor positivo.")
    else:
        L = P * 0.035
        print(f"Você deveria beber {L} litros de água por dia.")

# Programas com menu

# 31.
# Faça uma função com menu que reúna os exercícios 4 a 15 (conversões de temperatura).
def menuConversaoTemperatura():
        print("\n=== MENU DE CONVERSÃO DE TEMPERATURA ===")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Celsius para Kelvin")
        print("4. Kelvin para Celsius")
        print("5. Celsius para Rankine")
        print("6. Rankine para Celsius")
        print("7. Fahrenheit para Kelvin")
        print("8. Kelvin para Fahrenheit")
        print("9. Fahrenheit para Rankine")
        print("10. Rankine para Fahrenheit")
        print("11. Kelvin para Rankine")
        print("12. Rankine para Kelvin")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        try:
            if opcao == "1":
                celciusToFahrenheit()
            elif opcao == "2":
                fahrenheitToCelcius()
            elif opcao == "3":
                celciusToKelvin()
            elif opcao == "4":
                kelvinToCelcius()
            elif opcao == "5":
                celciusToRankine()
            elif opcao == "6":
                rankineToCelcius()
            elif opcao == "7":
                fahrenheitToKelvin()
            elif opcao == "8":
                kelvinToFahrenheit()
            elif opcao == "9":
                fahrenheitToRankine()
            elif opcao == "10":
                rankineToFahrenheit()
            elif opcao == "11":
                kelvinToRankine()
            elif opcao == "12":
                rankineToKelvin()
            elif opcao == "0":
                print("Saindo do menu...")
            else:
                print("Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Tente novamente.")
menuConversaoTemperatura()
# 32.
# Faça uma função com menu que reúna os exercícios 16 a 21 (perímetros).
def menuPerimetros():
    while True:
        print("\n=== MENU DE PERÍMETROS ===")
        print("1. Perímetro de um Triângulo")
        print("2. Perímetro de um Quadrado/Losango")
        print("3. Perímetro de um Retângulo/Paralelogramo")
        print("4. Perímetro de um Trapézio Isósceles")
        print("5. Perímetro de um Trapézio Escaleno")
        print("6. Perímetro de um Polígono Regular")
        print("7. Perímetro de um Círculo")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            perimetroTriangulo()
        elif opcao == "2":
            perimetroQuadrado()
        elif opcao == "3":
            perimetroRetanguloOuParalelogramo()
        elif opcao == "4":
            perimetroTrapezioIsoseleces()
        elif opcao == "5":
            perimetroTrapezioEscaleno()
        elif opcao == "6":
            perimetroPoligonoRegular()
        elif opcao == "7":
            perimetroCirculo()
        elif opcao == "0":
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# 33.
# Faça uma função com menu que reúna os exercícios 22 a 28 (áreas).
def menuAreas():
    while True:
        print("\n=== MENU DE ÁREAS ===")
        print("1. Área de um Triângulo")
        print("2. Área de um Quadrado")
        print("3. Área de um Retângulo")
        print("4. Área de um Losango")
        print("5. Área de um Trapézio")
        print("6. Área de um Polígono Regular")
        print("7. Área de um Círculo")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            areaTriangulo()
        elif opcao == "2":
            areaQuadrado()
        elif opcao == "3":
            areaRetangulo()
        elif opcao == "4":
            areaLosango()
        elif opcao == "5":
            areaTrapezio()
        elif opcao == "6":
            areaPoligonoRegular()
        elif opcao == "7":
            areaCirculo()
        elif opcao == "0":
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Valelifações

# 34.elif Crie uma função que receba horas, minutos e segundos
# e veique se formam um horário válido.
def verifcarHorarioValido():
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))

    if 0 <= horas <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59:
        print("Horário válido.")
    else:
        print("Horário inválido.")    

#um relogio que funciona e e atualizado em tempo real no terminal
def relogio():
    import time
    
    while True:
        print(time.strftime("%H:%M:%S"), end="\r")
        time.sleep(1)
        

# 35.
# Crie uma função que receba 3 segmentos de reta
# e verifique se podem formar um triângulo.
def verificarSeFormarTrianguloComSegmentos():
    a = float(input("Digite o comprimento do primeiro segmento: "))
    b = float(input("Digite o comprimento do segundo segmento: "))
    c = float(input("Digite o comprimento do terceiro segmento: "))

    if a + b > c and a + c > b and b + c > a:
        print("Os segmentos podem formar um triângulo.")
    else:
        print("Os segmentos não podem formar um triângulo.")


# 36.
# Se puder formar um triângulo, classifique:
# Equilátero (3 lados iguais)
# Isósceles (2 lados iguais)
# Escaleno (todos diferentes)

def classificarTriangulo():
    a = float(input("Digite o comprimento do primeiro lado: "))
    b = float(input("Digite o comprimento do segundo lado: "))
    c = float(input("Digite o comprimento do terceiro lado: "))

    if a == b == c:
        print("O triângulo é equilátero.")
    elif a == b or a == c or b == c:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")

# 37.
# Verifique se 3 ângulos podem formar um triângulo.
def verificarSeFormarTrianguloComAngulos():
    angulo1 = float(input("Digite o primeiro ângulo: "))
    angulo2 = float(input("Digite o segundo ângulo: "))
    angulo3 = float(input("Digite o terceiro ângulo: "))

    if angulo1 + angulo2 + angulo3 == 180:
        print("Os ângulos podem formar um triângulo.")
    else:
        print("Os ângulos não podem formar um triângulo.")


# 38.
# Classifique o triângulo pelos ângulos:
# Acutângulo (todos < 90°)
# Retângulo (um = 90°)
# Obtusângulo (um > 90°)
def classificarTrianguloPorAngulos():
    angulo1 = float(input("Digite o primeiro ângulo: "))
    angulo2 = float(input("Digite o segundo ângulo: "))
    angulo3 = float(input("Digite o terceiro ângulo: "))

    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        print("O triângulo é acutângulo.")
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("O triângulo é retângulo.")
    else:
        print("O triângulo é obtusângulo.")

# 39.
# Resolva uma equação do 2º grau:
# ax² + bx + c = 0
# Informar:
# nenhuma raiz
# uma raiz
# duas raízes

def resolverEquacaoSegundoGrau():
    A = float(input("Digite o valor de A: "))
    B = float(input("Digite o valor de B: "))
    C = float(input("Digite o valor de C: "))
    if A == 0:
        print("A equação não é do 2º grau. Use a função para resolver equações do 1º grau.")
    else:
        delta = B**2 - 4*A*C # Δ = -b² - 4ac
        if delta < 0: #porque número negativo não tem raiz quadrada real
            print("A equação não tem raízes reais.")
        elif delta == 0: #o numero 0 tem apenas uma raiz real, que é ele mesmo
            raiz = -B / (2*A) # x = b / 2a
            print(f"A equação tem uma raiz real: {raiz}")
        else: #existem duas raizes reais e diferentes
            #√Δ é a mesma coisa que Δ**1/2 ou Δ**0.5
            x1 = (-B + delta**0.5) / (2*A) #x1 = (-b + √Δ) / 2a   
            x2 = (-B - delta**0.5) / (2*A) #x2 = (-b - √Δ) / 2a 
            print(f"A equação tem duas raízes reais: {x1} e {x2}")
    
# 40.
# Crie uma função que verifique se uma data é válida.
# Entradas: dia, mês, ano
# Considerar meses de 30 e 31 dias, fevereiro e anos bissextos.
def verificarDataValida():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    if mes < 1 or mes > 12:
        print("Mês inválido.")
        return

    if dia < 1:
        print("Dia inválido.")
        return

    if mes in [1, 3, 5, 7, 8, 10, 12]: #meses com 31 dias
        if dia > 31:
            print("Dia inválido para o mês informado.")
            return
    elif mes in [4, 6, 9, 11]: #meses com 30 dias
        if dia > 30:
            print("Dia inválido para o mês informado.")
            return
    else: #fevereiro
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): #ano bissexto
            if dia > 29:
                print("Dia inválido para fevereiro em ano bissexto.")
                return
        else:
            if dia > 28:
                print("Dia inválido para fevereiro em ano não bissexto.")
                return

    print("Data válida.")

#funcao q eu criei para resolver de um outro jeito os exercicios abaixo
def nPorExtenso(num: int) -> str:
    if num < 0:
        return "menos " + nPorExtenso(-num)
    if num == 0:
        return "zero"

    unidades = {
        1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
        6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez",
        11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze",
        16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove"
    }
    dezenas = {
        20: "vinte", 30: "trinta", 40: "quarenta", 50: "cinquenta",
        60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa"
    }
    centenas = {
        100: "cem", 200: "duzentos", 300: "trezentos", 400: "quatrocentos",
        500: "quinhentos", 600: "seiscentos", 700: "setecentos",
        800: "oitocentos", 900: "novecentos"
    }

    partes = []
    # centenas
    if num >= 100:
        c = (num // 100) * 100
        if num == 100:
            partes.append("cem")
        else:
            partes.append(centenas[c])
        num %= 100
        if num:
            partes.append("e")
    # dezenas e unidades
    if num >= 20:
        d = (num // 10) * 10
        partes.append(dezenas[d])
        num %= 10
        if num:
            partes.append("e")
    if 0 < num < 20:
        partes.append(unidades[num])

    return " ".join(partes)

#funcao para criar funocoes de if, elif e else
def gerarFuncaoIfElseComNPorExtenso():
    
    minimo = int(input("Digite o número mínimo: "))
    maximo = int(input("Digite o número máximo: "))

    if minimo > maximo:
        print("Erro: o número mínimo não pode ser maior que o máximo.")
        return

    # Definição automática do nome da função gerada
    if minimo == 0:
        nomeFuncao = f"n{maximo}ToExtensoIfElse"
    elif minimo < 0:
        nomeFuncao = f"nMenos{abs(minimo)}a{maximo}ToExtensoIfElse"
    else:
        # numero minimo maior que 0, maniaco
        nomeFuncao = f"n{minimo}a{maximo}ToExtensoIfElse"

    nomeArquivo = f"{nomeFuncao}.txt"

    with open(nomeArquivo, "w", encoding="utf-8") as f:

        # Cabeçalho da função gerada
        f.write(f"def {nomeFuncao}():\n")
        f.write(
            f'    numero = int(input("Digite um número entre {minimo} e {maximo}: "))\n'
        )
        f.write(f"    if numero < {minimo} or numero > {maximo}:\n")
        f.write('        print("Fora do intervalo permitido.")\n')
        f.write("        return\n")

        # Geração dos if / elif
        for i in range(minimo, maximo + 1):
            if i == minimo:
                f.write(f"    if numero == {i}:\n")
            else:
                f.write(f"    elif numero == {i}:\n")

            f.write(f'        print("{nPorExtenso(i)}")\n')

    print(f"Arquivo '{nomeArquivo}' gerado com sucesso.")

def gerarFuncaoIfElseSemNPorExtenso():
    minimo = int(input("Digite o número mínimo: "))
    maximo = int(input("Digite o número máximo: "))
    if minimo > maximo:
        print("Erro: o número mínimo não pode ser maior que o máximo.")
        return
    #nome da funcao
    if minimo == 0:
        nomeFuncao = f"n{maximo}ToExtensoIfElse"
    elif minimo < 0:
        nomeFuncao = f"nMenos{abs(minimo)}a{maximo}ToExtensoIfElse" # abs porque o numero minimo é negativo, entao tem que tirar o sinal de menos pra ficar bonitinho no nome da funcao
    else:
        nomeFuncao = f"n{minimo}a{maximo}ToExtensoIfElse"
    nomeArquivo = f"{nomeFuncao}.txt"
    #tabelas
    unidades = [
        "zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove"
    ]
    dezADezenove = [
        "dez", "onze", "doze", "treze", "quatorze",
        "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"
    ]
    dezenas = [
        "", "", "vinte", "trinta", "quarenta",
        "cinquenta", "oitenta", "noventa"
    ]
    centenas = [
        "", "cento", "duzentos", "trezentos", "quatrocentos",
        "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"
    ]
    with open(nomeArquivo, "w", encoding="utf-8") as f:
        #cabecalho da função gerada
        f.write(f"def {nomeFuncao}():\n")
        f.write(
            f'    numero = int(input("Digite um número entre {minimo} e {maximo}: "))\n'
        )
        f.write(f"    if numero < {minimo} or numero > {maximo}:\n")
        f.write('        print("Fora do intervalo permitido.")\n')
        f.write("        return\n\n")
        for i in range(minimo, maximo + 1):
            #conversao para extenso
            n = i
            texto = ""
            if n < 0:
                texto += "menos "
                n = -n
            if n == 0:
                texto += "zero"
            elif n == 100:
                texto += "cem"
            else:
                partes = []
                c = n // 100
                d = (n % 100) // 10
                u = n % 10
                if c > 0:
                    partes.append(centenas[c])
                if d == 1:
                    partes.append(dezADezenove[u])
                else:
                    if d > 1:
                        partes.append(dezenas[d])
                    if u > 0:
                        partes.append(unidades[u])
                texto += " e ".join(partes)
            #escrita do if/elif
            if i == minimo:
                f.write(f"    if numero == {i}:\n")
            else:
                f.write(f"    elif numero == {i}:\n")
            f.write(f'        print("{texto}")\n')
    print(f"Arquivo '{nomeArquivo}' gerado com sucesso.")


# 41.
# Receba um número até 9 e escreva por extenso.
# Exemplo: 5 → cinco

#usando a biblioteca num2words
def n9ToExtensoNum2Words():
    from num2words import num2words
    numero = int(input("Digite um número até 9: "))
    print(num2words(numero, lang='pt_BR'))


#versão com cadeia de if/elif/else
def n9ToExtensoIfElse():
    numero = int(input("Digite um número até 9: "))
    if numero < 0 or numero > 9:
        print("Fora do intervalo permitido.")
    if numero == 0:
        print("zero")
    elif numero == 1:
        print("um")
    elif numero == 2:
        print("dois")
    elif numero == 3:
        print("três")
    elif numero == 4:
        print("quatro")
    elif numero == 5:
        print("cinco")
    elif numero == 6:
        print("seis")
    elif numero == 7:
        print("sete")
    elif numero == 8:
        print("oito")
    else:
        print("nove")




def n9ToExtenso2Func():
    numero = int(input("Digite um número até 9: "))
    if numero < 0 or numero > 9:
        print("Fora do intervalo permitido.")
    else:
        print(nPorExtenso(numero))

# 42.
# Receba um número até 99 e escreva por extenso.

def n99ToExtensoNum2Words():
    from num2words import num2words
    numero = int(input("Digite um número até 99: "))
    print(num2words(numero, lang='pt_BR'))


# para versao if  else, use gerarFuncaoIfElseSemNPorExtenso() ou gerarFuncaoIfElseComNPorExtenso() 

def n99ToExtenso2Func():
    numero = int(input("Digite um número até 99: "))
    if numero < 0 or numero > 99:
        print("Fora do intervalo permitido.")
    else:
        print(nPorExtenso(numero))
# 43.
# Receba um número até 999 e escreva por extenso.

def n999ToExtensoNum2Words():
    from num2words import num2words
    numero = int(input("Digite um número até 999: "))
    print(num2words(numero, lang='pt_BR'))

# para versao if  else, use gerarFuncaoIfElseSemNPorExtenso() ou gerarFuncaoIfElseComNPorExtenso() 


def n999ToExtenso2Func():
    numero = int(input("Digite um número até 999: "))
    if numero < 0 or numero > 999:
        print("Fora do intervalo permitido.")
    else:
        print(nPorExtenso(numero))



# 44.
# Faça uma função em Python que solicite a digitação de um número natural entre -9 e 9,
# escrevendo então na tela o valor fornecido por extenso.
# Versões: biblioteca, if/elif, usando a funcao nPorExtenso que criei.

def nMenos9a9ToExtensoNum2Words():
    from num2words import num2words
    numero = int(input("Digite um número natural entre -9 e 9: "))
    print(num2words(numero, lang='pt_BR'))


def nMenos9a9ToExtensoIfElse():
    numero = int(input("Digite um número entre -9 e 9: "))
    if numero < -9 or numero > 9:
        print("Fora do intervalo permitido.")
        return
    if numero == -9:
        print("menos nove")
    elif numero == -8:
        print("menos oito")
    elif numero == -7:
        print("menos sete")
    elif numero == -6:
        print("menos seis")
    elif numero == -5:
        print("menos cinco")
    elif numero == -4:
        print("menos quatro")
    elif numero == -3:
        print("menos três")
    elif numero == -2:
        print("menos dois")
    elif numero == -1:
        print("menos um")
    elif numero == 0:
        print("zero")
    elif numero == 1:
        print("um")
    elif numero == 2:
        print("dois")
    elif numero == 3:
        print("três")
    elif numero == 4:
        print("quatro")
    elif numero == 5:
        print("cinco")
    elif numero == 6:
        print("seis")
    elif numero == 7:
        print("sete")
    elif numero == 8:
        print("oito")
    elif numero == 9:
        print("nove")

def nMenos9a9ToExtenso2Func():
    numero = int(input("Digite um número natural entre -9 e 9: "))
    if numero < -9 or numero > 9:
        print("Fora do intervalo permitido.")
    else:
        print(nPorExtenso(numero))

# 45.
# Faça uma função em Python que solicite a digitação de um número natural entre -99 e 99,
# escrevendo então na tela o valor fornecido por extenso.
# Versões: biblioteca, if/elif, usando a funcao nPorExtenso que criei.

def nMenos99a99ToExtensoNum2Words():
    from num2words import num2words
    numero = int(input("Digite um número natural entre -99 e 99: "))
    print(num2words(numero, lang='pt_BR'))


# para versao if  else, use gerarFuncaoIfElseSemNPorExtenso() ou gerarFuncaoIfElseComNPorExtenso() 



def nMenos99a99ToExtenso2Func():
    numero = int(input("Digite um número natural entre -99 e 99: "))
    if numero < -99 or numero > 99:
        print("Fora do intervalo permitido.")
    else:
        print(nPorExtenso(numero))

# 46.
# Faça uma função em Python que solicite a digitação de um número natural entre -999 e 999,
# escrevendo então na tela o valor fornecido por extenso.
# Versões: biblioteca, if/elif, helper.

def nMenos999a999ToExtensoNum2Words():
    from num2words import num2words
    numero = int(input("Digite um número natural entre -999 e 999: "))
    print(num2words(numero, lang='pt_BR'))

# para versao if  else, use gerarFuncaoIfElseSemNPorExtenso() ou gerarFuncaoIfElseComNPorExtenso() 

def nMenos999a999ToExtenso2Func():
    numero = int(input("Digite um número natural entre -999 e 999: "))
    if numero < -999 or numero > 999:
        print("Fora do intervalo permitido.")
    else:
        print(nPorExtenso(numero))
        
        
        
        
# funcao para gerar as funcoes dos exercicios de valor monetario com if else
def gerarFuncaoValorMonetarioIfElse():
    nomeFuncao = "valorMonetarioExtensoIfElse"
    nomeArquivo = f"{nomeFuncao}.txt"
    with open(nomeArquivo, "w", encoding="utf-8") as f:
        f.write(f"def {nomeFuncao}():\n")
        f.write('    try:\n')
        f.write('        valor = float(input("Digite um valor entre -9.99 e 9.99: ").replace(",", "."))\n')
        f.write('        if valor < -9.99 or valor > 9.99:\n')
        f.write('            raise ValueError\n')
        f.write('        if valor == 0:\n')
        f.write('            print("zero reais")\n')
        f.write('            return\n')
        f.write('        negativo = valor < 0\n')
        f.write('        valor = abs(valor)\n')
        f.write('        reais = int(valor)\n')
        f.write('        centavos = int(round((valor - reais) * 100))\n')
        f.write('        resultado = []\n\n')
        # negativo
        f.write('        if negativo:\n')
        f.write('            resultado.append("menos")\n\n')
        for i, texto in [
            (1, "um real"), (2, "dois reais"), (3, "três reais"),
            (4, "quatro reais"), (5, "cinco reais"), (6, "seis reais"),
            (7, "sete reais"), (8, "oito reais"), (9, "nove reais")
        ]:
            if i == 1:
                f.write(f'        if reais == {i}:\n')
            else:
                f.write(f'        elif reais == {i}:\n')
            f.write(f'            resultado.append("{texto}")\n')
        f.write('\n        if centavos > 0:\n')
        f.write('            if reais > 0:\n')
        f.write('                resultado.append("e")\n')
        centavos_extenso = {
            1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
            6: "seis", 7: "sete", 8: "oito", 9: "nove",
            10: "dez", 11: "onze", 12: "doze", 13: "treze",
            14: "quatorze", 15: "quinze", 16: "dezesseis",
            17: "dezessete", 18: "dezoito", 19: "dezenove",
            20: "vinte", 21: "vinte e um", 22: "vinte e dois",
            23: "vinte e três", 24: "vinte e quatro",
            25: "vinte e cinco", 26: "vinte e seis",
            27: "vinte e sete", 28: "vinte e oito",
            29: "vinte e nove", 30: "trinta",
            31: "trinta e um", 32: "trinta e dois",
            33: "trinta e três", 34: "trinta e quatro",
            35: "trinta e cinco", 36: "trinta e seis",
            37: "trinta e sete", 38: "trinta e oito",
            39: "trinta e nove", 40: "quarenta",
            41: "quarenta e um", 42: "quarenta e dois",
            43: "quarenta e três", 44: "quarenta e quatro",
            45: "quarenta e cinco", 46: "quarenta e seis",
            47: "quarenta e sete", 48: "quarenta e oito",
            49: "quarenta e nove", 50: "cinquenta",
            51: "cinquenta e um", 52: "cinquenta e dois",
            53: "cinquenta e três", 54: "cinquenta e quatro",
            55: "cinquenta e cinco", 56: "cinquenta e seis",
            57: "cinquenta e sete", 58: "cinquenta e oito",
            59: "cinquenta e nove", 60: "sessenta",
            61: "sessenta e um", 62: "sessenta e dois",
            63: "sessenta e três", 64: "sessenta e quatro",
            65: "sessenta e cinco", 66: "sessenta e seis",
            67: "sessenta e sete", 68: "sessenta e oito",
            69: "sessenta e nove", 70: "setenta",
            71: "setenta e um", 72: "setenta e dois",
            73: "setenta e três", 74: "setenta e quatro",
            75: "setenta e cinco", 76: "setenta e seis",
            77: "setenta e sete", 78: "setenta e oito",
            79: "setenta e nove", 80: "oitenta",
            81: "oitenta e um", 82: "oitenta e dois",
            83: "oitenta e três", 84: "oitenta e quatro",
            85: "oitenta e cinco", 86: "oitenta e seis",
            87: "oitenta e sete", 88: "oitenta e oito",
            89: "oitenta e nove", 90: "noventa",
            91: "noventa e um", 92: "noventa e dois",
            93: "noventa e três", 94: "noventa e quatro",
            95: "noventa e cinco", 96: "noventa e seis",
            97: "noventa e sete", 98: "noventa e oito",
            99: "noventa e nove"
        }
        primeiro = True
        for c in range(1, 100):
            if primeiro:
                f.write(f'            if centavos == {c}:\n')
                primeiro = False
            else:
                f.write(f'            elif centavos == {c}:\n')
            f.write(f'                resultado.append("{centavos_extenso[c]} centavos")\n')
        f.write('\n        print(" ".join(resultado))\n')
        f.write('    except ValueError:\n')
        f.write('        print("Entrada inválida. Digite um valor válido entre -9,99 e 9,99.")\n')
    print(f"Arquivo '{nomeArquivo}' gerado com sucesso.")        


# 47.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -9,99 e R$ 9,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.


#versao n2words
def valorMonetarioExtensoMenos9a9N2Words():
    from n2words import n2words
    try:
        valor = float(input("Digite um valor entre -9.99 e 9.99: ").replace(",", "."))
        if valor < -9.99 or valor > 9.99:
            raise ValueError("Valor fora do intervalo permitido.") #podia ser print com return mas queria testar assim
        if valor == 0:
            print("zero reais")
            return
        negativo = valor < 0 # verifica se o valor e negativo (true or false)
        valor = abs(valor) # transforma o valor em positivo para facilitar a conversao
        reais = int(valor) # valor em reais
        centavos = int(round((valor - reais) * 100)) #valor em centavos, valor-reais = centavos, e faz * 100 para converter para centavos, round arredonda
        partes = [] # lista das palavras 
        if negativo:
            partes.append("menos") # se for negativo adiciona menos na frente
        if reais > 0:
            reaisExt = n2words(reais, lang="pt_BR") # converte reais para extenso
            partes.append(reaisExt) # adiciona reais na lista
            partes.append("real" if reais == 1 else "reais") # adiciona a palavra real/reais na lista
        if centavos > 0: 
            centavosExt = n2words(centavos, lang="pt_BR") # converte centavos para extenso
            partes.append(centavosExt)  # adiciona centavos na lista
            partes.append("centavo" if centavos == 1 else "centavos") # adiciona a palavra centavo/centavos na lista
        print(" ".join(partes)) # junta as partes
    except ValueError:
        print("Entrada inválida. Digite um número válido entre -9,99 e 9,99.")

#versao if/else
def valorMonetarioExtensoIfElse():
    try:
        valor = float(input("Digite um valor entre -9.99 e 9.99: ").replace(",", "."))
        if valor < -9.99 or valor > 9.99:
            raise ValueError("Fora do intervalo")
        if valor == 0:
            print("zero reais")
            return
        negativo = valor < 0
        valor = abs(valor)
        reais = int(valor)
        centavos = int(round((valor - reais) * 100))
        resultado = []
        if negativo:
            resultado.append("menos")
        if reais == 1:
            resultado.append("um real")
        elif reais == 2:
            resultado.append("dois reais")
        elif reais == 3:
            resultado.append("três reais")
        elif reais == 4:
            resultado.append("quatro reais")
        elif reais == 5:
            resultado.append("cinco reais")
        elif reais == 6:
            resultado.append("seis reais")
        elif reais == 7:
            resultado.append("sete reais")
        elif reais == 8:
            resultado.append("oito reais")
        elif reais == 9:
            resultado.append("nove reais")
            
        if centavos > 0:
            if reais > 0:
                resultado.append(" e ")
            if centavos == 1:
                resultado.append("um centavo")
            elif centavos == 2:
                resultado.append("dois centavos")
            elif centavos == 3:
                resultado.append("três centavos")
            elif centavos == 4:
                resultado.append("quatro centavos")
            elif centavos == 5:
                resultado.append("cinco centavos")
            elif centavos == 6:
                resultado.append("seis centavos")
            elif centavos == 7:
                resultado.append("sete centavos")
            elif centavos == 8:
                resultado.append("oito centavos")
            elif centavos == 9:
                resultado.append("nove centavos")
            elif centavos == 10:
                resultado.append("dez centavos")
            elif centavos == 11:
                resultado.append("onze centavos")
            elif centavos == 12:
                resultado.append("doze centavos")
            elif centavos == 13:
                resultado.append("treze centavos")
            elif centavos == 14:
                resultado.append("quatorze centavos")
            elif centavos == 15:
                resultado.append("quinze centavos")
            elif centavos == 16:
                resultado.append("dezesseis centavos")
            elif centavos == 17:
                resultado.append("dezessete centavos")
            elif centavos == 18:
                resultado.append("dezoito centavos")
            elif centavos == 19:
                resultado.append("dezenove centavos")
            elif centavos == 20:
                resultado.append("vinte centavos")
            elif centavos == 21:
                resultado.append("vinte e um centavos")
            elif centavos == 22:
                resultado.append("vinte e dois centavos")
            elif centavos == 23:
                resultado.append("vinte e três centavos")
            elif centavos == 24:
                resultado.append("vinte e quatro centavos")
            elif centavos == 25:
                resultado.append("vinte e cinco centavos")
            elif centavos == 26:
                resultado.append("vinte e seis centavos")
            elif centavos == 27:
                resultado.append("vinte e sete centavos")
            elif centavos == 28:
                resultado.append("vinte e oito centavos")
            elif centavos == 29:
                resultado.append("vinte e nove centavos")
            elif centavos == 30:
                resultado.append("trinta centavos")
            elif centavos == 31:
                resultado.append("trinta e um centavos")
            elif centavos == 32:
                resultado.append("trinta e dois centavos")
            elif centavos == 33:
                resultado.append("trinta e três centavos")
            elif centavos == 34:
                resultado.append("trinta e quatro centavos")
            elif centavos == 35:
                resultado.append("trinta e cinco centavos")
            elif centavos == 36:
                resultado.append("trinta e seis centavos")
            elif centavos == 37:
                resultado.append("trinta e sete centavos")
            elif centavos == 38:
                resultado.append("trinta e oito centavos")
            elif centavos == 39:
                resultado.append("trinta e nove centavos")
            elif centavos == 40:
                resultado.append("quarenta centavos")
            elif centavos == 41:
                resultado.append("quarenta e um centavos")
            elif centavos == 42:
                resultado.append("quarenta e dois centavos")
            elif centavos == 43:
                resultado.append("quarenta e três centavos")
            elif centavos == 44:
                resultado.append("quarenta e quatro centavos")
            elif centavos == 45:
                resultado.append("quarenta e cinco centavos")
            elif centavos == 46:
                resultado.append("quarenta e seis centavos")
            elif centavos == 47:
                resultado.append("quarenta e sete centavos")
            elif centavos == 48:
                resultado.append("quarenta e oito centavos")
            elif centavos == 49:
                resultado.append("quarenta e nove centavos")
            elif centavos == 50:
                resultado.append("cinquenta centavos")
            elif centavos == 51:
                resultado.append("cinquenta e um centavos")
            elif centavos == 52:
                resultado.append("cinquenta e dois centavos")
            elif centavos == 53:
                resultado.append("cinquenta e três centavos")
            elif centavos == 54:
                resultado.append("cinquenta e quatro centavos")
            elif centavos == 55:
                resultado.append("cinquenta e cinco centavos")
            elif centavos == 56:
                resultado.append("cinquenta e seis centavos")
            elif centavos == 57:
                resultado.append("cinquenta e sete centavos")
            elif centavos == 58:
                resultado.append("cinquenta e oito centavos")
            elif centavos == 59:
                resultado.append("cinquenta e nove centavos")
            elif centavos == 60:
                resultado.append("sessenta centavos")
            elif centavos == 61:
                resultado.append("sessenta e um centavos")
            elif centavos == 62:
                resultado.append("sessenta e dois centavos")
            elif centavos == 63:
                resultado.append("sessenta e três centavos")
            elif centavos == 64:
                resultado.append("sessenta e quatro centavos")
            elif centavos == 65:
                resultado.append("sessenta e cinco centavos")
            elif centavos == 66:
                resultado.append("sessenta e seis centavos")
            elif centavos == 67:
                resultado.append("sessenta e sete centavos")
            elif centavos == 68:
                resultado.append("sessenta e oito centavos")
            elif centavos == 69:
                resultado.append("sessenta e nove centavos")
            elif centavos == 70:
                resultado.append("setenta centavos")
            elif centavos == 71:
                resultado.append("setenta e um centavos")
            elif centavos == 72:
                resultado.append("setenta e dois centavos")
            elif centavos == 73:
                resultado.append("setenta e três centavos")
            elif centavos == 74:
                resultado.append("setenta e quatro centavos")
            elif centavos == 75:
                resultado.append("setenta e cinco centavos")
            elif centavos == 76:
                resultado.append("setenta e seis centavos")
            elif centavos == 77:
                resultado.append("setenta e sete centavos")
            elif centavos == 78:
                resultado.append("setenta e oito centavos")
            elif centavos == 79:
                resultado.append("setenta e nove centavos")
            elif centavos == 80:
                resultado.append("oitenta centavos")
            elif centavos == 81:
                resultado.append("oitenta e um centavos")
            elif centavos == 82:
                resultado.append("oitenta e dois centavos")
            elif centavos == 83:
                resultado.append("oitenta e três centavos")
            elif centavos == 84:
                resultado.append("oitenta e quatro centavos")
            elif centavos == 85:
                resultado.append("oitenta e cinco centavos")
            elif centavos == 86:
                resultado.append("oitenta e seis centavos")
            elif centavos == 87:
                resultado.append("oitenta e sete centavos")
            elif centavos == 88:
                resultado.append("oitenta e oito centavos")
            elif centavos == 89:
                resultado.append("oitenta e nove centavos")
            elif centavos == 90:
                resultado.append("noventa centavos")
            elif centavos == 91:
                resultado.append("noventa e um centavos")
            elif centavos == 92:
                resultado.append("noventa e dois centavos")
            elif centavos == 93:
                resultado.append("noventa e três centavos")
            elif centavos == 94:
                resultado.append("noventa e quatro centavos")
            elif centavos == 95:
                resultado.append("noventa e cinco centavos")
            elif centavos == 96:
                resultado.append("noventa e seis centavos")
            elif centavos == 97:
                resultado.append("noventa e sete centavos")
            elif centavos == 98:
                resultado.append("noventa e oito centavos")
            elif centavos == 99:
                resultado.append("noventa e nove centavos")
        print(resultado)
    except ValueError:
        print("Entrada inválida. Digite um valor válido entre -9,99 e 9,99.")




# 48.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -99,99 e R$ 99,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.

#versao n2words
def valorMonetarioExtensoMenos99a99N2Words():
    from n2words import n2words
    try:
        valor = float(input("Digite um valor entre -99.99 e 99.99: ").replace(",", "."))
        if valor < -99.99 or valor > 99.99:
            raise ValueError("Valor fora do intervalo permitido.") #podia ser print com return mas queria testar assim
        if valor == 0:
            print("zero reais")
            return
        negativo = valor < 0 # verifica se o valor e negativo (true or false)
        valor = abs(valor) # transforma o valor em positivo para facilitar a conversao
        reais = int(valor) # valor em reais
        centavos = int(round((valor - reais) * 100)) #valor em centavos, valor-reais = centavos, e faz * 100 para converter para centavos, round arredonda
        partes = [] # lista das palavras 
        if negativo:
            partes.append("menos") # se for negativo adiciona menos na frente
        if reais > 0:
            reaisExt = n2words(reais, lang="pt_BR") # converte reais para extenso
            partes.append(reaisExt) # adiciona reais na lista
            partes.append("real" if reais == 1 else "reais") # adiciona a palavra real/reais na lista
        if centavos > 0: 
            centavosExt = n2words(centavos, lang="pt_BR") # converte centavos para extenso
            partes.append(centavosExt)  # adiciona centavos na lista
            partes.append("centavo" if centavos == 1 else "centavos") # adiciona a palavra centavo/centavos na lista
        print(" ".join(partes)) # junta as partes
    except ValueError:
        print("Entrada inválida. Digite um número válido entre -99,99 e 99,99.")

# para versao if else, use a  gerarFuncaoValorMonetarioIfElse()

# 49.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -999,99 e R$ 999,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.

#versao n2words
def valorMonetarioExtensoMenos999a999N2Words():
    from n2words import n2words
    try:
        valor = float(input("Digite um valor entre -999.99 e 999.99: ").replace(",", "."))
        if valor < -999.99 or valor > 999.99:
            raise ValueError("Valor fora do intervalo permitido.") #podia ser print com return mas queria testar assim
        if valor == 0:
            print("zero reais")
            return
        negativo = valor < 0 # verifica se o valor e negativo (true or false)
        valor = abs(valor) # transforma o valor em positivo para facilitar a conversao
        reais = int(valor) # valor em reais
        centavos = int(round((valor - reais) * 100)) #valor em centavos, valor-reais = centavos, e faz * 100 para converter para centavos, round arredonda
        partes = [] # lista das palavras 
        if negativo:
            partes.append("menos") # se for negativo adiciona menos na frente
        if reais > 0:
            reaisExt = n2words(reais, lang="pt_BR") # converte reais para extenso
            partes.append(reaisExt) # adiciona reais na lista
            partes.append("real" if reais == 1 else "reais") # adiciona a palavra real/reais na lista
        if centavos > 0: 
            centavosExt = n2words(centavos, lang="pt_BR") # converte centavos para extenso
            partes.append(centavosExt)  # adiciona centavos na lista
            partes.append("centavo" if centavos == 1 else "centavos") # adiciona a palavra centavo/centavos na lista
        print(" ".join(partes)) # junta as partes
    except ValueError:
        print("Entrada inválida. Digite um número válido entre -999,99 e 999,99.")
        
# para versao if else, use a  gerarFuncaoValorMonetarioIfElse()
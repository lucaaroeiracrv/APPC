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
    while True:
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
                break
            else:
                print("Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Tente novamente.")

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
        nomeFuncao = f"nMenos{abs(minimo)}a{maximo}ToExtensoIfElse"
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

gerarFuncaoIfElseComNPorExtenso()

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


def n99ToExtensoIfElse():
    numero = int(input("Digite um número até 99: "))
    if numero < 0 or numero > 99:
        print("Fora do intervalo permitido.")
        return
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
    elif numero == 9:
        print("nove")
    elif numero == 10:
        print("dez")
    elif numero == 11:
        print("onze")
    elif numero == 12:
        print("doze")
    elif numero == 13:
        print("treze")
    elif numero == 14:
        print("quatorze")
    elif numero == 15:
        print("quinze")
    elif numero == 16:
        print("dezesseis")
    elif numero == 17:
        print("dezessete")
    elif numero == 18:
        print("dezoito")
    elif numero == 19:
        print("dezenove")
    elif numero == 20:
        print("vinte")
    elif numero == 21:
        print("vinte e um")
    elif numero == 22:
        print("vinte e dois")
    elif numero == 23:
        print("vinte e três")
    elif numero == 24:
        print("vinte e quatro")
    elif numero == 25:
        print("vinte e cinco")
    elif numero == 26:
        print("vinte e seis")
    elif numero == 27:
        print("vinte e sete")
    elif numero == 28:
        print("vinte e oito")
    elif numero == 29:
        print("vinte e nove")
    elif numero == 30:
        print("trinta")
    elif numero == 31:
        print("trinta e um")
    elif numero == 32:
        print("trinta e dois")
    elif numero == 33:
        print("trinta e três")
    elif numero == 34:
        print("trinta e quatro")
    elif numero == 35:
        print("trinta e cinco")
    elif numero == 36:
        print("trinta e seis")
    elif numero == 37:
        print("trinta e sete")
    elif numero == 38:
        print("trinta e oito")
    elif numero == 39:
        print("trinta e nove")
    elif numero == 40:
        print("quarenta")
    elif numero == 41:
        print("quarenta e um")
    elif numero == 42:
        print("quarenta e dois")
    elif numero == 43:
        print("quarenta e três")
    elif numero == 44:
        print("quarenta e quatro")
    elif numero == 45:
        print("quarenta e cinco")
    elif numero == 46:
        print("quarenta e seis")
    elif numero == 47:
        print("quarenta e sete")
    elif numero == 48:
        print("quarenta e oito")
    elif numero == 49:
        print("quarenta e nove")
    elif numero == 50:
        print("cinquenta")
    elif numero == 51:
        print("cinquenta e um")
    elif numero == 52:
        print("cinquenta e dois")
    elif numero == 53:
        print("cinquenta e três")
    elif numero == 54:
        print("cinquenta e quatro")
    elif numero == 55:
        print("cinquenta e cinco")
    elif numero == 56:
        print("cinquenta e seis")
    elif numero == 57:
        print("cinquenta e sete")
    elif numero == 58:
        print("cinquenta e oito")
    elif numero == 59:
        print("cinquenta e nove")
    elif numero == 60:
        print("sessenta")
    elif numero == 61:
        print("sessenta e um")
    elif numero == 62:
        print("sessenta e dois")
    elif numero == 63:
        print("sessenta e três")
    elif numero == 64:
        print("sessenta e quatro")
    elif numero == 65:
        print("sessenta e cinco")
    elif numero == 66:
        print("sessenta e seis")
    elif numero == 67:
        print("sessenta e sete")
    elif numero == 68:
        print("sessenta e oito")
    elif numero == 69:
        print("sessenta e nove")
    elif numero == 70:
        print("setenta")
    elif numero == 71:
        print("setenta e um")
    elif numero == 72:
        print("setenta e dois")
    elif numero == 73:
        print("setenta e três")
    elif numero == 74:
        print("setenta e quatro")
    elif numero == 75:
        print("setenta e cinco")
    elif numero == 76:
        print("setenta e seis")
    elif numero == 77:
        print("setenta e sete")
    elif numero == 78:
        print("setenta e oito")
    elif numero == 79:
        print("setenta e nove")
    elif numero == 80:
        print("oitenta")
    elif numero == 81:
        print("oitenta e um")
    elif numero == 82:
        print("oitenta e dois")
    elif numero == 83:
        print("oitenta e três")
    elif numero == 84:
        print("oitenta e quatro")
    elif numero == 85:
        print("oitenta e cinco")
    elif numero == 86:
        print("oitenta e seis")
    elif numero == 87:
        print("oitenta e sete")
    elif numero == 88:
        print("oitenta e oito")
    elif numero == 89:
        print("oitenta e nove")
    elif numero == 90:
        print("noventa")
    elif numero == 91:
        print("noventa e um")
    elif numero == 92:
        print("noventa e dois")
    elif numero == 93:
        print("noventa e três")
    elif numero == 94:
        print("noventa e quatro")
    elif numero == 95:
        print("noventa e cinco")
    elif numero == 96:
        print("noventa e seis")
    elif numero == 97:
        print("noventa e sete")
    elif numero == 98:
        print("noventa e oito")
    else:
        print("noventa e nove")

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

def n999ToExtensoIfElse():
    numero = int(input("Digite um número até 999: "))
    if numero < 0 or numero > 999:
        print("Fora do intervalo permitido.")
        return

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
    elif numero == 9:
        print("nove")
    elif numero == 10:
        print("dez")
    elif numero == 11:
        print("onze")
    elif numero == 12:
        print("doze")
    elif numero == 13:
        print("treze")
    elif numero == 14:
        print("quatorze")
    elif numero == 15:
        print("quinze")
    elif numero == 16:
        print("dezesseis")
    elif numero == 17:
        print("dezessete")
    elif numero == 18:
        print("dezoito")
    elif numero == 19:
        print("dezenove")
    elif numero == 20:
        print("vinte")
    elif numero == 21:
        print("vinte e um")
    elif numero == 22:
        print("vinte e dois")
    elif numero == 23:
        print("vinte e três")
    elif numero == 24:
        print("vinte e quatro")
    elif numero == 25:
        print("vinte e cinco")
    elif numero == 26:
        print("vinte e seis")
    elif numero == 27:
        print("vinte e sete")
    elif numero == 28:
        print("vinte e oito")
    elif numero == 29:
        print("vinte e nove")
    elif numero == 30:
        print("trinta")
    elif numero == 31:
        print("trinta e um")
    elif numero == 32:
        print("trinta e dois")
    elif numero == 33:
        print("trinta e três")
    elif numero == 34:
        print("trinta e quatro")
    elif numero == 35:
        print("trinta e cinco")
    elif numero == 36:
        print("trinta e seis")
    elif numero == 37:
        print("trinta e sete")
    elif numero == 38:
        print("trinta e oito")
    elif numero == 39:
        print("trinta e nove")
    elif numero == 40:
        print("quarenta")
    elif numero == 41:
        print("quarenta e um")
    elif numero == 42:
        print("quarenta e dois")
    elif numero == 43:
        print("quarenta e três")
    elif numero == 44:
        print("quarenta e quatro")
    elif numero == 45:
        print("quarenta e cinco")
    elif numero == 46:
        print("quarenta e seis")
    elif numero == 47:
        print("quarenta e sete")
    elif numero == 48:
        print("quarenta e oito")
    elif numero == 49:
        print("quarenta e nove")
    elif numero == 50:
        print("cinquenta")
    elif numero == 51:
        print("cinquenta e um")
    elif numero == 52:
        print("cinquenta e dois")
    elif numero == 53:
        print("cinquenta e três")
    elif numero == 54:
        print("cinquenta e quatro")
    elif numero == 55:
        print("cinquenta e cinco")
    elif numero == 56:
        print("cinquenta e seis")
    elif numero == 57:
        print("cinquenta e sete")
    elif numero == 58:
        print("cinquenta e oito")
    elif numero == 59:
        print("cinquenta e nove")
    elif numero == 60:
        print("sessenta")
    elif numero == 61:
        print("sessenta e um")
    elif numero == 62:
        print("sessenta e dois")
    elif numero == 63:
        print("sessenta e três")
    elif numero == 64:
        print("sessenta e quatro")
    elif numero == 65:
        print("sessenta e cinco")
    elif numero == 66:
        print("sessenta e seis")
    elif numero == 67:
        print("sessenta e sete")
    elif numero == 68:
        print("sessenta e oito")
    elif numero == 69:
        print("sessenta e nove")
    elif numero == 70:
        print("setenta")
    elif numero == 71:
        print("setenta e um")
    elif numero == 72:
        print("setenta e dois")
    elif numero == 73:
        print("setenta e três")
    elif numero == 74:
        print("setenta e quatro")
    elif numero == 75:
        print("setenta e cinco")
    elif numero == 76:
        print("setenta e seis")
    elif numero == 77:
        print("setenta e sete")
    elif numero == 78:
        print("setenta e oito")
    elif numero == 79:
        print("setenta e nove")
    elif numero == 80:
        print("oitenta")
    elif numero == 81:
        print("oitenta e um")
    elif numero == 82:
        print("oitenta e dois")
    elif numero == 83:
        print("oitenta e três")
    elif numero == 84:
        print("oitenta e quatro")
    elif numero == 85:
        print("oitenta e cinco")
    elif numero == 86:
        print("oitenta e seis")
    elif numero == 87:
        print("oitenta e sete")
    elif numero == 88:
        print("oitenta e oito")
    elif numero == 89:
        print("oitenta e nove")
    elif numero == 90:
        print("noventa")
    elif numero == 91:
        print("noventa e um")
    elif numero == 92:
        print("noventa e dois")
    elif numero == 93:
        print("noventa e três")
    elif numero == 94:
        print("noventa e quatro")
    elif numero == 95:
        print("noventa e cinco")
    elif numero == 96:
        print("noventa e seis")
    elif numero == 97:
        print("noventa e sete")
    elif numero == 98:
        print("noventa e oito")
    elif numero == 99:
        print("noventa e nove")
    elif numero == 100:
        print("cem")
    elif numero == 101:
        print("cem e um")
    elif numero == 102:
        print("cem e dois")
    elif numero == 103:
        print("cem e três")
    elif numero == 104:
        print("cem e quatro")
    elif numero == 105:
        print("cem e cinco")
    elif numero == 106:
        print("cem e seis")
    elif numero == 107:
        print("cem e sete")
    elif numero == 108:
        print("cem e oito")
    elif numero == 109:
        print("cem e nove")
    elif numero == 110:
        print("cem e dez")
    elif numero == 111:
        print("cem e onze")
    elif numero == 112:
        print("cem e doze")
    elif numero == 113:
        print("cem e treze")
    elif numero == 114:
        print("cem e quatorze")
    elif numero == 115:
        print("cem e quinze")
    elif numero == 116:
        print("cem e dezesseis")
    elif numero == 117:
        print("cem e dezessete")
    elif numero == 118:
        print("cem e dezoito")
    elif numero == 119:
        print("cem e dezenove")
    elif numero == 120:
        print("cem e vinte")
    elif numero == 121:
        print("cem e vinte e um")
    elif numero == 122:
        print("cem e vinte e dois")
    elif numero == 123:
        print("cem e vinte e três")
    elif numero == 124:
        print("cem e vinte e quatro")
    elif numero == 125:
        print("cem e vinte e cinco")
    elif numero == 126:
        print("cem e vinte e seis")
    elif numero == 127:
        print("cem e vinte e sete")
    elif numero == 128:
        print("cem e vinte e oito")
    elif numero == 129:
        print("cem e vinte e nove")
    elif numero == 130:
        print("cem e trinta")
    elif numero == 131:
        print("cem e trinta e um")
    elif numero == 132:
        print("cem e trinta e dois")
    elif numero == 133:
        print("cem e trinta e três")
    elif numero == 134:
        print("cem e trinta e quatro")
    elif numero == 135:
        print("cem e trinta e cinco")
    elif numero == 136:
        print("cem e trinta e seis")
    elif numero == 137:
        print("cem e trinta e sete")
    elif numero == 138:
        print("cem e trinta e oito")
    elif numero == 139:
        print("cem e trinta e nove")
    elif numero == 140:
        print("cem e quarenta")
    elif numero == 141:
        print("cem e quarenta e um")
    elif numero == 142:
        print("cem e quarenta e dois")
    elif numero == 143:
        print("cem e quarenta e três")
    elif numero == 144:
        print("cem e quarenta e quatro")
    elif numero == 145:
        print("cem e quarenta e cinco")
    elif numero == 146:
        print("cem e quarenta e seis")
    elif numero == 147:
        print("cem e quarenta e sete")
    elif numero == 148:
        print("cem e quarenta e oito")
    elif numero == 149:
        print("cem e quarenta e nove")
    elif numero == 150:
        print("cem e cinquenta")
    elif numero == 151:
        print("cem e cinquenta e um")
    elif numero == 152:
        print("cem e cinquenta e dois")
    elif numero == 153:
        print("cem e cinquenta e três")
    elif numero == 154:
        print("cem e cinquenta e quatro")
    elif numero == 155:
        print("cem e cinquenta e cinco")
    elif numero == 156:
        print("cem e cinquenta e seis")
    elif numero == 157:
        print("cem e cinquenta e sete")
    elif numero == 158:
        print("cem e cinquenta e oito")
    elif numero == 159:
        print("cem e cinquenta e nove")
    elif numero == 160:
        print("cem e sessenta")
    elif numero == 161:
        print("cem e sessenta e um")
    elif numero == 162:
        print("cem e sessenta e dois")
    elif numero == 163:
        print("cem e sessenta e três")
    elif numero == 164:
        print("cem e sessenta e quatro")
    elif numero == 165:
        print("cem e sessenta e cinco")
    elif numero == 166:
        print("cem e sessenta e seis")
    elif numero == 167:
        print("cem e sessenta e sete")
    elif numero == 168:
        print("cem e sessenta e oito")
    elif numero == 169:
        print("cem e sessenta e nove")
    elif numero == 170:
        print("cem e setenta")
    elif numero == 171:
        print("cem e setenta e um")
    elif numero == 172:
        print("cem e setenta e dois")
    elif numero == 173:
        print("cem e setenta e três")
    elif numero == 174:
        print("cem e setenta e quatro")
    elif numero == 175:
        print("cem e setenta e cinco")
    elif numero == 176:
        print("cem e setenta e seis")
    elif numero == 177:
        print("cem e setenta e sete")
    elif numero == 178:
        print("cem e setenta e oito")
    elif numero == 179:
        print("cem e setenta e nove")
    elif numero == 180:
        print("cem e oitenta")
    elif numero == 181:
        print("cem e oitenta e um")
    elif numero == 182:
        print("cem e oitenta e dois")
    elif numero == 183:
        print("cem e oitenta e três")
    elif numero == 184:
        print("cem e oitenta e quatro")
    elif numero == 185:
        print("cem e oitenta e cinco")
    elif numero == 186:
        print("cem e oitenta e seis")
    elif numero == 187:
        print("cem e oitenta e sete")
    elif numero == 188:
        print("cem e oitenta e oito")
    elif numero == 189:
        print("cem e oitenta e nove")
    elif numero == 190:
        print("cem e noventa")
    elif numero == 191:
        print("cem e noventa e um")
    elif numero == 192:
        print("cem e noventa e dois")
    elif numero == 193:
        print("cem e noventa e três")
    elif numero == 194:
        print("cem e noventa e quatro")
    elif numero == 195:
        print("cem e noventa e cinco")
    elif numero == 196:
        print("cem e noventa e seis")
    elif numero == 197:
        print("cem e noventa e sete")
    elif numero == 198:
        print("cem e noventa e oito")
    elif numero == 199:
        print("cem e noventa e nove")
    elif numero == 200:
        print("duzentos")
    elif numero == 201:
        print("duzentos e um")
    elif numero == 202:
        print("duzentos e dois")
    elif numero == 203:
        print("duzentos e três")
    elif numero == 204:
        print("duzentos e quatro")
    elif numero == 205:
        print("duzentos e cinco")
    elif numero == 206:
        print("duzentos e seis")
    elif numero == 207:
        print("duzentos e sete")
    elif numero == 208:
        print("duzentos e oito")
    elif numero == 209:
        print("duzentos e nove")
    elif numero == 210:
        print("duzentos e dez")
    elif numero == 211:
        print("duzentos e onze")
    elif numero == 212:
        print("duzentos e doze")
    elif numero == 213:
        print("duzentos e treze")
    elif numero == 214:
        print("duzentos e quatorze")
    elif numero == 215:
        print("duzentos e quinze")
    elif numero == 216:
        print("duzentos e dezesseis")
    elif numero == 217:
        print("duzentos e dezessete")
    elif numero == 218:
        print("duzentos e dezoito")
    elif numero == 219:
        print("duzentos e dezenove")
    elif numero == 220:
        print("duzentos e vinte")
    elif numero == 221:
        print("duzentos e vinte e um")
    elif numero == 222:
        print("duzentos e vinte e dois")
    elif numero == 223:
        print("duzentos e vinte e três")
    elif numero == 224:
        print("duzentos e vinte e quatro")
    elif numero == 225:
        print("duzentos e vinte e cinco")
    elif numero == 226:
        print("duzentos e vinte e seis")
    elif numero == 227:
        print("duzentos e vinte e sete")
    elif numero == 228:
        print("duzentos e vinte e oito")
    elif numero == 229:
        print("duzentos e vinte e nove")
    elif numero == 230:
        print("duzentos e trinta")
    elif numero == 231:
        print("duzentos e trinta e um")
    elif numero == 232:
        print("duzentos e trinta e dois")
    elif numero == 233:
        print("duzentos e trinta e três")
    elif numero == 234:
        print("duzentos e trinta e quatro")
    elif numero == 235:
        print("duzentos e trinta e cinco")
    elif numero == 236:
        print("duzentos e trinta e seis")
    elif numero == 237:
        print("duzentos e trinta e sete")
    elif numero == 238:
        print("duzentos e trinta e oito")
    elif numero == 239:
        print("duzentos e trinta e nove")
    elif numero == 240:
        print("duzentos e quarenta")
    elif numero == 241:
        print("duzentos e quarenta e um")
    elif numero == 242:
        print("duzentos e quarenta e dois")
    elif numero == 243:
        print("duzentos e quarenta e três")
    elif numero == 244:
        print("duzentos e quarenta e quatro")
    elif numero == 245:
        print("duzentos e quarenta e cinco")
    elif numero == 246:
        print("duzentos e quarenta e seis")
    elif numero == 247:
        print("duzentos e quarenta e sete")
    elif numero == 248:
        print("duzentos e quarenta e oito")
    elif numero == 249:
        print("duzentos e quarenta e nove")
    elif numero == 250:
        print("duzentos e cinquenta")
    elif numero == 251:
        print("duzentos e cinquenta e um")
    elif numero == 252:
        print("duzentos e cinquenta e dois")
    elif numero == 253:
        print("duzentos e cinquenta e três")
    elif numero == 254:
        print("duzentos e cinquenta e quatro")
    elif numero == 255:
        print("duzentos e cinquenta e cinco")
    elif numero == 256:
        print("duzentos e cinquenta e seis")
    elif numero == 257:
        print("duzentos e cinquenta e sete")
    elif numero == 258:
        print("duzentos e cinquenta e oito")
    elif numero == 259:
        print("duzentos e cinquenta e nove")
    elif numero == 260:
        print("duzentos e sessenta")
    elif numero == 261:
        print("duzentos e sessenta e um")
    elif numero == 262:
        print("duzentos e sessenta e dois")
    elif numero == 263:
        print("duzentos e sessenta e três")
    elif numero == 264:
        print("duzentos e sessenta e quatro")
    elif numero == 265:
        print("duzentos e sessenta e cinco")
    elif numero == 266:
        print("duzentos e sessenta e seis")
    elif numero == 267:
        print("duzentos e sessenta e sete")
    elif numero == 268:
        print("duzentos e sessenta e oito")
    elif numero == 269:
        print("duzentos e sessenta e nove")
    elif numero == 270:
        print("duzentos e setenta")
    elif numero == 271:
        print("duzentos e setenta e um")
    elif numero == 272:
        print("duzentos e setenta e dois")
    elif numero == 273:
        print("duzentos e setenta e três")
    elif numero == 274:
        print("duzentos e setenta e quatro")
    elif numero == 275:
        print("duzentos e setenta e cinco")
    elif numero == 276:
        print("duzentos e setenta e seis")
    elif numero == 277:
        print("duzentos e setenta e sete")
    elif numero == 278:
        print("duzentos e setenta e oito")
    elif numero == 279:
        print("duzentos e setenta e nove")
    elif numero == 280:
        print("duzentos e oitenta")
    elif numero == 281:
        print("duzentos e oitenta e um")
    elif numero == 282:
        print("duzentos e oitenta e dois")
    elif numero == 283:
        print("duzentos e oitenta e três")
    elif numero == 284:
        print("duzentos e oitenta e quatro")
    elif numero == 285:
        print("duzentos e oitenta e cinco")
    elif numero == 286:
        print("duzentos e oitenta e seis")
    elif numero == 287:
        print("duzentos e oitenta e sete")
    elif numero == 288:
        print("duzentos e oitenta e oito")
    elif numero == 289:
        print("duzentos e oitenta e nove")
    elif numero == 290:
        print("duzentos e noventa")
    elif numero == 291:
        print("duzentos e noventa e um")
    elif numero == 292:
        print("duzentos e noventa e dois")
    elif numero == 293:
        print("duzentos e noventa e três")
    elif numero == 294:
        print("duzentos e noventa e quatro")
    elif numero == 295:
        print("duzentos e noventa e cinco")
    elif numero == 296:
        print("duzentos e noventa e seis")
    elif numero == 297:
        print("duzentos e noventa e sete")
    elif numero == 298:
        print("duzentos e noventa e oito")
    elif numero == 299:
        print("duzentos e noventa e nove")
    elif numero == 300:
        print("trezentos")
    elif numero == 301:
        print("trezentos e um")
    elif numero == 302:
        print("trezentos e dois")
    elif numero == 303:
        print("trezentos e três")
    elif numero == 304:
        print("trezentos e quatro")
    elif numero == 305:
        print("trezentos e cinco")
    elif numero == 306:
        print("trezentos e seis")
    elif numero == 307:
        print("trezentos e sete")
    elif numero == 308:
        print("trezentos e oito")
    elif numero == 309:
        print("trezentos e nove")
    elif numero == 310:
        print("trezentos e dez")
    elif numero == 311:
        print("trezentos e onze")
    elif numero == 312:
        print("trezentos e doze")
    elif numero == 313:
        print("trezentos e treze")
    elif numero == 314:
        print("trezentos e quatorze")
    elif numero == 315:
        print("trezentos e quinze")
    elif numero == 316:
        print("trezentos e dezesseis")
    elif numero == 317:
        print("trezentos e dezessete")
    elif numero == 318:
        print("trezentos e dezoito")
    elif numero == 319:
        print("trezentos e dezenove")
    elif numero == 320:
        print("trezentos e vinte")
    elif numero == 321:
        print("trezentos e vinte e um")
    elif numero == 322:
        print("trezentos e vinte e dois")
    elif numero == 323:
        print("trezentos e vinte e três")
    elif numero == 324:
        print("trezentos e vinte e quatro")
    elif numero == 325:
        print("trezentos e vinte e cinco")
    elif numero == 326:
        print("trezentos e vinte e seis")
    elif numero == 327:
        print("trezentos e vinte e sete")
    elif numero == 328:
        print("trezentos e vinte e oito")
    elif numero == 329:
        print("trezentos e vinte e nove")
    elif numero == 330:
        print("trezentos e trinta")
    elif numero == 331:
        print("trezentos e trinta e um")
    elif numero == 332:
        print("trezentos e trinta e dois")
    elif numero == 333:
        print("trezentos e trinta e três")
    elif numero == 334:
        print("trezentos e trinta e quatro")
    elif numero == 335:
        print("trezentos e trinta e cinco")
    elif numero == 336:
        print("trezentos e trinta e seis")
    elif numero == 337:
        print("trezentos e trinta e sete")
    elif numero == 338:
        print("trezentos e trinta e oito")
    elif numero == 339:
        print("trezentos e trinta e nove")
    elif numero == 340:
        print("trezentos e quarenta")
    elif numero == 341:
        print("trezentos e quarenta e um")
    elif numero == 342:
        print("trezentos e quarenta e dois")
    elif numero == 343:
        print("trezentos e quarenta e três")
    elif numero == 344:
        print("trezentos e quarenta e quatro")
    elif numero == 345:
        print("trezentos e quarenta e cinco")
    elif numero == 346:
        print("trezentos e quarenta e seis")
    elif numero == 347:
        print("trezentos e quarenta e sete")
    elif numero == 348:
        print("trezentos e quarenta e oito")
    elif numero == 349:
        print("trezentos e quarenta e nove")
    elif numero == 350:
        print("trezentos e cinquenta")
    elif numero == 351:
        print("trezentos e cinquenta e um")
    elif numero == 352:
        print("trezentos e cinquenta e dois")
    elif numero == 353:
        print("trezentos e cinquenta e três")
    elif numero == 354:
        print("trezentos e cinquenta e quatro")
    elif numero == 355:
        print("trezentos e cinquenta e cinco")
    elif numero == 356:
        print("trezentos e cinquenta e seis")
    elif numero == 357:
        print("trezentos e cinquenta e sete")
    elif numero == 358:
        print("trezentos e cinquenta e oito")
    elif numero == 359:
        print("trezentos e cinquenta e nove")
    elif numero == 360:
        print("trezentos e sessenta")
    elif numero == 361:
        print("trezentos e sessenta e um")
    elif numero == 362:
        print("trezentos e sessenta e dois")
    elif numero == 363:
        print("trezentos e sessenta e três")
    elif numero == 364:
        print("trezentos e sessenta e quatro")
    elif numero == 365:
        print("trezentos e sessenta e cinco")
    elif numero == 366:
        print("trezentos e sessenta e seis")
    elif numero == 367:
        print("trezentos e sessenta e sete")
    elif numero == 368:
        print("trezentos e sessenta e oito")
    elif numero == 369:
        print("trezentos e sessenta e nove")
    elif numero == 370:
        print("trezentos e setenta")
    elif numero == 371:
        print("trezentos e setenta e um")
    elif numero == 372:
        print("trezentos e setenta e dois")
    elif numero == 373:
        print("trezentos e setenta e três")
    elif numero == 374:
        print("trezentos e setenta e quatro")
    elif numero == 375:
        print("trezentos e setenta e cinco")
    elif numero == 376:
        print("trezentos e setenta e seis")
    elif numero == 377:
        print("trezentos e setenta e sete")
    elif numero == 378:
        print("trezentos e setenta e oito")
    elif numero == 379:
        print("trezentos e setenta e nove")
    elif numero == 380:
        print("trezentos e oitenta")
    elif numero == 381:
        print("trezentos e oitenta e um")
    elif numero == 382:
        print("trezentos e oitenta e dois")
    elif numero == 383:
        print("trezentos e oitenta e três")
    elif numero == 384:
        print("trezentos e oitenta e quatro")
    elif numero == 385:
        print("trezentos e oitenta e cinco")
    elif numero == 386:
        print("trezentos e oitenta e seis")
    elif numero == 387:
        print("trezentos e oitenta e sete")
    elif numero == 388:
        print("trezentos e oitenta e oito")
    elif numero == 389:
        print("trezentos e oitenta e nove")
    elif numero == 390:
        print("trezentos e noventa")
    elif numero == 391:
        print("trezentos e noventa e um")
    elif numero == 392:
        print("trezentos e noventa e dois")
    elif numero == 393:
        print("trezentos e noventa e três")
    elif numero == 394:
        print("trezentos e noventa e quatro")
    elif numero == 395:
        print("trezentos e noventa e cinco")
    elif numero == 396:
        print("trezentos e noventa e seis")
    elif numero == 397:
        print("trezentos e noventa e sete")
    elif numero == 398:
        print("trezentos e noventa e oito")
    elif numero == 399:
        print("trezentos e noventa e nove")
    elif numero == 400:
        print("quatrocentos")
    elif numero == 401:
        print("quatrocentos e um")
    elif numero == 402:
        print("quatrocentos e dois")
    elif numero == 403:
        print("quatrocentos e três")
    elif numero == 404:
        print("quatrocentos e quatro")
    elif numero == 405:
        print("quatrocentos e cinco")
    elif numero == 406:
        print("quatrocentos e seis")
    elif numero == 407:
        print("quatrocentos e sete")
    elif numero == 408:
        print("quatrocentos e oito")
    elif numero == 409:
        print("quatrocentos e nove")
    elif numero == 410:
        print("quatrocentos e dez")
    elif numero == 411:
        print("quatrocentos e onze")
    elif numero == 412:
        print("quatrocentos e doze")
    elif numero == 413:
        print("quatrocentos e treze")
    elif numero == 414:
        print("quatrocentos e quatorze")
    elif numero == 415:
        print("quatrocentos e quinze")
    elif numero == 416:
        print("quatrocentos e dezesseis")
    elif numero == 417:
        print("quatrocentos e dezessete")
    elif numero == 418:
        print("quatrocentos e dezoito")
    elif numero == 419:
        print("quatrocentos e dezenove")
    elif numero == 420:
        print("quatrocentos e vinte")
    elif numero == 421:
        print("quatrocentos e vinte e um")
    elif numero == 422:
        print("quatrocentos e vinte e dois")
    elif numero == 423:
        print("quatrocentos e vinte e três")
    elif numero == 424:
        print("quatrocentos e vinte e quatro")
    elif numero == 425:
        print("quatrocentos e vinte e cinco")
    elif numero == 426:
        print("quatrocentos e vinte e seis")
    elif numero == 427:
        print("quatrocentos e vinte e sete")
    elif numero == 428:
        print("quatrocentos e vinte e oito")
    elif numero == 429:
        print("quatrocentos e vinte e nove")
    elif numero == 430:
        print("quatrocentos e trinta")
    elif numero == 431:
        print("quatrocentos e trinta e um")
    elif numero == 432:
        print("quatrocentos e trinta e dois")
    elif numero == 433:
        print("quatrocentos e trinta e três")
    elif numero == 434:
        print("quatrocentos e trinta e quatro")
    elif numero == 435:
        print("quatrocentos e trinta e cinco")
    elif numero == 436:
        print("quatrocentos e trinta e seis")
    elif numero == 437:
        print("quatrocentos e trinta e sete")
    elif numero == 438:
        print("quatrocentos e trinta e oito")
    elif numero == 439:
        print("quatrocentos e trinta e nove")
    elif numero == 440:
        print("quatrocentos e quarenta")
    elif numero == 441:
        print("quatrocentos e quarenta e um")
    elif numero == 442:
        print("quatrocentos e quarenta e dois")
    elif numero == 443:
        print("quatrocentos e quarenta e três")
    elif numero == 444:
        print("quatrocentos e quarenta e quatro")
    elif numero == 445:
        print("quatrocentos e quarenta e cinco")
    elif numero == 446:
        print("quatrocentos e quarenta e seis")
    elif numero == 447:
        print("quatrocentos e quarenta e sete")
    elif numero == 448:
        print("quatrocentos e quarenta e oito")
    elif numero == 449:
        print("quatrocentos e quarenta e nove")
    elif numero == 450:
        print("quatrocentos e cinquenta")
    elif numero == 451:
        print("quatrocentos e cinquenta e um")
    elif numero == 452:
        print("quatrocentos e cinquenta e dois")
    elif numero == 453:
        print("quatrocentos e cinquenta e três")
    elif numero == 454:
        print("quatrocentos e cinquenta e quatro")
    elif numero == 455:
        print("quatrocentos e cinquenta e cinco")
    elif numero == 456:
        print("quatrocentos e cinquenta e seis")
    elif numero == 457:
        print("quatrocentos e cinquenta e sete")
    elif numero == 458:
        print("quatrocentos e cinquenta e oito")
    elif numero == 459:
        print("quatrocentos e cinquenta e nove")
    elif numero == 460:
        print("quatrocentos e sessenta")
    elif numero == 461:
        print("quatrocentos e sessenta e um")
    elif numero == 462:
        print("quatrocentos e sessenta e dois")
    elif numero == 463:
        print("quatrocentos e sessenta e três")
    elif numero == 464:
        print("quatrocentos e sessenta e quatro")
    elif numero == 465:
        print("quatrocentos e sessenta e cinco")
    elif numero == 466:
        print("quatrocentos e sessenta e seis")
    elif numero == 467:
        print("quatrocentos e sessenta e sete")
    elif numero == 468:
        print("quatrocentos e sessenta e oito")
    elif numero == 469:
        print("quatrocentos e sessenta e nove")
    elif numero == 470:
        print("quatrocentos e setenta")
    elif numero == 471:
        print("quatrocentos e setenta e um")
    elif numero == 472:
        print("quatrocentos e setenta e dois")
    elif numero == 473:
        print("quatrocentos e setenta e três")
    elif numero == 474:
        print("quatrocentos e setenta e quatro")
    elif numero == 475:
        print("quatrocentos e setenta e cinco")
    elif numero == 476:
        print("quatrocentos e setenta e seis")
    elif numero == 477:
        print("quatrocentos e setenta e sete")
    elif numero == 478:
        print("quatrocentos e setenta e oito")
    elif numero == 479:
        print("quatrocentos e setenta e nove")
    elif numero == 480:
        print("quatrocentos e oitenta")
    elif numero == 481:
        print("quatrocentos e oitenta e um")
    elif numero == 482:
        print("quatrocentos e oitenta e dois")
    elif numero == 483:
        print("quatrocentos e oitenta e três")
    elif numero == 484:
        print("quatrocentos e oitenta e quatro")
    elif numero == 485:
        print("quatrocentos e oitenta e cinco")
    elif numero == 486:
        print("quatrocentos e oitenta e seis")
    elif numero == 487:
        print("quatrocentos e oitenta e sete")
    elif numero == 488:
        print("quatrocentos e oitenta e oito")
    elif numero == 489:
        print("quatrocentos e oitenta e nove")
    elif numero == 490:
        print("quatrocentos e noventa")
    elif numero == 491:
        print("quatrocentos e noventa e um")
    elif numero == 492:
        print("quatrocentos e noventa e dois")
    elif numero == 493:
        print("quatrocentos e noventa e três")
    elif numero == 494:
        print("quatrocentos e noventa e quatro")
    elif numero == 495:
        print("quatrocentos e noventa e cinco")
    elif numero == 496:
        print("quatrocentos e noventa e seis")
    elif numero == 497:
        print("quatrocentos e noventa e sete")
    elif numero == 498:
        print("quatrocentos e noventa e oito")
    elif numero == 499:
        print("quatrocentos e noventa e nove")
    elif numero == 500:
        print("quinhentos")
    elif numero == 501:
        print("quinhentos e um")
    elif numero == 502:
        print("quinhentos e dois")
    elif numero == 503:
        print("quinhentos e três")
    elif numero == 504:
        print("quinhentos e quatro")
    elif numero == 505:
        print("quinhentos e cinco")
    elif numero == 506:
        print("quinhentos e seis")
    elif numero == 507:
        print("quinhentos e sete")
    elif numero == 508:
        print("quinhentos e oito")
    elif numero == 509:
        print("quinhentos e nove")
    elif numero == 510:
        print("quinhentos e dez")
    elif numero == 511:
        print("quinhentos e onze")
    elif numero == 512:
        print("quinhentos e doze")
    elif numero == 513:
        print("quinhentos e treze")
    elif numero == 514:
        print("quinhentos e quatorze")
    elif numero == 515:
        print("quinhentos e quinze")
    elif numero == 516:
        print("quinhentos e dezesseis")
    elif numero == 517:
        print("quinhentos e dezessete")
    elif numero == 518:
        print("quinhentos e dezoito")
    elif numero == 519:
        print("quinhentos e dezenove")
    elif numero == 520:
        print("quinhentos e vinte")
    elif numero == 521:
        print("quinhentos e vinte e um")
    elif numero == 522:
        print("quinhentos e vinte e dois")
    elif numero == 523:
        print("quinhentos e vinte e três")
    elif numero == 524:
        print("quinhentos e vinte e quatro")
    elif numero == 525:
        print("quinhentos e vinte e cinco")
    elif numero == 526:
        print("quinhentos e vinte e seis")
    elif numero == 527:
        print("quinhentos e vinte e sete")
    elif numero == 528:
        print("quinhentos e vinte e oito")
    elif numero == 529:
        print("quinhentos e vinte e nove")
    elif numero == 530:
        print("quinhentos e trinta")
    elif numero == 531:
        print("quinhentos e trinta e um")
    elif numero == 532:
        print("quinhentos e trinta e dois")
    elif numero == 533:
        print("quinhentos e trinta e três")
    elif numero == 534:
        print("quinhentos e trinta e quatro")
    elif numero == 535:
        print("quinhentos e trinta e cinco")
    elif numero == 536:
        print("quinhentos e trinta e seis")
    elif numero == 537:
        print("quinhentos e trinta e sete")
    elif numero == 538:
        print("quinhentos e trinta e oito")
    elif numero == 539:
        print("quinhentos e trinta e nove")
    elif numero == 540:
        print("quinhentos e quarenta")
    elif numero == 541:
        print("quinhentos e quarenta e um")
    elif numero == 542:
        print("quinhentos e quarenta e dois")
    elif numero == 543:
        print("quinhentos e quarenta e três")
    elif numero == 544:
        print("quinhentos e quarenta e quatro")
    elif numero == 545:
        print("quinhentos e quarenta e cinco")
    elif numero == 546:
        print("quinhentos e quarenta e seis")
    elif numero == 547:
        print("quinhentos e quarenta e sete")
    elif numero == 548:
        print("quinhentos e quarenta e oito")
    elif numero == 549:
        print("quinhentos e quarenta e nove")
    elif numero == 550:
        print("quinhentos e cinquenta")
    elif numero == 551:
        print("quinhentos e cinquenta e um")
    elif numero == 552:
        print("quinhentos e cinquenta e dois")
    elif numero == 553:
        print("quinhentos e cinquenta e três")
    elif numero == 554:
        print("quinhentos e cinquenta e quatro")
    elif numero == 555:
        print("quinhentos e cinquenta e cinco")
    elif numero == 556:
        print("quinhentos e cinquenta e seis")
    elif numero == 557:
        print("quinhentos e cinquenta e sete")
    elif numero == 558:
        print("quinhentos e cinquenta e oito")
    elif numero == 559:
        print("quinhentos e cinquenta e nove")
    elif numero == 560:
        print("quinhentos e sessenta")
    elif numero == 561:
        print("quinhentos e sessenta e um")
    elif numero == 562:
        print("quinhentos e sessenta e dois")
    elif numero == 563:
        print("quinhentos e sessenta e três")
    elif numero == 564:
        print("quinhentos e sessenta e quatro")
    elif numero == 565:
        print("quinhentos e sessenta e cinco")
    elif numero == 566:
        print("quinhentos e sessenta e seis")
    elif numero == 567:
        print("quinhentos e sessenta e sete")
    elif numero == 568:
        print("quinhentos e sessenta e oito")
    elif numero == 569:
        print("quinhentos e sessenta e nove")
    elif numero == 570:
        print("quinhentos e setenta")
    elif numero == 571:
        print("quinhentos e setenta e um")
    elif numero == 572:
        print("quinhentos e setenta e dois")
    elif numero == 573:
        print("quinhentos e setenta e três")
    elif numero == 574:
        print("quinhentos e setenta e quatro")
    elif numero == 575:
        print("quinhentos e setenta e cinco")
    elif numero == 576:
        print("quinhentos e setenta e seis")
    elif numero == 577:
        print("quinhentos e setenta e sete")
    elif numero == 578:
        print("quinhentos e setenta e oito")
    elif numero == 579:
        print("quinhentos e setenta e nove")
    elif numero == 580:
        print("quinhentos e oitenta")
    elif numero == 581:
        print("quinhentos e oitenta e um")
    elif numero == 582:
        print("quinhentos e oitenta e dois")
    elif numero == 583:
        print("quinhentos e oitenta e três")
    elif numero == 584:
        print("quinhentos e oitenta e quatro")
    elif numero == 585:
        print("quinhentos e oitenta e cinco")
    elif numero == 586:
        print("quinhentos e oitenta e seis")
    elif numero == 587:
        print("quinhentos e oitenta e sete")
    elif numero == 588:
        print("quinhentos e oitenta e oito")
    elif numero == 589:
        print("quinhentos e oitenta e nove")
    elif numero == 590:
        print("quinhentos e noventa")
    elif numero == 591:
        print("quinhentos e noventa e um")
    elif numero == 592:
        print("quinhentos e noventa e dois")
    elif numero == 593:
        print("quinhentos e noventa e três")
    elif numero == 594:
        print("quinhentos e noventa e quatro")
    elif numero == 595:
        print("quinhentos e noventa e cinco")
    elif numero == 596:
        print("quinhentos e noventa e seis")
    elif numero == 597:
        print("quinhentos e noventa e sete")
    elif numero == 598:
        print("quinhentos e noventa e oito")
    elif numero == 599:
        print("quinhentos e noventa e nove")
    elif numero == 600:
        print("seiscentos")
    elif numero == 601:
        print("seiscentos e um")
    elif numero == 602:
        print("seiscentos e dois")
    elif numero == 603:
        print("seiscentos e três")
    elif numero == 604:
        print("seiscentos e quatro")
    elif numero == 605:
        print("seiscentos e cinco")
    elif numero == 606:
        print("seiscentos e seis")
    elif numero == 607:
        print("seiscentos e sete")
    elif numero == 608:
        print("seiscentos e oito")
    elif numero == 609:
        print("seiscentos e nove")
    elif numero == 610:
        print("seiscentos e dez")
    elif numero == 611:
        print("seiscentos e onze")
    elif numero == 612:
        print("seiscentos e doze")
    elif numero == 613:
        print("seiscentos e treze")
    elif numero == 614:
        print("seiscentos e quatorze")
    elif numero == 615:
        print("seiscentos e quinze")
    elif numero == 616:
        print("seiscentos e dezesseis")
    elif numero == 617:
        print("seiscentos e dezessete")
    elif numero == 618:
        print("seiscentos e dezoito")
    elif numero == 619:
        print("seiscentos e dezenove")
    elif numero == 620:
        print("seiscentos e vinte")
    elif numero == 621:
        print("seiscentos e vinte e um")
    elif numero == 622:
        print("seiscentos e vinte e dois")
    elif numero == 623:
        print("seiscentos e vinte e três")
    elif numero == 624:
        print("seiscentos e vinte e quatro")
    elif numero == 625:
        print("seiscentos e vinte e cinco")
    elif numero == 626:
        print("seiscentos e vinte e seis")
    elif numero == 627:
        print("seiscentos e vinte e sete")
    elif numero == 628:
        print("seiscentos e vinte e oito")
    elif numero == 629:
        print("seiscentos e vinte e nove")
    elif numero == 630:
        print("seiscentos e trinta")
    elif numero == 631:
        print("seiscentos e trinta e um")
    elif numero == 632:
        print("seiscentos e trinta e dois")
    elif numero == 633:
        print("seiscentos e trinta e três")
    elif numero == 634:
        print("seiscentos e trinta e quatro")
    elif numero == 635:
        print("seiscentos e trinta e cinco")
    elif numero == 636:
        print("seiscentos e trinta e seis")
    elif numero == 637:
        print("seiscentos e trinta e sete")
    elif numero == 638:
        print("seiscentos e trinta e oito")
    elif numero == 639:
        print("seiscentos e trinta e nove")
    elif numero == 640:
        print("seiscentos e quarenta")
    elif numero == 641:
        print("seiscentos e quarenta e um")
    elif numero == 642:
        print("seiscentos e quarenta e dois")
    elif numero == 643:
        print("seiscentos e quarenta e três")
    elif numero == 644:
        print("seiscentos e quarenta e quatro")
    elif numero == 645:
        print("seiscentos e quarenta e cinco")
    elif numero == 646:
        print("seiscentos e quarenta e seis")
    elif numero == 647:
        print("seiscentos e quarenta e sete")
    elif numero == 648:
        print("seiscentos e quarenta e oito")
    elif numero == 649:
        print("seiscentos e quarenta e nove")
    elif numero == 650:
        print("seiscentos e cinquenta")
    elif numero == 651:
        print("seiscentos e cinquenta e um")
    elif numero == 652:
        print("seiscentos e cinquenta e dois")
    elif numero == 653:
        print("seiscentos e cinquenta e três")
    elif numero == 654:
        print("seiscentos e cinquenta e quatro")
    elif numero == 655:
        print("seiscentos e cinquenta e cinco")
    elif numero == 656:
        print("seiscentos e cinquenta e seis")
    elif numero == 657:
        print("seiscentos e cinquenta e sete")
    elif numero == 658:
        print("seiscentos e cinquenta e oito")
    elif numero == 659:
        print("seiscentos e cinquenta e nove")
    elif numero == 660:
        print("seiscentos e sessenta")
    elif numero == 661:
        print("seiscentos e sessenta e um")
    elif numero == 662:
        print("seiscentos e sessenta e dois")
    elif numero == 663:
        print("seiscentos e sessenta e três")
    elif numero == 664:
        print("seiscentos e sessenta e quatro")
    elif numero == 665:
        print("seiscentos e sessenta e cinco")
    elif numero == 666:
        print("seiscentos e sessenta e seis")
    elif numero == 667:
        print("seiscentos e sessenta e sete")
    elif numero == 668:
        print("seiscentos e sessenta e oito")
    elif numero == 669:
        print("seiscentos e sessenta e nove")
    elif numero == 670:
        print("seiscentos e setenta")
    elif numero == 671:
        print("seiscentos e setenta e um")
    elif numero == 672:
        print("seiscentos e setenta e dois")
    elif numero == 673:
        print("seiscentos e setenta e três")
    elif numero == 674:
        print("seiscentos e setenta e quatro")
    elif numero == 675:
        print("seiscentos e setenta e cinco")
    elif numero == 676:
        print("seiscentos e setenta e seis")
    elif numero == 677:
        print("seiscentos e setenta e sete")
    elif numero == 678:
        print("seiscentos e setenta e oito")
    elif numero == 679:
        print("seiscentos e setenta e nove")
    elif numero == 680:
        print("seiscentos e oitenta")
    elif numero == 681:
        print("seiscentos e oitenta e um")
    elif numero == 682:
        print("seiscentos e oitenta e dois")
    elif numero == 683:
        print("seiscentos e oitenta e três")
    elif numero == 684:
        print("seiscentos e oitenta e quatro")
    elif numero == 685:
        print("seiscentos e oitenta e cinco")
    elif numero == 686:
        print("seiscentos e oitenta e seis")
    elif numero == 687:
        print("seiscentos e oitenta e sete")
    elif numero == 688:
        print("seiscentos e oitenta e oito")
    elif numero == 689:
        print("seiscentos e oitenta e nove")
    elif numero == 690:
        print("seiscentos e noventa")
    elif numero == 691:
        print("seiscentos e noventa e um")
    elif numero == 692:
        print("seiscentos e noventa e dois")
    elif numero == 693:
        print("seiscentos e noventa e três")
    elif numero == 694:
        print("seiscentos e noventa e quatro")
    elif numero == 695:
        print("seiscentos e noventa e cinco")
    elif numero == 696:
        print("seiscentos e noventa e seis")
    elif numero == 697:
        print("seiscentos e noventa e sete")
    elif numero == 698:
        print("seiscentos e noventa e oito")
    elif numero == 699:
        print("seiscentos e noventa e nove")
    elif numero == 700:
        print("setecentos")
    elif numero == 701:
        print("setecentos e um")
    elif numero == 702:
        print("setecentos e dois")
    elif numero == 703:
        print("setecentos e três")
    elif numero == 704:
        print("setecentos e quatro")
    elif numero == 705:
        print("setecentos e cinco")
    elif numero == 706:
        print("setecentos e seis")
    elif numero == 707:
        print("setecentos e sete")
    elif numero == 708:
        print("setecentos e oito")
    elif numero == 709:
        print("setecentos e nove")
    elif numero == 710:
        print("setecentos e dez")
    elif numero == 711:
        print("setecentos e onze")
    elif numero == 712:
        print("setecentos e doze")
    elif numero == 713:
        print("setecentos e treze")
    elif numero == 714:
        print("setecentos e quatorze")
    elif numero == 715:
        print("setecentos e quinze")
    elif numero == 716:
        print("setecentos e dezesseis")
    elif numero == 717:
        print("setecentos e dezessete")
    elif numero == 718:
        print("setecentos e dezoito")
    elif numero == 719:
        print("setecentos e dezenove")
    elif numero == 720:
        print("setecentos e vinte")
    elif numero == 721:
        print("setecentos e vinte e um")
    elif numero == 722:
        print("setecentos e vinte e dois")
    elif numero == 723:
        print("setecentos e vinte e três")
    elif numero == 724:
        print("setecentos e vinte e quatro")
    elif numero == 725:
        print("setecentos e vinte e cinco")
    elif numero == 726:
        print("setecentos e vinte e seis")
    elif numero == 727:
        print("setecentos e vinte e sete")
    elif numero == 728:
        print("setecentos e vinte e oito")
    elif numero == 729:
        print("setecentos e vinte e nove")
    elif numero == 730:
        print("setecentos e trinta")
    elif numero == 731:
        print("setecentos e trinta e um")
    elif numero == 732:
        print("setecentos e trinta e dois")
    elif numero == 733:
        print("setecentos e trinta e três")
    elif numero == 734:
        print("setecentos e trinta e quatro")
    elif numero == 735:
        print("setecentos e trinta e cinco")
    elif numero == 736:
        print("setecentos e trinta e seis")
    elif numero == 737:
        print("setecentos e trinta e sete")
    elif numero == 738:
        print("setecentos e trinta e oito")
    elif numero == 739:
        print("setecentos e trinta e nove")
    elif numero == 740:
        print("setecentos e quarenta")
    elif numero == 741:
        print("setecentos e quarenta e um")
    elif numero == 742:
        print("setecentos e quarenta e dois")
    elif numero == 743:
        print("setecentos e quarenta e três")
    elif numero == 744:
        print("setecentos e quarenta e quatro")
    elif numero == 745:
        print("setecentos e quarenta e cinco")
    elif numero == 746:
        print("setecentos e quarenta e seis")
    elif numero == 747:
        print("setecentos e quarenta e sete")
    elif numero == 748:
        print("setecentos e quarenta e oito")
    elif numero == 749:
        print("setecentos e quarenta e nove")
    elif numero == 750:
        print("setecentos e cinquenta")
    elif numero == 751:
        print("setecentos e cinquenta e um")
    elif numero == 752:
        print("setecentos e cinquenta e dois")
    elif numero == 753:
        print("setecentos e cinquenta e três")
    elif numero == 754:
        print("setecentos e cinquenta e quatro")
    elif numero == 755:
        print("setecentos e cinquenta e cinco")
    elif numero == 756:
        print("setecentos e cinquenta e seis")
    elif numero == 757:
        print("setecentos e cinquenta e sete")
    elif numero == 758:
        print("setecentos e cinquenta e oito")
    elif numero == 759:
        print("setecentos e cinquenta e nove")
    elif numero == 760:
        print("setecentos e sessenta")
    elif numero == 761:
        print("setecentos e sessenta e um")
    elif numero == 762:
        print("setecentos e sessenta e dois")
    elif numero == 763:
        print("setecentos e sessenta e três")
    elif numero == 764:
        print("setecentos e sessenta e quatro")
    elif numero == 765:
        print("setecentos e sessenta e cinco")
    elif numero == 766:
        print("setecentos e sessenta e seis")
    elif numero == 767:
        print("setecentos e sessenta e sete")
    elif numero == 768:
        print("setecentos e sessenta e oito")
    elif numero == 769:
        print("setecentos e sessenta e nove")
    elif numero == 770:
        print("setecentos e setenta")
    elif numero == 771:
        print("setecentos e setenta e um")
    elif numero == 772:
        print("setecentos e setenta e dois")
    elif numero == 773:
        print("setecentos e setenta e três")
    elif numero == 774:
        print("setecentos e setenta e quatro")
    elif numero == 775:
        print("setecentos e setenta e cinco")
    elif numero == 776:
        print("setecentos e setenta e seis")
    elif numero == 777:
        print("setecentos e setenta e sete")
    elif numero == 778:
        print("setecentos e setenta e oito")
    elif numero == 779:
        print("setecentos e setenta e nove")
    elif numero == 780:
        print("setecentos e oitenta")
    elif numero == 781:
        print("setecentos e oitenta e um")
    elif numero == 782:
        print("setecentos e oitenta e dois")
    elif numero == 783:
        print("setecentos e oitenta e três")
    elif numero == 784:
        print("setecentos e oitenta e quatro")
    elif numero == 785:
        print("setecentos e oitenta e cinco")
    elif numero == 786:
        print("setecentos e oitenta e seis")
    elif numero == 787:
        print("setecentos e oitenta e sete")
    elif numero == 788:
        print("setecentos e oitenta e oito")
    elif numero == 789:
        print("setecentos e oitenta e nove")
    elif numero == 790:
        print("setecentos e noventa")
    elif numero == 791:
        print("setecentos e noventa e um")
    elif numero == 792:
        print("setecentos e noventa e dois")
    elif numero == 793:
        print("setecentos e noventa e três")
    elif numero == 794:
        print("setecentos e noventa e quatro")
    elif numero == 795:
        print("setecentos e noventa e cinco")
    elif numero == 796:
        print("setecentos e noventa e seis")
    elif numero == 797:
        print("setecentos e noventa e sete")
    elif numero == 798:
        print("setecentos e noventa e oito")
    elif numero == 799:
        print("setecentos e noventa e nove")
    elif numero == 800:
        print("oitocentos")
    elif numero == 801:
        print("oitocentos e um")
    elif numero == 802:
        print("oitocentos e dois")
    elif numero == 803:
        print("oitocentos e três")
    elif numero == 804:
        print("oitocentos e quatro")
    elif numero == 805:
        print("oitocentos e cinco")
    elif numero == 806:
        print("oitocentos e seis")
    elif numero == 807:
        print("oitocentos e sete")
    elif numero == 808:
        print("oitocentos e oito")
    elif numero == 809:
        print("oitocentos e nove")
    elif numero == 810:
        print("oitocentos e dez")
    elif numero == 811:
        print("oitocentos e onze")
    elif numero == 812:
        print("oitocentos e doze")
    elif numero == 813:
        print("oitocentos e treze")
    elif numero == 814:
        print("oitocentos e quatorze")
    elif numero == 815:
        print("oitocentos e quinze")
    elif numero == 816:
        print("oitocentos e dezesseis")
    elif numero == 817:
        print("oitocentos e dezessete")
    elif numero == 818:
        print("oitocentos e dezoito")
    elif numero == 819:
        print("oitocentos e dezenove")
    elif numero == 820:
        print("oitocentos e vinte")
    elif numero == 821:
        print("oitocentos e vinte e um")
    elif numero == 822:
        print("oitocentos e vinte e dois")
    elif numero == 823:
        print("oitocentos e vinte e três")
    elif numero == 824:
        print("oitocentos e vinte e quatro")
    elif numero == 825:
        print("oitocentos e vinte e cinco")
    elif numero == 826:
        print("oitocentos e vinte e seis")
    elif numero == 827:
        print("oitocentos e vinte e sete")
    elif numero == 828:
        print("oitocentos e vinte e oito")
    elif numero == 829:
        print("oitocentos e vinte e nove")
    elif numero == 830:
        print("oitocentos e trinta")
    elif numero == 831:
        print("oitocentos e trinta e um")
    elif numero == 832:
        print("oitocentos e trinta e dois")
    elif numero == 833:
        print("oitocentos e trinta e três")
    elif numero == 834:
        print("oitocentos e trinta e quatro")
    elif numero == 835:
        print("oitocentos e trinta e cinco")
    elif numero == 836:
        print("oitocentos e trinta e seis")
    elif numero == 837:
        print("oitocentos e trinta e sete")
    elif numero == 838:
        print("oitocentos e trinta e oito")
    elif numero == 839:
        print("oitocentos e trinta e nove")
    elif numero == 840:
        print("oitocentos e quarenta")
    elif numero == 841:
        print("oitocentos e quarenta e um")
    elif numero == 842:
        print("oitocentos e quarenta e dois")
    elif numero == 843:
        print("oitocentos e quarenta e três")
    elif numero == 844:
        print("oitocentos e quarenta e quatro")
    elif numero == 845:
        print("oitocentos e quarenta e cinco")
    elif numero == 846:
        print("oitocentos e quarenta e seis")
    elif numero == 847:
        print("oitocentos e quarenta e sete")
    elif numero == 848:
        print("oitocentos e quarenta e oito")
    elif numero == 849:
        print("oitocentos e quarenta e nove")
    elif numero == 850:
        print("oitocentos e cinquenta")
    elif numero == 851:
        print("oitocentos e cinquenta e um")
    elif numero == 852:
        print("oitocentos e cinquenta e dois")
    elif numero == 853:
        print("oitocentos e cinquenta e três")
    elif numero == 854:
        print("oitocentos e cinquenta e quatro")
    elif numero == 855:
        print("oitocentos e cinquenta e cinco")
    elif numero == 856:
        print("oitocentos e cinquenta e seis")
    elif numero == 857:
        print("oitocentos e cinquenta e sete")
    elif numero == 858:
        print("oitocentos e cinquenta e oito")
    elif numero == 859:
        print("oitocentos e cinquenta e nove")
    elif numero == 860:
        print("oitocentos e sessenta")
    elif numero == 861:
        print("oitocentos e sessenta e um")
    elif numero == 862:
        print("oitocentos e sessenta e dois")
    elif numero == 863:
        print("oitocentos e sessenta e três")
    elif numero == 864:
        print("oitocentos e sessenta e quatro")
    elif numero == 865:
        print("oitocentos e sessenta e cinco")
    elif numero == 866:
        print("oitocentos e sessenta e seis")
    elif numero == 867:
        print("oitocentos e sessenta e sete")
    elif numero == 868:
        print("oitocentos e sessenta e oito")
    elif numero == 869:
        print("oitocentos e sessenta e nove")
    elif numero == 870:
        print("oitocentos e setenta")
    elif numero == 871:
        print("oitocentos e setenta e um")
    elif numero == 872:
        print("oitocentos e setenta e dois")
    elif numero == 873:
        print("oitocentos e setenta e três")
    elif numero == 874:
        print("oitocentos e setenta e quatro")
    elif numero == 875:
        print("oitocentos e setenta e cinco")
    elif numero == 876:
        print("oitocentos e setenta e seis")
    elif numero == 877:
        print("oitocentos e setenta e sete")
    elif numero == 878:
        print("oitocentos e setenta e oito")
    elif numero == 879:
        print("oitocentos e setenta e nove")
    elif numero == 880:
        print("oitocentos e oitenta")
    elif numero == 881:
        print("oitocentos e oitenta e um")
    elif numero == 882:
        print("oitocentos e oitenta e dois")
    elif numero == 883:
        print("oitocentos e oitenta e três")
    elif numero == 884:
        print("oitocentos e oitenta e quatro")
    elif numero == 885:
        print("oitocentos e oitenta e cinco")
    elif numero == 886:
        print("oitocentos e oitenta e seis")
    elif numero == 887:
        print("oitocentos e oitenta e sete")
    elif numero == 888:
        print("oitocentos e oitenta e oito")
    elif numero == 889:
        print("oitocentos e oitenta e nove")
    elif numero == 890:
        print("oitocentos e noventa")
    elif numero == 891:
        print("oitocentos e noventa e um")
    elif numero == 892:
        print("oitocentos e noventa e dois")
    elif numero == 893:
        print("oitocentos e noventa e três")
    elif numero == 894:
        print("oitocentos e noventa e quatro")
    elif numero == 895:
        print("oitocentos e noventa e cinco")
    elif numero == 896:
        print("oitocentos e noventa e seis")
    elif numero == 897:
        print("oitocentos e noventa e sete")
    elif numero == 898:
        print("oitocentos e noventa e oito")
    elif numero == 899:
        print("oitocentos e noventa e nove")
    elif numero == 900:
        print("novecentos")
    elif numero == 901:
        print("novecentos e um")
    elif numero == 902:
        print("novecentos e dois")
    elif numero == 903:
        print("novecentos e três")
    elif numero == 904:
        print("novecentos e quatro")
    elif numero == 905:
        print("novecentos e cinco")
    elif numero == 906:
        print("novecentos e seis")
    elif numero == 907:
        print("novecentos e sete")
    elif numero == 908:
        print("novecentos e oito")
    elif numero == 909:
        print("novecentos e nove")
    elif numero == 910:
        print("novecentos e dez")
    elif numero == 911:
        print("novecentos e onze")
    elif numero == 912:
        print("novecentos e doze")
    elif numero == 913:
        print("novecentos e treze")
    elif numero == 914:
        print("novecentos e quatorze")
    elif numero == 915:
        print("novecentos e quinze")
    elif numero == 916:
        print("novecentos e dezesseis")
    elif numero == 917:
        print("novecentos e dezessete")
    elif numero == 918:
        print("novecentos e dezoito")
    elif numero == 919:
        print("novecentos e dezenove")
    elif numero == 920:
        print("novecentos e vinte")
    elif numero == 921:
        print("novecentos e vinte e um")
    elif numero == 922:
        print("novecentos e vinte e dois")
    elif numero == 923:
        print("novecentos e vinte e três")
    elif numero == 924:
        print("novecentos e vinte e quatro")
    elif numero == 925:
        print("novecentos e vinte e cinco")
    elif numero == 926:
        print("novecentos e vinte e seis")
    elif numero == 927:
        print("novecentos e vinte e sete")
    elif numero == 928:
        print("novecentos e vinte e oito")
    elif numero == 929:
        print("novecentos e vinte e nove")
    elif numero == 930:
        print("novecentos e trinta")
    elif numero == 931:
        print("novecentos e trinta e um")
    elif numero == 932:
        print("novecentos e trinta e dois")
    elif numero == 933:
        print("novecentos e trinta e três")
    elif numero == 934:
        print("novecentos e trinta e quatro")
    elif numero == 935:
        print("novecentos e trinta e cinco")
    elif numero == 936:
        print("novecentos e trinta e seis")
    elif numero == 937:
        print("novecentos e trinta e sete")
    elif numero == 938:
        print("novecentos e trinta e oito")
    elif numero == 939:
        print("novecentos e trinta e nove")
    elif numero == 940:
        print("novecentos e quarenta")
    elif numero == 941:
        print("novecentos e quarenta e um")
    elif numero == 942:
        print("novecentos e quarenta e dois")
    elif numero == 943:
        print("novecentos e quarenta e três")
    elif numero == 944:
        print("novecentos e quarenta e quatro")
    elif numero == 945:
        print("novecentos e quarenta e cinco")
    elif numero == 946:
        print("novecentos e quarenta e seis")
    elif numero == 947:
        print("novecentos e quarenta e sete")
    elif numero == 948:
        print("novecentos e quarenta e oito")
    elif numero == 949:
        print("novecentos e quarenta e nove")
    elif numero == 950:
        print("novecentos e cinquenta")
    elif numero == 951:
        print("novecentos e cinquenta e um")
    elif numero == 952:
        print("novecentos e cinquenta e dois")
    elif numero == 953:
        print("novecentos e cinquenta e três")
    elif numero == 954:
        print("novecentos e cinquenta e quatro")
    elif numero == 955:
        print("novecentos e cinquenta e cinco")
    elif numero == 956:
        print("novecentos e cinquenta e seis")
    elif numero == 957:
        print("novecentos e cinquenta e sete")
    elif numero == 958:
        print("novecentos e cinquenta e oito")
    elif numero == 959:
        print("novecentos e cinquenta e nove")
    elif numero == 960:
        print("novecentos e sessenta")
    elif numero == 961:
        print("novecentos e sessenta e um")
    elif numero == 962:
        print("novecentos e sessenta e dois")
    elif numero == 963:
        print("novecentos e sessenta e três")
    elif numero == 964:
        print("novecentos e sessenta e quatro")
    elif numero == 965:
        print("novecentos e sessenta e cinco")
    elif numero == 966:
        print("novecentos e sessenta e seis")
    elif numero == 967:
        print("novecentos e sessenta e sete")
    elif numero == 968:
        print("novecentos e sessenta e oito")
    elif numero == 969:
        print("novecentos e sessenta e nove")
    elif numero == 970:
        print("novecentos e setenta")
    elif numero == 971:
        print("novecentos e setenta e um")
    elif numero == 972:
        print("novecentos e setenta e dois")
    elif numero == 973:
        print("novecentos e setenta e três")
    elif numero == 974:
        print("novecentos e setenta e quatro")
    elif numero == 975:
        print("novecentos e setenta e cinco")
    elif numero == 976:
        print("novecentos e setenta e seis")
    elif numero == 977:
        print("novecentos e setenta e sete")
    elif numero == 978:
        print("novecentos e setenta e oito")
    elif numero == 979:
        print("novecentos e setenta e nove")
    elif numero == 980:
        print("novecentos e oitenta")
    elif numero == 981:
        print("novecentos e oitenta e um")
    elif numero == 982:
        print("novecentos e oitenta e dois")
    elif numero == 983:
        print("novecentos e oitenta e três")
    elif numero == 984:
        print("novecentos e oitenta e quatro")
    elif numero == 985:
        print("novecentos e oitenta e cinco")
    elif numero == 986:
        print("novecentos e oitenta e seis")
    elif numero == 987:
        print("novecentos e oitenta e sete")
    elif numero == 988:
        print("novecentos e oitenta e oito")
    elif numero == 989:
        print("novecentos e oitenta e nove")
    elif numero == 990:
        print("novecentos e noventa")
    elif numero == 991:
        print("novecentos e noventa e um")
    elif numero == 992:
        print("novecentos e noventa e dois")
    elif numero == 993:
        print("novecentos e noventa e três")
    elif numero == 994:
        print("novecentos e noventa e quatro")
    elif numero == 995:
        print("novecentos e noventa e cinco")
    elif numero == 996:
        print("novecentos e noventa e seis")
    elif numero == 997:
        print("novecentos e noventa e sete")
    elif numero == 998:
        print("novecentos e noventa e oito")
    elif numero == 999:
        print("novecentos e noventa e nove")


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


def nMenos99a99ToExtensoIfElse():
    numero = int(input("Digite um número entre -99 e 99: "))
    if numero < -99 or numero > 99:
        print("Fora do intervalo permitido.")
        return
    if numero == -99:
        print("menos noventa e nove")
    elif numero == -98:
        print("menos noventa e oito")
    elif numero == -97:
        print("menos noventa e sete")
    elif numero == -96:
        print("menos noventa e seis")
    elif numero == -95:
        print("menos noventa e cinco")
    elif numero == -94:
        print("menos noventa e quatro")
    elif numero == -93:
        print("menos noventa e três")
    elif numero == -92:
        print("menos noventa e dois")
    elif numero == -91:
        print("menos noventa e um")
    elif numero == -90:
        print("menos noventa")
    elif numero == -89:
        print("menos oitenta e nove")
    elif numero == -88:
        print("menos oitenta e oito")
    elif numero == -87:
        print("menos oitenta e sete")
    elif numero == -86:
        print("menos oitenta e seis")
    elif numero == -85:
        print("menos oitenta e cinco")
    elif numero == -84:
        print("menos oitenta e quatro")
    elif numero == -83:
        print("menos oitenta e três")
    elif numero == -82:
        print("menos oitenta e dois")
    elif numero == -81:
        print("menos oitenta e um")
    elif numero == -80:
        print("menos oitenta")
    elif numero == -79:
        print("menos setenta e nove")
    elif numero == -78:
        print("menos setenta e oito")
    elif numero == -77:
        print("menos setenta e sete")
    elif numero == -76:
        print("menos setenta e seis")
    elif numero == -75:
        print("menos setenta e cinco")
    elif numero == -74:
        print("menos setenta e quatro")
    elif numero == -73:
        print("menos setenta e três")
    elif numero == -72:
        print("menos setenta e dois")
    elif numero == -71:
        print("menos setenta e um")
    elif numero == -70:
        print("menos setenta")
    elif numero == -69:
        print("menos sessenta e nove")
    elif numero == -68:
        print("menos sessenta e oito")
    elif numero == -67:
        print("menos sessenta e sete")
    elif numero == -66:
        print("menos sessenta e seis")
    elif numero == -65:
        print("menos sessenta e cinco")
    elif numero == -64:
        print("menos sessenta e quatro")
    elif numero == -63:
        print("menos sessenta e três")
    elif numero == -62:
        print("menos sessenta e dois")
    elif numero == -61:
        print("menos sessenta e um")
    elif numero == -60:
        print("menos sessenta")
    elif numero == -59:
        print("menos cinquenta e nove")
    elif numero == -58:
        print("menos cinquenta e oito")
    elif numero == -57:
        print("menos cinquenta e sete")
    elif numero == -56:
        print("menos cinquenta e seis")
    elif numero == -55:
        print("menos cinquenta e cinco")
    elif numero == -54:
        print("menos cinquenta e quatro")
    elif numero == -53:
        print("menos cinquenta e três")
    elif numero == -52:
        print("menos cinquenta e dois")
    elif numero == -51:
        print("menos cinquenta e um")
    elif numero == -50:
        print("menos cinquenta")
    elif numero == -49:
        print("menos quarenta e nove")
    elif numero == -48:
        print("menos quarenta e oito")
    elif numero == -47:
        print("menos quarenta e sete")
    elif numero == -46:
        print("menos quarenta e seis")
    elif numero == -45:
        print("menos quarenta e cinco")
    elif numero == -44:
        print("menos quarenta e quatro")
    elif numero == -43:
        print("menos quarenta e três")
    elif numero == -42:
        print("menos quarenta e dois")
    elif numero == -41:
        print("menos quarenta e um")
    elif numero == -40:
        print("menos quarenta")
    elif numero == -39:
        print("menos trinta e nove")
    elif numero == -38:
        print("menos trinta e oito")
    elif numero == -37:
        print("menos trinta e sete")
    elif numero == -36:
        print("menos trinta e seis")
    elif numero == -35:
        print("menos trinta e cinco")
    elif numero == -34:
        print("menos trinta e quatro")
    elif numero == -33:
        print("menos trinta e três")
    elif numero == -32:
        print("menos trinta e dois")
    elif numero == -31:
        print("menos trinta e um")
    elif numero == -30:
        print("menos trinta")
    elif numero == -29:
        print("menos vinte e nove")
    elif numero == -28:
        print("menos vinte e oito")
    elif numero == -27:
        print("menos vinte e sete")
    elif numero == -26:
        print("menos vinte e seis")
    elif numero == -25:
        print("menos vinte e cinco")
    elif numero == -24:
        print("menos vinte e quatro")
    elif numero == -23:
        print("menos vinte e três")
    elif numero == -22:
        print("menos vinte e dois")
    elif numero == -21:
        print("menos vinte e um")
    elif numero == -20:
        print("menos vinte")
    elif numero == -19:
        print("menos dezenove")
    elif numero == -18:
        print("menos dezoito")
    elif numero == -17:
        print("menos dezessete")
    elif numero == -16:
        print("menos dezesseis")
    elif numero == -15:
        print("menos quinze")
    elif numero == -14:
        print("menos quatorze")
    elif numero == -13:
        print("menos treze")
    elif numero == -12:
        print("menos doze")
    elif numero == -11:
        print("menos onze")
    elif numero == -10:
        print("menos dez")
    elif numero == -9:
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
    elif numero == 10:
        print("dez")
    elif numero == 11:
        print("onze")
    elif numero == 12:
        print("doze")
    elif numero == 13:
        print("treze")
    elif numero == 14:
        print("quatorze")
    elif numero == 15:
        print("quinze")
    elif numero == 16:
        print("dezesseis")
    elif numero == 17:
        print("dezessete")
    elif numero == 18:
        print("dezoito")
    elif numero == 19:
        print("dezenove")
    elif numero == 20:
        print("vinte")
    elif numero == 21:
        print("vinte e um")
    elif numero == 22:
        print("vinte e dois")
    elif numero == 23:
        print("vinte e três")
    elif numero == 24:
        print("vinte e quatro")
    elif numero == 25:
        print("vinte e cinco")
    elif numero == 26:
        print("vinte e seis")
    elif numero == 27:
        print("vinte e sete")
    elif numero == 28:
        print("vinte e oito")
    elif numero == 29:
        print("vinte e nove")
    elif numero == 30:
        print("trinta")
    elif numero == 31:
        print("trinta e um")
    elif numero == 32:
        print("trinta e dois")
    elif numero == 33:
        print("trinta e três")
    elif numero == 34:
        print("trinta e quatro")
    elif numero == 35:
        print("trinta e cinco")
    elif numero == 36:
        print("trinta e seis")
    elif numero == 37:
        print("trinta e sete")
    elif numero == 38:
        print("trinta e oito")
    elif numero == 39:
        print("trinta e nove")
    elif numero == 40:
        print("quarenta")
    elif numero == 41:
        print("quarenta e um")
    elif numero == 42:
        print("quarenta e dois")
    elif numero == 43:
        print("quarenta e três")
    elif numero == 44:
        print("quarenta e quatro")
    elif numero == 45:
        print("quarenta e cinco")
    elif numero == 46:
        print("quarenta e seis")
    elif numero == 47:
        print("quarenta e sete")
    elif numero == 48:
        print("quarenta e oito")
    elif numero == 49:
        print("quarenta e nove")
    elif numero == 50:
        print("cinquenta")
    elif numero == 51:
        print("cinquenta e um")
    elif numero == 52:
        print("cinquenta e dois")
    elif numero == 53:
        print("cinquenta e três")
    elif numero == 54:
        print("cinquenta e quatro")
    elif numero == 55:
        print("cinquenta e cinco")
    elif numero == 56:
        print("cinquenta e seis")
    elif numero == 57:
        print("cinquenta e sete")
    elif numero == 58:
        print("cinquenta e oito")
    elif numero == 59:
        print("cinquenta e nove")
    elif numero == 60:
        print("sessenta")
    elif numero == 61:
        print("sessenta e um")
    elif numero == 62:
        print("sessenta e dois")
    elif numero == 63:
        print("sessenta e três")
    elif numero == 64:
        print("sessenta e quatro")
    elif numero == 65:
        print("sessenta e cinco")
    elif numero == 66:
        print("sessenta e seis")
    elif numero == 67:
        print("sessenta e sete")
    elif numero == 68:
        print("sessenta e oito")
    elif numero == 69:
        print("sessenta e nove")
    elif numero == 70:
        print("setenta")
    elif numero == 71:
        print("setenta e um")
    elif numero == 72:
        print("setenta e dois")
    elif numero == 73:
        print("setenta e três")
    elif numero == 74:
        print("setenta e quatro")
    elif numero == 75:
        print("setenta e cinco")
    elif numero == 76:
        print("setenta e seis")
    elif numero == 77:
        print("setenta e sete")
    elif numero == 78:
        print("setenta e oito")
    elif numero == 79:
        print("setenta e nove")
    elif numero == 80:
        print("oitenta")
    elif numero == 81:
        print("oitenta e um")
    elif numero == 82:
        print("oitenta e dois")
    elif numero == 83:
        print("oitenta e três")
    elif numero == 84:
        print("oitenta e quatro")
    elif numero == 85:
        print("oitenta e cinco")
    elif numero == 86:
        print("oitenta e seis")
    elif numero == 87:
        print("oitenta e sete")
    elif numero == 88:
        print("oitenta e oito")
    elif numero == 89:
        print("oitenta e nove")
    elif numero == 90:
        print("noventa")
    elif numero == 91:
        print("noventa e um")
    elif numero == 92:
        print("noventa e dois")
    elif numero == 93:
        print("noventa e três")
    elif numero == 94:
        print("noventa e quatro")
    elif numero == 95:
        print("noventa e cinco")
    elif numero == 96:
        print("noventa e seis")
    elif numero == 97:
        print("noventa e sete")
    elif numero == 98:
        print("noventa e oito")
    elif numero == 99:
        print("noventa e nove")



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


def nMenos999a999ToExtensoIfElse():
    numero = int(input("Digite um número entre -999 e 999: "))
    if numero < -999 or numero > 999:
        print("Fora do intervalo permitido.")
        return
    if numero == -999:
        print("menos novecentos e noventa e nove")
    elif numero == -998:
        print("menos novecentos e noventa e oito")
    elif numero == -997:
        print("menos novecentos e noventa e sete")
    elif numero == -996:
        print("menos novecentos e noventa e seis")
    elif numero == -995:
        print("menos novecentos e noventa e cinco")
    elif numero == -994:
        print("menos novecentos e noventa e quatro")
    elif numero == -993:
        print("menos novecentos e noventa e três")
    elif numero == -992:
        print("menos novecentos e noventa e dois")
    elif numero == -991:
        print("menos novecentos e noventa e um")
    elif numero == -990:
        print("menos novecentos e noventa")
    elif numero == -989:
        print("menos novecentos e oitenta e nove")
    elif numero == -988:
        print("menos novecentos e oitenta e oito")
    elif numero == -987:
        print("menos novecentos e oitenta e sete")
    elif numero == -986:
        print("menos novecentos e oitenta e seis")
    elif numero == -985:
        print("menos novecentos e oitenta e cinco")
    elif numero == -984:
        print("menos novecentos e oitenta e quatro")
    elif numero == -983:
        print("menos novecentos e oitenta e três")
    elif numero == -982:
        print("menos novecentos e oitenta e dois")
    elif numero == -981:
        print("menos novecentos e oitenta e um")
    elif numero == -980:
        print("menos novecentos e oitenta")
    elif numero == -979:
        print("menos novecentos e setenta e nove")
    elif numero == -978:
        print("menos novecentos e setenta e oito")
    elif numero == -977:
        print("menos novecentos e setenta e sete")
    elif numero == -976:
        print("menos novecentos e setenta e seis")
    elif numero == -975:
        print("menos novecentos e setenta e cinco")
    elif numero == -974:
        print("menos novecentos e setenta e quatro")
    elif numero == -973:
        print("menos novecentos e setenta e três")
    elif numero == -972:
        print("menos novecentos e setenta e dois")
    elif numero == -971:
        print("menos novecentos e setenta e um")
    elif numero == -970:
        print("menos novecentos e setenta")
    elif numero == -969:
        print("menos novecentos e sessenta e nove")
    elif numero == -968:
        print("menos novecentos e sessenta e oito")
    elif numero == -967:
        print("menos novecentos e sessenta e sete")
    elif numero == -966:
        print("menos novecentos e sessenta e seis")
    elif numero == -965:
        print("menos novecentos e sessenta e cinco")
    elif numero == -964:
        print("menos novecentos e sessenta e quatro")
    elif numero == -963:
        print("menos novecentos e sessenta e três")
    elif numero == -962:
        print("menos novecentos e sessenta e dois")
    elif numero == -961:
        print("menos novecentos e sessenta e um")
    elif numero == -960:
        print("menos novecentos e sessenta")
    elif numero == -959:
        print("menos novecentos e cinquenta e nove")
    elif numero == -958:
        print("menos novecentos e cinquenta e oito")
    elif numero == -957:
        print("menos novecentos e cinquenta e sete")
    elif numero == -956:
        print("menos novecentos e cinquenta e seis")
    elif numero == -955:
        print("menos novecentos e cinquenta e cinco")
    elif numero == -954:
        print("menos novecentos e cinquenta e quatro")
    elif numero == -953:
        print("menos novecentos e cinquenta e três")
    elif numero == -952:
        print("menos novecentos e cinquenta e dois")
    elif numero == -951:
        print("menos novecentos e cinquenta e um")
    elif numero == -950:
        print("menos novecentos e cinquenta")
    elif numero == -949:
        print("menos novecentos e quarenta e nove")
    elif numero == -948:
        print("menos novecentos e quarenta e oito")
    elif numero == -947:
        print("menos novecentos e quarenta e sete")
    elif numero == -946:
        print("menos novecentos e quarenta e seis")
    elif numero == -945:
        print("menos novecentos e quarenta e cinco")
    elif numero == -944:
        print("menos novecentos e quarenta e quatro")
    elif numero == -943:
        print("menos novecentos e quarenta e três")
    elif numero == -942:
        print("menos novecentos e quarenta e dois")
    elif numero == -941:
        print("menos novecentos e quarenta e um")
    elif numero == -940:
        print("menos novecentos e quarenta")
    elif numero == -939:
        print("menos novecentos e trinta e nove")
    elif numero == -938:
        print("menos novecentos e trinta e oito")
    elif numero == -937:
        print("menos novecentos e trinta e sete")
    elif numero == -936:
        print("menos novecentos e trinta e seis")
    elif numero == -935:
        print("menos novecentos e trinta e cinco")
    elif numero == -934:
        print("menos novecentos e trinta e quatro")
    elif numero == -933:
        print("menos novecentos e trinta e três")
    elif numero == -932:
        print("menos novecentos e trinta e dois")
    elif numero == -931:
        print("menos novecentos e trinta e um")
    elif numero == -930:
        print("menos novecentos e trinta")
    elif numero == -929:
        print("menos novecentos e vinte e nove")
    elif numero == -928:
        print("menos novecentos e vinte e oito")
    elif numero == -927:
        print("menos novecentos e vinte e sete")
    elif numero == -926:
        print("menos novecentos e vinte e seis")
    elif numero == -925:
        print("menos novecentos e vinte e cinco")
    elif numero == -924:
        print("menos novecentos e vinte e quatro")
    elif numero == -923:
        print("menos novecentos e vinte e três")
    elif numero == -922:
        print("menos novecentos e vinte e dois")
    elif numero == -921:
        print("menos novecentos e vinte e um")
    elif numero == -920:
        print("menos novecentos e vinte")
    elif numero == -919:
        print("menos novecentos e dezenove")
    elif numero == -918:
        print("menos novecentos e dezoito")
    elif numero == -917:
        print("menos novecentos e dezessete")
    elif numero == -916:
        print("menos novecentos e dezesseis")
    elif numero == -915:
        print("menos novecentos e quinze")
    elif numero == -914:
        print("menos novecentos e quatorze")
    elif numero == -913:
        print("menos novecentos e treze")
    elif numero == -912:
        print("menos novecentos e doze")
    elif numero == -911:
        print("menos novecentos e onze")
    elif numero == -910:
        print("menos novecentos e dez")
    elif numero == -909:
        print("menos novecentos e nove")
    elif numero == -908:
        print("menos novecentos e oito")
    elif numero == -907:
        print("menos novecentos e sete")
    elif numero == -906:
        print("menos novecentos e seis")
    elif numero == -905:
        print("menos novecentos e cinco")
    elif numero == -904:
        print("menos novecentos e quatro")
    elif numero == -903:
        print("menos novecentos e três")
    elif numero == -902:
        print("menos novecentos e dois")
    elif numero == -901:
        print("menos novecentos e um")
    elif numero == -900:
        print("menos novecentos")
    elif numero == -899:
        print("menos oitocentos e noventa e nove")
    elif numero == -898:
        print("menos oitocentos e noventa e oito")
    elif numero == -897:
        print("menos oitocentos e noventa e sete")
    elif numero == -896:
        print("menos oitocentos e noventa e seis")
    elif numero == -895:
        print("menos oitocentos e noventa e cinco")
    elif numero == -894:
        print("menos oitocentos e noventa e quatro")
    elif numero == -893:
        print("menos oitocentos e noventa e três")
    elif numero == -892:
        print("menos oitocentos e noventa e dois")
    elif numero == -891:
        print("menos oitocentos e noventa e um")
    elif numero == -890:
        print("menos oitocentos e noventa")
    elif numero == -889:
        print("menos oitocentos e oitenta e nove")
    elif numero == -888:
        print("menos oitocentos e oitenta e oito")
    elif numero == -887:
        print("menos oitocentos e oitenta e sete")
    elif numero == -886:
        print("menos oitocentos e oitenta e seis")
    elif numero == -885:
        print("menos oitocentos e oitenta e cinco")
    elif numero == -884:
        print("menos oitocentos e oitenta e quatro")
    elif numero == -883:
        print("menos oitocentos e oitenta e três")
    elif numero == -882:
        print("menos oitocentos e oitenta e dois")
    elif numero == -881:
        print("menos oitocentos e oitenta e um")
    elif numero == -880:
        print("menos oitocentos e oitenta")
    elif numero == -879:
        print("menos oitocentos e setenta e nove")
    elif numero == -878:
        print("menos oitocentos e setenta e oito")
    elif numero == -877:
        print("menos oitocentos e setenta e sete")
    elif numero == -876:
        print("menos oitocentos e setenta e seis")
    elif numero == -875:
        print("menos oitocentos e setenta e cinco")
    elif numero == -874:
        print("menos oitocentos e setenta e quatro")
    elif numero == -873:
        print("menos oitocentos e setenta e três")
    elif numero == -872:
        print("menos oitocentos e setenta e dois")
    elif numero == -871:
        print("menos oitocentos e setenta e um")
    elif numero == -870:
        print("menos oitocentos e setenta")
    elif numero == -869:
        print("menos oitocentos e sessenta e nove")
    elif numero == -868:
        print("menos oitocentos e sessenta e oito")
    elif numero == -867:
        print("menos oitocentos e sessenta e sete")
    elif numero == -866:
        print("menos oitocentos e sessenta e seis")
    elif numero == -865:
        print("menos oitocentos e sessenta e cinco")
    elif numero == -864:
        print("menos oitocentos e sessenta e quatro")
    elif numero == -863:
        print("menos oitocentos e sessenta e três")
    elif numero == -862:
        print("menos oitocentos e sessenta e dois")
    elif numero == -861:
        print("menos oitocentos e sessenta e um")
    elif numero == -860:
        print("menos oitocentos e sessenta")
    elif numero == -859:
        print("menos oitocentos e cinquenta e nove")
    elif numero == -858:
        print("menos oitocentos e cinquenta e oito")
    elif numero == -857:
        print("menos oitocentos e cinquenta e sete")
    elif numero == -856:
        print("menos oitocentos e cinquenta e seis")
    elif numero == -855:
        print("menos oitocentos e cinquenta e cinco")
    elif numero == -854:
        print("menos oitocentos e cinquenta e quatro")
    elif numero == -853:
        print("menos oitocentos e cinquenta e três")
    elif numero == -852:
        print("menos oitocentos e cinquenta e dois")
    elif numero == -851:
        print("menos oitocentos e cinquenta e um")
    elif numero == -850:
        print("menos oitocentos e cinquenta")
    elif numero == -849:
        print("menos oitocentos e quarenta e nove")
    elif numero == -848:
        print("menos oitocentos e quarenta e oito")
    elif numero == -847:
        print("menos oitocentos e quarenta e sete")
    elif numero == -846:
        print("menos oitocentos e quarenta e seis")
    elif numero == -845:
        print("menos oitocentos e quarenta e cinco")
    elif numero == -844:
        print("menos oitocentos e quarenta e quatro")
    elif numero == -843:
        print("menos oitocentos e quarenta e três")
    elif numero == -842:
        print("menos oitocentos e quarenta e dois")
    elif numero == -841:
        print("menos oitocentos e quarenta e um")
    elif numero == -840:
        print("menos oitocentos e quarenta")
    elif numero == -839:
        print("menos oitocentos e trinta e nove")
    elif numero == -838:
        print("menos oitocentos e trinta e oito")
    elif numero == -837:
        print("menos oitocentos e trinta e sete")
    elif numero == -836:
        print("menos oitocentos e trinta e seis")
    elif numero == -835:
        print("menos oitocentos e trinta e cinco")
    elif numero == -834:
        print("menos oitocentos e trinta e quatro")
    elif numero == -833:
        print("menos oitocentos e trinta e três")
    elif numero == -832:
        print("menos oitocentos e trinta e dois")
    elif numero == -831:
        print("menos oitocentos e trinta e um")
    elif numero == -830:
        print("menos oitocentos e trinta")
    elif numero == -829:
        print("menos oitocentos e vinte e nove")
    elif numero == -828:
        print("menos oitocentos e vinte e oito")
    elif numero == -827:
        print("menos oitocentos e vinte e sete")
    elif numero == -826:
        print("menos oitocentos e vinte e seis")
    elif numero == -825:
        print("menos oitocentos e vinte e cinco")
    elif numero == -824:
        print("menos oitocentos e vinte e quatro")
    elif numero == -823:
        print("menos oitocentos e vinte e três")
    elif numero == -822:
        print("menos oitocentos e vinte e dois")
    elif numero == -821:
        print("menos oitocentos e vinte e um")
    elif numero == -820:
        print("menos oitocentos e vinte")
    elif numero == -819:
        print("menos oitocentos e dezenove")
    elif numero == -818:
        print("menos oitocentos e dezoito")
    elif numero == -817:
        print("menos oitocentos e dezessete")
    elif numero == -816:
        print("menos oitocentos e dezesseis")
    elif numero == -815:
        print("menos oitocentos e quinze")
    elif numero == -814:
        print("menos oitocentos e quatorze")
    elif numero == -813:
        print("menos oitocentos e treze")
    elif numero == -812:
        print("menos oitocentos e doze")
    elif numero == -811:
        print("menos oitocentos e onze")
    elif numero == -810:
        print("menos oitocentos e dez")
    elif numero == -809:
        print("menos oitocentos e nove")
    elif numero == -808:
        print("menos oitocentos e oito")
    elif numero == -807:
        print("menos oitocentos e sete")
    elif numero == -806:
        print("menos oitocentos e seis")
    elif numero == -805:
        print("menos oitocentos e cinco")
    elif numero == -804:
        print("menos oitocentos e quatro")
    elif numero == -803:
        print("menos oitocentos e três")
    elif numero == -802:
        print("menos oitocentos e dois")
    elif numero == -801:
        print("menos oitocentos e um")
    elif numero == -800:
        print("menos oitocentos")
    elif numero == -799:
        print("menos setecentos e noventa e nove")
    elif numero == -798:
        print("menos setecentos e noventa e oito")
    elif numero == -797:
        print("menos setecentos e noventa e sete")
    elif numero == -796:
        print("menos setecentos e noventa e seis")
    elif numero == -795:
        print("menos setecentos e noventa e cinco")
    elif numero == -794:
        print("menos setecentos e noventa e quatro")
    elif numero == -793:
        print("menos setecentos e noventa e três")
    elif numero == -792:
        print("menos setecentos e noventa e dois")
    elif numero == -791:
        print("menos setecentos e noventa e um")
    elif numero == -790:
        print("menos setecentos e noventa")
    elif numero == -789:
        print("menos setecentos e oitenta e nove")
    elif numero == -788:
        print("menos setecentos e oitenta e oito")
    elif numero == -787:
        print("menos setecentos e oitenta e sete")
    elif numero == -786:
        print("menos setecentos e oitenta e seis")
    elif numero == -785:
        print("menos setecentos e oitenta e cinco")
    elif numero == -784:
        print("menos setecentos e oitenta e quatro")
    elif numero == -783:
        print("menos setecentos e oitenta e três")
    elif numero == -782:
        print("menos setecentos e oitenta e dois")
    elif numero == -781:
        print("menos setecentos e oitenta e um")
    elif numero == -780:
        print("menos setecentos e oitenta")
    elif numero == -779:
        print("menos setecentos e setenta e nove")
    elif numero == -778:
        print("menos setecentos e setenta e oito")
    elif numero == -777:
        print("menos setecentos e setenta e sete")
    elif numero == -776:
        print("menos setecentos e setenta e seis")
    elif numero == -775:
        print("menos setecentos e setenta e cinco")
    elif numero == -774:
        print("menos setecentos e setenta e quatro")
    elif numero == -773:
        print("menos setecentos e setenta e três")
    elif numero == -772:
        print("menos setecentos e setenta e dois")
    elif numero == -771:
        print("menos setecentos e setenta e um")
    elif numero == -770:
        print("menos setecentos e setenta")
    elif numero == -769:
        print("menos setecentos e sessenta e nove")
    elif numero == -768:
        print("menos setecentos e sessenta e oito")
    elif numero == -767:
        print("menos setecentos e sessenta e sete")
    elif numero == -766:
        print("menos setecentos e sessenta e seis")
    elif numero == -765:
        print("menos setecentos e sessenta e cinco")
    elif numero == -764:
        print("menos setecentos e sessenta e quatro")
    elif numero == -763:
        print("menos setecentos e sessenta e três")
    elif numero == -762:
        print("menos setecentos e sessenta e dois")
    elif numero == -761:
        print("menos setecentos e sessenta e um")
    elif numero == -760:
        print("menos setecentos e sessenta")
    elif numero == -759:
        print("menos setecentos e cinquenta e nove")
    elif numero == -758:
        print("menos setecentos e cinquenta e oito")
    elif numero == -757:
        print("menos setecentos e cinquenta e sete")
    elif numero == -756:
        print("menos setecentos e cinquenta e seis")
    elif numero == -755:
        print("menos setecentos e cinquenta e cinco")
    elif numero == -754:
        print("menos setecentos e cinquenta e quatro")
    elif numero == -753:
        print("menos setecentos e cinquenta e três")
    elif numero == -752:
        print("menos setecentos e cinquenta e dois")
    elif numero == -751:
        print("menos setecentos e cinquenta e um")
    elif numero == -750:
        print("menos setecentos e cinquenta")
    elif numero == -749:
        print("menos setecentos e quarenta e nove")
    elif numero == -748:
        print("menos setecentos e quarenta e oito")
    elif numero == -747:
        print("menos setecentos e quarenta e sete")
    elif numero == -746:
        print("menos setecentos e quarenta e seis")
    elif numero == -745:
        print("menos setecentos e quarenta e cinco")
    elif numero == -744:
        print("menos setecentos e quarenta e quatro")
    elif numero == -743:
        print("menos setecentos e quarenta e três")
    elif numero == -742:
        print("menos setecentos e quarenta e dois")
    elif numero == -741:
        print("menos setecentos e quarenta e um")
    elif numero == -740:
        print("menos setecentos e quarenta")
    elif numero == -739:
        print("menos setecentos e trinta e nove")
    elif numero == -738:
        print("menos setecentos e trinta e oito")
    elif numero == -737:
        print("menos setecentos e trinta e sete")
    elif numero == -736:
        print("menos setecentos e trinta e seis")
    elif numero == -735:
        print("menos setecentos e trinta e cinco")
    elif numero == -734:
        print("menos setecentos e trinta e quatro")
    elif numero == -733:
        print("menos setecentos e trinta e três")
    elif numero == -732:
        print("menos setecentos e trinta e dois")
    elif numero == -731:
        print("menos setecentos e trinta e um")
    elif numero == -730:
        print("menos setecentos e trinta")
    elif numero == -729:
        print("menos setecentos e vinte e nove")
    elif numero == -728:
        print("menos setecentos e vinte e oito")
    elif numero == -727:
        print("menos setecentos e vinte e sete")
    elif numero == -726:
        print("menos setecentos e vinte e seis")
    elif numero == -725:
        print("menos setecentos e vinte e cinco")
    elif numero == -724:
        print("menos setecentos e vinte e quatro")
    elif numero == -723:
        print("menos setecentos e vinte e três")
    elif numero == -722:
        print("menos setecentos e vinte e dois")
    elif numero == -721:
        print("menos setecentos e vinte e um")
    elif numero == -720:
        print("menos setecentos e vinte")
    elif numero == -719:
        print("menos setecentos e dezenove")
    elif numero == -718:
        print("menos setecentos e dezoito")
    elif numero == -717:
        print("menos setecentos e dezessete")
    elif numero == -716:
        print("menos setecentos e dezesseis")
    elif numero == -715:
        print("menos setecentos e quinze")
    elif numero == -714:
        print("menos setecentos e quatorze")
    elif numero == -713:
        print("menos setecentos e treze")
    elif numero == -712:
        print("menos setecentos e doze")
    elif numero == -711:
        print("menos setecentos e onze")
    elif numero == -710:
        print("menos setecentos e dez")
    elif numero == -709:
        print("menos setecentos e nove")
    elif numero == -708:
        print("menos setecentos e oito")
    elif numero == -707:
        print("menos setecentos e sete")
    elif numero == -706:
        print("menos setecentos e seis")
    elif numero == -705:
        print("menos setecentos e cinco")
    elif numero == -704:
        print("menos setecentos e quatro")
    elif numero == -703:
        print("menos setecentos e três")
    elif numero == -702:
        print("menos setecentos e dois")
    elif numero == -701:
        print("menos setecentos e um")
    elif numero == -700:
        print("menos setecentos")
    elif numero == -699:
        print("menos seiscentos e noventa e nove")
    elif numero == -698:
        print("menos seiscentos e noventa e oito")
    elif numero == -697:
        print("menos seiscentos e noventa e sete")
    elif numero == -696:
        print("menos seiscentos e noventa e seis")
    elif numero == -695:
        print("menos seiscentos e noventa e cinco")
    elif numero == -694:
        print("menos seiscentos e noventa e quatro")
    elif numero == -693:
        print("menos seiscentos e noventa e três")
    elif numero == -692:
        print("menos seiscentos e noventa e dois")
    elif numero == -691:
        print("menos seiscentos e noventa e um")
    elif numero == -690:
        print("menos seiscentos e noventa")
    elif numero == -689:
        print("menos seiscentos e oitenta e nove")
    elif numero == -688:
        print("menos seiscentos e oitenta e oito")
    elif numero == -687:
        print("menos seiscentos e oitenta e sete")
    elif numero == -686:
        print("menos seiscentos e oitenta e seis")
    elif numero == -685:
        print("menos seiscentos e oitenta e cinco")
    elif numero == -684:
        print("menos seiscentos e oitenta e quatro")
    elif numero == -683:
        print("menos seiscentos e oitenta e três")
    elif numero == -682:
        print("menos seiscentos e oitenta e dois")
    elif numero == -681:
        print("menos seiscentos e oitenta e um")
    elif numero == -680:
        print("menos seiscentos e oitenta")
    elif numero == -679:
        print("menos seiscentos e setenta e nove")
    elif numero == -678:
        print("menos seiscentos e setenta e oito")
    elif numero == -677:
        print("menos seiscentos e setenta e sete")
    elif numero == -676:
        print("menos seiscentos e setenta e seis")
    elif numero == -675:
        print("menos seiscentos e setenta e cinco")
    elif numero == -674:
        print("menos seiscentos e setenta e quatro")
    elif numero == -673:
        print("menos seiscentos e setenta e três")
    elif numero == -672:
        print("menos seiscentos e setenta e dois")
    elif numero == -671:
        print("menos seiscentos e setenta e um")
    elif numero == -670:
        print("menos seiscentos e setenta")
    elif numero == -669:
        print("menos seiscentos e sessenta e nove")
    elif numero == -668:
        print("menos seiscentos e sessenta e oito")
    elif numero == -667:
        print("menos seiscentos e sessenta e sete")
    elif numero == -666:
        print("menos seiscentos e sessenta e seis")
    elif numero == -665:
        print("menos seiscentos e sessenta e cinco")
    elif numero == -664:
        print("menos seiscentos e sessenta e quatro")
    elif numero == -663:
        print("menos seiscentos e sessenta e três")
    elif numero == -662:
        print("menos seiscentos e sessenta e dois")
    elif numero == -661:
        print("menos seiscentos e sessenta e um")
    elif numero == -660:
        print("menos seiscentos e sessenta")
    elif numero == -659:
        print("menos seiscentos e cinquenta e nove")
    elif numero == -658:
        print("menos seiscentos e cinquenta e oito")
    elif numero == -657:
        print("menos seiscentos e cinquenta e sete")
    elif numero == -656:
        print("menos seiscentos e cinquenta e seis")
    elif numero == -655:
        print("menos seiscentos e cinquenta e cinco")
    elif numero == -654:
        print("menos seiscentos e cinquenta e quatro")
    elif numero == -653:
        print("menos seiscentos e cinquenta e três")
    elif numero == -652:
        print("menos seiscentos e cinquenta e dois")
    elif numero == -651:
        print("menos seiscentos e cinquenta e um")
    elif numero == -650:
        print("menos seiscentos e cinquenta")
    elif numero == -649:
        print("menos seiscentos e quarenta e nove")
    elif numero == -648:
        print("menos seiscentos e quarenta e oito")
    elif numero == -647:
        print("menos seiscentos e quarenta e sete")
    elif numero == -646:
        print("menos seiscentos e quarenta e seis")
    elif numero == -645:
        print("menos seiscentos e quarenta e cinco")
    elif numero == -644:
        print("menos seiscentos e quarenta e quatro")
    elif numero == -643:
        print("menos seiscentos e quarenta e três")
    elif numero == -642:
        print("menos seiscentos e quarenta e dois")
    elif numero == -641:
        print("menos seiscentos e quarenta e um")
    elif numero == -640:
        print("menos seiscentos e quarenta")
    elif numero == -639:
        print("menos seiscentos e trinta e nove")
    elif numero == -638:
        print("menos seiscentos e trinta e oito")
    elif numero == -637:
        print("menos seiscentos e trinta e sete")
    elif numero == -636:
        print("menos seiscentos e trinta e seis")
    elif numero == -635:
        print("menos seiscentos e trinta e cinco")
    elif numero == -634:
        print("menos seiscentos e trinta e quatro")
    elif numero == -633:
        print("menos seiscentos e trinta e três")
    elif numero == -632:
        print("menos seiscentos e trinta e dois")
    elif numero == -631:
        print("menos seiscentos e trinta e um")
    elif numero == -630:
        print("menos seiscentos e trinta")
    elif numero == -629:
        print("menos seiscentos e vinte e nove")
    elif numero == -628:
        print("menos seiscentos e vinte e oito")
    elif numero == -627:
        print("menos seiscentos e vinte e sete")
    elif numero == -626:
        print("menos seiscentos e vinte e seis")
    elif numero == -625:
        print("menos seiscentos e vinte e cinco")
    elif numero == -624:
        print("menos seiscentos e vinte e quatro")
    elif numero == -623:
        print("menos seiscentos e vinte e três")
    elif numero == -622:
        print("menos seiscentos e vinte e dois")
    elif numero == -621:
        print("menos seiscentos e vinte e um")
    elif numero == -620:
        print("menos seiscentos e vinte")
    elif numero == -619:
        print("menos seiscentos e dezenove")
    elif numero == -618:
        print("menos seiscentos e dezoito")
    elif numero == -617:
        print("menos seiscentos e dezessete")
    elif numero == -616:
        print("menos seiscentos e dezesseis")
    elif numero == -615:
        print("menos seiscentos e quinze")
    elif numero == -614:
        print("menos seiscentos e quatorze")
    elif numero == -613:
        print("menos seiscentos e treze")
    elif numero == -612:
        print("menos seiscentos e doze")
    elif numero == -611:
        print("menos seiscentos e onze")
    elif numero == -610:
        print("menos seiscentos e dez")
    elif numero == -609:
        print("menos seiscentos e nove")
    elif numero == -608:
        print("menos seiscentos e oito")
    elif numero == -607:
        print("menos seiscentos e sete")
    elif numero == -606:
        print("menos seiscentos e seis")
    elif numero == -605:
        print("menos seiscentos e cinco")
    elif numero == -604:
        print("menos seiscentos e quatro")
    elif numero == -603:
        print("menos seiscentos e três")
    elif numero == -602:
        print("menos seiscentos e dois")
    elif numero == -601:
        print("menos seiscentos e um")
    elif numero == -600:
        print("menos seiscentos")
    elif numero == -599:
        print("menos quinhentos e noventa e nove")
    elif numero == -598:
        print("menos quinhentos e noventa e oito")
    elif numero == -597:
        print("menos quinhentos e noventa e sete")
    elif numero == -596:
        print("menos quinhentos e noventa e seis")
    elif numero == -595:
        print("menos quinhentos e noventa e cinco")
    elif numero == -594:
        print("menos quinhentos e noventa e quatro")
    elif numero == -593:
        print("menos quinhentos e noventa e três")
    elif numero == -592:
        print("menos quinhentos e noventa e dois")
    elif numero == -591:
        print("menos quinhentos e noventa e um")
    elif numero == -590:
        print("menos quinhentos e noventa")
    elif numero == -589:
        print("menos quinhentos e oitenta e nove")
    elif numero == -588:
        print("menos quinhentos e oitenta e oito")
    elif numero == -587:
        print("menos quinhentos e oitenta e sete")
    elif numero == -586:
        print("menos quinhentos e oitenta e seis")
    elif numero == -585:
        print("menos quinhentos e oitenta e cinco")
    elif numero == -584:
        print("menos quinhentos e oitenta e quatro")
    elif numero == -583:
        print("menos quinhentos e oitenta e três")
    elif numero == -582:
        print("menos quinhentos e oitenta e dois")
    elif numero == -581:
        print("menos quinhentos e oitenta e um")
    elif numero == -580:
        print("menos quinhentos e oitenta")
    elif numero == -579:
        print("menos quinhentos e setenta e nove")
    elif numero == -578:
        print("menos quinhentos e setenta e oito")
    elif numero == -577:
        print("menos quinhentos e setenta e sete")
    elif numero == -576:
        print("menos quinhentos e setenta e seis")
    elif numero == -575:
        print("menos quinhentos e setenta e cinco")
    elif numero == -574:
        print("menos quinhentos e setenta e quatro")
    elif numero == -573:
        print("menos quinhentos e setenta e três")
    elif numero == -572:
        print("menos quinhentos e setenta e dois")
    elif numero == -571:
        print("menos quinhentos e setenta e um")
    elif numero == -570:
        print("menos quinhentos e setenta")
    elif numero == -569:
        print("menos quinhentos e sessenta e nove")
    elif numero == -568:
        print("menos quinhentos e sessenta e oito")
    elif numero == -567:
        print("menos quinhentos e sessenta e sete")
    elif numero == -566:
        print("menos quinhentos e sessenta e seis")
    elif numero == -565:
        print("menos quinhentos e sessenta e cinco")
    elif numero == -564:
        print("menos quinhentos e sessenta e quatro")
    elif numero == -563:
        print("menos quinhentos e sessenta e três")
    elif numero == -562:
        print("menos quinhentos e sessenta e dois")
    elif numero == -561:
        print("menos quinhentos e sessenta e um")
    elif numero == -560:
        print("menos quinhentos e sessenta")
    elif numero == -559:
        print("menos quinhentos e cinquenta e nove")
    elif numero == -558:
        print("menos quinhentos e cinquenta e oito")
    elif numero == -557:
        print("menos quinhentos e cinquenta e sete")
    elif numero == -556:
        print("menos quinhentos e cinquenta e seis")
    elif numero == -555:
        print("menos quinhentos e cinquenta e cinco")
    elif numero == -554:
        print("menos quinhentos e cinquenta e quatro")
    elif numero == -553:
        print("menos quinhentos e cinquenta e três")
    elif numero == -552:
        print("menos quinhentos e cinquenta e dois")
    elif numero == -551:
        print("menos quinhentos e cinquenta e um")
    elif numero == -550:
        print("menos quinhentos e cinquenta")
    elif numero == -549:
        print("menos quinhentos e quarenta e nove")
    elif numero == -548:
        print("menos quinhentos e quarenta e oito")
    elif numero == -547:
        print("menos quinhentos e quarenta e sete")
    elif numero == -546:
        print("menos quinhentos e quarenta e seis")
    elif numero == -545:
        print("menos quinhentos e quarenta e cinco")
    elif numero == -544:
        print("menos quinhentos e quarenta e quatro")
    elif numero == -543:
        print("menos quinhentos e quarenta e três")
    elif numero == -542:
        print("menos quinhentos e quarenta e dois")
    elif numero == -541:
        print("menos quinhentos e quarenta e um")
    elif numero == -540:
        print("menos quinhentos e quarenta")
    elif numero == -539:
        print("menos quinhentos e trinta e nove")
    elif numero == -538:
        print("menos quinhentos e trinta e oito")
    elif numero == -537:
        print("menos quinhentos e trinta e sete")
    elif numero == -536:
        print("menos quinhentos e trinta e seis")
    elif numero == -535:
        print("menos quinhentos e trinta e cinco")
    elif numero == -534:
        print("menos quinhentos e trinta e quatro")
    elif numero == -533:
        print("menos quinhentos e trinta e três")
    elif numero == -532:
        print("menos quinhentos e trinta e dois")
    elif numero == -531:
        print("menos quinhentos e trinta e um")
    elif numero == -530:
        print("menos quinhentos e trinta")
    elif numero == -529:
        print("menos quinhentos e vinte e nove")
    elif numero == -528:
        print("menos quinhentos e vinte e oito")
    elif numero == -527:
        print("menos quinhentos e vinte e sete")
    elif numero == -526:
        print("menos quinhentos e vinte e seis")
    elif numero == -525:
        print("menos quinhentos e vinte e cinco")
    elif numero == -524:
        print("menos quinhentos e vinte e quatro")
    elif numero == -523:
        print("menos quinhentos e vinte e três")
    elif numero == -522:
        print("menos quinhentos e vinte e dois")
    elif numero == -521:
        print("menos quinhentos e vinte e um")
    elif numero == -520:
        print("menos quinhentos e vinte")
    elif numero == -519:
        print("menos quinhentos e dezenove")
    elif numero == -518:
        print("menos quinhentos e dezoito")
    elif numero == -517:
        print("menos quinhentos e dezessete")
    elif numero == -516:
        print("menos quinhentos e dezesseis")
    elif numero == -515:
        print("menos quinhentos e quinze")
    elif numero == -514:
        print("menos quinhentos e quatorze")
    elif numero == -513:
        print("menos quinhentos e treze")
    elif numero == -512:
        print("menos quinhentos e doze")
    elif numero == -511:
        print("menos quinhentos e onze")
    elif numero == -510:
        print("menos quinhentos e dez")
    elif numero == -509:
        print("menos quinhentos e nove")
    elif numero == -508:
        print("menos quinhentos e oito")
    elif numero == -507:
        print("menos quinhentos e sete")
    elif numero == -506:
        print("menos quinhentos e seis")
    elif numero == -505:
        print("menos quinhentos e cinco")
    elif numero == -504:
        print("menos quinhentos e quatro")
    elif numero == -503:
        print("menos quinhentos e três")
    elif numero == -502:
        print("menos quinhentos e dois")
    elif numero == -501:
        print("menos quinhentos e um")
    elif numero == -500:
        print("menos quinhentos")
    elif numero == -499:
        print("menos quatrocentos e noventa e nove")
    elif numero == -498:
        print("menos quatrocentos e noventa e oito")
    elif numero == -497:
        print("menos quatrocentos e noventa e sete")
    elif numero == -496:
        print("menos quatrocentos e noventa e seis")
    elif numero == -495:
        print("menos quatrocentos e noventa e cinco")
    elif numero == -494:
        print("menos quatrocentos e noventa e quatro")
    elif numero == -493:
        print("menos quatrocentos e noventa e três")
    elif numero == -492:
        print("menos quatrocentos e noventa e dois")
    elif numero == -491:
        print("menos quatrocentos e noventa e um")
    elif numero == -490:
        print("menos quatrocentos e noventa")
    elif numero == -489:
        print("menos quatrocentos e oitenta e nove")
    elif numero == -488:
        print("menos quatrocentos e oitenta e oito")
    elif numero == -487:
        print("menos quatrocentos e oitenta e sete")
    elif numero == -486:
        print("menos quatrocentos e oitenta e seis")
    elif numero == -485:
        print("menos quatrocentos e oitenta e cinco")
    elif numero == -484:
        print("menos quatrocentos e oitenta e quatro")
    elif numero == -483:
        print("menos quatrocentos e oitenta e três")
    elif numero == -482:
        print("menos quatrocentos e oitenta e dois")
    elif numero == -481:
        print("menos quatrocentos e oitenta e um")
    elif numero == -480:
        print("menos quatrocentos e oitenta")
    elif numero == -479:
        print("menos quatrocentos e setenta e nove")
    elif numero == -478:
        print("menos quatrocentos e setenta e oito")
    elif numero == -477:
        print("menos quatrocentos e setenta e sete")
    elif numero == -476:
        print("menos quatrocentos e setenta e seis")
    elif numero == -475:
        print("menos quatrocentos e setenta e cinco")
    elif numero == -474:
        print("menos quatrocentos e setenta e quatro")
    elif numero == -473:
        print("menos quatrocentos e setenta e três")
    elif numero == -472:
        print("menos quatrocentos e setenta e dois")
    elif numero == -471:
        print("menos quatrocentos e setenta e um")
    elif numero == -470:
        print("menos quatrocentos e setenta")
    elif numero == -469:
        print("menos quatrocentos e sessenta e nove")
    elif numero == -468:
        print("menos quatrocentos e sessenta e oito")
    elif numero == -467:
        print("menos quatrocentos e sessenta e sete")
    elif numero == -466:
        print("menos quatrocentos e sessenta e seis")
    elif numero == -465:
        print("menos quatrocentos e sessenta e cinco")
    elif numero == -464:
        print("menos quatrocentos e sessenta e quatro")
    elif numero == -463:
        print("menos quatrocentos e sessenta e três")
    elif numero == -462:
        print("menos quatrocentos e sessenta e dois")
    elif numero == -461:
        print("menos quatrocentos e sessenta e um")
    elif numero == -460:
        print("menos quatrocentos e sessenta")
    elif numero == -459:
        print("menos quatrocentos e cinquenta e nove")
    elif numero == -458:
        print("menos quatrocentos e cinquenta e oito")
    elif numero == -457:
        print("menos quatrocentos e cinquenta e sete")
    elif numero == -456:
        print("menos quatrocentos e cinquenta e seis")
    elif numero == -455:
        print("menos quatrocentos e cinquenta e cinco")
    elif numero == -454:
        print("menos quatrocentos e cinquenta e quatro")
    elif numero == -453:
        print("menos quatrocentos e cinquenta e três")
    elif numero == -452:
        print("menos quatrocentos e cinquenta e dois")
    elif numero == -451:
        print("menos quatrocentos e cinquenta e um")
    elif numero == -450:
        print("menos quatrocentos e cinquenta")
    elif numero == -449:
        print("menos quatrocentos e quarenta e nove")
    elif numero == -448:
        print("menos quatrocentos e quarenta e oito")
    elif numero == -447:
        print("menos quatrocentos e quarenta e sete")
    elif numero == -446:
        print("menos quatrocentos e quarenta e seis")
    elif numero == -445:
        print("menos quatrocentos e quarenta e cinco")
    elif numero == -444:
        print("menos quatrocentos e quarenta e quatro")
    elif numero == -443:
        print("menos quatrocentos e quarenta e três")
    elif numero == -442:
        print("menos quatrocentos e quarenta e dois")
    elif numero == -441:
        print("menos quatrocentos e quarenta e um")
    elif numero == -440:
        print("menos quatrocentos e quarenta")
    elif numero == -439:
        print("menos quatrocentos e trinta e nove")
    elif numero == -438:
        print("menos quatrocentos e trinta e oito")
    elif numero == -437:
        print("menos quatrocentos e trinta e sete")
    elif numero == -436:
        print("menos quatrocentos e trinta e seis")
    elif numero == -435:
        print("menos quatrocentos e trinta e cinco")
    elif numero == -434:
        print("menos quatrocentos e trinta e quatro")
    elif numero == -433:
        print("menos quatrocentos e trinta e três")
    elif numero == -432:
        print("menos quatrocentos e trinta e dois")
    elif numero == -431:
        print("menos quatrocentos e trinta e um")
    elif numero == -430:
        print("menos quatrocentos e trinta")
    elif numero == -429:
        print("menos quatrocentos e vinte e nove")
    elif numero == -428:
        print("menos quatrocentos e vinte e oito")
    elif numero == -427:
        print("menos quatrocentos e vinte e sete")
    elif numero == -426:
        print("menos quatrocentos e vinte e seis")
    elif numero == -425:
        print("menos quatrocentos e vinte e cinco")
    elif numero == -424:
        print("menos quatrocentos e vinte e quatro")
    elif numero == -423:
        print("menos quatrocentos e vinte e três")
    elif numero == -422:
        print("menos quatrocentos e vinte e dois")
    elif numero == -421:
        print("menos quatrocentos e vinte e um")
    elif numero == -420:
        print("menos quatrocentos e vinte")
    elif numero == -419:
        print("menos quatrocentos e dezenove")
    elif numero == -418:
        print("menos quatrocentos e dezoito")
    elif numero == -417:
        print("menos quatrocentos e dezessete")
    elif numero == -416:
        print("menos quatrocentos e dezesseis")
    elif numero == -415:
        print("menos quatrocentos e quinze")
    elif numero == -414:
        print("menos quatrocentos e quatorze")
    elif numero == -413:
        print("menos quatrocentos e treze")
    elif numero == -412:
        print("menos quatrocentos e doze")
    elif numero == -411:
        print("menos quatrocentos e onze")
    elif numero == -410:
        print("menos quatrocentos e dez")
    elif numero == -409:
        print("menos quatrocentos e nove")
    elif numero == -408:
        print("menos quatrocentos e oito")
    elif numero == -407:
        print("menos quatrocentos e sete")
    elif numero == -406:
        print("menos quatrocentos e seis")
    elif numero == -405:
        print("menos quatrocentos e cinco")
    elif numero == -404:
        print("menos quatrocentos e quatro")
    elif numero == -403:
        print("menos quatrocentos e três")
    elif numero == -402:
        print("menos quatrocentos e dois")
    elif numero == -401:
        print("menos quatrocentos e um")
    elif numero == -400:
        print("menos quatrocentos")
    elif numero == -399:
        print("menos trezentos e noventa e nove")
    elif numero == -398:
        print("menos trezentos e noventa e oito")
    elif numero == -397:
        print("menos trezentos e noventa e sete")
    elif numero == -396:
        print("menos trezentos e noventa e seis")
    elif numero == -395:
        print("menos trezentos e noventa e cinco")
    elif numero == -394:
        print("menos trezentos e noventa e quatro")
    elif numero == -393:
        print("menos trezentos e noventa e três")
    elif numero == -392:
        print("menos trezentos e noventa e dois")
    elif numero == -391:
        print("menos trezentos e noventa e um")
    elif numero == -390:
        print("menos trezentos e noventa")
    elif numero == -389:
        print("menos trezentos e oitenta e nove")
    elif numero == -388:
        print("menos trezentos e oitenta e oito")
    elif numero == -387:
        print("menos trezentos e oitenta e sete")
    elif numero == -386:
        print("menos trezentos e oitenta e seis")
    elif numero == -385:
        print("menos trezentos e oitenta e cinco")
    elif numero == -384:
        print("menos trezentos e oitenta e quatro")
    elif numero == -383:
        print("menos trezentos e oitenta e três")
    elif numero == -382:
        print("menos trezentos e oitenta e dois")
    elif numero == -381:
        print("menos trezentos e oitenta e um")
    elif numero == -380:
        print("menos trezentos e oitenta")
    elif numero == -379:
        print("menos trezentos e setenta e nove")
    elif numero == -378:
        print("menos trezentos e setenta e oito")
    elif numero == -377:
        print("menos trezentos e setenta e sete")
    elif numero == -376:
        print("menos trezentos e setenta e seis")
    elif numero == -375:
        print("menos trezentos e setenta e cinco")
    elif numero == -374:
        print("menos trezentos e setenta e quatro")
    elif numero == -373:
        print("menos trezentos e setenta e três")
    elif numero == -372:
        print("menos trezentos e setenta e dois")
    elif numero == -371:
        print("menos trezentos e setenta e um")
    elif numero == -370:
        print("menos trezentos e setenta")
    elif numero == -369:
        print("menos trezentos e sessenta e nove")
    elif numero == -368:
        print("menos trezentos e sessenta e oito")
    elif numero == -367:
        print("menos trezentos e sessenta e sete")
    elif numero == -366:
        print("menos trezentos e sessenta e seis")
    elif numero == -365:
        print("menos trezentos e sessenta e cinco")
    elif numero == -364:
        print("menos trezentos e sessenta e quatro")
    elif numero == -363:
        print("menos trezentos e sessenta e três")
    elif numero == -362:
        print("menos trezentos e sessenta e dois")
    elif numero == -361:
        print("menos trezentos e sessenta e um")
    elif numero == -360:
        print("menos trezentos e sessenta")
    elif numero == -359:
        print("menos trezentos e cinquenta e nove")
    elif numero == -358:
        print("menos trezentos e cinquenta e oito")
    elif numero == -357:
        print("menos trezentos e cinquenta e sete")
    elif numero == -356:
        print("menos trezentos e cinquenta e seis")
    elif numero == -355:
        print("menos trezentos e cinquenta e cinco")
    elif numero == -354:
        print("menos trezentos e cinquenta e quatro")
    elif numero == -353:
        print("menos trezentos e cinquenta e três")
    elif numero == -352:
        print("menos trezentos e cinquenta e dois")
    elif numero == -351:
        print("menos trezentos e cinquenta e um")
    elif numero == -350:
        print("menos trezentos e cinquenta")
    elif numero == -349:
        print("menos trezentos e quarenta e nove")
    elif numero == -348:
        print("menos trezentos e quarenta e oito")
    elif numero == -347:
        print("menos trezentos e quarenta e sete")
    elif numero == -346:
        print("menos trezentos e quarenta e seis")
    elif numero == -345:
        print("menos trezentos e quarenta e cinco")
    elif numero == -344:
        print("menos trezentos e quarenta e quatro")
    elif numero == -343:
        print("menos trezentos e quarenta e três")
    elif numero == -342:
        print("menos trezentos e quarenta e dois")
    elif numero == -341:
        print("menos trezentos e quarenta e um")
    elif numero == -340:
        print("menos trezentos e quarenta")
    elif numero == -339:
        print("menos trezentos e trinta e nove")
    elif numero == -338:
        print("menos trezentos e trinta e oito")
    elif numero == -337:
        print("menos trezentos e trinta e sete")
    elif numero == -336:
        print("menos trezentos e trinta e seis")
    elif numero == -335:
        print("menos trezentos e trinta e cinco")
    elif numero == -334:
        print("menos trezentos e trinta e quatro")
    elif numero == -333:
        print("menos trezentos e trinta e três")
    elif numero == -332:
        print("menos trezentos e trinta e dois")
    elif numero == -331:
        print("menos trezentos e trinta e um")
    elif numero == -330:
        print("menos trezentos e trinta")
    elif numero == -329:
        print("menos trezentos e vinte e nove")
    elif numero == -328:
        print("menos trezentos e vinte e oito")
    elif numero == -327:
        print("menos trezentos e vinte e sete")
    elif numero == -326:
        print("menos trezentos e vinte e seis")
    elif numero == -325:
        print("menos trezentos e vinte e cinco")
    elif numero == -324:
        print("menos trezentos e vinte e quatro")
    elif numero == -323:
        print("menos trezentos e vinte e três")
    elif numero == -322:
        print("menos trezentos e vinte e dois")
    elif numero == -321:
        print("menos trezentos e vinte e um")
    elif numero == -320:
        print("menos trezentos e vinte")
    elif numero == -319:
        print("menos trezentos e dezenove")
    elif numero == -318:
        print("menos trezentos e dezoito")
    elif numero == -317:
        print("menos trezentos e dezessete")
    elif numero == -316:
        print("menos trezentos e dezesseis")
    elif numero == -315:
        print("menos trezentos e quinze")
    elif numero == -314:
        print("menos trezentos e quatorze")
    elif numero == -313:
        print("menos trezentos e treze")
    elif numero == -312:
        print("menos trezentos e doze")
    elif numero == -311:
        print("menos trezentos e onze")
    elif numero == -310:
        print("menos trezentos e dez")
    elif numero == -309:
        print("menos trezentos e nove")
    elif numero == -308:
        print("menos trezentos e oito")
    elif numero == -307:
        print("menos trezentos e sete")
    elif numero == -306:
        print("menos trezentos e seis")
    elif numero == -305:
        print("menos trezentos e cinco")
    elif numero == -304:
        print("menos trezentos e quatro")
    elif numero == -303:
        print("menos trezentos e três")
    elif numero == -302:
        print("menos trezentos e dois")
    elif numero == -301:
        print("menos trezentos e um")
    elif numero == -300:
        print("menos trezentos")
    elif numero == -299:
        print("menos duzentos e noventa e nove")
    elif numero == -298:
        print("menos duzentos e noventa e oito")
    elif numero == -297:
        print("menos duzentos e noventa e sete")
    elif numero == -296:
        print("menos duzentos e noventa e seis")
    elif numero == -295:
        print("menos duzentos e noventa e cinco")
    elif numero == -294:
        print("menos duzentos e noventa e quatro")
    elif numero == -293:
        print("menos duzentos e noventa e três")
    elif numero == -292:
        print("menos duzentos e noventa e dois")
    elif numero == -291:
        print("menos duzentos e noventa e um")
    elif numero == -290:
        print("menos duzentos e noventa")
    elif numero == -289:
        print("menos duzentos e oitenta e nove")
    elif numero == -288:
        print("menos duzentos e oitenta e oito")
    elif numero == -287:
        print("menos duzentos e oitenta e sete")
    elif numero == -286:
        print("menos duzentos e oitenta e seis")
    elif numero == -285:
        print("menos duzentos e oitenta e cinco")
    elif numero == -284:
        print("menos duzentos e oitenta e quatro")
    elif numero == -283:
        print("menos duzentos e oitenta e três")
    elif numero == -282:
        print("menos duzentos e oitenta e dois")
    elif numero == -281:
        print("menos duzentos e oitenta e um")
    elif numero == -280:
        print("menos duzentos e oitenta")
    elif numero == -279:
        print("menos duzentos e setenta e nove")
    elif numero == -278:
        print("menos duzentos e setenta e oito")
    elif numero == -277:
        print("menos duzentos e setenta e sete")
    elif numero == -276:
        print("menos duzentos e setenta e seis")
    elif numero == -275:
        print("menos duzentos e setenta e cinco")
    elif numero == -274:
        print("menos duzentos e setenta e quatro")
    elif numero == -273:
        print("menos duzentos e setenta e três")
    elif numero == -272:
        print("menos duzentos e setenta e dois")
    elif numero == -271:
        print("menos duzentos e setenta e um")
    elif numero == -270:
        print("menos duzentos e setenta")
    elif numero == -269:
        print("menos duzentos e sessenta e nove")
    elif numero == -268:
        print("menos duzentos e sessenta e oito")
    elif numero == -267:
        print("menos duzentos e sessenta e sete")
    elif numero == -266:
        print("menos duzentos e sessenta e seis")
    elif numero == -265:
        print("menos duzentos e sessenta e cinco")
    elif numero == -264:
        print("menos duzentos e sessenta e quatro")
    elif numero == -263:
        print("menos duzentos e sessenta e três")
    elif numero == -262:
        print("menos duzentos e sessenta e dois")
    elif numero == -261:
        print("menos duzentos e sessenta e um")
    elif numero == -260:
        print("menos duzentos e sessenta")
    elif numero == -259:
        print("menos duzentos e cinquenta e nove")
    elif numero == -258:
        print("menos duzentos e cinquenta e oito")
    elif numero == -257:
        print("menos duzentos e cinquenta e sete")
    elif numero == -256:
        print("menos duzentos e cinquenta e seis")
    elif numero == -255:
        print("menos duzentos e cinquenta e cinco")
    elif numero == -254:
        print("menos duzentos e cinquenta e quatro")
    elif numero == -253:
        print("menos duzentos e cinquenta e três")
    elif numero == -252:
        print("menos duzentos e cinquenta e dois")
    elif numero == -251:
        print("menos duzentos e cinquenta e um")
    elif numero == -250:
        print("menos duzentos e cinquenta")
    elif numero == -249:
        print("menos duzentos e quarenta e nove")
    elif numero == -248:
        print("menos duzentos e quarenta e oito")
    elif numero == -247:
        print("menos duzentos e quarenta e sete")
    elif numero == -246:
        print("menos duzentos e quarenta e seis")
    elif numero == -245:
        print("menos duzentos e quarenta e cinco")
    elif numero == -244:
        print("menos duzentos e quarenta e quatro")
    elif numero == -243:
        print("menos duzentos e quarenta e três")
    elif numero == -242:
        print("menos duzentos e quarenta e dois")
    elif numero == -241:
        print("menos duzentos e quarenta e um")
    elif numero == -240:
        print("menos duzentos e quarenta")
    elif numero == -239:
        print("menos duzentos e trinta e nove")
    elif numero == -238:
        print("menos duzentos e trinta e oito")
    elif numero == -237:
        print("menos duzentos e trinta e sete")
    elif numero == -236:
        print("menos duzentos e trinta e seis")
    elif numero == -235:
        print("menos duzentos e trinta e cinco")
    elif numero == -234:
        print("menos duzentos e trinta e quatro")
    elif numero == -233:
        print("menos duzentos e trinta e três")
    elif numero == -232:
        print("menos duzentos e trinta e dois")
    elif numero == -231:
        print("menos duzentos e trinta e um")
    elif numero == -230:
        print("menos duzentos e trinta")
    elif numero == -229:
        print("menos duzentos e vinte e nove")
    elif numero == -228:
        print("menos duzentos e vinte e oito")
    elif numero == -227:
        print("menos duzentos e vinte e sete")
    elif numero == -226:
        print("menos duzentos e vinte e seis")
    elif numero == -225:
        print("menos duzentos e vinte e cinco")
    elif numero == -224:
        print("menos duzentos e vinte e quatro")
    elif numero == -223:
        print("menos duzentos e vinte e três")
    elif numero == -222:
        print("menos duzentos e vinte e dois")
    elif numero == -221:
        print("menos duzentos e vinte e um")
    elif numero == -220:
        print("menos duzentos e vinte")
    elif numero == -219:
        print("menos duzentos e dezenove")
    elif numero == -218:
        print("menos duzentos e dezoito")
    elif numero == -217:
        print("menos duzentos e dezessete")
    elif numero == -216:
        print("menos duzentos e dezesseis")
    elif numero == -215:
        print("menos duzentos e quinze")
    elif numero == -214:
        print("menos duzentos e quatorze")
    elif numero == -213:
        print("menos duzentos e treze")
    elif numero == -212:
        print("menos duzentos e doze")
    elif numero == -211:
        print("menos duzentos e onze")
    elif numero == -210:
        print("menos duzentos e dez")
    elif numero == -209:
        print("menos duzentos e nove")
    elif numero == -208:
        print("menos duzentos e oito")
    elif numero == -207:
        print("menos duzentos e sete")
    elif numero == -206:
        print("menos duzentos e seis")
    elif numero == -205:
        print("menos duzentos e cinco")
    elif numero == -204:
        print("menos duzentos e quatro")
    elif numero == -203:
        print("menos duzentos e três")
    elif numero == -202:
        print("menos duzentos e dois")
    elif numero == -201:
        print("menos duzentos e um")
    elif numero == -200:
        print("menos duzentos")
    elif numero == -199:
        print("menos cem e noventa e nove")
    elif numero == -198:
        print("menos cem e noventa e oito")
    elif numero == -197:
        print("menos cem e noventa e sete")
    elif numero == -196:
        print("menos cem e noventa e seis")
    elif numero == -195:
        print("menos cem e noventa e cinco")
    elif numero == -194:
        print("menos cem e noventa e quatro")
    elif numero == -193:
        print("menos cem e noventa e três")
    elif numero == -192:
        print("menos cem e noventa e dois")
    elif numero == -191:
        print("menos cem e noventa e um")
    elif numero == -190:
        print("menos cem e noventa")
    elif numero == -189:
        print("menos cem e oitenta e nove")
    elif numero == -188:
        print("menos cem e oitenta e oito")
    elif numero == -187:
        print("menos cem e oitenta e sete")
    elif numero == -186:
        print("menos cem e oitenta e seis")
    elif numero == -185:
        print("menos cem e oitenta e cinco")
    elif numero == -184:
        print("menos cem e oitenta e quatro")
    elif numero == -183:
        print("menos cem e oitenta e três")
    elif numero == -182:
        print("menos cem e oitenta e dois")
    elif numero == -181:
        print("menos cem e oitenta e um")
    elif numero == -180:
        print("menos cem e oitenta")
    elif numero == -179:
        print("menos cem e setenta e nove")
    elif numero == -178:
        print("menos cem e setenta e oito")
    elif numero == -177:
        print("menos cem e setenta e sete")
    elif numero == -176:
        print("menos cem e setenta e seis")
    elif numero == -175:
        print("menos cem e setenta e cinco")
    elif numero == -174:
        print("menos cem e setenta e quatro")
    elif numero == -173:
        print("menos cem e setenta e três")
    elif numero == -172:
        print("menos cem e setenta e dois")
    elif numero == -171:
        print("menos cem e setenta e um")
    elif numero == -170:
        print("menos cem e setenta")
    elif numero == -169:
        print("menos cem e sessenta e nove")
    elif numero == -168:
        print("menos cem e sessenta e oito")
    elif numero == -167:
        print("menos cem e sessenta e sete")
    elif numero == -166:
        print("menos cem e sessenta e seis")
    elif numero == -165:
        print("menos cem e sessenta e cinco")
    elif numero == -164:
        print("menos cem e sessenta e quatro")
    elif numero == -163:
        print("menos cem e sessenta e três")
    elif numero == -162:
        print("menos cem e sessenta e dois")
    elif numero == -161:
        print("menos cem e sessenta e um")
    elif numero == -160:
        print("menos cem e sessenta")
    elif numero == -159:
        print("menos cem e cinquenta e nove")
    elif numero == -158:
        print("menos cem e cinquenta e oito")
    elif numero == -157:
        print("menos cem e cinquenta e sete")
    elif numero == -156:
        print("menos cem e cinquenta e seis")
    elif numero == -155:
        print("menos cem e cinquenta e cinco")
    elif numero == -154:
        print("menos cem e cinquenta e quatro")
    elif numero == -153:
        print("menos cem e cinquenta e três")
    elif numero == -152:
        print("menos cem e cinquenta e dois")
    elif numero == -151:
        print("menos cem e cinquenta e um")
    elif numero == -150:
        print("menos cem e cinquenta")
    elif numero == -149:
        print("menos cem e quarenta e nove")
    elif numero == -148:
        print("menos cem e quarenta e oito")
    elif numero == -147:
        print("menos cem e quarenta e sete")
    elif numero == -146:
        print("menos cem e quarenta e seis")
    elif numero == -145:
        print("menos cem e quarenta e cinco")
    elif numero == -144:
        print("menos cem e quarenta e quatro")
    elif numero == -143:
        print("menos cem e quarenta e três")
    elif numero == -142:
        print("menos cem e quarenta e dois")
    elif numero == -141:
        print("menos cem e quarenta e um")
    elif numero == -140:
        print("menos cem e quarenta")
    elif numero == -139:
        print("menos cem e trinta e nove")
    elif numero == -138:
        print("menos cem e trinta e oito")
    elif numero == -137:
        print("menos cem e trinta e sete")
    elif numero == -136:
        print("menos cem e trinta e seis")
    elif numero == -135:
        print("menos cem e trinta e cinco")
    elif numero == -134:
        print("menos cem e trinta e quatro")
    elif numero == -133:
        print("menos cem e trinta e três")
    elif numero == -132:
        print("menos cem e trinta e dois")
    elif numero == -131:
        print("menos cem e trinta e um")
    elif numero == -130:
        print("menos cem e trinta")
    elif numero == -129:
        print("menos cem e vinte e nove")
    elif numero == -128:
        print("menos cem e vinte e oito")
    elif numero == -127:
        print("menos cem e vinte e sete")
    elif numero == -126:
        print("menos cem e vinte e seis")
    elif numero == -125:
        print("menos cem e vinte e cinco")
    elif numero == -124:
        print("menos cem e vinte e quatro")
    elif numero == -123:
        print("menos cem e vinte e três")
    elif numero == -122:
        print("menos cem e vinte e dois")
    elif numero == -121:
        print("menos cem e vinte e um")
    elif numero == -120:
        print("menos cem e vinte")
    elif numero == -119:
        print("menos cem e dezenove")
    elif numero == -118:
        print("menos cem e dezoito")
    elif numero == -117:
        print("menos cem e dezessete")
    elif numero == -116:
        print("menos cem e dezesseis")
    elif numero == -115:
        print("menos cem e quinze")
    elif numero == -114:
        print("menos cem e quatorze")
    elif numero == -113:
        print("menos cem e treze")
    elif numero == -112:
        print("menos cem e doze")
    elif numero == -111:
        print("menos cem e onze")
    elif numero == -110:
        print("menos cem e dez")
    elif numero == -109:
        print("menos cem e nove")
    elif numero == -108:
        print("menos cem e oito")
    elif numero == -107:
        print("menos cem e sete")
    elif numero == -106:
        print("menos cem e seis")
    elif numero == -105:
        print("menos cem e cinco")
    elif numero == -104:
        print("menos cem e quatro")
    elif numero == -103:
        print("menos cem e três")
    elif numero == -102:
        print("menos cem e dois")
    elif numero == -101:
        print("menos cem e um")
    elif numero == -100:
        print("menos cem")
    elif numero == -99:
        print("menos noventa e nove")
    elif numero == -98:
        print("menos noventa e oito")
    elif numero == -97:
        print("menos noventa e sete")
    elif numero == -96:
        print("menos noventa e seis")
    elif numero == -95:
        print("menos noventa e cinco")
    elif numero == -94:
        print("menos noventa e quatro")
    elif numero == -93:
        print("menos noventa e três")
    elif numero == -92:
        print("menos noventa e dois")
    elif numero == -91:
        print("menos noventa e um")
    elif numero == -90:
        print("menos noventa")
    elif numero == -89:
        print("menos oitenta e nove")
    elif numero == -88:
        print("menos oitenta e oito")
    elif numero == -87:
        print("menos oitenta e sete")
    elif numero == -86:
        print("menos oitenta e seis")
    elif numero == -85:
        print("menos oitenta e cinco")
    elif numero == -84:
        print("menos oitenta e quatro")
    elif numero == -83:
        print("menos oitenta e três")
    elif numero == -82:
        print("menos oitenta e dois")
    elif numero == -81:
        print("menos oitenta e um")
    elif numero == -80:
        print("menos oitenta")
    elif numero == -79:
        print("menos setenta e nove")
    elif numero == -78:
        print("menos setenta e oito")
    elif numero == -77:
        print("menos setenta e sete")
    elif numero == -76:
        print("menos setenta e seis")
    elif numero == -75:
        print("menos setenta e cinco")
    elif numero == -74:
        print("menos setenta e quatro")
    elif numero == -73:
        print("menos setenta e três")
    elif numero == -72:
        print("menos setenta e dois")
    elif numero == -71:
        print("menos setenta e um")
    elif numero == -70:
        print("menos setenta")
    elif numero == -69:
        print("menos sessenta e nove")
    elif numero == -68:
        print("menos sessenta e oito")
    elif numero == -67:
        print("menos sessenta e sete")
    elif numero == -66:
        print("menos sessenta e seis")
    elif numero == -65:
        print("menos sessenta e cinco")
    elif numero == -64:
        print("menos sessenta e quatro")
    elif numero == -63:
        print("menos sessenta e três")
    elif numero == -62:
        print("menos sessenta e dois")
    elif numero == -61:
        print("menos sessenta e um")
    elif numero == -60:
        print("menos sessenta")
    elif numero == -59:
        print("menos cinquenta e nove")
    elif numero == -58:
        print("menos cinquenta e oito")
    elif numero == -57:
        print("menos cinquenta e sete")
    elif numero == -56:
        print("menos cinquenta e seis")
    elif numero == -55:
        print("menos cinquenta e cinco")
    elif numero == -54:
        print("menos cinquenta e quatro")
    elif numero == -53:
        print("menos cinquenta e três")
    elif numero == -52:
        print("menos cinquenta e dois")
    elif numero == -51:
        print("menos cinquenta e um")
    elif numero == -50:
        print("menos cinquenta")
    elif numero == -49:
        print("menos quarenta e nove")
    elif numero == -48:
        print("menos quarenta e oito")
    elif numero == -47:
        print("menos quarenta e sete")
    elif numero == -46:
        print("menos quarenta e seis")
    elif numero == -45:
        print("menos quarenta e cinco")
    elif numero == -44:
        print("menos quarenta e quatro")
    elif numero == -43:
        print("menos quarenta e três")
    elif numero == -42:
        print("menos quarenta e dois")
    elif numero == -41:
        print("menos quarenta e um")
    elif numero == -40:
        print("menos quarenta")
    elif numero == -39:
        print("menos trinta e nove")
    elif numero == -38:
        print("menos trinta e oito")
    elif numero == -37:
        print("menos trinta e sete")
    elif numero == -36:
        print("menos trinta e seis")
    elif numero == -35:
        print("menos trinta e cinco")
    elif numero == -34:
        print("menos trinta e quatro")
    elif numero == -33:
        print("menos trinta e três")
    elif numero == -32:
        print("menos trinta e dois")
    elif numero == -31:
        print("menos trinta e um")
    elif numero == -30:
        print("menos trinta")
    elif numero == -29:
        print("menos vinte e nove")
    elif numero == -28:
        print("menos vinte e oito")
    elif numero == -27:
        print("menos vinte e sete")
    elif numero == -26:
        print("menos vinte e seis")
    elif numero == -25:
        print("menos vinte e cinco")
    elif numero == -24:
        print("menos vinte e quatro")
    elif numero == -23:
        print("menos vinte e três")
    elif numero == -22:
        print("menos vinte e dois")
    elif numero == -21:
        print("menos vinte e um")
    elif numero == -20:
        print("menos vinte")
    elif numero == -19:
        print("menos dezenove")
    elif numero == -18:
        print("menos dezoito")
    elif numero == -17:
        print("menos dezessete")
    elif numero == -16:
        print("menos dezesseis")
    elif numero == -15:
        print("menos quinze")
    elif numero == -14:
        print("menos quatorze")
    elif numero == -13:
        print("menos treze")
    elif numero == -12:
        print("menos doze")
    elif numero == -11:
        print("menos onze")
    elif numero == -10:
        print("menos dez")
    elif numero == -9:
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
    elif numero == 10:
        print("dez")
    elif numero == 11:
        print("onze")
    elif numero == 12:
        print("doze")
    elif numero == 13:
        print("treze")
    elif numero == 14:
        print("quatorze")
    elif numero == 15:
        print("quinze")
    elif numero == 16:
        print("dezesseis")
    elif numero == 17:
        print("dezessete")
    elif numero == 18:
        print("dezoito")
    elif numero == 19:
        print("dezenove")
    elif numero == 20:
        print("vinte")
    elif numero == 21:
        print("vinte e um")
    elif numero == 22:
        print("vinte e dois")
    elif numero == 23:
        print("vinte e três")
    elif numero == 24:
        print("vinte e quatro")
    elif numero == 25:
        print("vinte e cinco")
    elif numero == 26:
        print("vinte e seis")
    elif numero == 27:
        print("vinte e sete")
    elif numero == 28:
        print("vinte e oito")
    elif numero == 29:
        print("vinte e nove")
    elif numero == 30:
        print("trinta")
    elif numero == 31:
        print("trinta e um")
    elif numero == 32:
        print("trinta e dois")
    elif numero == 33:
        print("trinta e três")
    elif numero == 34:
        print("trinta e quatro")
    elif numero == 35:
        print("trinta e cinco")
    elif numero == 36:
        print("trinta e seis")
    elif numero == 37:
        print("trinta e sete")
    elif numero == 38:
        print("trinta e oito")
    elif numero == 39:
        print("trinta e nove")
    elif numero == 40:
        print("quarenta")
    elif numero == 41:
        print("quarenta e um")
    elif numero == 42:
        print("quarenta e dois")
    elif numero == 43:
        print("quarenta e três")
    elif numero == 44:
        print("quarenta e quatro")
    elif numero == 45:
        print("quarenta e cinco")
    elif numero == 46:
        print("quarenta e seis")
    elif numero == 47:
        print("quarenta e sete")
    elif numero == 48:
        print("quarenta e oito")
    elif numero == 49:
        print("quarenta e nove")
    elif numero == 50:
        print("cinquenta")
    elif numero == 51:
        print("cinquenta e um")
    elif numero == 52:
        print("cinquenta e dois")
    elif numero == 53:
        print("cinquenta e três")
    elif numero == 54:
        print("cinquenta e quatro")
    elif numero == 55:
        print("cinquenta e cinco")
    elif numero == 56:
        print("cinquenta e seis")
    elif numero == 57:
        print("cinquenta e sete")
    elif numero == 58:
        print("cinquenta e oito")
    elif numero == 59:
        print("cinquenta e nove")
    elif numero == 60:
        print("sessenta")
    elif numero == 61:
        print("sessenta e um")
    elif numero == 62:
        print("sessenta e dois")
    elif numero == 63:
        print("sessenta e três")
    elif numero == 64:
        print("sessenta e quatro")
    elif numero == 65:
        print("sessenta e cinco")
    elif numero == 66:
        print("sessenta e seis")
    elif numero == 67:
        print("sessenta e sete")
    elif numero == 68:
        print("sessenta e oito")
    elif numero == 69:
        print("sessenta e nove")
    elif numero == 70:
        print("setenta")
    elif numero == 71:
        print("setenta e um")
    elif numero == 72:
        print("setenta e dois")
    elif numero == 73:
        print("setenta e três")
    elif numero == 74:
        print("setenta e quatro")
    elif numero == 75:
        print("setenta e cinco")
    elif numero == 76:
        print("setenta e seis")
    elif numero == 77:
        print("setenta e sete")
    elif numero == 78:
        print("setenta e oito")
    elif numero == 79:
        print("setenta e nove")
    elif numero == 80:
        print("oitenta")
    elif numero == 81:
        print("oitenta e um")
    elif numero == 82:
        print("oitenta e dois")
    elif numero == 83:
        print("oitenta e três")
    elif numero == 84:
        print("oitenta e quatro")
    elif numero == 85:
        print("oitenta e cinco")
    elif numero == 86:
        print("oitenta e seis")
    elif numero == 87:
        print("oitenta e sete")
    elif numero == 88:
        print("oitenta e oito")
    elif numero == 89:
        print("oitenta e nove")
    elif numero == 90:
        print("noventa")
    elif numero == 91:
        print("noventa e um")
    elif numero == 92:
        print("noventa e dois")
    elif numero == 93:
        print("noventa e três")
    elif numero == 94:
        print("noventa e quatro")
    elif numero == 95:
        print("noventa e cinco")
    elif numero == 96:
        print("noventa e seis")
    elif numero == 97:
        print("noventa e sete")
    elif numero == 98:
        print("noventa e oito")
    elif numero == 99:
        print("noventa e nove")
    elif numero == 100:
        print("cem")
    elif numero == 101:
        print("cem e um")
    elif numero == 102:
        print("cem e dois")
    elif numero == 103:
        print("cem e três")
    elif numero == 104:
        print("cem e quatro")
    elif numero == 105:
        print("cem e cinco")
    elif numero == 106:
        print("cem e seis")
    elif numero == 107:
        print("cem e sete")
    elif numero == 108:
        print("cem e oito")
    elif numero == 109:
        print("cem e nove")
    elif numero == 110:
        print("cem e dez")
    elif numero == 111:
        print("cem e onze")
    elif numero == 112:
        print("cem e doze")
    elif numero == 113:
        print("cem e treze")
    elif numero == 114:
        print("cem e quatorze")
    elif numero == 115:
        print("cem e quinze")
    elif numero == 116:
        print("cem e dezesseis")
    elif numero == 117:
        print("cem e dezessete")
    elif numero == 118:
        print("cem e dezoito")
    elif numero == 119:
        print("cem e dezenove")
    elif numero == 120:
        print("cem e vinte")
    elif numero == 121:
        print("cem e vinte e um")
    elif numero == 122:
        print("cem e vinte e dois")
    elif numero == 123:
        print("cem e vinte e três")
    elif numero == 124:
        print("cem e vinte e quatro")
    elif numero == 125:
        print("cem e vinte e cinco")
    elif numero == 126:
        print("cem e vinte e seis")
    elif numero == 127:
        print("cem e vinte e sete")
    elif numero == 128:
        print("cem e vinte e oito")
    elif numero == 129:
        print("cem e vinte e nove")
    elif numero == 130:
        print("cem e trinta")
    elif numero == 131:
        print("cem e trinta e um")
    elif numero == 132:
        print("cem e trinta e dois")
    elif numero == 133:
        print("cem e trinta e três")
    elif numero == 134:
        print("cem e trinta e quatro")
    elif numero == 135:
        print("cem e trinta e cinco")
    elif numero == 136:
        print("cem e trinta e seis")
    elif numero == 137:
        print("cem e trinta e sete")
    elif numero == 138:
        print("cem e trinta e oito")
    elif numero == 139:
        print("cem e trinta e nove")
    elif numero == 140:
        print("cem e quarenta")
    elif numero == 141:
        print("cem e quarenta e um")
    elif numero == 142:
        print("cem e quarenta e dois")
    elif numero == 143:
        print("cem e quarenta e três")
    elif numero == 144:
        print("cem e quarenta e quatro")
    elif numero == 145:
        print("cem e quarenta e cinco")
    elif numero == 146:
        print("cem e quarenta e seis")
    elif numero == 147:
        print("cem e quarenta e sete")
    elif numero == 148:
        print("cem e quarenta e oito")
    elif numero == 149:
        print("cem e quarenta e nove")
    elif numero == 150:
        print("cem e cinquenta")
    elif numero == 151:
        print("cem e cinquenta e um")
    elif numero == 152:
        print("cem e cinquenta e dois")
    elif numero == 153:
        print("cem e cinquenta e três")
    elif numero == 154:
        print("cem e cinquenta e quatro")
    elif numero == 155:
        print("cem e cinquenta e cinco")
    elif numero == 156:
        print("cem e cinquenta e seis")
    elif numero == 157:
        print("cem e cinquenta e sete")
    elif numero == 158:
        print("cem e cinquenta e oito")
    elif numero == 159:
        print("cem e cinquenta e nove")
    elif numero == 160:
        print("cem e sessenta")
    elif numero == 161:
        print("cem e sessenta e um")
    elif numero == 162:
        print("cem e sessenta e dois")
    elif numero == 163:
        print("cem e sessenta e três")
    elif numero == 164:
        print("cem e sessenta e quatro")
    elif numero == 165:
        print("cem e sessenta e cinco")
    elif numero == 166:
        print("cem e sessenta e seis")
    elif numero == 167:
        print("cem e sessenta e sete")
    elif numero == 168:
        print("cem e sessenta e oito")
    elif numero == 169:
        print("cem e sessenta e nove")
    elif numero == 170:
        print("cem e setenta")
    elif numero == 171:
        print("cem e setenta e um")
    elif numero == 172:
        print("cem e setenta e dois")
    elif numero == 173:
        print("cem e setenta e três")
    elif numero == 174:
        print("cem e setenta e quatro")
    elif numero == 175:
        print("cem e setenta e cinco")
    elif numero == 176:
        print("cem e setenta e seis")
    elif numero == 177:
        print("cem e setenta e sete")
    elif numero == 178:
        print("cem e setenta e oito")
    elif numero == 179:
        print("cem e setenta e nove")
    elif numero == 180:
        print("cem e oitenta")
    elif numero == 181:
        print("cem e oitenta e um")
    elif numero == 182:
        print("cem e oitenta e dois")
    elif numero == 183:
        print("cem e oitenta e três")
    elif numero == 184:
        print("cem e oitenta e quatro")
    elif numero == 185:
        print("cem e oitenta e cinco")
    elif numero == 186:
        print("cem e oitenta e seis")
    elif numero == 187:
        print("cem e oitenta e sete")
    elif numero == 188:
        print("cem e oitenta e oito")
    elif numero == 189:
        print("cem e oitenta e nove")
    elif numero == 190:
        print("cem e noventa")
    elif numero == 191:
        print("cem e noventa e um")
    elif numero == 192:
        print("cem e noventa e dois")
    elif numero == 193:
        print("cem e noventa e três")
    elif numero == 194:
        print("cem e noventa e quatro")
    elif numero == 195:
        print("cem e noventa e cinco")
    elif numero == 196:
        print("cem e noventa e seis")
    elif numero == 197:
        print("cem e noventa e sete")
    elif numero == 198:
        print("cem e noventa e oito")
    elif numero == 199:
        print("cem e noventa e nove")
    elif numero == 200:
        print("duzentos")
    elif numero == 201:
        print("duzentos e um")
    elif numero == 202:
        print("duzentos e dois")
    elif numero == 203:
        print("duzentos e três")
    elif numero == 204:
        print("duzentos e quatro")
    elif numero == 205:
        print("duzentos e cinco")
    elif numero == 206:
        print("duzentos e seis")
    elif numero == 207:
        print("duzentos e sete")
    elif numero == 208:
        print("duzentos e oito")
    elif numero == 209:
        print("duzentos e nove")
    elif numero == 210:
        print("duzentos e dez")
    elif numero == 211:
        print("duzentos e onze")
    elif numero == 212:
        print("duzentos e doze")
    elif numero == 213:
        print("duzentos e treze")
    elif numero == 214:
        print("duzentos e quatorze")
    elif numero == 215:
        print("duzentos e quinze")
    elif numero == 216:
        print("duzentos e dezesseis")
    elif numero == 217:
        print("duzentos e dezessete")
    elif numero == 218:
        print("duzentos e dezoito")
    elif numero == 219:
        print("duzentos e dezenove")
    elif numero == 220:
        print("duzentos e vinte")
    elif numero == 221:
        print("duzentos e vinte e um")
    elif numero == 222:
        print("duzentos e vinte e dois")
    elif numero == 223:
        print("duzentos e vinte e três")
    elif numero == 224:
        print("duzentos e vinte e quatro")
    elif numero == 225:
        print("duzentos e vinte e cinco")
    elif numero == 226:
        print("duzentos e vinte e seis")
    elif numero == 227:
        print("duzentos e vinte e sete")
    elif numero == 228:
        print("duzentos e vinte e oito")
    elif numero == 229:
        print("duzentos e vinte e nove")
    elif numero == 230:
        print("duzentos e trinta")
    elif numero == 231:
        print("duzentos e trinta e um")
    elif numero == 232:
        print("duzentos e trinta e dois")
    elif numero == 233:
        print("duzentos e trinta e três")
    elif numero == 234:
        print("duzentos e trinta e quatro")
    elif numero == 235:
        print("duzentos e trinta e cinco")
    elif numero == 236:
        print("duzentos e trinta e seis")
    elif numero == 237:
        print("duzentos e trinta e sete")
    elif numero == 238:
        print("duzentos e trinta e oito")
    elif numero == 239:
        print("duzentos e trinta e nove")
    elif numero == 240:
        print("duzentos e quarenta")
    elif numero == 241:
        print("duzentos e quarenta e um")
    elif numero == 242:
        print("duzentos e quarenta e dois")
    elif numero == 243:
        print("duzentos e quarenta e três")
    elif numero == 244:
        print("duzentos e quarenta e quatro")
    elif numero == 245:
        print("duzentos e quarenta e cinco")
    elif numero == 246:
        print("duzentos e quarenta e seis")
    elif numero == 247:
        print("duzentos e quarenta e sete")
    elif numero == 248:
        print("duzentos e quarenta e oito")
    elif numero == 249:
        print("duzentos e quarenta e nove")
    elif numero == 250:
        print("duzentos e cinquenta")
    elif numero == 251:
        print("duzentos e cinquenta e um")
    elif numero == 252:
        print("duzentos e cinquenta e dois")
    elif numero == 253:
        print("duzentos e cinquenta e três")
    elif numero == 254:
        print("duzentos e cinquenta e quatro")
    elif numero == 255:
        print("duzentos e cinquenta e cinco")
    elif numero == 256:
        print("duzentos e cinquenta e seis")
    elif numero == 257:
        print("duzentos e cinquenta e sete")
    elif numero == 258:
        print("duzentos e cinquenta e oito")
    elif numero == 259:
        print("duzentos e cinquenta e nove")
    elif numero == 260:
        print("duzentos e sessenta")
    elif numero == 261:
        print("duzentos e sessenta e um")
    elif numero == 262:
        print("duzentos e sessenta e dois")
    elif numero == 263:
        print("duzentos e sessenta e três")
    elif numero == 264:
        print("duzentos e sessenta e quatro")
    elif numero == 265:
        print("duzentos e sessenta e cinco")
    elif numero == 266:
        print("duzentos e sessenta e seis")
    elif numero == 267:
        print("duzentos e sessenta e sete")
    elif numero == 268:
        print("duzentos e sessenta e oito")
    elif numero == 269:
        print("duzentos e sessenta e nove")
    elif numero == 270:
        print("duzentos e setenta")
    elif numero == 271:
        print("duzentos e setenta e um")
    elif numero == 272:
        print("duzentos e setenta e dois")
    elif numero == 273:
        print("duzentos e setenta e três")
    elif numero == 274:
        print("duzentos e setenta e quatro")
    elif numero == 275:
        print("duzentos e setenta e cinco")
    elif numero == 276:
        print("duzentos e setenta e seis")
    elif numero == 277:
        print("duzentos e setenta e sete")
    elif numero == 278:
        print("duzentos e setenta e oito")
    elif numero == 279:
        print("duzentos e setenta e nove")
    elif numero == 280:
        print("duzentos e oitenta")
    elif numero == 281:
        print("duzentos e oitenta e um")
    elif numero == 282:
        print("duzentos e oitenta e dois")
    elif numero == 283:
        print("duzentos e oitenta e três")
    elif numero == 284:
        print("duzentos e oitenta e quatro")
    elif numero == 285:
        print("duzentos e oitenta e cinco")
    elif numero == 286:
        print("duzentos e oitenta e seis")
    elif numero == 287:
        print("duzentos e oitenta e sete")
    elif numero == 288:
        print("duzentos e oitenta e oito")
    elif numero == 289:
        print("duzentos e oitenta e nove")
    elif numero == 290:
        print("duzentos e noventa")
    elif numero == 291:
        print("duzentos e noventa e um")
    elif numero == 292:
        print("duzentos e noventa e dois")
    elif numero == 293:
        print("duzentos e noventa e três")
    elif numero == 294:
        print("duzentos e noventa e quatro")
    elif numero == 295:
        print("duzentos e noventa e cinco")
    elif numero == 296:
        print("duzentos e noventa e seis")
    elif numero == 297:
        print("duzentos e noventa e sete")
    elif numero == 298:
        print("duzentos e noventa e oito")
    elif numero == 299:
        print("duzentos e noventa e nove")
    elif numero == 300:
        print("trezentos")
    elif numero == 301:
        print("trezentos e um")
    elif numero == 302:
        print("trezentos e dois")
    elif numero == 303:
        print("trezentos e três")
    elif numero == 304:
        print("trezentos e quatro")
    elif numero == 305:
        print("trezentos e cinco")
    elif numero == 306:
        print("trezentos e seis")
    elif numero == 307:
        print("trezentos e sete")
    elif numero == 308:
        print("trezentos e oito")
    elif numero == 309:
        print("trezentos e nove")
    elif numero == 310:
        print("trezentos e dez")
    elif numero == 311:
        print("trezentos e onze")
    elif numero == 312:
        print("trezentos e doze")
    elif numero == 313:
        print("trezentos e treze")
    elif numero == 314:
        print("trezentos e quatorze")
    elif numero == 315:
        print("trezentos e quinze")
    elif numero == 316:
        print("trezentos e dezesseis")
    elif numero == 317:
        print("trezentos e dezessete")
    elif numero == 318:
        print("trezentos e dezoito")
    elif numero == 319:
        print("trezentos e dezenove")
    elif numero == 320:
        print("trezentos e vinte")
    elif numero == 321:
        print("trezentos e vinte e um")
    elif numero == 322:
        print("trezentos e vinte e dois")
    elif numero == 323:
        print("trezentos e vinte e três")
    elif numero == 324:
        print("trezentos e vinte e quatro")
    elif numero == 325:
        print("trezentos e vinte e cinco")
    elif numero == 326:
        print("trezentos e vinte e seis")
    elif numero == 327:
        print("trezentos e vinte e sete")
    elif numero == 328:
        print("trezentos e vinte e oito")
    elif numero == 329:
        print("trezentos e vinte e nove")
    elif numero == 330:
        print("trezentos e trinta")
    elif numero == 331:
        print("trezentos e trinta e um")
    elif numero == 332:
        print("trezentos e trinta e dois")
    elif numero == 333:
        print("trezentos e trinta e três")
    elif numero == 334:
        print("trezentos e trinta e quatro")
    elif numero == 335:
        print("trezentos e trinta e cinco")
    elif numero == 336:
        print("trezentos e trinta e seis")
    elif numero == 337:
        print("trezentos e trinta e sete")
    elif numero == 338:
        print("trezentos e trinta e oito")
    elif numero == 339:
        print("trezentos e trinta e nove")
    elif numero == 340:
        print("trezentos e quarenta")
    elif numero == 341:
        print("trezentos e quarenta e um")
    elif numero == 342:
        print("trezentos e quarenta e dois")
    elif numero == 343:
        print("trezentos e quarenta e três")
    elif numero == 344:
        print("trezentos e quarenta e quatro")
    elif numero == 345:
        print("trezentos e quarenta e cinco")
    elif numero == 346:
        print("trezentos e quarenta e seis")
    elif numero == 347:
        print("trezentos e quarenta e sete")
    elif numero == 348:
        print("trezentos e quarenta e oito")
    elif numero == 349:
        print("trezentos e quarenta e nove")
    elif numero == 350:
        print("trezentos e cinquenta")
    elif numero == 351:
        print("trezentos e cinquenta e um")
    elif numero == 352:
        print("trezentos e cinquenta e dois")
    elif numero == 353:
        print("trezentos e cinquenta e três")
    elif numero == 354:
        print("trezentos e cinquenta e quatro")
    elif numero == 355:
        print("trezentos e cinquenta e cinco")
    elif numero == 356:
        print("trezentos e cinquenta e seis")
    elif numero == 357:
        print("trezentos e cinquenta e sete")
    elif numero == 358:
        print("trezentos e cinquenta e oito")
    elif numero == 359:
        print("trezentos e cinquenta e nove")
    elif numero == 360:
        print("trezentos e sessenta")
    elif numero == 361:
        print("trezentos e sessenta e um")
    elif numero == 362:
        print("trezentos e sessenta e dois")
    elif numero == 363:
        print("trezentos e sessenta e três")
    elif numero == 364:
        print("trezentos e sessenta e quatro")
    elif numero == 365:
        print("trezentos e sessenta e cinco")
    elif numero == 366:
        print("trezentos e sessenta e seis")
    elif numero == 367:
        print("trezentos e sessenta e sete")
    elif numero == 368:
        print("trezentos e sessenta e oito")
    elif numero == 369:
        print("trezentos e sessenta e nove")
    elif numero == 370:
        print("trezentos e setenta")
    elif numero == 371:
        print("trezentos e setenta e um")
    elif numero == 372:
        print("trezentos e setenta e dois")
    elif numero == 373:
        print("trezentos e setenta e três")
    elif numero == 374:
        print("trezentos e setenta e quatro")
    elif numero == 375:
        print("trezentos e setenta e cinco")
    elif numero == 376:
        print("trezentos e setenta e seis")
    elif numero == 377:
        print("trezentos e setenta e sete")
    elif numero == 378:
        print("trezentos e setenta e oito")
    elif numero == 379:
        print("trezentos e setenta e nove")
    elif numero == 380:
        print("trezentos e oitenta")
    elif numero == 381:
        print("trezentos e oitenta e um")
    elif numero == 382:
        print("trezentos e oitenta e dois")
    elif numero == 383:
        print("trezentos e oitenta e três")
    elif numero == 384:
        print("trezentos e oitenta e quatro")
    elif numero == 385:
        print("trezentos e oitenta e cinco")
    elif numero == 386:
        print("trezentos e oitenta e seis")
    elif numero == 387:
        print("trezentos e oitenta e sete")
    elif numero == 388:
        print("trezentos e oitenta e oito")
    elif numero == 389:
        print("trezentos e oitenta e nove")
    elif numero == 390:
        print("trezentos e noventa")
    elif numero == 391:
        print("trezentos e noventa e um")
    elif numero == 392:
        print("trezentos e noventa e dois")
    elif numero == 393:
        print("trezentos e noventa e três")
    elif numero == 394:
        print("trezentos e noventa e quatro")
    elif numero == 395:
        print("trezentos e noventa e cinco")
    elif numero == 396:
        print("trezentos e noventa e seis")
    elif numero == 397:
        print("trezentos e noventa e sete")
    elif numero == 398:
        print("trezentos e noventa e oito")
    elif numero == 399:
        print("trezentos e noventa e nove")
    elif numero == 400:
        print("quatrocentos")
    elif numero == 401:
        print("quatrocentos e um")
    elif numero == 402:
        print("quatrocentos e dois")
    elif numero == 403:
        print("quatrocentos e três")
    elif numero == 404:
        print("quatrocentos e quatro")
    elif numero == 405:
        print("quatrocentos e cinco")
    elif numero == 406:
        print("quatrocentos e seis")
    elif numero == 407:
        print("quatrocentos e sete")
    elif numero == 408:
        print("quatrocentos e oito")
    elif numero == 409:
        print("quatrocentos e nove")
    elif numero == 410:
        print("quatrocentos e dez")
    elif numero == 411:
        print("quatrocentos e onze")
    elif numero == 412:
        print("quatrocentos e doze")
    elif numero == 413:
        print("quatrocentos e treze")
    elif numero == 414:
        print("quatrocentos e quatorze")
    elif numero == 415:
        print("quatrocentos e quinze")
    elif numero == 416:
        print("quatrocentos e dezesseis")
    elif numero == 417:
        print("quatrocentos e dezessete")
    elif numero == 418:
        print("quatrocentos e dezoito")
    elif numero == 419:
        print("quatrocentos e dezenove")
    elif numero == 420:
        print("quatrocentos e vinte")
    elif numero == 421:
        print("quatrocentos e vinte e um")
    elif numero == 422:
        print("quatrocentos e vinte e dois")
    elif numero == 423:
        print("quatrocentos e vinte e três")
    elif numero == 424:
        print("quatrocentos e vinte e quatro")
    elif numero == 425:
        print("quatrocentos e vinte e cinco")
    elif numero == 426:
        print("quatrocentos e vinte e seis")
    elif numero == 427:
        print("quatrocentos e vinte e sete")
    elif numero == 428:
        print("quatrocentos e vinte e oito")
    elif numero == 429:
        print("quatrocentos e vinte e nove")
    elif numero == 430:
        print("quatrocentos e trinta")
    elif numero == 431:
        print("quatrocentos e trinta e um")
    elif numero == 432:
        print("quatrocentos e trinta e dois")
    elif numero == 433:
        print("quatrocentos e trinta e três")
    elif numero == 434:
        print("quatrocentos e trinta e quatro")
    elif numero == 435:
        print("quatrocentos e trinta e cinco")
    elif numero == 436:
        print("quatrocentos e trinta e seis")
    elif numero == 437:
        print("quatrocentos e trinta e sete")
    elif numero == 438:
        print("quatrocentos e trinta e oito")
    elif numero == 439:
        print("quatrocentos e trinta e nove")
    elif numero == 440:
        print("quatrocentos e quarenta")
    elif numero == 441:
        print("quatrocentos e quarenta e um")
    elif numero == 442:
        print("quatrocentos e quarenta e dois")
    elif numero == 443:
        print("quatrocentos e quarenta e três")
    elif numero == 444:
        print("quatrocentos e quarenta e quatro")
    elif numero == 445:
        print("quatrocentos e quarenta e cinco")
    elif numero == 446:
        print("quatrocentos e quarenta e seis")
    elif numero == 447:
        print("quatrocentos e quarenta e sete")
    elif numero == 448:
        print("quatrocentos e quarenta e oito")
    elif numero == 449:
        print("quatrocentos e quarenta e nove")
    elif numero == 450:
        print("quatrocentos e cinquenta")
    elif numero == 451:
        print("quatrocentos e cinquenta e um")
    elif numero == 452:
        print("quatrocentos e cinquenta e dois")
    elif numero == 453:
        print("quatrocentos e cinquenta e três")
    elif numero == 454:
        print("quatrocentos e cinquenta e quatro")
    elif numero == 455:
        print("quatrocentos e cinquenta e cinco")
    elif numero == 456:
        print("quatrocentos e cinquenta e seis")
    elif numero == 457:
        print("quatrocentos e cinquenta e sete")
    elif numero == 458:
        print("quatrocentos e cinquenta e oito")
    elif numero == 459:
        print("quatrocentos e cinquenta e nove")
    elif numero == 460:
        print("quatrocentos e sessenta")
    elif numero == 461:
        print("quatrocentos e sessenta e um")
    elif numero == 462:
        print("quatrocentos e sessenta e dois")
    elif numero == 463:
        print("quatrocentos e sessenta e três")
    elif numero == 464:
        print("quatrocentos e sessenta e quatro")
    elif numero == 465:
        print("quatrocentos e sessenta e cinco")
    elif numero == 466:
        print("quatrocentos e sessenta e seis")
    elif numero == 467:
        print("quatrocentos e sessenta e sete")
    elif numero == 468:
        print("quatrocentos e sessenta e oito")
    elif numero == 469:
        print("quatrocentos e sessenta e nove")
    elif numero == 470:
        print("quatrocentos e setenta")
    elif numero == 471:
        print("quatrocentos e setenta e um")
    elif numero == 472:
        print("quatrocentos e setenta e dois")
    elif numero == 473:
        print("quatrocentos e setenta e três")
    elif numero == 474:
        print("quatrocentos e setenta e quatro")
    elif numero == 475:
        print("quatrocentos e setenta e cinco")
    elif numero == 476:
        print("quatrocentos e setenta e seis")
    elif numero == 477:
        print("quatrocentos e setenta e sete")
    elif numero == 478:
        print("quatrocentos e setenta e oito")
    elif numero == 479:
        print("quatrocentos e setenta e nove")
    elif numero == 480:
        print("quatrocentos e oitenta")
    elif numero == 481:
        print("quatrocentos e oitenta e um")
    elif numero == 482:
        print("quatrocentos e oitenta e dois")
    elif numero == 483:
        print("quatrocentos e oitenta e três")
    elif numero == 484:
        print("quatrocentos e oitenta e quatro")
    elif numero == 485:
        print("quatrocentos e oitenta e cinco")
    elif numero == 486:
        print("quatrocentos e oitenta e seis")
    elif numero == 487:
        print("quatrocentos e oitenta e sete")
    elif numero == 488:
        print("quatrocentos e oitenta e oito")
    elif numero == 489:
        print("quatrocentos e oitenta e nove")
    elif numero == 490:
        print("quatrocentos e noventa")
    elif numero == 491:
        print("quatrocentos e noventa e um")
    elif numero == 492:
        print("quatrocentos e noventa e dois")
    elif numero == 493:
        print("quatrocentos e noventa e três")
    elif numero == 494:
        print("quatrocentos e noventa e quatro")
    elif numero == 495:
        print("quatrocentos e noventa e cinco")
    elif numero == 496:
        print("quatrocentos e noventa e seis")
    elif numero == 497:
        print("quatrocentos e noventa e sete")
    elif numero == 498:
        print("quatrocentos e noventa e oito")
    elif numero == 499:
        print("quatrocentos e noventa e nove")
    elif numero == 500:
        print("quinhentos")
    elif numero == 501:
        print("quinhentos e um")
    elif numero == 502:
        print("quinhentos e dois")
    elif numero == 503:
        print("quinhentos e três")
    elif numero == 504:
        print("quinhentos e quatro")
    elif numero == 505:
        print("quinhentos e cinco")
    elif numero == 506:
        print("quinhentos e seis")
    elif numero == 507:
        print("quinhentos e sete")
    elif numero == 508:
        print("quinhentos e oito")
    elif numero == 509:
        print("quinhentos e nove")
    elif numero == 510:
        print("quinhentos e dez")
    elif numero == 511:
        print("quinhentos e onze")
    elif numero == 512:
        print("quinhentos e doze")
    elif numero == 513:
        print("quinhentos e treze")
    elif numero == 514:
        print("quinhentos e quatorze")
    elif numero == 515:
        print("quinhentos e quinze")
    elif numero == 516:
        print("quinhentos e dezesseis")
    elif numero == 517:
        print("quinhentos e dezessete")
    elif numero == 518:
        print("quinhentos e dezoito")
    elif numero == 519:
        print("quinhentos e dezenove")
    elif numero == 520:
        print("quinhentos e vinte")
    elif numero == 521:
        print("quinhentos e vinte e um")
    elif numero == 522:
        print("quinhentos e vinte e dois")
    elif numero == 523:
        print("quinhentos e vinte e três")
    elif numero == 524:
        print("quinhentos e vinte e quatro")
    elif numero == 525:
        print("quinhentos e vinte e cinco")
    elif numero == 526:
        print("quinhentos e vinte e seis")
    elif numero == 527:
        print("quinhentos e vinte e sete")
    elif numero == 528:
        print("quinhentos e vinte e oito")
    elif numero == 529:
        print("quinhentos e vinte e nove")
    elif numero == 530:
        print("quinhentos e trinta")
    elif numero == 531:
        print("quinhentos e trinta e um")
    elif numero == 532:
        print("quinhentos e trinta e dois")
    elif numero == 533:
        print("quinhentos e trinta e três")
    elif numero == 534:
        print("quinhentos e trinta e quatro")
    elif numero == 535:
        print("quinhentos e trinta e cinco")
    elif numero == 536:
        print("quinhentos e trinta e seis")
    elif numero == 537:
        print("quinhentos e trinta e sete")
    elif numero == 538:
        print("quinhentos e trinta e oito")
    elif numero == 539:
        print("quinhentos e trinta e nove")
    elif numero == 540:
        print("quinhentos e quarenta")
    elif numero == 541:
        print("quinhentos e quarenta e um")
    elif numero == 542:
        print("quinhentos e quarenta e dois")
    elif numero == 543:
        print("quinhentos e quarenta e três")
    elif numero == 544:
        print("quinhentos e quarenta e quatro")
    elif numero == 545:
        print("quinhentos e quarenta e cinco")
    elif numero == 546:
        print("quinhentos e quarenta e seis")
    elif numero == 547:
        print("quinhentos e quarenta e sete")
    elif numero == 548:
        print("quinhentos e quarenta e oito")
    elif numero == 549:
        print("quinhentos e quarenta e nove")
    elif numero == 550:
        print("quinhentos e cinquenta")
    elif numero == 551:
        print("quinhentos e cinquenta e um")
    elif numero == 552:
        print("quinhentos e cinquenta e dois")
    elif numero == 553:
        print("quinhentos e cinquenta e três")
    elif numero == 554:
        print("quinhentos e cinquenta e quatro")
    elif numero == 555:
        print("quinhentos e cinquenta e cinco")
    elif numero == 556:
        print("quinhentos e cinquenta e seis")
    elif numero == 557:
        print("quinhentos e cinquenta e sete")
    elif numero == 558:
        print("quinhentos e cinquenta e oito")
    elif numero == 559:
        print("quinhentos e cinquenta e nove")
    elif numero == 560:
        print("quinhentos e sessenta")
    elif numero == 561:
        print("quinhentos e sessenta e um")
    elif numero == 562:
        print("quinhentos e sessenta e dois")
    elif numero == 563:
        print("quinhentos e sessenta e três")
    elif numero == 564:
        print("quinhentos e sessenta e quatro")
    elif numero == 565:
        print("quinhentos e sessenta e cinco")
    elif numero == 566:
        print("quinhentos e sessenta e seis")
    elif numero == 567:
        print("quinhentos e sessenta e sete")
    elif numero == 568:
        print("quinhentos e sessenta e oito")
    elif numero == 569:
        print("quinhentos e sessenta e nove")
    elif numero == 570:
        print("quinhentos e setenta")
    elif numero == 571:
        print("quinhentos e setenta e um")
    elif numero == 572:
        print("quinhentos e setenta e dois")
    elif numero == 573:
        print("quinhentos e setenta e três")
    elif numero == 574:
        print("quinhentos e setenta e quatro")
    elif numero == 575:
        print("quinhentos e setenta e cinco")
    elif numero == 576:
        print("quinhentos e setenta e seis")
    elif numero == 577:
        print("quinhentos e setenta e sete")
    elif numero == 578:
        print("quinhentos e setenta e oito")
    elif numero == 579:
        print("quinhentos e setenta e nove")
    elif numero == 580:
        print("quinhentos e oitenta")
    elif numero == 581:
        print("quinhentos e oitenta e um")
    elif numero == 582:
        print("quinhentos e oitenta e dois")
    elif numero == 583:
        print("quinhentos e oitenta e três")
    elif numero == 584:
        print("quinhentos e oitenta e quatro")
    elif numero == 585:
        print("quinhentos e oitenta e cinco")
    elif numero == 586:
        print("quinhentos e oitenta e seis")
    elif numero == 587:
        print("quinhentos e oitenta e sete")
    elif numero == 588:
        print("quinhentos e oitenta e oito")
    elif numero == 589:
        print("quinhentos e oitenta e nove")
    elif numero == 590:
        print("quinhentos e noventa")
    elif numero == 591:
        print("quinhentos e noventa e um")
    elif numero == 592:
        print("quinhentos e noventa e dois")
    elif numero == 593:
        print("quinhentos e noventa e três")
    elif numero == 594:
        print("quinhentos e noventa e quatro")
    elif numero == 595:
        print("quinhentos e noventa e cinco")
    elif numero == 596:
        print("quinhentos e noventa e seis")
    elif numero == 597:
        print("quinhentos e noventa e sete")
    elif numero == 598:
        print("quinhentos e noventa e oito")
    elif numero == 599:
        print("quinhentos e noventa e nove")
    elif numero == 600:
        print("seiscentos")
    elif numero == 601:
        print("seiscentos e um")
    elif numero == 602:
        print("seiscentos e dois")
    elif numero == 603:
        print("seiscentos e três")
    elif numero == 604:
        print("seiscentos e quatro")
    elif numero == 605:
        print("seiscentos e cinco")
    elif numero == 606:
        print("seiscentos e seis")
    elif numero == 607:
        print("seiscentos e sete")
    elif numero == 608:
        print("seiscentos e oito")
    elif numero == 609:
        print("seiscentos e nove")
    elif numero == 610:
        print("seiscentos e dez")
    elif numero == 611:
        print("seiscentos e onze")
    elif numero == 612:
        print("seiscentos e doze")
    elif numero == 613:
        print("seiscentos e treze")
    elif numero == 614:
        print("seiscentos e quatorze")
    elif numero == 615:
        print("seiscentos e quinze")
    elif numero == 616:
        print("seiscentos e dezesseis")
    elif numero == 617:
        print("seiscentos e dezessete")
    elif numero == 618:
        print("seiscentos e dezoito")
    elif numero == 619:
        print("seiscentos e dezenove")
    elif numero == 620:
        print("seiscentos e vinte")
    elif numero == 621:
        print("seiscentos e vinte e um")
    elif numero == 622:
        print("seiscentos e vinte e dois")
    elif numero == 623:
        print("seiscentos e vinte e três")
    elif numero == 624:
        print("seiscentos e vinte e quatro")
    elif numero == 625:
        print("seiscentos e vinte e cinco")
    elif numero == 626:
        print("seiscentos e vinte e seis")
    elif numero == 627:
        print("seiscentos e vinte e sete")
    elif numero == 628:
        print("seiscentos e vinte e oito")
    elif numero == 629:
        print("seiscentos e vinte e nove")
    elif numero == 630:
        print("seiscentos e trinta")
    elif numero == 631:
        print("seiscentos e trinta e um")
    elif numero == 632:
        print("seiscentos e trinta e dois")
    elif numero == 633:
        print("seiscentos e trinta e três")
    elif numero == 634:
        print("seiscentos e trinta e quatro")
    elif numero == 635:
        print("seiscentos e trinta e cinco")
    elif numero == 636:
        print("seiscentos e trinta e seis")
    elif numero == 637:
        print("seiscentos e trinta e sete")
    elif numero == 638:
        print("seiscentos e trinta e oito")
    elif numero == 639:
        print("seiscentos e trinta e nove")
    elif numero == 640:
        print("seiscentos e quarenta")
    elif numero == 641:
        print("seiscentos e quarenta e um")
    elif numero == 642:
        print("seiscentos e quarenta e dois")
    elif numero == 643:
        print("seiscentos e quarenta e três")
    elif numero == 644:
        print("seiscentos e quarenta e quatro")
    elif numero == 645:
        print("seiscentos e quarenta e cinco")
    elif numero == 646:
        print("seiscentos e quarenta e seis")
    elif numero == 647:
        print("seiscentos e quarenta e sete")
    elif numero == 648:
        print("seiscentos e quarenta e oito")
    elif numero == 649:
        print("seiscentos e quarenta e nove")
    elif numero == 650:
        print("seiscentos e cinquenta")
    elif numero == 651:
        print("seiscentos e cinquenta e um")
    elif numero == 652:
        print("seiscentos e cinquenta e dois")
    elif numero == 653:
        print("seiscentos e cinquenta e três")
    elif numero == 654:
        print("seiscentos e cinquenta e quatro")
    elif numero == 655:
        print("seiscentos e cinquenta e cinco")
    elif numero == 656:
        print("seiscentos e cinquenta e seis")
    elif numero == 657:
        print("seiscentos e cinquenta e sete")
    elif numero == 658:
        print("seiscentos e cinquenta e oito")
    elif numero == 659:
        print("seiscentos e cinquenta e nove")
    elif numero == 660:
        print("seiscentos e sessenta")
    elif numero == 661:
        print("seiscentos e sessenta e um")
    elif numero == 662:
        print("seiscentos e sessenta e dois")
    elif numero == 663:
        print("seiscentos e sessenta e três")
    elif numero == 664:
        print("seiscentos e sessenta e quatro")
    elif numero == 665:
        print("seiscentos e sessenta e cinco")
    elif numero == 666:
        print("seiscentos e sessenta e seis")
    elif numero == 667:
        print("seiscentos e sessenta e sete")
    elif numero == 668:
        print("seiscentos e sessenta e oito")
    elif numero == 669:
        print("seiscentos e sessenta e nove")
    elif numero == 670:
        print("seiscentos e setenta")
    elif numero == 671:
        print("seiscentos e setenta e um")
    elif numero == 672:
        print("seiscentos e setenta e dois")
    elif numero == 673:
        print("seiscentos e setenta e três")
    elif numero == 674:
        print("seiscentos e setenta e quatro")
    elif numero == 675:
        print("seiscentos e setenta e cinco")
    elif numero == 676:
        print("seiscentos e setenta e seis")
    elif numero == 677:
        print("seiscentos e setenta e sete")
    elif numero == 678:
        print("seiscentos e setenta e oito")
    elif numero == 679:
        print("seiscentos e setenta e nove")
    elif numero == 680:
        print("seiscentos e oitenta")
    elif numero == 681:
        print("seiscentos e oitenta e um")
    elif numero == 682:
        print("seiscentos e oitenta e dois")
    elif numero == 683:
        print("seiscentos e oitenta e três")
    elif numero == 684:
        print("seiscentos e oitenta e quatro")
    elif numero == 685:
        print("seiscentos e oitenta e cinco")
    elif numero == 686:
        print("seiscentos e oitenta e seis")
    elif numero == 687:
        print("seiscentos e oitenta e sete")
    elif numero == 688:
        print("seiscentos e oitenta e oito")
    elif numero == 689:
        print("seiscentos e oitenta e nove")
    elif numero == 690:
        print("seiscentos e noventa")
    elif numero == 691:
        print("seiscentos e noventa e um")
    elif numero == 692:
        print("seiscentos e noventa e dois")
    elif numero == 693:
        print("seiscentos e noventa e três")
    elif numero == 694:
        print("seiscentos e noventa e quatro")
    elif numero == 695:
        print("seiscentos e noventa e cinco")
    elif numero == 696:
        print("seiscentos e noventa e seis")
    elif numero == 697:
        print("seiscentos e noventa e sete")
    elif numero == 698:
        print("seiscentos e noventa e oito")
    elif numero == 699:
        print("seiscentos e noventa e nove")
    elif numero == 700:
        print("setecentos")
    elif numero == 701:
        print("setecentos e um")
    elif numero == 702:
        print("setecentos e dois")
    elif numero == 703:
        print("setecentos e três")
    elif numero == 704:
        print("setecentos e quatro")
    elif numero == 705:
        print("setecentos e cinco")
    elif numero == 706:
        print("setecentos e seis")
    elif numero == 707:
        print("setecentos e sete")
    elif numero == 708:
        print("setecentos e oito")
    elif numero == 709:
        print("setecentos e nove")
    elif numero == 710:
        print("setecentos e dez")
    elif numero == 711:
        print("setecentos e onze")
    elif numero == 712:
        print("setecentos e doze")
    elif numero == 713:
        print("setecentos e treze")
    elif numero == 714:
        print("setecentos e quatorze")
    elif numero == 715:
        print("setecentos e quinze")
    elif numero == 716:
        print("setecentos e dezesseis")
    elif numero == 717:
        print("setecentos e dezessete")
    elif numero == 718:
        print("setecentos e dezoito")
    elif numero == 719:
        print("setecentos e dezenove")
    elif numero == 720:
        print("setecentos e vinte")
    elif numero == 721:
        print("setecentos e vinte e um")
    elif numero == 722:
        print("setecentos e vinte e dois")
    elif numero == 723:
        print("setecentos e vinte e três")
    elif numero == 724:
        print("setecentos e vinte e quatro")
    elif numero == 725:
        print("setecentos e vinte e cinco")
    elif numero == 726:
        print("setecentos e vinte e seis")
    elif numero == 727:
        print("setecentos e vinte e sete")
    elif numero == 728:
        print("setecentos e vinte e oito")
    elif numero == 729:
        print("setecentos e vinte e nove")
    elif numero == 730:
        print("setecentos e trinta")
    elif numero == 731:
        print("setecentos e trinta e um")
    elif numero == 732:
        print("setecentos e trinta e dois")
    elif numero == 733:
        print("setecentos e trinta e três")
    elif numero == 734:
        print("setecentos e trinta e quatro")
    elif numero == 735:
        print("setecentos e trinta e cinco")
    elif numero == 736:
        print("setecentos e trinta e seis")
    elif numero == 737:
        print("setecentos e trinta e sete")
    elif numero == 738:
        print("setecentos e trinta e oito")
    elif numero == 739:
        print("setecentos e trinta e nove")
    elif numero == 740:
        print("setecentos e quarenta")
    elif numero == 741:
        print("setecentos e quarenta e um")
    elif numero == 742:
        print("setecentos e quarenta e dois")
    elif numero == 743:
        print("setecentos e quarenta e três")
    elif numero == 744:
        print("setecentos e quarenta e quatro")
    elif numero == 745:
        print("setecentos e quarenta e cinco")
    elif numero == 746:
        print("setecentos e quarenta e seis")
    elif numero == 747:
        print("setecentos e quarenta e sete")
    elif numero == 748:
        print("setecentos e quarenta e oito")
    elif numero == 749:
        print("setecentos e quarenta e nove")
    elif numero == 750:
        print("setecentos e cinquenta")
    elif numero == 751:
        print("setecentos e cinquenta e um")
    elif numero == 752:
        print("setecentos e cinquenta e dois")
    elif numero == 753:
        print("setecentos e cinquenta e três")
    elif numero == 754:
        print("setecentos e cinquenta e quatro")
    elif numero == 755:
        print("setecentos e cinquenta e cinco")
    elif numero == 756:
        print("setecentos e cinquenta e seis")
    elif numero == 757:
        print("setecentos e cinquenta e sete")
    elif numero == 758:
        print("setecentos e cinquenta e oito")
    elif numero == 759:
        print("setecentos e cinquenta e nove")
    elif numero == 760:
        print("setecentos e sessenta")
    elif numero == 761:
        print("setecentos e sessenta e um")
    elif numero == 762:
        print("setecentos e sessenta e dois")
    elif numero == 763:
        print("setecentos e sessenta e três")
    elif numero == 764:
        print("setecentos e sessenta e quatro")
    elif numero == 765:
        print("setecentos e sessenta e cinco")
    elif numero == 766:
        print("setecentos e sessenta e seis")
    elif numero == 767:
        print("setecentos e sessenta e sete")
    elif numero == 768:
        print("setecentos e sessenta e oito")
    elif numero == 769:
        print("setecentos e sessenta e nove")
    elif numero == 770:
        print("setecentos e setenta")
    elif numero == 771:
        print("setecentos e setenta e um")
    elif numero == 772:
        print("setecentos e setenta e dois")
    elif numero == 773:
        print("setecentos e setenta e três")
    elif numero == 774:
        print("setecentos e setenta e quatro")
    elif numero == 775:
        print("setecentos e setenta e cinco")
    elif numero == 776:
        print("setecentos e setenta e seis")
    elif numero == 777:
        print("setecentos e setenta e sete")
    elif numero == 778:
        print("setecentos e setenta e oito")
    elif numero == 779:
        print("setecentos e setenta e nove")
    elif numero == 780:
        print("setecentos e oitenta")
    elif numero == 781:
        print("setecentos e oitenta e um")
    elif numero == 782:
        print("setecentos e oitenta e dois")
    elif numero == 783:
        print("setecentos e oitenta e três")
    elif numero == 784:
        print("setecentos e oitenta e quatro")
    elif numero == 785:
        print("setecentos e oitenta e cinco")
    elif numero == 786:
        print("setecentos e oitenta e seis")
    elif numero == 787:
        print("setecentos e oitenta e sete")
    elif numero == 788:
        print("setecentos e oitenta e oito")
    elif numero == 789:
        print("setecentos e oitenta e nove")
    elif numero == 790:
        print("setecentos e noventa")
    elif numero == 791:
        print("setecentos e noventa e um")
    elif numero == 792:
        print("setecentos e noventa e dois")
    elif numero == 793:
        print("setecentos e noventa e três")
    elif numero == 794:
        print("setecentos e noventa e quatro")
    elif numero == 795:
        print("setecentos e noventa e cinco")
    elif numero == 796:
        print("setecentos e noventa e seis")
    elif numero == 797:
        print("setecentos e noventa e sete")
    elif numero == 798:
        print("setecentos e noventa e oito")
    elif numero == 799:
        print("setecentos e noventa e nove")
    elif numero == 800:
        print("oitocentos")
    elif numero == 801:
        print("oitocentos e um")
    elif numero == 802:
        print("oitocentos e dois")
    elif numero == 803:
        print("oitocentos e três")
    elif numero == 804:
        print("oitocentos e quatro")
    elif numero == 805:
        print("oitocentos e cinco")
    elif numero == 806:
        print("oitocentos e seis")
    elif numero == 807:
        print("oitocentos e sete")
    elif numero == 808:
        print("oitocentos e oito")
    elif numero == 809:
        print("oitocentos e nove")
    elif numero == 810:
        print("oitocentos e dez")
    elif numero == 811:
        print("oitocentos e onze")
    elif numero == 812:
        print("oitocentos e doze")
    elif numero == 813:
        print("oitocentos e treze")
    elif numero == 814:
        print("oitocentos e quatorze")
    elif numero == 815:
        print("oitocentos e quinze")
    elif numero == 816:
        print("oitocentos e dezesseis")
    elif numero == 817:
        print("oitocentos e dezessete")
    elif numero == 818:
        print("oitocentos e dezoito")
    elif numero == 819:
        print("oitocentos e dezenove")
    elif numero == 820:
        print("oitocentos e vinte")
    elif numero == 821:
        print("oitocentos e vinte e um")
    elif numero == 822:
        print("oitocentos e vinte e dois")
    elif numero == 823:
        print("oitocentos e vinte e três")
    elif numero == 824:
        print("oitocentos e vinte e quatro")
    elif numero == 825:
        print("oitocentos e vinte e cinco")
    elif numero == 826:
        print("oitocentos e vinte e seis")
    elif numero == 827:
        print("oitocentos e vinte e sete")
    elif numero == 828:
        print("oitocentos e vinte e oito")
    elif numero == 829:
        print("oitocentos e vinte e nove")
    elif numero == 830:
        print("oitocentos e trinta")
    elif numero == 831:
        print("oitocentos e trinta e um")
    elif numero == 832:
        print("oitocentos e trinta e dois")
    elif numero == 833:
        print("oitocentos e trinta e três")
    elif numero == 834:
        print("oitocentos e trinta e quatro")
    elif numero == 835:
        print("oitocentos e trinta e cinco")
    elif numero == 836:
        print("oitocentos e trinta e seis")
    elif numero == 837:
        print("oitocentos e trinta e sete")
    elif numero == 838:
        print("oitocentos e trinta e oito")
    elif numero == 839:
        print("oitocentos e trinta e nove")
    elif numero == 840:
        print("oitocentos e quarenta")
    elif numero == 841:
        print("oitocentos e quarenta e um")
    elif numero == 842:
        print("oitocentos e quarenta e dois")
    elif numero == 843:
        print("oitocentos e quarenta e três")
    elif numero == 844:
        print("oitocentos e quarenta e quatro")
    elif numero == 845:
        print("oitocentos e quarenta e cinco")
    elif numero == 846:
        print("oitocentos e quarenta e seis")
    elif numero == 847:
        print("oitocentos e quarenta e sete")
    elif numero == 848:
        print("oitocentos e quarenta e oito")
    elif numero == 849:
        print("oitocentos e quarenta e nove")
    elif numero == 850:
        print("oitocentos e cinquenta")
    elif numero == 851:
        print("oitocentos e cinquenta e um")
    elif numero == 852:
        print("oitocentos e cinquenta e dois")
    elif numero == 853:
        print("oitocentos e cinquenta e três")
    elif numero == 854:
        print("oitocentos e cinquenta e quatro")
    elif numero == 855:
        print("oitocentos e cinquenta e cinco")
    elif numero == 856:
        print("oitocentos e cinquenta e seis")
    elif numero == 857:
        print("oitocentos e cinquenta e sete")
    elif numero == 858:
        print("oitocentos e cinquenta e oito")
    elif numero == 859:
        print("oitocentos e cinquenta e nove")
    elif numero == 860:
        print("oitocentos e sessenta")
    elif numero == 861:
        print("oitocentos e sessenta e um")
    elif numero == 862:
        print("oitocentos e sessenta e dois")
    elif numero == 863:
        print("oitocentos e sessenta e três")
    elif numero == 864:
        print("oitocentos e sessenta e quatro")
    elif numero == 865:
        print("oitocentos e sessenta e cinco")
    elif numero == 866:
        print("oitocentos e sessenta e seis")
    elif numero == 867:
        print("oitocentos e sessenta e sete")
    elif numero == 868:
        print("oitocentos e sessenta e oito")
    elif numero == 869:
        print("oitocentos e sessenta e nove")
    elif numero == 870:
        print("oitocentos e setenta")
    elif numero == 871:
        print("oitocentos e setenta e um")
    elif numero == 872:
        print("oitocentos e setenta e dois")
    elif numero == 873:
        print("oitocentos e setenta e três")
    elif numero == 874:
        print("oitocentos e setenta e quatro")
    elif numero == 875:
        print("oitocentos e setenta e cinco")
    elif numero == 876:
        print("oitocentos e setenta e seis")
    elif numero == 877:
        print("oitocentos e setenta e sete")
    elif numero == 878:
        print("oitocentos e setenta e oito")
    elif numero == 879:
        print("oitocentos e setenta e nove")
    elif numero == 880:
        print("oitocentos e oitenta")
    elif numero == 881:
        print("oitocentos e oitenta e um")
    elif numero == 882:
        print("oitocentos e oitenta e dois")
    elif numero == 883:
        print("oitocentos e oitenta e três")
    elif numero == 884:
        print("oitocentos e oitenta e quatro")
    elif numero == 885:
        print("oitocentos e oitenta e cinco")
    elif numero == 886:
        print("oitocentos e oitenta e seis")
    elif numero == 887:
        print("oitocentos e oitenta e sete")
    elif numero == 888:
        print("oitocentos e oitenta e oito")
    elif numero == 889:
        print("oitocentos e oitenta e nove")
    elif numero == 890:
        print("oitocentos e noventa")
    elif numero == 891:
        print("oitocentos e noventa e um")
    elif numero == 892:
        print("oitocentos e noventa e dois")
    elif numero == 893:
        print("oitocentos e noventa e três")
    elif numero == 894:
        print("oitocentos e noventa e quatro")
    elif numero == 895:
        print("oitocentos e noventa e cinco")
    elif numero == 896:
        print("oitocentos e noventa e seis")
    elif numero == 897:
        print("oitocentos e noventa e sete")
    elif numero == 898:
        print("oitocentos e noventa e oito")
    elif numero == 899:
        print("oitocentos e noventa e nove")
    elif numero == 900:
        print("novecentos")
    elif numero == 901:
        print("novecentos e um")
    elif numero == 902:
        print("novecentos e dois")
    elif numero == 903:
        print("novecentos e três")
    elif numero == 904:
        print("novecentos e quatro")
    elif numero == 905:
        print("novecentos e cinco")
    elif numero == 906:
        print("novecentos e seis")
    elif numero == 907:
        print("novecentos e sete")
    elif numero == 908:
        print("novecentos e oito")
    elif numero == 909:
        print("novecentos e nove")
    elif numero == 910:
        print("novecentos e dez")
    elif numero == 911:
        print("novecentos e onze")
    elif numero == 912:
        print("novecentos e doze")
    elif numero == 913:
        print("novecentos e treze")
    elif numero == 914:
        print("novecentos e quatorze")
    elif numero == 915:
        print("novecentos e quinze")
    elif numero == 916:
        print("novecentos e dezesseis")
    elif numero == 917:
        print("novecentos e dezessete")
    elif numero == 918:
        print("novecentos e dezoito")
    elif numero == 919:
        print("novecentos e dezenove")
    elif numero == 920:
        print("novecentos e vinte")
    elif numero == 921:
        print("novecentos e vinte e um")
    elif numero == 922:
        print("novecentos e vinte e dois")
    elif numero == 923:
        print("novecentos e vinte e três")
    elif numero == 924:
        print("novecentos e vinte e quatro")
    elif numero == 925:
        print("novecentos e vinte e cinco")
    elif numero == 926:
        print("novecentos e vinte e seis")
    elif numero == 927:
        print("novecentos e vinte e sete")
    elif numero == 928:
        print("novecentos e vinte e oito")
    elif numero == 929:
        print("novecentos e vinte e nove")
    elif numero == 930:
        print("novecentos e trinta")
    elif numero == 931:
        print("novecentos e trinta e um")
    elif numero == 932:
        print("novecentos e trinta e dois")
    elif numero == 933:
        print("novecentos e trinta e três")
    elif numero == 934:
        print("novecentos e trinta e quatro")
    elif numero == 935:
        print("novecentos e trinta e cinco")
    elif numero == 936:
        print("novecentos e trinta e seis")
    elif numero == 937:
        print("novecentos e trinta e sete")
    elif numero == 938:
        print("novecentos e trinta e oito")
    elif numero == 939:
        print("novecentos e trinta e nove")
    elif numero == 940:
        print("novecentos e quarenta")
    elif numero == 941:
        print("novecentos e quarenta e um")
    elif numero == 942:
        print("novecentos e quarenta e dois")
    elif numero == 943:
        print("novecentos e quarenta e três")
    elif numero == 944:
        print("novecentos e quarenta e quatro")
    elif numero == 945:
        print("novecentos e quarenta e cinco")
    elif numero == 946:
        print("novecentos e quarenta e seis")
    elif numero == 947:
        print("novecentos e quarenta e sete")
    elif numero == 948:
        print("novecentos e quarenta e oito")
    elif numero == 949:
        print("novecentos e quarenta e nove")
    elif numero == 950:
        print("novecentos e cinquenta")
    elif numero == 951:
        print("novecentos e cinquenta e um")
    elif numero == 952:
        print("novecentos e cinquenta e dois")
    elif numero == 953:
        print("novecentos e cinquenta e três")
    elif numero == 954:
        print("novecentos e cinquenta e quatro")
    elif numero == 955:
        print("novecentos e cinquenta e cinco")
    elif numero == 956:
        print("novecentos e cinquenta e seis")
    elif numero == 957:
        print("novecentos e cinquenta e sete")
    elif numero == 958:
        print("novecentos e cinquenta e oito")
    elif numero == 959:
        print("novecentos e cinquenta e nove")
    elif numero == 960:
        print("novecentos e sessenta")
    elif numero == 961:
        print("novecentos e sessenta e um")
    elif numero == 962:
        print("novecentos e sessenta e dois")
    elif numero == 963:
        print("novecentos e sessenta e três")
    elif numero == 964:
        print("novecentos e sessenta e quatro")
    elif numero == 965:
        print("novecentos e sessenta e cinco")
    elif numero == 966:
        print("novecentos e sessenta e seis")
    elif numero == 967:
        print("novecentos e sessenta e sete")
    elif numero == 968:
        print("novecentos e sessenta e oito")
    elif numero == 969:
        print("novecentos e sessenta e nove")
    elif numero == 970:
        print("novecentos e setenta")
    elif numero == 971:
        print("novecentos e setenta e um")
    elif numero == 972:
        print("novecentos e setenta e dois")
    elif numero == 973:
        print("novecentos e setenta e três")
    elif numero == 974:
        print("novecentos e setenta e quatro")
    elif numero == 975:
        print("novecentos e setenta e cinco")
    elif numero == 976:
        print("novecentos e setenta e seis")
    elif numero == 977:
        print("novecentos e setenta e sete")
    elif numero == 978:
        print("novecentos e setenta e oito")
    elif numero == 979:
        print("novecentos e setenta e nove")
    elif numero == 980:
        print("novecentos e oitenta")
    elif numero == 981:
        print("novecentos e oitenta e um")
    elif numero == 982:
        print("novecentos e oitenta e dois")
    elif numero == 983:
        print("novecentos e oitenta e três")
    elif numero == 984:
        print("novecentos e oitenta e quatro")
    elif numero == 985:
        print("novecentos e oitenta e cinco")
    elif numero == 986:
        print("novecentos e oitenta e seis")
    elif numero == 987:
        print("novecentos e oitenta e sete")
    elif numero == 988:
        print("novecentos e oitenta e oito")
    elif numero == 989:
        print("novecentos e oitenta e nove")
    elif numero == 990:
        print("novecentos e noventa")
    elif numero == 991:
        print("novecentos e noventa e um")
    elif numero == 992:
        print("novecentos e noventa e dois")
    elif numero == 993:
        print("novecentos e noventa e três")
    elif numero == 994:
        print("novecentos e noventa e quatro")
    elif numero == 995:
        print("novecentos e noventa e cinco")
    elif numero == 996:
        print("novecentos e noventa e seis")
    elif numero == 997:
        print("novecentos e noventa e sete")
    elif numero == 998:
        print("novecentos e noventa e oito")
    elif numero == 999:
        print("novecentos e noventa e nove")



def nMenos999a999ToExtenso2Func():
    numero = int(input("Digite um número natural entre -999 e 999: "))
    if numero < -999 or numero > 999:
        print("Fora do intervalo permitido.")
    else:
        print(nPorExtenso(numero))

# 47.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -9,99 e R$ 9,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.


# 48.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -99,99 e R$ 99,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.

# 49.
# Faça uma função em Python que solicite a digitação de um valor monetário entre R$ -999,99 e R$ 999,99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.
# Usar as palavras “real”, “reais”, “centavo” e “centavos” de forma apropriada.
# Não escrever “zero reais” e nem “zero centavos”, exceto no caso do saldo ser igual a zero.
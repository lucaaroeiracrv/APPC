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
def ordenar4NumerosEmCrescente():
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
    c = float(input("Digite a temperatura em Celsius: "))
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
    f = float(input("Digite a temperatura em Fahrenheit: "))
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
    c = float(input("Digite a temperatura em Celsius: "))
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
    k = float(input("Digite a temperatura em Kelvin: "))
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
    c = float(input("Digite a temperatura em Celsius: "))
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
    r = float(input("Digite a temperatura em Rankine: "))
    if r < 0:
        print("Temperatura inválida. A menor temperatura possível em Rankine é 0.")
    else:
        c = (r / 1.8) - 491.67
        print(f"{r}°R é igual a {c}°C.")
# 10.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Kelvin.
# Menor temperatura possível em Fahrenheit: -459.67
def fahrenheitToKelvin():
    f = float(input("Digite a temperatura em Fahrenheit: "))
    if f < -459.67:
        print("Temperatura inválida. A menor temperatura possível em Fahrenheit é -459.67.")
    else:
        k = (f - 32) / 1.8 + 273.15  
        print(f"{f}°F é igual a {k}K.")

# 11.
# Faça uma função em Python que converta temperaturas de Kelvin para Fahrenheit.
# Menor temperatura possível em Kelvin: 0
def kelvinToFahrenheit():
    k = float(input("Digite a temperatura em Kelvin: "))
    if k < 0:
        print("Temperatura inválida. A menor temperatura possível em Kelvin é 0.")
    else:
        f = (k - 273.15) * 1.8 + 32 
        print(f"{k}K é igual a {f}°F.")

# 12.
# Faça uma função em Python que converta temperaturas de Fahrenheit para Rankine.
# Menor temperatura possível em Fahrenheit: -459.67
def fahrenheitToRankine():
    f = float(input("Digite a temperatura em Fahrenheit: "))
    if f < -459.67:
        print("Temperatura inválida. A menor temperatura possível em Fahrenheit é -459.67.")
    else:
        r = f + 459.67
        print(f"{f}°F é igual a {r}°R.")

# 13.
# Faça uma função em Python que converta temperaturas de Rankine para Fahrenheit.
# Menor temperatura possível em Rankine: 0
def rankineToFahrenheit():
    r = float(input("Digite a temperatura em Rankine: "))
    if r < 0:
        print("Temperatura inválida. A menor temperatura possível em Rankine é 0.")
    else:
        f = r - 459.67
        print(f"{r}°R é igual a {f}°F.")
# 14.
# Faça uma função em Python que converta temperaturas de Kelvin para Rankine.
# Menor temperatura possível em Kelvin: 0
def kelvinToRankine():
    k = float(input("Digite a temperatura em Kelvin: "))
    if k < 0:
        print("Temperatura inválida. A menor temperatura possível em Kelvin é 0.")
    else:
        r = k * 1.8
        print(f"{k}K é igual a {r}°R.")

# 15.
# Faça uma função em Python que converta temperaturas de Rankine para Kelvin.
# Menor temperatura possível em Rankine: 0
def rankineToKelvin():
    r = float(input("Digite a temperatura em Rankine: "))
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



# Outros exercícios

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

#30.2 
#Faça uma função que resolva uma equação de 2º grau.
#Forma: AX² + BX + C = 0
#Entradas: A, B e C
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
            raiz = -B / (2*A) # x = -b / 2a
            print(f"A equação tem uma raiz real: {raiz}")
        else: #existem duas raizes reais e diferentes
            raiz1 = (-B + delta**0.5) / (2*A) #x1 = (-b + √Δ) / 2a
            raiz2 = (-B - delta**0.5) / (2*A) #x2 = (-b - √Δ) / 2a
            print(f"A equação tem duas raízes reais: {raiz1} e {raiz2}")


# Programas com menu

# 31.
# Faça uma função com menu que reúna os exercícios 4 a 15 (conversões de temperatura).

# 32.
# Faça uma função com menu que reúna os exercícios 16 a 21 (perímetros).

# 33.
# Faça uma função com menu que reúna os exercícios 22 a 28 (áreas).

# Valelifações

# 34.elif Crie uma função que receba horas, minutos e segundos
# e veique se formam um horário válido.
# 35.
# Crie uma função que receba 3 segmentos de reta
# e verifique se podem formar um triângulo.

# 36.
# Se puder formar um triângulo, classifique:
# Equilátero (3 lados iguais)
# Isósceles (2 lados iguais)
# Escaleno (todos diferentes)

# 37.
# Verifique se 3 ângulos podem formar um triângulo.

# 38.
# Classifique o triângulo pelos ângulos:
# Acutângulo (todos < 90°)
# Retângulo (um = 90°)
# Obtusângulo (um > 90°)

# 39.
# Resolva uma equação do 2º grau:
# ax² + bx + c = 0
# Informar:
# nenhuma raiz
# uma raiz
# duas raízes

# 40.
# Crie uma função que verifique se uma data é válida.
# Entradas: dia, mês, ano
# Considerar meses de 30 e 31 dias, fevereiro e anos bissextos.

# 41.
# Receba um número até 9 e escreva por extenso.
# Exemplo: 5 → cinco

# 42.
# Receba um número até 99 e escreva por extenso.
def n99ToExtenso():
    from num2words import num2words #before, you need to install num2words with pip install num2words
    numero = int(input("Digite um número até 99: "))  
    print(num2words(numero, lang='pt_BR'))
    
# 43.
# Receba um número até 999 e escreva por extenso.
def n999ToExtenso():
    from num2words import num2words 
    numero = int(input("Digite um número até 999: "))  
    print(num2words(numero, lang='pt_BR'))
    
# 44.
# Faça uma função em Python que solicite a digitação de um número natural entre -9 e 9,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.

# 45.
# Faça uma função em Python que solicite a digitação de um número natural entre -99 e 99,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.

# 46.
# Faça uma função em Python que solicite a digitação de um número natural entre -999 e 999,
# escrevendo então na tela o valor fornecido por extenso.
# Faça a função de forma inteligente, procurando reduzir a quantidade de comandos print.

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
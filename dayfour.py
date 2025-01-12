nome: str
idade: int
altura: float
peso: float
sexo: str

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
sexo = str(input("Digite F para feminino ou M para masculino: "))

print(f"O(a) senhor(a) {nome} tem {idade} anos de idade, possui uma altura de {altura}, pesando {peso} kg, e essa pessoa é do sexo {sexo}")

nome = input("Informe seu nome: ")
print("Bem-vindo ao PetVida!",nome)

#tipo do pet
tipo = input("Seu pet é um: cachorro\ gato\ ave: ")
print("Ok ele é um(a)",tipo)

#idade_pet
idade_pet = int(input("Diga a idade do seu pet"))
if idade_pet < 2:
    print("filhote")
elif  idade_pet <= 7:
    print("adulto")
else:
    print("idoso")
    
#peso
peso = float(input("Diga a massa do seu pet: "))
if peso >= 40:
    print("Atendimento  especial!")
else: 
    print("Atendimento normal!")

#temperatura
temp = float(input("Informe agora a sua temperatura: "))
if temp >= 39:
    print("febre")
else:
    print("normal")

#hotelzinho
vacina = input("Ele é vacinado: ")
if vacina == "sim" :
    print("Pode usar hotelzinho")
else:
    ("Não pode usar o hotelzinho")

#grupo Risco
if idade_pet > 10 or peso < 2:
    print("Grupo de Risco por peso ou idade")
else:
    print("Atendimento Normal")

#Cadastro Final
print("Ok para que seu pet seja atendido por um de nossos especialistas precisamos do seu número de celular:")
cel = input("Digite aqui: ")

if not cel or nome:
    print("Para dar continuidade ao tratamento precisamos de um cadastro válido, tente novamente!")
 
#planos
print("Selecione o seu plano:")
print("1 -> Básico \n 2-> Premium \n 3-> VIP")
input("Digite o número do plano: ")

if plano == "1":
    print(" \n Plano Básico \n Benefícios: \n 10% de desconto por consulta \n \n Acumulação de pontos para ganhar uma tosa grátis")
elif plano == "2":
    print("\n Plano Premium \n Benefícios: \n 4 tosas disponíveis por mês \n Vacinas inclusas \n Desconto em medicamentos")
elif plano == "3":
    print("\n Plano VIP \n Benefícios: Tudo do Premium \n Consulta 24h com atendimento prioritário \n 2 vezes hotelzinho\mês e pode ser acumulativo! e muito mais")
    
nota = int(input("Nota de Satisfação perante aos nossos Benefícios dos planos: "))
if nota >= 9:
    print("Você disse que é excelente, obrigado!")
elif nota >= 7:
    print("Você disse que é bom,veremos o que podemos fazer para melhorarmos para atingirmos a excelência!")
elif nota >= 5:
    print("Você disse que é regular,obrigada por compartilhar sua opinião!")
else: 
    print("Nota ruim, vamos rever para melhorarmos!")

#cirurgia
cirurgia = str(input("Quer castrar o seu animal: "))
if "sim" :
    if idade_pet >= 1 and peso >= 2:
        print("pode fazer a cirurgia")
if cirurgia == "sim":
    cliente_vip = input("Você é cliente vip")
    
    
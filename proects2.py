print("Passageiros do voo:\n ")
passageiros = ['Ana','Bruno','Carlos','Daniela','Eduardo']

for voo in passageiros:
    
    if voo == 'Carlos':
        print(voo,"perdeu o check-in!")
        continue
    
    print(voo,"realizou o check-in!")

for embarque in passageiros:
    if embarque == "Daniela":
        break 
    if embarque == "Carlos":
        print(embarque,"perdeu o embarque")
        continue
    else: 
        print("Embarque encerrado!")
 
        print(embarque,"pode embarcar")

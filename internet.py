d = int(input("tamanho do arquivo em gigabytes:"))
i = int(input("sua velocidade de internet:"))
resultado = (d/1000)/(i*60)

def bola():
    print(resultado,"minutos")



bola()

distancia = float(input("Digite a quilometagem: "))
gasosa = float(input("Quanto tu gasta em gasosa: "))

kmPerl = distancia / gasosa

if kmPerl <= 8:
    print("Seu carro não aguenta o tranco")

elif kmPerl > 8 and kmPerl <= 14:
    print("Seu carro aguenta o tranco")

else:
    print("Seu carro é uma nave")
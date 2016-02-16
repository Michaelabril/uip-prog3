class Perro:
    Puntos_vida =5
    Puntos_alegria=5

    def __init__(self,Puntos_vida,Puntos_alegria):
        self.Puntos_vida = Puntos_vida
        self.Puntos_alegria = Puntos_alegria

    def caminar (self):

        self.Puntos_vida -= 2
        self.Puntos_alegria += 1

    def correr (self):
        self.Puntos_vida -= 4
        self.Puntos_alegria += 3

    def dormir (self):

        self.Puntos_vida += 1
        self.Puntos_alegria -= 3

    def jugar (self):
        self.Puntos_vida -= 3
        self.Puntos_alegria += 4

    def comer (self):

        self.Puntos_vida += 5
        self.Puntos_alegria += 1

contador=0
lassie = Perro(5,5)
while contador!=10:
    lassie.dormir()
    if lassie.Puntos_vida == 0:
        print ("lassie murio ")
        break
    else:
        contador+=1
    lassie.jugar()
    if lassie.Puntos_vida == 0:
        print ("lassie murio")
        break
    else:
        contador+=1
    lassie.comer()
    if lassie.Puntos_vida == 0:
        print ("lassie murio")
        break
    else:
        contador+=1
    lassie.jugar()
    if lassie.Puntos_vida == 0:
        print ("lassie murio")
        break
    else:
        contador+=1
    lassie.caminar()
    if lassie.Puntos_vida == 0:
        print ("lassie murio")
        break
    else:
        contador+=1
    lassie.dormir()
    if lassie.Puntos_vida == 0:
        print ("lassie murio")
        break
    else:
        contador+=1
    lassie.correr()
    if lassie.Puntos_vida == 0:
        print ("lassie murio...")
        break
    else:
        contador+=1
    lassie.dormir()
    if lassie.Puntos_vida == 0:
        print ("lassie murio")
        break
    else:
        contador+=1
    lassie.dormir()
    if lassie.Puntos_vida == 0:
        print ("lassie murio")
        break
    else:
        contador+=1
    lassie.comer()
    if lassie.Puntos_vida == 0:
        print ("lassie murio")
        break
    else:
        contador+=1


if contador == 10:
    print ("........lassie sobrevivio a sus activides........")


import os

lista_super=[]
tupla = ("arroz", "leche", "tuna", "cereal" , "jugo")

opcion=1
while opcion!='4':
	print('1-agregar\n2-eliminar\n3-ver\n4-salir')
	opcion=input()
	if opcion=='1':
		print ( "solo puedes agregar estos elementos" )
		print (tupla)
		agr=input()
		lista_super.append(agr)
	elif opcion=='2':
		print ("solo puedes eliminar estos elementos:\n" )
		print (lista_super)

		print ("elemento que deseas eliminar: ")
		eli=input()
		try:
			lista_super.remove(str(eli))
		except ValueError:
			print('no esta en la lista')
	elif opcion=='3':
		print(lista_super)
		e=input()
	os.system('CLS')
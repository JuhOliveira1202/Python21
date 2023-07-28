#Exercício 24:
#Dadad a lista de cidades a baixo, substitua uma cidade
#indicada pelo utilizador por Porto.
#Cidades = ["Aveiro", "Braga", "Bragança", "Régua"]

lista_cidades = ['Aveiro', 'Braga', 'Bragança', 'Régua']

c1=input ("Introduza uma cidade a alterar")
i=lista_cidades.index(c1)
lista_cidades[i] = "Porto"
print (lista_cidades)


#Торта  – цената ѝ е 20% от наема на залата
#Напитки – цената им е 45% по-малко от тази на тортата
#Аниматор – цената му е 1/3 от цената за наема на залата
#Вход
#От конзолата се четe 1 ред:
#Наем за залата – цяло число
#Изход
#Да се отпечата на конзолата какъв бюджет ще бъде необходим за организиране на тържеството.
#Примерен вход и изход

#2250 #3697.5
#3720 #6113.2

naem = int(input())
torta= naem * 20 / 100
napitki = torta - (torta * 45 / 100)
animator = naem / 3
suma = naem + napitki + animator + torta
print(suma)




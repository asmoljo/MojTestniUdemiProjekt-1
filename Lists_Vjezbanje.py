my_list = ['A string',23,100.232,'o']
print(my_list)
print(len(my_list))
print(my_list[2])
print(my_list[:2+1])


print(my_list + ['new item']) # ovo ne mijenja listu, nego samo privremeno dodaje element kod ispisa
my_list = my_list + ['ovo se sad dodaje u listu za stalno']
print(my_list)

nova_lista = my_list * 2 # ovo poduplava listu. iza zadnjeg elementa jos jednom doda sve elemente istim redom

print(nova_lista)

a_list = [1,2,3,6,7]

print(a_list)

a_list.append(10)

print(a_list)

a_list.pop(3)

print(a_list)
list_1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
list_asc = []
list_desc = []
list_par = []
list_impar = []
list_m3 = []
l_par = []
l_impar = []
l_m3 = []

print('Lista originala: ', list_1)
list_asc = list(list_1)
list_asc.sort()
print('Lista ascendenta:', list_asc)
list_desc = list(list_asc)
list_desc.reverse()
print('Lista descententa:', list_desc)
list_par = list(list_asc[1::2])
print('Lista pare:', list_par)
list_impar = list(list_asc[0::2])
print('Lista impare:', list_impar)
list_m3 = list(list_asc[2::3])
print('Lista multipli de 3:', list_m3)

for i in list_1:
    if i%2 == 0:
        l_par.append(i)
    if i%2 != 0:
        l_impar.append(i)
    if i%3 == 0:
        l_m3.append(i)

print('Lista % pare: ', l_par)
print('Lista % impare:', l_impar)
print('Lista % multipli de 3:', l_m3)

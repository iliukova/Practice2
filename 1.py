# Дан список списков [[1, 2, 3], [4, 5, 6]]
# Надо сделать 123456

list=[[1, 2, 3], [4, 5, 6]]
string = ''
for el in list[0]:
    string += str(el)
for el in list[1]:
        string += str(el)
print(string)
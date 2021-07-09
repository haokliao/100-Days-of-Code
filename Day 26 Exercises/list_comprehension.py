numbers =[1,2,3]

new_list = []

for i in numbers:
    new = i
    new_list.append(new)

print(new_list)

#listcomprehension saves that entire for loop

newlist = [i + 1 for i in numbers]

print(newlist)

heh = range(1,5)

newrange = [i * 2 for i in heh]
print(newrange)

newlist = [newitem for item in list if test]

names = ['Kev','Sam','Sean','Caro','Ren']

short_names = [name.upper() for name in names if len(name) < 4]
print(short_names)
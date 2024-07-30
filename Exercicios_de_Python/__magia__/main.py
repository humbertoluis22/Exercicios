from pessoa import * 

p = Pessoa()
# print(p.pessoa) # chama o __init__

#print(p)  # chama o __str__

#print(p[2]) # faz uso do __getitem__

# print(len(p.pessoa))   # utileza o __len__

# print(p + ['patricia','carol']) # utileza o __add__

#print(p  * 2 ) #utileza o metodo __mul__ 

# print(p.pessoa[2])
# del p.pessoa[2]   #utiliza o __del__
# print(p.pessoa)

#print(reversed(p))  #utiliza o __reversed__

# p2= ['henrique', 'caio', 'geovanna', 'beatriz', 'fernanda']
# print(p.pessoa == p2)   #utiliza o __eq__

for i in range(len(p.pessoa)):
    print(p[i])
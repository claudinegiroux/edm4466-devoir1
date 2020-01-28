### BONJOUR CLAUDINE, ICI JEAN-HUGUES ROY
### TOUS MES COMMENTAIRES SERONT EN MAJUSCULES ET PRÉCÉDÉS DE 3 # (HASHTAGS)

# encoding:utf-8

l1= list(range(20000,30151))
# print(l1) ### EXCELLENTE PRATIQUE: IMPRIMER LE CONTENU D'UNE VARIABLE EST UNE EXCELLENTE FAÇON DE VOIR CE QUE NOTRE CODE FAIT ET, DONC, S'IL FONCTIONNE
n=0
url="https://montrealcampus.ca?p="
urlfinal=[]
# mc= url.replace("z","l1")
# print(mc)

for num in range(20000,30151):
    n+=1
    print(n,url+str(num))
    urlfinal.append(url+str(num))

print(urlfinal)
print(len(urlfinal))

### SUPER! ÇA MARCHE! BRAVO!
### IL MANQUAIT PEUT-ÊTRE QUELQUES COMMENTAIRES DANS TON CODE POUR ME PERMETTRE DE COMPRENDRE CE QUE TU FAISAIS (OU TENTAIS)
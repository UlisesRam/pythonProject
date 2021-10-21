l1 = set([0,3,4,5,6,7,8,9,1,2])
l2 = set([0,2,3,4,5,7,8,9,6])

B = l1.difference(l2)
A = l2.difference(l1)

print("Lista 1: ", l1)
print("Lista 2: ", l2 )

if len(A) > 0 :
    print("\nElementos faltantes en la Lista 1: {}".format(A))
if len(B) > 0 :
    print("\nElementos faltantes en la Lista 2: {}".format(B))
elif A == B:
    print("\nLas listas son iguales")

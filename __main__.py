from codage import *
print("Ce code permet de déterminer si un langage L est un code ou non\n\n")

L = ("00", "01", "110", "001")  # Le langage L à déterminer si c'est un code ou pas

def test_prefix(L):
# Exemple de test
    for i in range(len(L)):
        for j in range(len(L)):
            if i != j:
                result = isPrefix(L[i], L[j])
                if result == 1:
                    print(f"{L[i]} est un préfixe de {L[j]}")
                elif result == 0:
                    print(f"{L[i]} est égal à {L[j]}")
                else:
                    print(f"{L[i]} n'est pas un préfixe de {L[j]}")

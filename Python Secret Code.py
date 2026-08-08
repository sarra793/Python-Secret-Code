
def len(ch):
    cpt=0
    for _ in ch:
        cpt+=1
    return cpt

def saisie():
    S = ""
    test = False

    while len(S) < 8 or len(S) > 30 or not test:
        S = input("Saisir une chaîne : ")
        l = len(S)
        test = True
        nbLettres = 0
        for i in range(l):
            if ord("A") <= ord(S[i]) <= ord("Z"):
                nbLettres += 1
            elif S[i] != " ":
                test = False
        if nbLettres < 5:
            test = False
    return S

def supprimerEspaces(S):
    S1=""
    l=len(S)
    for i in range(l):
        if S[i]!=" ":
            S1+=S[i]
    return S1

def inverse(I):
    I1=""
    l=len(I)
    for i in range(l-1, -1, -1):
        I1+=I[i]
    return I1

def construireCode(S):
    l=len(S)
    S1=supprimerEspaces(S)
    P=""
    I=""
    for i in range(l):
        if i%2==0:
            P+=S1[i]
        else:
            I+=S[i]
    I1=inverse(I)
    C=P+I1
    return C

def nbVoyelles(S):
    S1=supprimerEspaces(S)
    l=len(S1)
    cpt=0
    for i in range(l):
        if S1[i] in "AEIOUY":
            cpt+=1
    return cpt

def plusFrequente(S):
    S1=supprimerEspaces(S)
    l=len(S1)
    k=0
    for i in range(l):
        cpt=0
        for j in range(i+1, l):
            if S1[i]==S1[j]:
                cpt+=1
        if cpt>k:
            k=cpt
            c=S1[i]
    return c

def estValide(C):
    C1=supprimerEspaces(C)
    l=len(C1)
    verif=True
    if l<8:
        verif=False
    cpt=0
    for i in range(l):
        if C1[i] in "AEIOUY":
            cpt+=1
    if cpt<3:
        verif=False
    cpt1=0
    for i in range(l-1):
        if C1[i]==C1[i+1]:
            cpt1+=1
    if cpt1<1:
        verif=False
    somme=0
    for i in range(l):
        if C[i]!=" ":
            somme+=ord(C[i]) - ord("A") + 1
    if somme%3!=0:
        verif=False
    return verif

def transformer(C):
    C1=supprimerEspaces(C)
    l=len(C1)
    C2=""
    for i in range(l):
        if ord(C1[i])<ord("W"):
            C2+=chr(ord(C1[i])+3)
        else:
            C2+=chr(ord(C1[i])-23)
    return C2

def estPalindrome(C):
    C1=supprimerEspaces(C)
    l=len(C1)
    C3=inverse(C1)
    if C1==C3:
        return True
    else:
        return False

S=saisie()
S1=supprimerEspaces(S)
print("la chaine sans espaces est: ", S1)
voyelles=nbVoyelles(S)
print("le nombre de voyelles est: ", voyelles)
frequence=plusFrequente(S)
print("la lettre la plus frequente est: ", frequence)
C=construireCode(S)
print("le code est: ", C)
if estValide(C):
    print("le code est valide")
else:
    print("le code n'est pas valide")
C2=transformer(C)
print("le code transforme est: ", C2)
if estPalindrome(C):
    print("le code est un palindrome")
else:
    print("le code n'est pas un palindrome")
# Prueba Andreina Gil 
import numpy as np
import itertools

validCodes = ['0412','0416','0426','0414','0424']

def phoneFormat(list1):
    for n in list1:
        stringNumber= createString(n)
        print(stringNumber[:4] + ' ' + stringNumber[4:7] + ' ' + stringNumber[7:])

def createString(num):
    stringInicial = ''
    for n in range(len(num)):
        stringInicial = stringInicial + str(num[n])
    return stringInicial

def validation8(num):
    first8 = False
    for n in range(len(num)):
        if num[n] == '8' and first8 == False:
            first8 = True
        elif num[n] == '8' and num[n-1] != '8' :
            return  False
    return True

def validation9(num):
    n = 0
    while n < len(num):
        if num[n] == '9':
            if (n+2 < len(num) and num[n+2] == '9') or (n+1 < len(num) and n+2 > len(num)):
                if num.count(num[n+1]) != 1:
                    return False
                n +=3
            elif n+1 < len(num) and n+2 < len(num) and num[n+2] != '9' :
                return False
        n +=1
    return True

def validation2dif(num):
    first8_ = -1
    second8 = -1
    for n in range(len(num)):
        if num[n] == '8' and first8_ == -1 :
            first8_ = n
        elif num[n] == '8' and n+1 <len(num) and num[n+1] != '8' :
            second8 = n
    if first8_-1 < 0:
        return False
    elif num[first8_-1] != num[second8+1] and num.count(str(num[first8_-1])) ==2 and num.count(str(num[second8+1])) ==2 :
        return True
    return False

def validation3(num):
    first3 = False
    edges = -1
    for n in range(len(num)):
        if num[n] == '3' and first3 == False :
            first3 = True
            if n>0 :
                edges = num[n-1]
                if n+1 <len(num) and num[n+1] != edges:
                    return False
            else:
                edges = num[n+1]
        elif num[n] == '3' and num[n-1] !=edges and n+1 <len(num) and num[n+1] != edges:
            return False
    return True

def validation567(num):
    divisores=[2,3,5,7]
    for n in divisores:
        if int(num[4]) % n == 0 and int(num[5]) % n == 0 and int(num[6]) % n == 0 :
            return True
    return False

def validationPenultimate(num):
    if int(num[len(num)-1]) != 0 and int(num[len(num)-2]) % int(num[len(num)-1]) == 0:
        return True
    return False

def validationLast(num):
    return int(num[len(num)-1]) in [2,3,5,7]

def isValid(num):
    return num[:4] in validCodes

def solution(listaPermutaciones):
    x = []
    for vector in listaPermutaciones:
        vectorAsString = createString(vector) 
        if isValid(vectorAsString) and validation8(vectorAsString) and validation9(vectorAsString) and validation2dif(vectorAsString) and validation3(vectorAsString) and validation567(vectorAsString) and validationPenultimate(vectorAsString) and validationLast(vectorAsString):
            x.append(vector)

    return x

vectorInicial = [0,0,2,2,3,4,4,8,8,9,9]

permutationes = set(list(itertools.permutations(vectorInicial)))
listaPermutaciones = [np.array(perm) for perm in permutationes]

phoneFormat(solution(listaPermutaciones))
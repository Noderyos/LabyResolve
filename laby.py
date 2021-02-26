import numpy as np
import random

height = 20
length = 40
matrix = np.zeros([height, length], dtype = int)

def main():
    line = ''
    cb = 0
    while resolve(matrix, (length - 1), (height - 1)) != 1:
        gen(height, length)
        resolve(matrix, (length - 1), (height - 1))
        cb +=1
        print('Essai numéro ' + str(cb))
    for k in range(height):
        for l in range(length):
            if matrix[k][l] == 1:
                line += ' '
            else:
                line += '█'
        print(line)
        line = ''
    
    
                

def gen(y, x):
    for i in range(y):
        for j in range(x):
            if j == 0:
                matrix[i][j] = 0
            elif j == (x-1):
                matrix[i][j] = 0
            elif i == 0:
                matrix[i][j] = 0
            elif i == (y-1):
                matrix[i][j] = 0
            else:
                if random.randint(0,2) != 1:
                    matrix[i][j] = 1

def resolve(matrice, endx, endy):
    print("Je teste")
    x = 1
    y = 1
    prevx = 1
    prevy = 1
    nb = 0
    print("endx vaut "+ str(endx))
    print("endy vaut "+ str(endy))
    
    while x != endx:
        while y != endy:
            while nb < 10000:
                rand = random.randint(1,4)
                print("pos x= "+ str(x) + " y = " + str(y))
                print("Rand vaut "+ str(rand))
                if rand == 1:
                    if prevx < 19:
                        x += 1
                        print('add x')
                elif rand == 2:
                    if prevy < (endy - 1):
                        y += 1
                        print('add y')
                elif rand == 3:
                    if prevx > -20:
                        x -= 1
                        print('del x')
                elif rand == 4:
                    if prevy > (0 - endy + 1):
                        y -= 1
                        print('del y')
                else:
                    print("Mais WTF")
                if matrice[x][y] == 0:
                    prevx = x
                    prevy = y
                    print("c bon")
                else:
                    x = prevx
                    y = prevy
                    print("c pas bon")
                nb += 1
                print(nb)
        
    if x == endx & y == endy:
        return 1
    else:
        return 0
        print("Non")
        print(nb)
    
    














































if __name__ == '__main__':
    main()
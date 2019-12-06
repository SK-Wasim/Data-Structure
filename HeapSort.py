import numpy as np
from copy import copy, deepcopy
count = 0
arrPuzzle = np.array([[1,6,5],[0,2,4],[3,7,8]])

for i in range(0,len(arrPuzzle)):
    for j in range(0,len(arrPuzzle[i])):
        if arrPuzzle[i][j] == 0:
            print(arrPuzzle)
            if (i-1) >= 0:
                count = count+1
                arrPuzzle1 = deepcopy(arrPuzzle)
                temp = arrPuzzle1[i-1][j]
                arrPuzzle1[i-1][j] = arrPuzzle1[i][j]
                arrPuzzle1[i][j] = temp
                print(arrPuzzle1)
                
            if (i+1) < len(arrPuzzle):
                temp = 0
                count = count+1
                arrPuzzle2 = deepcopy(arrPuzzle)
                temp = arrPuzzle2[i+1][j]
                arrPuzzle2[i+1][j] = arrPuzzle2[i][j]
                arrPuzzle2[i][j] = temp
                print(arrPuzzle2)
                
            if (j-1) >= 0:
                count = count+1
                arrPuzzle3 = deepcopy(arrPuzzle)
                temp = arrPuzzle3[i][j-1]
                arrPuzzle3[i][j-1] = arrPuzzle3[i][j]
                arrPuzzle3[i][j] = temp
                print(arrPuzzle3)
                
            if (j+1) < len(arrPuzzle[i]):
                count = count+1
                arrPuzzle4 = deepcopy(arrPuzzle)
                temp = arrPuzzle4[i][j+1]
                arrPuzzle4[i][j+1] = arrPuzzle4[i][j]
                arrPuzzle4[i][j] = temp
                print(arrPuzzle4)
            break;
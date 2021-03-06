import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.7, 0.7])
    b = -0.5
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NOR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.7, -0.7])
    b = 0.5
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

def tbl(logic):
    x1 = [0, 1]
    x2 = [0, 1]
    for a in x1:
        for b in x2:
            if logic == AND:
                print(f'{a} AND {b} = ' + '{}'.format(logic(a, b)))
            elif logic == OR:
                print(f'{a} O R {b} = ' + '{}'.format(logic(a, b)))
            elif logic == NAND:
                print(f'{a} NAND {b} = ' + '{}'.format(logic(a, b)))
            elif logic == NOR:
                print(f'{a} NOR {b} = ' + '{}'.format(logic(a, b)))
            elif logic == XOR:
                print(f'{a} XOR {b} = ' + '{}'.format(logic(a,b))) 
def main():
    tbl(AND)
    tbl(OR)
    tbl(NAND)
    tbl(NOR)
    tbl(XOR)


if __name__ == "__main__":
    main()

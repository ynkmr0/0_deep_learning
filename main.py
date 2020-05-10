def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
def OR(x1,x2):
    w1 ,w2, theta = 0.7, 0.7, 0.5
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def main():
    a=AND(0, 1)
    b=OR(1, 1)
    c=OR(0, 0)
    print(a)
    print(b)
    print(c)

if __name__ == "__main__":
    main()

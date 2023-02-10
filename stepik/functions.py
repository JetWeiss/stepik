def f(x):
    if x <= -2:
        return 1-(x+2)**2
    elif -2 < x <= 2:
        return -(x/2)
    else:
        return (x-2)**2 +1

def modify_list(l):
    b = []
    for i in range(len(l)):
        if int(l[i]) % 2 == 0:
            b.append(int(l[i]) // 2)
    l.clear()
    l.extend(b)
    print(l)

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6]
    modify_list(lst)
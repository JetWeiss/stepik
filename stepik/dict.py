def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2*key in d:
        d[2*key] += [value]
    else:
        d[2*key] = [value]

def dictionary_counter():
    a = input().lower().split()
    d = {}
    for i in a:
        if i not in d:
            d[i] = a.count(i)
    for j in d.items():
        print(*j)

if __name__ == "__main__":
   n = int(input())
   d = {}
   for i in range(n):
       x = int(input())
       if x not in d:
           d[x] = f(x)
           print(d[x])
       else:
           print(d[x])

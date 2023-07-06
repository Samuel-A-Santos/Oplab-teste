n = 10000
m = [True] * (n + 1) 

m[0] = False
m[1] = False

primos = []

for a, b in enumerate(m) : 

    if b : 
        primos.append(a) 

        for i in range(a * 2 , n+1, a) : 
            print(a)
            m[i] = False 

print(primos[3:6])
a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

MaiorAB = (a+b+abs(a-b)) / 2

MaiorAB = (MaiorAB + c + abs(MaiorAB - c)) / 2 

print(f'{int(MaiorAB)} eh o maior')
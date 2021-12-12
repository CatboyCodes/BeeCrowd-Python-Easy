A, B, C = input().split()

triangulo = 0.5 * float(A) * float(C)

pi = 3.14159

circulo = pi * float(C) * float(C)

trapezio = ((float(A) + float(B)) / 2) * float(C)

quadrado = float(B) * float(B)

retangulo = float(A) * float(B)

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
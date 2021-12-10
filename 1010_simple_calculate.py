p1_code, p1_q, p1_p = input().split()
p2_code, p2_q, p2_p = input().split()
total = int(p1_q) * float(p1_p) + int(p2_q) * float(p2_p)
print(f'VALOR A PAGAR: R$ {total:.2f}')
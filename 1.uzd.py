Aprēķināt faktoriālu un pārbaudīt vai ievadītais skaitlis ir pirmskaitlis.
1) kas ir faktoriāls?





>def faktoriāls(n)








> def ir_pirmskaitlis(num):
# Pārbauda vai skaitlis ir pirmskaitlis, izmantojot ciklus while
if num < 2:
    return False
1 = 2
while i * i <= num:
    if num % i == 0:
        return False
    i += 1 
return True

# Ievada skaitlis
n = int(input("Ievadiet veselu pzitīvu skaitli: "))
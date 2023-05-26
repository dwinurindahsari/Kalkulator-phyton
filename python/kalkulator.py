print("")
print("Ini adalah kalkulator buatan Dwi nur indah sari")
print("")
num1 = float(input("Masukan angka pertama: "))
op = input("masukkan oprator:")
num2 = float(input("masukkan angka kedua: "))

if op =='+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1 / num2)    
elif op == '*':
    print(num1 * num2)   

else:
    print("operator tidak valid")     

print("Terima Kasih")
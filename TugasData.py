import os
import random
import string

data = []

while True:
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen for Windows or Linux/Mac
    print(f"{'DATA SNACK SUPERMARKET':#^35}")
    
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    
    Produk = input("Enter Produk\t\t: ")
    Jenis = input("Enter Jenis\t\t: ")
    Harga = input("Enter Harga\t\t: ")
    
    data.append({'Key': keyFinal, 'Produk': Produk, 'Jenis': Jenis, 'Harga': Harga})
    
    opsi = input("Input data LAGI (y/t)? ").lower()
    if opsi == 't':
        break

print("\nTabel Snack Supermarket:")
print("-" * 40)
print(f"{'Key':<5} {'Produk':<15} {'Jenis':<10} {'Harga':<10}")
print("-" * 40)

for item in data:
    print(f"{item['Key']:<5} {item['Produk']:<15} {item['Jenis']:<10} {item['Harga']:<10}")

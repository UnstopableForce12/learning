import pandas as pd
import matplotlib.pyplot as plt

data = {
    'nama': [],
    'nilai': []
}

while True: # Use an infinite loop and break when the user is done
    nama = input("Silakan masukkan nama Anda: ")

    while True: # Loop to ensure valid numerical input for 'nilai'
        try:
            nilai = int(input("Berapa nilai Anda? "))
            break # Exit the inner loop if input is valid
        except ValueError:
            print("Nilai harus berupa angka. Silakan coba lagi.")

    data['nama'].append(nama)
    data['nilai'].append(nilai)

    while True: # Loop to ensure valid 'y' or 'n' input
        tambah = input("Lanjutkan? (y/n): ").lower() # Convert to lowercase for consistent checking
        if tambah in ['y', 'n']:
            break # Exit the inner loop if input is valid
        else:
            print("Tolong input dengan benar! (y/n)")

    if tambah == 'n':
        break # Exit the main loop if the user doesn't want to continue

listdata = pd.DataFrame(data)
plt.figure(figsize=(10,6))
plt.plot(listdata(nama),listdata(nilai),)
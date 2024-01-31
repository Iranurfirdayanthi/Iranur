import tkinter as tk

def konversi_suhu():
    try:
        input_suhu = float(entry_suhu.get())

        if var.get() == 1:  # Celsius to Fahrenheit
            hasil = (input_suhu * 9/5) + 32
        elif var.get() == 2:  # Celsius to Kelvin
            hasil = input_suhu + 273.15
        elif var.get() == 3:  # Fahrenheit to Celsius
            hasil = (input_suhu - 32) * 5/9
        elif var.get() == 4:  # Fahrenheit to Kelvin
            hasil = (input_suhu - 32) * 5/9 + 273.15
        elif var.get() == 5:  # Kelvin to Celsius
            hasil = input_suhu - 273.15
        elif var.get() == 6:  # Kelvin to Fahrenheit
            hasil = (input_suhu - 273.15) * 9/5 + 32
        else:
            hasil = input_suhu  # Sama-saja jika satuan sama

        label_hasil.config(text=f"Hasil: {hasil:.2f} {satuan[var.get()]}")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid!")

# Main window
window = tk.Tk()
window.title("Konversi Suhu")

# Variabel untuk menyimpan pilihan satuan
var = tk.IntVar()

# Label dan Entry untuk input suhu
label_input = tk.Label(window, text="Masukkan Suhu:")
label_input.pack()

entry_suhu = tk.Entry(window)
entry_suhu.pack()

# Radiobuttons untuk pilihan satuan
label_satuan = tk.Label(window, text="Pilih Satuan:")
label_satuan.pack()

satuan = {1: "Fahrenheit", 2: "Kelvin", 3: "Celsius", 4: "Kelvin", 5: "Celsius", 6: "Fahrenheit"}

for i in range(1, 7):
    tk.Radiobutton(window, text=satuan[i], variable=var, value=i).pack()

# Tombol konversi
button_convert = tk.Button(window, text="Konversi", command=konversi_suhu)
button_convert.pack()

# Label untuk menampilkan hasil konversi
label_hasil = tk.Label(window, text="Hasil:")
label_hasil.pack()

# Menjalankan aplikasi
window.mainloop()
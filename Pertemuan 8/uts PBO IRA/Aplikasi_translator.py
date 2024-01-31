from tkinter import Tk, Label, StringVar, OptionMenu, Entry, Button
from googletrans import Translator

def translate_text():
    input_text = entry.get()
    selected_language = language_var.get()

    translator = Translator()
    translated_text = translator.translate(input_text, dest=selected_language).text

    output_var.set(translated_text)

# Buat jendela aplikasi
app = Tk()
app.title("Aplikasi Translator")

# Variabel untuk menyimpan bahasa terpilih
language_var = StringVar(app)
language_var.set("en")  # Default bahasa: Inggris

# Label dan input untuk teks
Label(app, text="Teks:").pack(pady=10)
entry = Entry(app, width=40)
entry.pack()

# Pilihan bahasa
Label(app, text="Pilih Bahasa:").pack(pady=5)
OptionMenu(app, language_var, "inggris", "indonesia", "sudanese", "javanese").pack()
# "jv" adalah kode bahasa untuk Jawa

# Tombol terjemahkan
Button(app, text="Terjemahkan", command=translate_text).pack(pady=10)

# Label untuk hasil terjemahan
output_var = StringVar(app)
Label(app, text="Hasil Terjemahan:").pack(pady=5)
Label(app, textvariable=output_var).pack()

# Jalankan aplikasi
app.mainloop()
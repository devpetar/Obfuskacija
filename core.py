######### Importi modula ###########

# import modula za grafičko sučelje
import tkinter as tk
# import built-in funcije za otvaranje dialoga za odabir (putanje) dokumenta 
from tkinter.filedialog import askopenfilename
# import modula za ASCII operacije
import ascii
# import modula base64 za kodiranje i dekodiranje binarnih podataka
import base64


######### Sučelje ###############

# Funkcija za odabir dokumenta za konvertiranje
# Učitava tekst iz odabranog dokumenta i prikazuje ga u sučelju
def file_for_converting():
    global input_file_path
    input_file_path = askopenfilename()
    global input_text_widget
    with open(input_file_path, "r", encoding='utf-8') as file:
        input_text_widget.delete("1.0", tk.END)
        input_text_widget.insert(tk.END, file.read())

input_file_path = ""

window = tk.Tk()
window.minsize(400, 700)
window.title("Obfuskacija teksta")

input_file_button = tk.Button(window, text= "Odabir teksta za konvertiranje iz dokumenta", command=file_for_converting)
input_file_button.grid(row=0, column=0, padx=5, pady=10)

input_text_lbl = tk.Label(window, text = "ili unesite tekst za konverziju u polje:")
input_text_lbl.grid(row=1, column=0, columnspan = 2, sticky="W", padx = 3)
input_text_widget = tk.Text(window, width=40, height=5)
input_text_widget.grid(row=2, column=0, rowspan = 4, columnspan = 2, sticky="W", padx = 5)

input_file_lbl = tk.Label(window, text = "Unesite putanju i ime za izlazni dokument (npr. C:\..\encoded.txt):")
input_file_lbl.grid(row=6, column=0, columnspan = 2, sticky="W", padx = 3, pady=5)
output_file_name_StringVar = tk.StringVar()
output_file_name = tk.Entry(window, width=55, textvariable = output_file_name_StringVar)
output_file_name.grid(row=7, column=0, columnspan = 2, sticky="W", padx = 5)

output_text_lbl = tk.Label(window, text = "Kovertirani tekst:")
output_text_lbl.grid(row=8, column=0, columnspan = 2, sticky="W", padx = 3, pady=5)
output_text_widget = tk.Text(window, width=40, height=5, state='disabled')
output_text_widget.grid(row=9, column=0, rowspan = 4, columnspan = 2, sticky="W", padx = 5)

separtator_text = "_"*80

input_text = ""
# Funkcija za dohvaćanje input teksta
# Uzima se tekst iz sučelja
def prepare_input_text():
    global input_text
    input_text = input_text_widget.get("1.0",'end-1c')

# Funkacija za ispis outputa u sučelje i opcionalno u dokument ako je uneseno ime dokumenta
def set_converted_text(converted_text):
    # Ispis u sučelje
    global output_text_widget
    output_text_widget.configure(state='normal')
    output_text_widget.delete("1.0", tk.END)
    output_text_widget.insert(tk.END, converted_text)
    output_text_widget.configure(state='disabled')
    # Ispis u file ako je korisnik naveo putanju i naziv izlaznog dokumenta.
    global output_file_name_StringVar
    if output_file_name_StringVar.get() != "":
        with open(output_file_name_StringVar.get(), "w", encoding='utf-8') as outfile:
            outfile.write(converted_text)
    

#########################################################################################
######################################## ASCII ##########################################

# Poziv funkcije za kodiranje plain text u ASCII
def ascii_encode():
    prepare_input_text()
    converted_text = ascii.ascii_encode(input_text, get_ascii_encoding_base())
    set_converted_text(converted_text)

# Poziv funkcije za dekodiranje ASCII-ja u plain text
def ascii_decode():
    prepare_input_text()
    converted_text = ascii.ascii_decode(input_text, get_ascii_encoding_base())
    set_converted_text(converted_text)

# Dohvaćanje baze za konvertiranje
def get_ascii_encoding_base():
    ascii_type = ascii_encoding_base_StrVar.get();
    if ascii_type == "Binary":
        return 2
    elif ascii_type == "Octal":
        return 8
    elif ascii_type == "Decimal":
        return 10
    elif ascii_type == "Hexadecimal":
        return 16
    else:
        from tkinter import messagebox
        messagebox.showerror("Greška!", "Greška! Odaberite ASCII tip!")

ascii_encoding_base = 2

separator1 = tk.Label(window, text = separtator_text)
separator1.grid(row=13, column=0, columnspan = 2)

natpisStr = tk.Label(window, text = "ASCII konvertiranje")
natpisStr.grid(row=14, column=0, sticky="W", padx = 5)

natpisStr = tk.Label(window, text = "ASCII tip:")
natpisStr.grid(row=15, column=0)
ascii_encoding_base_StrVar = tk.StringVar()
ascii_base_option_menu = tk.OptionMenu(window, ascii_encoding_base_StrVar, "Binary", "Octal", "Decimal", "Hexadecimal")
ascii_encoding_base_StrVar.set("Binary")
ascii_base_option_menu.grid(row=16, column=0)

asci_encode_bttn = tk.Button(window, text="Konvertiranje u ASCII", command=ascii_encode)
asci_encode_bttn.grid(row=15, column=1)

asci_decode_bttn = tk.Button(window, text="Konvertiranje iz ASCII-a", command=ascii_decode)
asci_decode_bttn.grid(row=16, column=1)

separator2 = tk.Label(window, text = separtator_text)
separator2.grid(row=17, column=0, columnspan = 2)

####################################### ASCII kraj ################################################
###################################################################################################

###################################################################################################
######################################## Base64 ###################################################
def base64_encode():
    prepare_input_text()
    base64_tekst = base64.b64encode(input_text)
    set_converted_text(base64_tekst)

def base64_decode():
    prepare_input_text()
    base64_tekst = base64.b64decode(input_text)
    set_converted_text(base64_tekst)
    
natpis_b64_Str = tk.Label(window, text = "Base64 konvertiranje")
natpis_b64_Str.grid(row=18, column=0, sticky="W", padx = 5, pady=10)

b64_encode_bttn = tk.Button(window, text="Konvertiranje u Base64", command=base64_encode)
b64_encode_bttn.grid(row=19, column=0)

b64_decode_bttn = tk.Button(window, text="Konvertiranje iz Base64", command=base64_decode)
b64_decode_bttn.grid(row=19, column=1)

separator4 = tk.Label(window, text = separtator_text)
separator4.grid(row=20, column=0, columnspan = 2)

####################################### Base64 kraj ###############################################
###################################################################################################

###################################################################################################
######################################## Unicode ##################################################
def unicode_encode():
    prepare_input_text()
    unicode_text = ''.join(r'\u{:04X}'.format(ord(char)) for char in input_text)
    set_converted_text(unicode_text)

def unicode_decode():
    prepare_input_text()
    regular_text = bytes(input_text, 'utf-8').decode('unicode_escape')
    set_converted_text(regular_text)
    
natpis_uni_Str = tk.Label(window, text = "Unicode konvertiranje")
natpis_uni_Str.grid(row=21, column=0, sticky="W", padx = 5, pady=10)

uni_encode_bttn = tk.Button(window, text="Konvertiranje u Unicode", command=unicode_encode)
uni_encode_bttn.grid(row=22, column=0)

uni_decode_bttn = tk.Button(window, text="Konvertiranje iz Unicoda", command=unicode_decode)
uni_decode_bttn.grid(row=22, column=1)

separator3 = tk.Label(window, text = separtator_text)
separator3.grid(row=23, column=0, columnspan = 2)

####################################### Unicode kraj ##############################################
###################################################################################################


# Ostale konverzije


window.mainloop()

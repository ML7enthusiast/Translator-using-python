from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type", src="src", dest="dest"):
    try:
        translator = Translator()
        translated = translator.translate(text, src=src, dest=dest)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"



# Function to handle user input and display translated text
def data():
    # Get source and destination languages
    source_language = comb_src.get().lower()
    dest_language = comb_dest.get().lower()

    # Get the source text
    msg = sor_txt.get(1.0, END).strip()

    if not msg:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, "Please enter text to translate.")
        return

    # Translate the text
    translated_text = change(text=msg, src=source_language, dest=dest_language)

    # Display the translated text
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, translated_text)


# Tkinter GUI setup
root = Tk()
root.title('Translator')
root.geometry("500x800")
root.config(bg='blue')

# Title label
lab_txt = Label(root, text="Anuwadak", font=("Times New Roman", 40, "bold"), bg='blue', fg='white')
lab_txt.place(x=100, y=40, height=50, width=300)

# Source text label
lab_src = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), bg='blue', fg='white')
lab_src.place(x=100, y=100, height=20, width=300)

# Source text input
sor_txt = Text(root, font=("Times New Roman", 15), wrap=WORD)
sor_txt.place(x=10, y=130, height=150, width=480)

# Language dropdowns
list_text = list(LANGUAGES.values())

# Source language combobox
comb_src = ttk.Combobox(root, value=list_text)
comb_src.place(x=10, y=300, height=30, width=150)
comb_src.set("english")

# Destination language combobox
comb_dest = ttk.Combobox(root, value=list_text)
comb_dest.place(x=180, y=300, height=30, width=150)
comb_dest.set("hindi")

# Translate button
button_change = Button(root, text="Translate", relief=RAISED, command=data, bg='white', fg='black',
                       font=("Times New Roman", 12))
button_change.place(x=350, y=300, height=30, width=100)

# Destination text label
lab_dest = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), bg='blue', fg='white')
lab_dest.place(x=100, y=360, height=20, width=300)

# Destination text output
dest_txt = Text(root, font=("Times New Roman", 15), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

# Run the GUI
root.mainloop()

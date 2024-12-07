from tkinter import *
from num2words import num2words
from PIL import Image, ImageTk

def convert_to_words(event=None):
    number_in_words = ""  # Initialize empty string

    try:
        number = int(entry.get())
        language = language_var.get()
        if language == 'fa':
            number_in_words = num2words(number, lang='fa')
        elif language == 'en':
            number_in_words = num2words(number, lang='en')

        result_label.configure(state='normal')
        result_label.delete(1.0, END)
        result_label.insert(END, number_in_words)
        result_label.configure(state='disabled')

    except (ValueError, OverflowError):
        result_label.configure(state='normal')
        result_label.delete(1.0, END)
        result_label.insert(END, "متن نامعتبر است. لطفاً عدد صحیح وارد کنید.")
        result_label.configure(state='disabled')

def on_language_change(*args):
    convert_to_words()  # Convert immediately when language changes

def copy_to_clipboard():
    result_text = result_label.get(1.0, END)
    window.clipboard_clear()
    window.clipboard_append(result_text)

def clear_fields():
    entry.delete(0, END)
    result_label.configure(state='normal')
    result_label.delete(1.0, END)
    result_label.configure(state='disabled')

# Create main window
window = Tk()
window.title("تبدیل عدد به حروف")
window.geometry("1000x500")

# Add image to the project using PIL
image = Image.open("123.jpg")
background_image = ImageTk.PhotoImage(image)
# Set background of the window
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create number input
entry = Entry(window, width=50, font=("Arial", 14))
entry.pack(pady=10)

# Bind key release event to the convert function
entry.bind("<KeyRelease>", convert_to_words)

# Create frame for language buttons
language_frame = Frame(window)
language_frame.pack(pady=10)

# Create language variable
language_var = StringVar()
language_var.set('fa')
language_var.trace("w", on_language_change)  # Trace changes to the language variable

# Create Persian button
fa_button = Radiobutton(language_frame, text="فارسی", variable=language_var, value='fa', font=("Arial", 12))
fa_button.pack(side=LEFT, padx=5)

# Create English button
en_button = Radiobutton(language_frame, text="انگلیسی", variable=language_var, value='en', font=("Arial", 12))
en_button.pack(side=LEFT, padx=5)

# Create frame for result display with scrollbar
result_frame = Frame(window)
result_frame.pack(pady=10)

# Create a canvas for the text area
result_canvas = Canvas(result_frame, width=800, height=30)
result_canvas.pack(side=LEFT)

# Create a vertical scrollbar
scrollbar = Scrollbar(result_frame, orient=VERTICAL, command=result_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Create text widget for displaying results
result_label = Text(result_canvas, font=("B Titr", 14), height=5, width=100, wrap='word', state='disabled')
result_canvas.create_window((0, 0), window=result_label, anchor='nw')

# Configure scrolling
result_label.bind("<Configure>", lambda e: result_canvas.configure(scrollregion=result_canvas.bbox("all")))
result_canvas.configure(yscrollcommand=scrollbar.set)

# Create copy button
copy_button = Button(window, text="کپی", command=copy_to_clipboard, font=("Arial", 12))
copy_button.pack(pady=5)

# Create clear button
clear_button = Button(window, text="پاک کردن", command=clear_fields, font=("Arial", 12))
clear_button.pack(pady=5)

# Start the GUI event loop
window.mainloop()
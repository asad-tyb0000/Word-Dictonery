import tkinter as tk
from tkinter import ttk
import json
import os

def process_text():
    input_text = text_input.get().strip().upper()
    option = combo.get()
    if not input_text:
        return
    
    first_char = input_text[0].upper()
    json_file = f"{first_char.lower()}.json"
    
    if not os.path.exists(json_file):
        result = "No data available"
    else:
        with open(json_file, 'r') as file:
            data = json.load(file)
            if input_text in data:
                if option == "synonym":
                    synonyms = data[input_text]["SYNONYMS"]
                    result = ", ".join(synonyms) if synonyms else "Synonym not found"
                elif option == "antonym":
                    antonyms = data[input_text]["ANTONYMS"]
                    result = ", ".join(antonyms) if antonyms else "Antonym not found"
                elif option == "meaning":
                    meanings = data[input_text]["MEANINGS"]
                    result = "\n".join([f"{k}: {v[1]}" for k, v in meanings.items()])
                else:
                    result = ""
            else:
                result = "Word not found in data"
    
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, result)


# Create the main window
root = tk.Tk()
root.title("Text Processor")

# Create and place the input textbox
text_input = tk.Entry(root, width=50)
text_input.grid(row=0, column=0, padx=10, pady=10)

# Create and place the combobox
combo = ttk.Combobox(root, values=["synonym", "antonym", "meaning"])
combo.grid(row=0, column=1, padx=10, pady=10)
combo.current(0)  # Set default value

# Create and place the button
process_button = tk.Button(root, text="Process", command=process_text)
process_button.grid(row=0, column=2, padx=10, pady=10)


# Create and place the output textbox
text_output = tk.Text(root, height=5, width=50)
text_output.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Run the application
root.mainloop()
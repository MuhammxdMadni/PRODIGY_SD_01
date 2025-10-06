import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        from_unit = combo_unit.get()
        if from_unit == "Celsius":
            celsius = temp
        elif from_unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
        elif from_unit == "Kelvin":
            celsius = temp - 273.15
        else:
            raise ValueError

        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        label_result.config(
            text=f"Celsius:    {celsius:.2f}°C\n"
                 f"Fahrenheit: {fahrenheit:.2f}°F\n"
                 f"Kelvin:     {kelvin:.2f}K"
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number and select a unit.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("320x220")

frame = ttk.Frame(root, padding=15)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Enter Temperature:").pack(anchor=tk.W)
entry_temp = ttk.Entry(frame)
entry_temp.pack(fill=tk.X, pady=5)

ttk.Label(frame, text="Select Unit:").pack(anchor=tk.W)
combo_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_unit.current(0)
combo_unit.pack(fill=tk.X, pady=5)

ttk.Button(frame, text="Convert", command=convert_temperature).pack(pady=10)

label_result = ttk.Label(frame, text="", font=("Arial", 11))
label_result.pack(pady=10)

root.mainloop()

import tkinter as tk
import customtkinter as ctk # import the customtkinter module; used to create custom widgets and windows for standalone apps

ctk.set_appearance_mode("system")  # Modes: system (OS settings decide), light, dark
ctk.set_default_color_theme("dark-blue") # set the default color theme for all widgets; 'dark-blue', 'blue', and 'green' are available

#? main window
# ==============================================================================================
window = ctk.CTk()  # create the main window
window.title("Temperature Converter")  # set the title of the main window
window.geometry("490x260")  # set the size of the main window
window.resizable(False, False)  # make the main window non-resizable
window.configure(bg="#243a57")  # set the background color of the main window
window.iconbitmap("images/icon/MERN16.ico")
# ==============================================================================================



#? Conversion functions
# ==============================================================================================
def FahrenheitToCelcius(): # function to convert Fahrenheit to Celsius
    if entry.get() == "":
        result_label.configure(text="Please enter a value")
        return
    temperature = float(entry.get()) # gets value from entry
    result = round((temperature - 32) * 5/9, 2)
    result_label.configure(text=f"{temperature}°F = {result}°C") # sends value to result_label

def FahrenheitToKelvin(): # function to convert Fahrenheit to Kelvin
    if entry.get() == "":
        result_label.configure(text="Please enter a value")
        return
    temperature = float(entry.get()) # gets value from entry
    result = round((temperature - 32) * 5/9 + 273.15, 2)
    result_label.configure(text=f"{temperature}°F = {result}°K") # sends value to result_label

def CelciusToFahrenheit(): # function to convert Celsius to Fahrenheit
    if entry.get() == "":
        result_label.configure(text="Please enter a value")
        return
    temperature = float(entry.get()) # gets value from entry
    result = round(temperature * 9/5 + 32, 2)
    result_label.configure(text=f"{temperature}°C = {result}°F") # sends value to result_label

def CelciusToKelvin(): # function to convert Celsius to Kelvin
    if entry.get() == "":
        result_label.configure(text="Please enter a value")
        return
    temperature = float(entry.get()) # gets value from entry
    result = round(temperature + 273.15, 2)
    result_label.configure(text=f"{temperature}°C = {result}°K") # sends value to result_label

def KelvinToFahrenheit(): # function to convert Kelvin to Fahrenheit
    if entry.get() == "":
        result_label.configure(text="Please enter a value")
        return
    temperature = float(entry.get()) # gets value from entry
    result = round((temperature - 273.15) * 9/5 + 32, 2)
    result_label.configure(text=f"{temperature}°K = {result}°F") # sends value to result_label

def KelvinToCelcius(): # function to convert Kelvin to Celsius
    if entry.get() == "":
        result_label.configure(text="Please enter a value")
        return
    temperature = float(entry.get()) # gets value from entry
    result = round(temperature - 273.15, 2)
    result_label.configure(text=f"{temperature}°K = {result}°C") # sends value to result_label
# ==============================================================================================



#? elements inside the main window (children); input box, buttons, labels, etc.
# ==============================================================================================

label = ctk.CTkLabel(window, text="Enter temperature:", font=("Arial", 20))  # create a label widget; child of root
label.grid(row=0, column=1, pady=10)  # make the label visible; pack it into the main window (root)

entry = ctk.CTkEntry(window,) # create an entry widget; child of root; this is the input box
entry.grid(row=1, column=1, pady=20)

BUTTON = ""

ctof_btn = ctk.CTkButton(window, text="Celsius to Fahrenheit", command=CelciusToFahrenheit)
ctof_btn.grid(row=2, column=0, pady=5, padx=10)

ctok_btn = ctk.CTkButton(window, text="Celsius to Kelvin", command=CelciusToKelvin)
ctok_btn.grid(row=3, column=0, pady=5, padx=10)

ftoc_btn = ctk.CTkButton(window, text="Fahrenheit to Celsius", command=FahrenheitToCelcius)
ftoc_btn.grid(row=2, column=1, pady=5)

ftok_btn = ctk.CTkButton(window, text="Fahrenheit to Kelvin", command=FahrenheitToKelvin)
ftok_btn.grid(row=3, column=1, pady=5)

ktoc_btn = ctk.CTkButton(window, text="Kelvin to Celsius", command=KelvinToCelcius)
ktoc_btn.grid(row=2, column=2, pady=5, padx=10)

ktof_btn = ctk.CTkButton(window, text="Kelvin to Fahrenheit", command=KelvinToFahrenheit)
ktof_btn.grid(row=3, column=2, pady=5, padx=10)

result_label = ctk.CTkLabel(window, text="", font=("Arial", 18), text_color="yellow")
result_label.grid(row=4, column=0, pady=20, columnspan=3)
# ==============================================================================================



# run the main window
window.mainloop()
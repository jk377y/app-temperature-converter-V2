import tkinter as tk # import the customtkinter module; used to create custom widgets and windows for standalone apps


#? main window
# ==============================================================================================
window = tk.Tk()  # create the main window
window.title("Temperature Converter")  # set the title of the main window
window.geometry("510x270")  # set the size of the main window
# ==============================================================================================



#? Conversion functions
# ==============================================================================================
def FahrenheitToCelcius(): # function to convert Fahrenheit to Celsius
    temperature = float(entry.get()) # gets value from entry
    result = round((temperature - 32) * 5/9, 2)
    result_label.configure(text=f"{temperature}°F = {result}°C") # sends value to result_label

def FahrenheitToKelvin(): # function to convert Fahrenheit to Kelvin
    temperature = float(entry.get()) # gets value from entry
    result = round((temperature - 32) * 5/9 + 273.15, 2)
    result_label.configure(text=f"{temperature}°F = {result}°K") # sends value to result_label

def CelciusToFahrenheit(): # function to convert Celsius to Fahrenheit
    temperature = float(entry.get()) # gets value from entry
    result = round(temperature * 9/5 + 32, 2)
    result_label.configure(text=f"{temperature}°C = {result}°F") # sends value to result_label

def CelciusToKelvin(): # function to convert Celsius to Kelvin
    temperature = float(entry.get()) # gets value from entry
    result = round(temperature + 273.15, 2)
    result_label.configure(text=f"{temperature}°C = {result}°K") # sends value to result_label

def KelvinToFahrenheit(): # function to convert Kelvin to Fahrenheit
    temperature = float(entry.get()) # gets value from entry
    result = round((temperature - 273.15) * 9/5 + 32, 2)
    result_label.configure(text=f"{temperature}°K = {result}°F") # sends value to result_label

def KelvinToCelcius(): # function to convert Kelvin to Celsius
    temperature = float(entry.get()) # gets value from entry
    result = round(temperature - 273.15, 2)
    result_label.configure(text=f"{temperature}°K = {result}°C") # sends value to result_label
# ==============================================================================================



#? elements inside the main window (children); input box, buttons, labels, etc.
# ==============================================================================================

label = tk.Label(window, text="Enter temperature:", font=("Arial", 20))  # create a label widget; child of root
label.grid(row=0, column=1, pady=20, padx=10)  # make the label visible; pack it into the main window (root)

entry = tk.Entry(window,) # create an entry widget; child of root; this is the input box
entry.grid(row=1, column=1)

ctof_btn = tk.Button(window, text="Celsius to Fahrenheit", command=CelciusToFahrenheit)
ctof_btn.grid(row=2, column=0)

ctok_btn = tk.Button(window, text="Celsius to Kelvin", command=CelciusToKelvin)
ctok_btn.grid(row=3, column=0)

ftoc_btn = tk.Button(window, text="Fahrenheit to Celsius", command=FahrenheitToCelcius)
ftoc_btn.grid(row=2, column=1)

ftok_btn = tk.Button(window, text="Fahrenheit to Kelvin", command=FahrenheitToKelvin)
ftok_btn.grid(row=3, column=1)

ktoc_btn = tk.Button(window, text="Kelvin to Celsius", command=KelvinToCelcius)
ktoc_btn.grid(row=2, column=2)

ktof_btn = tk.Button(window, text="Kelvin to Fahrenheit", command=KelvinToFahrenheit)
ktof_btn.grid(row=3, column=2)

result_label = tk.Label(window, text="", font=("Arial", 18))
result_label.grid(row=4, column=0)
# ==============================================================================================



# run the main window
window.mainloop()
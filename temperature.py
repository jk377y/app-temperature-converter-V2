import customtkinter as ctk # import the customtkinter module; used to create custom widgets and windows for standalone apps


#? main window
# ==============================================================================================
window = ctk.CTk()  # create the main window
window.title("Temperature Converter")  # set the title of the main window
window.geometry("300x450")  # set the size of the main window
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

label = ctk.CTkLabel(window, text="Enter temperature:", font=("Arial", 20))  # create a label widget; child of root
label.pack(pady=10)  # make the label visible; pack it into the main window (root)

entry = ctk.CTkEntry(window) # create an entry widget; child of root; this is the input box
entry.pack(pady=10)

ctof_btn = ctk.CTkButton(window, text="Celsius to Fahrenheit", command=CelciusToFahrenheit)
ctof_btn.pack(pady=10)

ctok_btn = ctk.CTkButton(window, text="Celsius to Kelvin", command=CelciusToKelvin)
ctok_btn.pack(pady=10)

ftoc_btn = ctk.CTkButton(window, text="Fahrenheit to Celsius", command=FahrenheitToCelcius)
ftoc_btn.pack(pady=10)

ftok_btn = ctk.CTkButton(window, text="Fahrenheit to Kelvin", command=FahrenheitToKelvin)
ftok_btn.pack(pady=10)

ktoc_btn = ctk.CTkButton(window, text="Kelvin to Celsius", command=KelvinToCelcius)
ktoc_btn.pack(pady=10)

ktof_btn = ctk.CTkButton(window, text="Kelvin to Fahrenheit", command=KelvinToFahrenheit)
ktof_btn.pack(pady=10)

result_label = ctk.CTkLabel(window, text="", font=("Arial", 24), text_color="yellow")
result_label.pack(pady=10)
# ==============================================================================================



# run the main window
window.mainloop()
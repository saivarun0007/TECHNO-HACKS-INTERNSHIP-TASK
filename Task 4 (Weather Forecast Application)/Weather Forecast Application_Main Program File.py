import requests
import tkinter as tk
from tkinter import ttk, messagebox

API_KEY = "e39aee2c595c82667c045c831b3cf93e"

def get_weather_data(city):
    city_with_country = f"{city},IN"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_with_country}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()
        country = data['sys']['country']
        city_name = data['name']

        result = (
            f"📍 Location: {city_name}, {country}\n"
            f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌥 Weather: {description}"
        )
        return result

    except requests.exceptions.HTTPError:
        return "❌ City not found! Please try again."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def show_weather():
    city = city_var.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please select a city!")
        return

    result = get_weather_data(city)
    output_label.config(text=result)

#  GUI Setup 
root = tk.Tk()
root.title("Techno Hacks Intern Weather App for INDIAN CITIES")
root.geometry("520x420")
root.configure(bg="#d1ecf1")

tk.Label(root, text="Select Indian City", font=("Arial", 14, "bold"), bg="#d1ecf1").pack(pady=10)

city_var = tk.StringVar()
city_options = [
    "Hyderabad", "Delhi", "Mumbai", "Bangalore", "Chennai",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow"
]

city_dropdown = ttk.Combobox(root, textvariable=city_var, values=city_options, state="readonly", width=25)
city_dropdown.pack(pady=5)
city_dropdown.current(0)

tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"),
          bg="#007bff", fg="white", command=show_weather).pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 11), bg="#d1ecf1", justify="left")
output_label.pack(pady=20)

root.mainloop()

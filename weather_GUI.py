from geopy.geocoders import Nominatim
import time
import tkinter as tk
import requests


# Weather API key
# 21e243ad884bfc5000aa8480a3a16e7e
# Set constants for cleanliness
geolocator = Nominatim(user_agent="weatherGodApp")
HEIGHT = 700
WIDTH = 600


def quit():
    global root
    root.quit()


def test(city):
    weather_key = '21e243ad884bfc5000aa8480a3a16e7e'
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    weather = requests.get(url, params=params).json()
    print(weather)
    print(weather['sys']['sunrise'])


def state_locator(coords):
    location = geolocator.reverse(coords, exactly_one=True)
    address = location.raw['address']
    state = address.get('state', '')
    return state


def format_weather(weather):
    name = weather['name']
    temp = weather['main']['temp']
    description = weather['weather'][0]['description']
    feels_like = weather['main']['feels_like']
    sunrise = weather['sys']['sunrise']
    sunset = weather['sys']['sunset']
    sunrise_time = time.strftime('%H:%M:%S', time.localtime(sunrise))
    sunset_time = time.strftime('%H:%M:%S', time.localtime(sunset))
    latitude = weather['coord']['lat']
    longitude = weather['coord']['lon']
    state = state_locator(str(latitude) + ", " + str(longitude))

    try:
        results = "State: %s \nCity: %s \nConditions: %s \nTemperature (F): %s \nFeels Like: %s \nSunrise: %s \nSunset: %s" % (
            state, name, description, temp, feels_like, sunrise_time, sunset_time)
    except KeyError:
        results = "Could not return results"

    return results


def get_weather(city):
    weather_key = '21e243ad884bfc5000aa8480a3a16e7e'
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    weather = requests.get(url, params=params).json()
    format_weather(weather)
    label['text'] = format_weather(weather)
    print(weather)


# Set the window
root = tk.Tk()
root.title("Weather God")

# Make Container for widgets
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='lightblue')
canvas.pack()


# lower_frame = tk.Frame(root, bg='red', bd=10)
# lower_frame.place(relx=.5, rely=.3, relwidth=.75, relheight=.7, anchor='n')

label = tk.Label(root, bg="white")
label.place(relx=.5, rely=.3, relwidth=.75, relheight=.5, anchor='n')

# rel... fills screen
frame = tk.Frame(root, bg="red", bd=5)
frame.place(relx=.5, rely=.1, relwidth=0.75,
            relheight=0.1, anchor='n')

entry = tk.Entry(frame)
entry.place(relwidth=.65, relheight=1)


# Button
button = tk.Button(frame, text="Ask Weather God", font=40,
                   command=lambda: get_weather(entry.get()))
button.place(relx=.7, relheight=1, relwidth=.3)


exit_button = tk.Button(root, text="Quit", font=50, command=lambda: quit())
exit_button.place(relx=.3, rely=.9, relheight=.05, relwidth=.4)

# lauching

root.mainloop()

'''
Main File for AAJ Weather App
Made by: Aadee Sawarkar,  Abdulla Dalwai,  Joshua Ferreria
Version: 1.4
Last Updated: 21,  Oct,  2021
'''

# from tkinter import Button,  Label,  Canvas,  Toplevel,  NW,  Frame, StringVar, Entry, PhotoImage, Tk
# Above line added for debugging purposes
from tkinter import *
from PIL import Image,  ImageTk
from tkinter import messagebox
import requests
import time
from forecast_days import forecast_five
import time as tm
from imgdisp import imagedisplay

# 5 day forecast
def forecast():
    if (loc_e.get() != ''):
        # degree
        deg = u"\N{DEGREE SIGN}"

        # window
        top = Toplevel()
        top.title('5 Day Forecast')
        top.iconbitmap('icon.ico')
        top.geometry('745x600')
        top.resizable(0,  0)

        # Getting Latitude and Longitude
        city = loc_e.get()
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=c8461f473291c2cfc27b573bfaa572b4'
        data = (requests.get(url)).json()

        if data['cod'] == '404':
            top.destroy()
            messagebox.showerror('Invalid City Name', 'City not Found')

        else:
            # Show image using label
            label2 = Label(top,  image=bgg)
            label2.place(x=0,  y=0)

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            # Getting Forecast information
            info = forecast_five(latitude,  longitude)

            # Header Label
            header = Label(top,  text='5 Day Forecast',  font=("Abadi MT Condensed Extra Bold",  20,  'bold'),  bg='#040641',  fg='white')
            header.grid(row=0,  column=0,  columnspan=5,  pady=10)

            # Day 1
            day1 = Frame(top,  bg="#adc2eb")
            day = 'day1'

            # image
            imagedisplay(info,  day)
            name = day+'.png'
            canvas1 = Canvas(day1,  bg="#adc2eb",  highlightthickness=0,  width=100,  height=100)
            canvas1.delete('all')
            img_day1 = ImageTk.PhotoImage(Image.open(name))
            canvas1.create_image(0,  0,  anchor=NW,  image=img_day1)
            canvas1.image = img_day1
            canvas1.grid(row=0,  column=0)

            # Abbreviated Name
            day1_label = Label(day1,  text=info['day1']['day'],  font=("Trebuchet MS",  14,  'bold'),  bg='#adc2eb')
            day1_label.grid(row=1,  column=0)

            # main
            main1_label = Label(day1,  text=info['day1']['main'],  font=("Trebuchet MS",  14,  'bold'),  bg='#adc2eb')
            main1_label.grid(row=2,  column=0)

            # day_temp
            day1_temp = 'Day Temperature: ' + str(info['day1']['day_temp']) + deg + 'C'
            day1_temp_label = Label(day1,  text=day1_temp,  font=("Trebuchet MS",  14,  'bold'),  bg='#adc2eb')
            day1_temp_label.grid(row=3,  column=0)

            # night temp
            night1_temp = 'Night Temperature: ' + str(info['day1']['night_temp']) + deg + 'C'
            night1_temp_label = Label(day1,  text=night1_temp,  font=("Trebuchet MS",  14,  'bold'),  bg='#adc2eb')
            night1_temp_label.grid(row=4,  column=0, padx=2)

            # rain
            rain_day1 = 'Precipitation: ' + info['day1']['pop']
            rain_day1_label = Label(day1,  text=rain_day1,  font=("Trebuchet MS",  14,  'bold'),  bg='#adc2eb')
            rain_day1_label.grid(row=5,  column=0)

            day1.grid(row=1, column=0,  padx=10)

            # Day 2
            day2 = Frame(top,  bg="#adc2eb")
            day = 'day2'

            # image
            imagedisplay(info,  day)
            name = day+'.png'
            canvas2 = Canvas(day2, bg="#adc2eb", highlightthickness=0, width=100,  height=100)
            canvas2.delete('all')
            img_day2 = ImageTk.PhotoImage(Image.open(name))
            canvas2.create_image(0,  0,  anchor=NW, image=img_day2)
            canvas2.image = img_day2
            canvas2.grid(row=0,  column=0)

            # Abbreviated Name
            day2_label = Label(day2,  text=info['day2']['day'],  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            day2_label.grid(row=1,  column=0)

            # main
            main2_label = Label(day2,  text=info['day2']['main'],  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            main2_label.grid(row=2,  column=0)

            # day_temp
            day2_temp = 'Day Temperature: ' + str(info['day2']['day_temp']) + deg + 'C'
            day2_temp_label = Label(day2,  text=day2_temp,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            day2_temp_label.grid(row=3,  column=0)

            # night temp
            night2_temp = 'Night Temperature: ' + str(info['day2']['night_temp']) + deg + 'C'
            night2_temp_label = Label(day2,  text=night2_temp,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            night2_temp_label.grid(row=4,  column=0, padx=2)

            # rain
            rain_day2 = 'Precipitation: ' + info['day2']['pop']
            rain_day2_label = Label(day2,  text=rain_day2,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            rain_day2_label.grid(row=5,  column=0)

            day2.grid(row=1, column=1,  padx=10)

            # Day 3
            day3 = Frame(top,  bg="#adc2eb")
            day = 'day3'

            # image
            imagedisplay(info,  day)
            name = day+'.png'
            canvas3 = Canvas(day3, bg="#adc2eb", highlightthickness=0,  width=100, height=100)
            canvas3.delete('all')
            img_day3 = ImageTk.PhotoImage(Image.open(name))
            canvas3.create_image(0,  0,  anchor=NW, image=img_day3)
            canvas3.image = img_day3
            canvas3.grid(row=0,  column=0)

            # Abbreviated Name
            day3_label = Label(day3,  text=info['day3']['day'],  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            day3_label.grid(row=1,  column=0)

            # main
            main3_label = Label(day3,  text=info['day3']['main'],  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            main3_label.grid(row=2,  column=0)

            # day_temp
            day3_temp = 'Day Temperature: ' + str(info['day3']['day_temp']) + deg + 'C'
            day3_temp_label = Label(day3,  text=day3_temp,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            day3_temp_label.grid(row=3,  column=0)

            # night temp
            night3_temp = 'Night Temperature: ' + str(info['day3']['night_temp']) + deg + 'C'
            night3_temp_label = Label(day3,  text=night3_temp,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            night3_temp_label.grid(row=4,  column=0, padx=2)

            # rain
            rain_day3 = 'Precipitation: ' + info['day3']['pop']
            rain_day3_label = Label(day3,  text=rain_day3,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            rain_day3_label.grid(row=5,  column=0)

            day3.grid(row=1, column=2,  padx=10)

            # Day 4
            day4 = Frame(top,  bg="#adc2eb")
            day = 'day4'

            # image
            imagedisplay(info,  day)
            name = day+'.png'
            canvas4 = Canvas(day4,  bg="#adc2eb", highlightthickness=0,  width=100,  height=100)
            canvas4.delete('all')
            img_day4 = ImageTk.PhotoImage(Image.open(name))
            canvas4.create_image(0,  0,  anchor=NW, image=img_day4)
            canvas4.image = img_day4
            canvas4.grid(row=0,  column=0)

            day4_label = Label(day4,  text=info['day4']['day'],  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            day4_label.grid(row=1,  column=0)

            # main
            main4_label = Label(day4,  text=info['day4']['main'],  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            main4_label.grid(row=2,  column=0)

            # day_temp
            day4_temp = 'Day Temperature: ' + str(info['day4']['day_temp']) + deg + 'C'
            day4_temp_label = Label(day4,  text=day4_temp,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            day4_temp_label.grid(row=3,  column=0)

            # night temp
            night4_temp = 'Night Temperature: ' + str(info['day4']['night_temp']) + deg + 'C'
            night4_temp_label = Label(day4,  text=night4_temp,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            night4_temp_label.grid(row=4,  column=0, padx=2)

            # rain
            rain_day4 = 'Precipitation: ' + info['day4']['pop']
            rain_day4_label = Label(day4,  text=rain_day4,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            rain_day4_label.grid(row=5,  column=0)

            day4.grid(row=2, column=0,  columnspan=2,  padx=10,  pady=20)

            # Day 5
            day5 = Frame(top,  bg="#adc2eb")
            day = 'day5'

            # image
            imagedisplay(info,  day)
            name = day+'.png'
            canvas5 = Canvas(day5,  bg="#adc2eb",  highlightthickness=0,  width=100,  height=100)
            canvas5.delete('all')
            img_day5 = ImageTk.PhotoImage(Image.open(name))
            canvas5.create_image(0,  0,  anchor=NW, image=img_day5)
            canvas5.image = img_day5
            canvas5.grid(row=0,  column=0)

            day5_label = Label(day5,  text=info['day5']['day'],  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            day5_label.grid(row=1,  column=0)

            # main
            main5_label = Label(day5,  text=info['day5']['main'],  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            main5_label.grid(row=2,  column=0)

            # day_temp
            day5_temp = 'Day Temperature: ' + str(info['day5']['day_temp']) + deg + 'C'
            day5_temp_label = Label(day5,  text=day5_temp,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            day5_temp_label.grid(row=3,  column=0)

            # night temp
            night5_temp = 'Night Temperature: ' + str(info['day5']['night_temp']) + deg + 'C'
            night5_temp_label = Label(day5,  text=night5_temp,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            night5_temp_label.grid(row=4,  column=0, padx=2)

            # rain
            rain_day5 = 'Precipitation: ' + info['day5']['pop']
            rain_day5_label = Label(day5,  text=rain_day5,  font=("Trebuchet MS", 14,  'bold'),  bg='#adc2eb')
            rain_day5_label.grid(row=5,  column=0)

            day5.grid(row=2, column=1,  columnspan=2,  padx=10,  pady=20)
    else:
        messagebox.showerror('Empty Field',  'Please Enter City Name')


# Current Weather
def getWeather():
    if (loc_e.get() != ''):
        city = loc_e.get()
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=c8461f473291c2cfc27b573bfaa572b4'
        data = (requests.get(url)).json()

        if data['cod'] == '404':
            messagebox.showerror('Invalid City Name', 'City not Found')

        else:
            timezones = data['timezone']

        # location text - City,  Country
        city_text = str(data['name'])
        state_text = str(data['sys']['country'])
        location_text_var.set(city_text + ',  ' + state_text)
        location_text.grid(row=0,  column=0,  padx=20,  pady=10)

        # icon
        icon_code = data['weather'][0]['icon']
        img_url = 'http://openweathermap.org/img/wn/' + icon_code + '@2x.png'
        img = requests.get(img_url)
        if img.status_code == 200:
            with open("icon.png", 'wb') as image_file:
                image_file.write(img.content)

        canvas.delete('all')
        image1 = Image.open("icon.png")
        test = ImageTk.PhotoImage(image1)
        canvas.create_image(0,  0,  anchor=NW, image=test)
        canvas.image = test
        canvas.grid(row=1, column=0)

        # weather details
        main_desc = data['weather'][0]['main']
        main = 'Description: ' + main_desc
        main_label['text'] = main
        main_label.grid(row=2,  column=0)

        # temperature
        deg = u"\N{DEGREE SIGN}"
        temp = int(data['main']['temp']-273.15)
        temp_feels_like = int(data['main']['feels_like']-273.15)
        temperature_label['text'] = ('Temperature: ' + str(temp) + deg + 'C'+'\tFeels Like: ' + str(temp_feels_like) + deg + 'C')
        temperature_label.grid(row=3, column=0)

        # Rain and humidity
        visibility = data['visibility']
        humidity = data['main']['humidity']
        visibility_humidity_label['text'] = ('Visibility: ' + str(visibility) + 'm' + '\t\tHumidity: ' + str(humidity) + '%')
        visibility_humidity_label.grid(row=4,  column=0)

        # Sunrise Sunset
        sunrise = time.strftime("%I:%M %p",  time.gmtime(data['sys']['sunrise'] + timezones))
        sunset = time.strftime("%I:%M %p",  time.gmtime(data['sys']['sunset'] + timezones))
        time_label['text'] = 'Sunrise at ' + sunrise + '\tSunset at ' + sunset
        time_label.grid(row=5, column=0, padx=3, pady=2)

        # time
        c_time = tm.strftime('%H:%M:%S')

        # file handling
        file = open("Weather_Logs.txt", 'a')
        file.write("\n" + str(c_time) + ":\nLocation : " + str(city_text) + ", " + str(state_text) + "\nWeather: " + str(main_desc) + "\nTemp: " + str(temp) + " degree C  \nVisibility: " + str(visibility) + "m \nHumidity: " + str(humidity) + "% \nSunrise: " + str(sunrise) + "\nSunset: " + str(sunset) + '\nDate: ' + str(time.strftime('%d/%m/%Y', time.localtime())) +"\n\n")
        file.close()
    else:
        messagebox.showerror('Empty Field', 'Please Enter City Name')


root = Tk()
bgg = PhotoImage(file="forecast1.png")
root.title('AAJ ka Weather')
root.geometry('500x600')
root.iconbitmap('icon.ico')
root.resizable(0, 0)

bg = PhotoImage(file="imgggg.png")

# Show image using label
label1 = Label(root,  image=bg)
label1.place(x=0, y=0)

# Weather App Title
title_label = Label(root,  text="Weather App",  font=("Abadi MT Condensed Extra Bold",  20,  'bold'),  bg="#040641",  fg="White")
title_label.pack(pady=15)

# Location Frame
mainframe = Frame(root,  bg="#adc2eb")
mainframe.pack(pady=10)

# Details Frame
displayframe = Frame(root,  bg="#adc2eb")
displayframe.pack(pady=20)

# Location Frame
loc = Label(mainframe,  text="Enter the location:",  font=("Trebuchet MS", ),  bg="#adc2eb",  fg="#000000")
loc_e = Entry(mainframe)
loc_e.config(highlightbackground="#234790",  highlightcolor="#234790",  highlightthickness=2)
weather_b = Button(mainframe,  text="AAJ ka Weather",  width=20,  font=("Abadi MT Condensed Extra Bold", ), command=getWeather,  bg="#234790",  fg="white")

# Get Weather Forecast
weather_forecast = Button(mainframe, text='5 Day Forecast', width=20, font=("Abadi MT Condensed Extra Bold", ), bg="#234790",  fg="white", command=forecast)

# Gridding
loc.grid(row=0,  column=0,  padx=15,  pady=20)
loc_e.grid(row=0,  column=1,  padx=15, pady=20)
weather_b.grid(row=1,  column=0,  padx=30,  pady=5,  columnspan=2)
weather_forecast.grid(row=2,  column=0,  padx=10,  pady=10,  columnspan=2)

# Details Frame
location_text_var = StringVar()
location_text_var.set('')
location_text = Label(displayframe,  textvariable=location_text_var,  font=("Trebuchet MS", ),  bg="#adc2eb",  fg="#000000")

canvas = Canvas(displayframe,  bg="#adc2eb",  highlightthickness=0,  width=100,  height=100)

main_label = Label(displayframe,  font=("Trebuchet MS", ),  bg="#adc2eb",  fg="#000000")
main_label['text'] = ''

temperature_label = Label(displayframe,  font=("Trebuchet MS", ),  bg="#adc2eb",  fg="#000000")
temperature_label['text'] = ''

visibility_humidity_label = Label(displayframe,  font=("Trebuchet MS", ),  bg="#adc2eb",  fg="#000000")
visibility_humidity_label['text'] = ''

time_label = Label(displayframe,  font=("Trebuchet MS", ),  bg="#adc2eb",  fg="#000000")
time_label['text'] = ''

root.mainloop()

import requests as re
from bs4 import BeautifulSoup as bs

class weather():
    def __init__(self, coords):
        self.name = coords.split(',(')[0]
        self.lat = float(coords.split('(')[1].split('&')[0])
        self.lon = float(coords.split('&')[1].split(')')[0])

    def get_weather(self):
        page = re.get(f'https://www.timeanddate.com/weather/@{self.lat},{self.lon}')
        soup = bs(page.content, 'html.parser')
        self.weather = soup.find_all("div", class_="bk-focus__qlook")
        self.weather2 = soup.find_all("div", class_="bk-focus__info")
        self.temp = str(self.weather).split('<div class="h2">')[1].split('<')[0]
        self.feels_like = str(self.weather).split('<p>Feels Like: ')[1].split('<')[0]
        self.high = str(self.weather).split('Forecast: ')[1].split(' /')[0]
        self.low = str(self.weather).split(' / ')[1].split(' °F')[0]
        self.visibility = str(self.weather2).split('Visibility: </th><td>')[1].split('<')[0]
        self.pressure = str(self.weather2).split('Pressure: </th><td>')[1].split('<')[0]
        self.humidity = str(self.weather2).split('Humidity: </th><td>')[1].split('<')[0]
        self.dew_point = str(self.weather2).split('Dew Point: </th><td>')[1].split('<')[0]
        self.dew = int(self.dew_point.split(' °F')[0])

    def get_sun_data(self):
        page = re.get(f'https://www.timeanddate.com/sun/@{self.lat},{self.lon}')
        soup = bs(page.content, 'html.parser')
        self.sun = soup.find_all("div", class_="bk-focus__info")
        self.altitude = str(self.sun).split('<td id="sunalt">')[1].split('<')[0]
        self.sunrise = str(self.sun).split('Sunrise Today: </th><td>')[1].split('<')[0]
        sunrise_alt = str(self.sun).split('Sunrise Today: </th><td>')[1]
        self.sunrise_alt = str(sunrise_alt).split('</span> ')[1].split('<')[0]
        self.sunset = str(self.sun).split('Sunset Today: </th><td>')[1].split('<')[0]
        sunset_alt = str(self.sun).split('Sunset Today: </th><td>')[1]
        self.sunset_alt = str(sunset_alt).split('</span> ')[1].split('<')[0]
        self.sunset_time = int(self.sunset.replace(':', '').split(' ')[0])

    def weather_report(self):
        import time as t

        self.get_weather()
        t.sleep(1)
        self.get_sun_data()

        import datetime as dt
        a = dt.datetime.now().strftime
        H, M, mod = int(a("%I")), a("%M"), a("%p")
        self.current_time = int(str(H) + M)

        close = False
        remaining = self.sunset_time - self.current_time
        if mod == 'PM' and remaining < 121:
            self.time_left = f"{remaining} minutes until sunset."
            close = True

        print(f"Current weather report for {self.name}")
        print(f"The sun rose at {self.sunrise}, {self.sunrise_alt}.")
        print(f"Temp: {self.temp}")
        print(f"Humidity: {self.humidity}")
        print(f"Feels Like: {self.feels_like}")
        if int(self.high) > 64: print(f"High: {self.high}, Low: {self.low}")
        else: print(f"Low: {self.low}, High: {self.high}")
        if self.visibility != 'N/A': print(f"Visibility: {self.visibility}")
        print(f"Pressure: {self.pressure}")
        if self.dew >= int(self.low): print(f"Dew Point: {self.dew_point}")
        print(f"Current Sun Altitude: {self.altitude}")
        print(f"The sun will set at {self.sunset}, {self.sunset_alt}.")
        if close: print(self.time_left)

jax_beach = "Jacksonville Beach, FL,(30.293868&-81.385696)" # https://www.latlong.net/
FL = weather(jax_beach)
FL.weather_report()

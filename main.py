import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import requests
from kivy.core.window import Window

class MainApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)

        self.city_input = TextInput(hint_text='Enter city name', multiline=False)
        self.country_input = TextInput(hint_text='Enter country code', multiline=False)
        self.fetch_btn = Button(text='Fetch Weather', on_press=self.get_weather)

        self.weather_label = Label(text='Weather Forecast will be displayed here',
                                   color=(0, 1, 0, 1),
                                   font_size=20, halign='center',
                                   valign='middle')

        layout.add_widget(self.city_input)
        layout.add_widget(self.country_input)
        layout.add_widget(self.fetch_btn)
        layout.add_widget(self.weather_label)

        return layout

    def get_weather(self, instance):
        city = self.city_input.text
        country = self.country_input.text
        api_key = os.environ.get('APIKEY')

        try:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'
            res = requests.get(url)
            data = res.json()
            weather_info = (f'Temperature: {data["main"]["temp"]} °C\n'
                            f'Humidity: {data["main"]["humidity"]} %\n'
                            f'Wind Speed: {data["wind"]["speed"]} m/s\n'
                            f'Description: {data["weather"][0]["description"]}\n')
            self.weather_label.text = weather_info

        except Exception as e:
            self.weather_label.text = f'Error: {e}'
            print(e)


if __name__ == '__main__':
    MainApp().run()

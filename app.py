from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result', methods=['POST'])
def res():
        import requests
        city_name = request.form.get('city')
        API_KEY = 'd8b296358b6b306e0f394bcfe12e7d68'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        url = base_url + "appid=" + API_KEY + "&q=" + city_name 

        try:

            response = requests.get(url).json()
            cname = response['name']
            temp = response["main"]["temp"]/10
            humidity = response["main"]["humidity"]
            wind_speed = response["wind"]["speed"]
            main = response['weather'][0]['main']
            return render_template('weather.html',temp=temp,cname=cname,wind_speed=wind_speed,humidity=humidity,main=main)
        except KeyError:
            return render_template('error_page.html', city_name=city_name)    

     

if __name__ == '__main__':
    app.run(debug=True)
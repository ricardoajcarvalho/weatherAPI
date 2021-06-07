from flask import Flask, render_template
import requests, os, segredos

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    query= "Lisbon,PT"
    unit = "metric"
    api_key = os.environ["weatherapp_API_pk_key"]
    url = "http://api.openweathermap.org/data/2.5/weather?q={0}&units={2}&appid={1}".format(query,api_key,unit)
    data = requests.get(url=url)
    print(data.json())
    return render_template("index.html", data=data.json())

if __name__ == '__main__':
    app.run(debug=True)
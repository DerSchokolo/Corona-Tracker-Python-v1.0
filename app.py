import json
import requests
from flask import Flask, url_for, request, render_template

# Flask config
app = Flask(__name__)


# Oberhavel
url_oberhavel = "https://api.corona-zahlen.org/districts"
resp_oberhavel = requests.get(url=url_oberhavel)
data_oberhavel = resp_oberhavel.json()

incidence_oberhavel = data_oberhavel["data"]["12065"]["weekIncidence"]

incidence_oberhavel = round(incidence_oberhavel, 1)


# Brandenburg
url_brandenburg = "https://api.corona-zahlen.org/states/BB"
resp_brandenburg = requests.get(url=url_brandenburg)
data_brandenburg = resp_brandenburg.json()

incidence_brandenburg = data_brandenburg["data"]["BB"]["weekIncidence"]

incidence_brandenburg = round(incidence_brandenburg, 1)

# Berlin
url_berlin = "https://api.corona-zahlen.org/states/BE"
resp_berlin = requests.get(url=url_berlin)
data_berlin = resp_berlin.json()

incidence_berlin = data_berlin["data"]["BE"]["weekIncidence"]

incidence_berlin = round(incidence_berlin, 1)


# Deutschland
url_deutschland = "https://api.corona-zahlen.org/germany"
resp_deutschland = requests.get(url=url_deutschland)
data_deutschland = resp_deutschland.json()

incidence_deutschland = data_deutschland["weekIncidence"]

incidence_deutschland = round(incidence_deutschland, 1)


# Deutschland Erste Impfungen
url_impfungen_erst = "https://api.corona-zahlen.org/vaccinations"
resp_impfungen_erst = requests.get(url=url_impfungen_erst)
data_impfungen_erst = resp_impfungen_erst.json()

impfungen_erst = data_impfungen_erst["data"]["vaccinated"]

impfungen_erst = impfungen_erst / 83020000
impfungen_erst = impfungen_erst * 100
impfungen_erst = round(impfungen_erst, 1)


# Deutschland Zweite Impfungen
url_impfungen_zweit = "https://api.corona-zahlen.org/vaccinations"
resp_impfungen_zweit = requests.get(url=url_impfungen_zweit)
data_impfungen_zweit = resp_impfungen_zweit.json()

impfungen_zweit = data_impfungen_zweit["data"]["secondVaccination"]["vaccinated"]

impfungen_zweit = impfungen_zweit / 83020000
impfungen_zweit = impfungen_zweit * 100
impfungen_zweit = round(impfungen_zweit, 1)


# Uhrzeit
url_time = "http://worldtimeapi.org/api/timezone/Europe/Berlin"
resp_time = requests.get(url=url_time)
data_time = resp_time.json()

data_time = data_time["datetime"]
data_time = data_time[0:19]


# Main Website
@app.route("/")
def home():
    return render_template("index.html", incidence_oberhavel=incidence_oberhavel, incidence_brandenburg=incidence_brandenburg, incidence_deutschland=incidence_deutschland, impfungen_erst=impfungen_erst, impfungen_zweit=impfungen_zweit)


# Help Website
@app.route("/help")
def info():
    return render_template("help.html", data_time=data_time)


# Starting Server
if __name__ == "__main__":
    app.run()

# Formating
#print(json.dumps(data_time, indent=4))
import json
import requests
from flask import Flask, url_for, request, render_template

#Flask config
app =  Flask(__name__)


#Oberhavel
url_oberhavel = "https://api.corona-zahlen.org/districts"
resp_oberhavel = requests.get(url=url_oberhavel)
data_oberhavel = resp_oberhavel.json()

incidence_oberhavel = data_oberhavel["data"]["12065"]["weekIncidence"]

incidence_oberhavel = round(incidence_oberhavel, 1)



#Brandenburg
url_brandenburg = "https://api.corona-zahlen.org/states/BB"
resp_brandenburg = requests.get(url=url_brandenburg)
data_brandenburg = resp_brandenburg.json()

incidence_brandenburg = data_brandenburg["data"]["BB"]["weekIncidence"]

incidence_brandenburg = round(incidence_brandenburg, 1)



#Deutschland
url_deutschland = "https://api.corona-zahlen.org/germany"
resp_deutschland = requests.get(url=url_deutschland)
data_deutschland = resp_deutschland.json()

incidence_deutschland = data_deutschland["weekIncidence"]

incidence_deutschland = round(incidence_deutschland, 1)



#Deutschland Impfungen
url_impfungen = "https://api.corona-zahlen.org/vaccinations"
resp_impfungen = requests.get(url=url_impfungen)
data_impfungen = resp_impfungen.json()

incidence_impfungen = data_impfungen["data"]["vaccinated"]

incidence_impfungen = incidence_impfungen / 83020000
incidence_impfungen = incidence_impfungen * 100
incidence_impfungen = round(incidence_impfungen, 1)



@app.route("/")
def home():
    return render_template("index.html", incidence_oberhavel=incidence_oberhavel, incidence_brandenburg=incidence_brandenburg, incidence_deutschland=incidence_deutschland, incidence_impfungen=incidence_impfungen)

@app.route("/help")
def info():
    return render_template("help.html")
    



if __name__ == "__main__":
    app.run()

#Formating
#print(json.dumps(data_impfungen, indent=4))
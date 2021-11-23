import json
import requests

###
# Old Code missing features
###

#Title
print("")
print("#########################################")
print("#########################################")
print("#########################################")
print("Corona Tracker v1.0")
print("Oberhavel, Brandenburg, Deutschland")
print("#########################################")
print("")





#Oberhavel
url_oberhavel = "https://api.corona-zahlen.org/districts"
resp_oberhavel = requests.get(url=url_oberhavel)
data_oberhavel = resp_oberhavel.json()

incidence_oberhavel = data_oberhavel["data"]["12065"]["weekIncidence"]

print("Incidence Oberhavel:")
incidence_oberhavel = round(incidence_oberhavel, 1)
print(incidence_oberhavel)
incidence_oberhavel = str(incidence_oberhavel)


#Break
print("")
print("#########################################")
print("")


#Brandenburg
url_brandenburg = "https://api.corona-zahlen.org/states/BB"
resp_brandenburg = requests.get(url=url_brandenburg)
data_brandenburg = resp_brandenburg.json()

incidence_brandenburg = data_brandenburg["data"]["BB"]["weekIncidence"]

print("Incidence Brandenburg:")
incidence_brandenburg = round(incidence_brandenburg, 1)
print(incidence_brandenburg)



#Break
print("")
print("#########################################")
print("")



#Deutschland
url_deutschland = "https://api.corona-zahlen.org/germany"
resp_deutschland = requests.get(url=url_deutschland)
data_deutschland = resp_deutschland.json()

incidence_deutschland = data_deutschland["weekIncidence"]

print("Incidence Deutschland:")
incidence_deutschland = round(incidence_deutschland, 1)
print(incidence_deutschland)


#Break
print("")

# Berlin
url_berlin = "https://api.corona-zahlen.org/states/BE"
resp_berlin = requests.get(url=url_berlin)
data_berlin = resp_berlin.json()

incidence_berlin = data_berlin["data"]["BE"]["weekIncidence"]

print("Incidence Berlin:")
incidence_berlin = round(incidence_berlin, 1)
print(incidence_berlin)


"""
#Deutschland Impfungen
url_impfungen = "https://api.corona-zahlen.org/vaccinations"
resp_impfungen = requests.get(url=url_impfungen)
data_impfungen = resp_impfungen.json()

incidence_impfungen = data_impfungen["data"]["vaccinated"]

print("Anzahl aller 1. Geimpften in Deutschland:")
incidence_impfungen = incidence_impfungen / 83020000
incidence_impfungen = incidence_impfungen * 100
incidence_impfungen = round(incidence_impfungen, 1)
incidence_impfungen = str(incidence_impfungen)

print(incidence_impfungen + "%")
"""


#End
print("")
print("#########################################")
print("#########################################")
print("#########################################")


#Formating
#print(json.dumps(data_impfungen, indent=4))
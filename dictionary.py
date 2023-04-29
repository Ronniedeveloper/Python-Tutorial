towns = {
    "MBL": "Mbale",
    "JIN": "Jinja",
    "MKN": "Mukono"
}
cities = {
    "Kampala": "KMP",
    "Mbarara": "MBR",
    "Mpigi": "MP"
}

cities["Alua"] = "ALU"
print("Short abbreviation" ,cities["Mpigi"])
print(cities["Kampala"] == "KMP")
for city,abbr in list(cities.items()):
    print(f"The abbbreviation for {city} is {abbr}")
for abbr,town in list(towns.items()):
    print(f"The abbreviation {abbr} is {town}")
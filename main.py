travelLog = [
    {
        "country": "France", "visit": 12, "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany", "visit": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def addNewCountry(countryVisited, timesVisited, citiesVisited):
    newCountry = {}
    newCountry["country"] = countryVisited
    newCountry["visits"] = timesVisited
    newCountry["cities"] = citiesVisited
    travelLog.append(newCountry)


addNewCountry("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travelLog)

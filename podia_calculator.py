import pandas as pd

#Zet de uren dat shows spelen samen in een lijst
#Haal uit hoe vaak de meest voorkomende uur voorkomt
#Dit is de hoeveelheid podia nodig

def podia_nodig(begin, eind):
    tijden = []
    for index in range(len(begin)):
        for tijd in range(begin[index],eind[index] + 1):
            tijden.append(tijd)

    distinct_tijden = list(set(tijden))

    max_tegelijk = 0
    for tijd in distinct_tijden:
        tegelijk = tijden.count(tijd)
        if tegelijk > max_tegelijk:
            max_tegelijk = tegelijk

    return max_tegelijk


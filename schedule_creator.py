import random

#Maak een dicitionary met alle podia als key en een list met de uren beschikbaar
#Maak een dictionary met alle podia als key en een leege list 
#Maak een while loop die stopt als alle shows zijn append of als het na 1000000 keer proberen niet lukt
#Per uur, filter df.Begintijd == uur, haal de podiums waar deze begintijd beschikbaar is, willekeurig append de rows in de gefilterd df naar een podium.
#Verwijder de show tijden van bij de beschikbare tijden van de podium
#Als er meer rows in df.Begintijd == uur dan podia beschikbaar zijn, begin dan opnieuw


def schedule_maker(df, begin, eind, hoeveelheid_stage):

    minimale_tijd = min(begin)
    maximale_tijd = max(eind)
    start_times = [numb for numb in range(minimale_tijd,maximale_tijd + 1)]

    bord_tijden = {}
    schedule = {}

    for numb in range(1,hoeveelheid_stage + 1):
        bord_tijden[f'stage_{numb}'] = start_times
        schedule[f'stage_{numb}'] = []


    errors = 0

    shows_appended = 0

    while shows_appended < len(df) and errors < 1000000:
        shows_appended = 0
        for time in start_times:
            df_temp = df[(df['Begintijd'] == time)]
            value_to_find = time

            keys_with_value = [key for key, value_list in bord_tijden.items() if value_to_find in value_list]

            if len(df_temp) > len(keys_with_value):
                print(f'Couldnt fit all shows {time}')
                errors += 1
                print('Combinatie niet mogelijk... begin opnieuw')
                break
            else:
                shuffled_list = random.sample(keys_with_value, len(df_temp))

                for index, key in enumerate(shuffled_list):
                    schedule[key].append(df_temp['show_tijd'].iloc[index])
                    print(f"{df_temp['show'].iloc[index]} bij {key} ingeroosterd")
                    shows_appended += 1
                    bord_tijden[key] = [item for item in bord_tijden[key] if item not in list(df_temp['tijden'].iloc[index])]

    return schedule, errors
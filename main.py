import pandas as pd
from datetime import datetime
import df_condities
import transformeer_df
import podia_calculator
import schedule_creator
import schedule_formatter



tijd_tussen_shows = None

#User geeft aan hoeveel tijd er minimaal tussen shows moet zijn op dezelfde podium
while tijd_tussen_shows == None:

    try:
        tijd_tussen_shows = int(input("\n\nHoeveel tijd (in hele uren) moet er minimaal tussen shows op dezelfde stage zijn?   "))
    except:
        print(f'\n\n\nOnjuiste input, vul een heel getal in (bijvoorbeeld: 0 \ 1 \ 2):')


formatted_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
begin_run_timestamp = formatted_timestamp

error_message = None
errors = 0
final_df = None

while error_message == None:

    #importeer input
    df = pd.read_csv('./input/input.csv', header=None)

    #valideer dat input klopt
    error_message = df_condities.valideer_input(df) 

    # Als het niet klopt, break uit de loop en vervolg naar eind conditie 1
    if error_message:
        break

    #Maak headers, maak nieuwe kolomm df.tijden die een lijst van range(begintijd, eindtijd + 1, 1) bevat. Maak een lijst van de begin- en eindtijden.
    df, begin, eind = transformeer_df.maak_kolommen(df, tijd_tussen_shows)

    #Calculeer hoeveel podia nodig is baseerd op hoeveel shows er max overlappen
    hoeveelheid_stage = podia_calculator.podia_nodig(begin, eind)


    #Maak een dicitonary met podium als key en lijst met shows als value.
    schedule, errors = schedule_creator.schedule_maker(df, begin, eind, hoeveelheid_stage)

    #Indien er na 1000000 pogingen nogsteeds niet alle shows heeft kunnen laten passen, voeg dan een podium toe
    if errors == 1000000:
        schedule, errors = schedule_creator.schedule_maker(df, begin, eind, hoeveelheid_stage + 1)
        #Om het naar eindconditie 2 waar te maken
        errors = 1000000

    #Maak van de json overzichtelijk outputs
    final_df_verticaal, final_df_horizontaal = schedule_formatter.schedule_formatter(schedule, df, begin, eind, tijd_tussen_shows)
    break


formatted_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
einde_run_timestamp = formatted_timestamp

#Eindconditie 1
#Geef aan wat fout ging en geef leege schema
if error_message != None:
    with open('./output/info.txt', 'w') as file:
        file.write(f'Begin code uitvoering:{begin_run_timestamp}\nBEinde code uitvoering:{einde_run_timestamp}\n {error_message}')
    pd.DataFrame(columns=['Error: zie info.txt bestand voor details']).to_csv('./output/schema_verticaal.csv', index=False)
    pd.DataFrame(columns=['Error: zie info.txt bestand voor details']).to_csv('./output/schema_horizontaal.csv', index=False)

#Eindconditie 2
#Geef aan wat fout ging en geef schema met extra podium
elif error_message == None and errors == 1000000:
    
    error_message = f'Helaas is het niet gelukt om de optredens met de minimale hoeveelheid podiums mogelijk in te plannen. Er is een extra podium toegevoegd.\n Voer de script opnieuw uit voor een nieuwe poging tot deze optimale planning te komen.\nPodia: {hoeveelheid_stage}\nMinimale tijd tussen shows: {tijd_tussen_shows} uur'
    with open('./output/info.txt', 'w') as file:
        file.write(f'Begin code uitvoering:{begin_run_timestamp}\nEinde code uitvoering:{einde_run_timestamp}\n {error_message}')
    final_df_verticaal.to_csv('./output/schema_verticaal.csv', index=False)
    final_df_horizontaal.to_csv('./output/schema_horizontaal.csv', index=False)

#Eindconditie 3
#Geef aan success en geef optimale schema
elif error_message == None and errors < 1000000:
    with open('./output/info.txt', 'w') as file:
        file.write(f'Begin code uitvoering:{begin_run_timestamp}\nEinde code uitvoering:{einde_run_timestamp}\nSchema succesful gemaakt met minimale podia.\nPodia: {hoeveelheid_stage}\nMinimale tijd tussen shows: {tijd_tussen_shows} uur')
    final_df_verticaal.to_csv('./output/schema_verticaal.csv', index=False)
    final_df_horizontaal.to_csv('./output/schema_horizontaal.csv', index=False)

#Eindconditie 4
#Geef aan onbekende fout en leege schema
else:
    error_message = f'Onbekende error'
    with open('./output/info.txt', 'w') as file:
        file.write(f'Begin code uitvoering:{begin_run_timestamp}\nEinde code uitvoering:{einde_run_timestamp}\n {error_message}')
    pd.DataFrame(columns=['Error: zie info.txt bestand voor details']).to_csv('./output/schema_verticaal.csv', index=False)
    pd.DataFrame(columns=['Error: zie info.txt bestand voor details']).to_csv('./output/schema_horizontaal.csv', index=False)

print('Zie output folder voor schema en bijhorende details')
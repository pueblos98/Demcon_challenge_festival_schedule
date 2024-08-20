import pandas as pd

#Deze functie 


def maak_kolommen(df, tijd_tussen_shows):
    headers = ['show', 'Begintijd', 'Eindtijd']

    df.columns = headers

    #Hier wordt tijd_tussen_shows opgeteld aan de eindtijd. Deze wordt later in de script afgetrokken
    df['Eindtijd'] = df['Eindtijd'] + tijd_tussen_shows

    #Maak list van de kolommen
    shows = df['show']
    begin = df['Begintijd']
    eind = df['Eindtijd']

    shows_time = [f"{shows[i]}: {begin[i]}_{eind[i]}" for i in range(len(begin))]
    df['show_tijd'] = shows_time
    

    
    tijden_list_df = [list(range(begin[i], eind[i] + 1)) for i in range(len(begin))]
    df['tijden'] = tijden_list_df

    return df, begin, eind
import pandas as pd

#Maakt een dataframe met time als header en range(min(begintijd), max(eindtijd) + 1) als values
#Maakt van elke podia in schedule een dataframe met een aparte row voor elke uur dat een show speelt
#Dataframe van de eerste punt wordt geleft joined door de dataframe van de tweede punt. Zo heb je elke speeltijd van de festival en zijn de dataframes per podia even lang.
#Append deze dataframes horizontaal, nu heb je de *verticale* output
#Volgende stappend doet een transpose om ook een *verticale* output te krijgen

def schedule_formatter(schedule, df, begin, eind, tijd_tussen_shows):
    start_times = [numb for numb in range(min(begin),max(eind) - tijd_tussen_shows + 1)]   
    start_times_df = pd.DataFrame(start_times, columns=['time'])

    

    if tijd_tussen_shows > 0:
        df['tijden'] = df['tijden'].apply(lambda x: x[:-1 * tijd_tussen_shows])

    df_written = df.explode('tijden')

    dfs = []

    for stage in list(schedule.keys()):
        df_fix = pd.DataFrame(schedule[stage], columns=['show_tijd'])

        merged_temp = pd.merge(df_fix, df_written, on='show_tijd', how='left')
        merged_temp.rename(columns={'show': stage}, inplace=True)
        merged_temp = pd.merge(start_times_df, merged_temp, left_on='time', right_on='tijden', how='left')[['time', stage]]

        dfs.append(merged_temp)

    final_df = pd.concat(dfs, axis=1)

    final_df_verticaal = final_df.loc[:,~final_df.columns.duplicated()]


    df = final_df_verticaal
    melted_df = df.melt(id_vars=['time'], var_name='stage', value_name='Stages\Time')


    melted_df = melted_df.dropna(subset=['Stages\Time'])

 
    final_df_horizontaal = melted_df.pivot(index='stage', columns='time', values='Stages\Time')


    final_df_horizontaal = final_df_horizontaal.reset_index()


    final_df_horizontaal.columns.name = None
    final_df_horizontaal.columns = ['Stages\Time'] + list(final_df_horizontaal.columns[1:])

    final_df_verticaal = final_df_verticaal.rename(columns={'time': 'Time\Stages'})

    return final_df_verticaal ,final_df_horizontaal
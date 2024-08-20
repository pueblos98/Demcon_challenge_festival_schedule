import pandas as pd


#Deze functie valideerd dat de input voldoet aan de input voorwaardes. Als die dit niet niet doet dan geeft het een ereor messsage mee

def valideer_input(df):


    if df.shape[1] < 3:
        error_message = 'Error: Input heeft te weinig kolommen. Input moet 3 kolommen zijn.'
        return error_message 


    elif df.shape[1] > 3:
        error_message = 'Error: Input heeft te veel kolommen. Input moet 3 kolommen zijn.'
        return error_message 

    if not df[1].apply(lambda x: isinstance(x, int)).all() or not df[2].apply(lambda x: isinstance(x, int)).all():
        error_message = 'Error: Begintijd en eindtijd moeten alleen gehele getallen bevatten.'
        return error_message
    

    if not (df[1] < df[2]).all():
        conditie = df[1] < df[2]
        voldoet_niet = df[~conditie].values
        error_message = f'Error: Voor de hieronder benoemde shows zijn de begintijden na de eindtijden:\n {voldoet_niet}\nDit voldoet niet aan de inputcondities van het script'
        return error_message



    return None
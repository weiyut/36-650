


import pandas as pd
import numpy as np
import psycopg2
import pandas.io.sql as sqlio
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="***", #change to your own password 
                        database="postgres"
                       )
sql = "SELECT * FROM fifa.players_20"

fifa = sqlio.read_sql(sql, conn)

conn.close()

def club_with_most_players(z = 10):
    if z < 5:
        """Reminder: Since z must >=5, if z is smaller than 5, it returns a value error message.
           Group the data first by club and count the numbers of players in each club, then return the top z clubs with largest number of players in the dataset. """
        print('The number of clubs must be at least 5')
    else: 
         
        return pd.DataFrame(fifa.groupby('club')['overall'].count().sort_values(ascending = False))               .rename(columns = {'overall':'number of players'}).head(z)

    
def test_most_players_happy_path():
    assert len(club_with_most_players()) == 10, "When there is no input, the dataframe should return 5 values"
    assert len(club_with_most_players(100)) == 100, "The length of the dataframe should be same as the input"
    assert isinstance(club_with_most_players(),pd.DataFrame), "The type of output should be Pandas Dataframe"
    
def test_most_players_sad_path():
    assert len(club_with_most_players(1990000)) == 1990000, "Length of the data should be the same as the input." 

    


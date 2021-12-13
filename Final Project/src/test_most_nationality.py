


import pandas as pd
import numpy as np
import psycopg2
import pandas.io.sql as sqlio
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="***", 
                        database="postgres"
                       )
sql = "SELECT * FROM fifa.players_20"

fifa = sqlio.read_sql(sql, conn)

conn.close()

def most_popular_nationality(n = 5):
    """Group the data first by nationality and count the numbers of players in each club, then return the top n nationality with largest number of players in the dataset. """
    return pd.DataFrame(fifa.groupby('nationality')['club'].count().sort_values(ascending = False)).               rename(columns = {'club': 'number of players'}).head(n)

def test_most_players_happy_path():
    assert len(most_popular_nationality()) == 5, "When there is no input, the dataframe should return 5 values"
    assert len(most_popular_nationality(100)) == 100, "The length of the dataframe should be same as the input"
    assert isinstance(most_popular_nationality(),pd.DataFrame), "The type of output should be Pandas Dataframe"
    
def test_most_players_sad_path():
    assert len(most_popular_nationality(1990000)) == 1990000, "Length of the data should be the same as the input." 

    







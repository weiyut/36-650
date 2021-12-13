

import pandas as pd
import numpy as np
import psycopg2
import pandas.io.sql as sqlio
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="***",  #change password to your own 
                        database="postgres"
                       )
sql = "SELECT * FROM fifa.players_20"

fifa = sqlio.read_sql(sql, conn)

conn.close()

def club_with_contract_ending_players(y = 5, year = 2021):
    """Filter the data to the players with contracts ending in year(default =  2021), 
       group the data by clubs, and count the number of data in each group, 
       and print out the top y clubs with the largest number of players with contracts ending in that year."""  
    return pd.DataFrame(fifa[fifa['contract_valid_until'] == year].groupby('club')['overall']                        .count().sort_values(ascending = False))                        .rename(columns = {'overall':'number of players'}).head(y)

def test_contract_happy_path():
    assert len(club_with_contract_ending_players()) == 5, "When there is no input, the dataframe should return 5 values"
    assert len(club_with_contract_ending_players(100)) == 100, "The length of the dataframe should be same as the input"
    assert isinstance(club_with_contract_ending_players(),pd.DataFrame), "The type of output should be Pandas Dataframe"
    
def test_contract_sad_path():
    assert len(club_with_contract_ending_players(1990000)) == 1990000, "Length of the data should be the same as the input." 

    


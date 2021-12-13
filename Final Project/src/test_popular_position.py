


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


def most_popular_position(n = 1,column = "nation_position"):
    """ Reminder: we only want to know the most popular position in nation_position and team_position,
        so if the input isn't either of these two categories, we return an error.
        Also, since SUB and RES are not the actual positions in soccer, we filter them out.
        
        Group the data by our input column, and sort the value to get the top n popular positions."""
    if column != 'nation_position' and column != 'team_position':
        print('Input must be nation_position or team_position')
    else:
         
        clean = fifa[(fifa[column] !="SUB") & (fifa[column] !="RES")]
        
        return pd.DataFrame(clean.groupby(column)['club'].count().sort_values(ascending = False)).               rename(columns = {'club': 'number of players'}).head(n)
    

def test_most_players_happy_path():
    assert len(most_popular_position()) == 1, "When there is no input, the dataframe should return 5 values"
    assert len(most_popular_position(25)) == 25, "The length of the dataframe should be same as the input"
    assert isinstance(most_popular_position(),pd.DataFrame), "The type of output should be Pandas Dataframe"
    
def test_most_players_sad_path():
    assert len(most_popular_position(1990000)) == 1990000, "Length of the data should be the same as the input." 

    


    


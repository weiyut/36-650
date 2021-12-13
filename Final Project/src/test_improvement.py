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

def highest_improvement(x = 10):
    """Step 1: Calculate the average skillset for each player
       Step 2: Calculate the difference between the each player's average skillset value the average of all players' average skillsets
       Step 3: Obtained x players with highest differences among the data"""
   
    fifa.loc[:,'avg_skill_set'] = fifa.loc[:,'attacking_crossing':'goalkeeping_positioning'].mean(axis = 1)
    
    fifa.loc[:, 'improvement'] = fifa.loc[:,'avg_skill_set'] - fifa.loc[:,'avg_skill_set'].mean()
    
    return fifa[['short_name','improvement']].sort_values('improvement',ascending = False).head(x)

def test_improvement_happy_path():
    assert len(highest_improvement()) == 10, "When there is no input, the dataframe should return 10 values."
    assert len(highest_improvement(100)) == 100, "The length of the dataframe should be same as the input."
    assert isinstance(highest_improvement(),pd.DataFrame), "The type of output should be Pandas Dataframe."
    
def test_improvement_sad_path():
    assert len(highest_improvement(1990000)) == 1990000, "Length of the data should be the same as the input." 

    


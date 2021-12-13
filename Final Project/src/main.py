import pandas as pd
import numpy as np

## Connect to SQL server
import psycopg2
import pandas.io.sql as sqlio
conn = psycopg2.connect(host="localhost", # Change the sql server information to your own server. 
                        user="postgres", 
                        password="***",  
                        database="postgres"
                       )
sql = "SELECT * FROM fifa.players_20"

fifa = sqlio.read_sql(sql, conn)

conn.close()

# Task II & III

## 1. List the x players who achieved highest improvement across all skillsets
def highest_improvement(x = 10):
    """Step 1: Calculate the average skillset for each player
       Step 2: Calculate the difference between the each player's average skillset value the average of all players' average skillsets
       Step 3: Obtained x players with highest differences among the data"""
   
    fifa.loc[:,'avg_skill_set'] = fifa.loc[:,'attacking_crossing':'goalkeeping_positioning'].mean(axis = 1)
    
    fifa.loc[:, 'improvement'] = fifa.loc[:,'avg_skill_set'] - fifa.loc[:,'avg_skill_set'].mean()
   
    return fifa[['short_name','improvement']].sort_values('improvement',ascending = False).head(x)

## when x = 10
print(highest_improvement())

## 2. What are the y clubs that have largest number of players with contracts ending in 2021?

def club_with_contract_ending_players(y = 5, year = 2021):
    """Filter the data to the players with contracts ending in year(default =  2021), 
       group the data by clubs, and count the number of data in each group, 
       and print out the top y clubs with the largest number of players with contracts ending in that year."""   
    return pd.DataFrame(fifa[fifa['contract_valid_until'] == year].groupby('club')['overall'].count().sort_values(ascending = False)).rename(columns = {'overall':'number of players'}).head(y)

## when y = 5, year = 2021  
print(club_with_contract_ending_players())


## 3. List the z clubs with largest number of players in the dataset where z >= 5

def club_with_most_players(z = 10):
    """Reminder: Since z must >=5, if z is smaller than 5, it returns a value error message.
       Group the data first by club and count the numbers of players in each club, then return the top z clubs with largest number of players in the dataset. """
        
    if z < 5:
        ## Since z must >=5, if z is smaller than 5, return a value error message.
        raise ValueError('The number of clubs must be at least 5')
    else: 
        ## Group the data first by club and count the numbers of players in each club, 
        ## then return the top z clubs with largest number of players in the dataset.
        return pd.DataFrame(fifa.groupby('club')['overall'].count().sort_values(ascending = False)).rename(columns = {'overall':'number of players'}).head(z)
    
## When z = 10
print(club_with_most_players())

## 4. What is the most popular nation_position and team_position in the dataset? (list the most popular for each)

def most_popular_position(n = 1,column = "nation_position"):
    """ Reminder: we only want to know the most popular position in nation_position and team_position,
        so if the input isn't either of these two categories, we return an error.
        Also, since SUB and RES are not the actual positions in soccer, we filter them out.
        
        Group the data by our input column, and sort the value to get the top n popular positions."""
    if column != 'nation_position' and column != 'team_position':
        print('Input must be nation_position or team_position')
    else:
         
        clean = fifa[(fifa[column] !="SUB") & (fifa[column] !="RES")]## Group the data by our input column, and sort the value to get the top n (default = 1) popular positions. 
        return pd.DataFrame(clean.groupby(column)['club'].count().sort_values(ascending = False)).rename(columns = {'club': 'number of players'}).head(n)

## nation_position
print(most_popular_position('nation_position'))

## team_position
print(most_popular_position('team_position'))


## 5. What is the most popular nationality for the players in the dataset?

def most_popular_nationality(n = 1):
    """Group the data first by nationality and count the numbers of players in each club, then return the top n nationality with largest number of players in the dataset. """
    
    return pd.DataFrame(fifa.groupby('nationality')['club'].count().sort_values(ascending = False)).rename(columns = {'club': 'number of players'}).head(n)
  
  
## most popular nationality for the players
print(most_popular_nationality())






# Task V: Seaborn

## 1. Develop Python function that graphically displays the 10 players who have achieved the highest improvement across all skillsets

def plot_players_with_highest_improvement(n):
    fig, ax = plt.subplots(figsize=(n,10))
    sns.barplot(x = 'short_name' ,y = 'improvement', data = highest_improvement(n), ax = ax)
    ax.set_ylim(highest_improvement(n).improvement.min() - 0.5,highest_improvement(n).improvement.max()+0.5)
    ax.set_title('Top ' + str(n)+' players who have achieved the highest improvement across all skillsets')
    ax.set_xlabel('Player')
    ax.set_ylabel('Improvement')
    ax.set_xticklabels(highest_improvement(n).short_name, rotation = 40)
    plt.show()
    
## 10 players who have achieved the highest improvement across all skillsets.
plot_players_with_highest_improvement(10)


## 2. Develop Python function that graphically displays the 5 players with highest value (value_eur).

def plot_players_with_highest_value(n):
    fifa['value_eur(M)'] = fifa['value_eur'].div(10**6)
    fig, ax = plt.subplots(figsize=(n,10))
    sns.barplot(x = 'short_name' ,y = 'value_eur(M)', data = fifa.sort_values(by = 'value_eur(M)', ascending = False).head(n)[['short_name','value_eur(M)']], ax = ax)
    ax.set_ylim(fifa.sort_values(by = 'value_eur(M)', ascending = False).head(n)['value_eur(M)'].min() - 10,fifa.sort_values(by = 'value_eur(M)', ascending = False).head(n)['value_eur(M)'].max()+1.5)
    ax.set_title('Top ' + str(n)+' players with highest value')
    ax.set_xlabel('Player')
    ax.set_ylabel('Value(in millions of Euros)')
    ax.set_xticklabels(fifa.sort_values(by = 'value_eur(M)', ascending = False).head(n).short_name, rotation = 40)
    plt.show()
 
## 5 players with highest value
plot_players_with_highest_value(5)


## 3. Develop Python function that graphically displays the 10 players with the largest number of player_traits. 
##    If there are more than 10 players, e.g. (players 9, 10, and 11 include same number of player traits), include all of them in the visualization.

for i in range(fifa.shape[0]):
    if fifa['player_traits'][i] is not None:
        fifa.loc[i,'nums_player_traits'] = len(fifa['player_traits'][i].split(','))
    else:
        fifa.loc[i,'nums_player_traits'] = 0
        
def plot_players_with_largest_number_traits(n):
      
    tmp = fifa.sort_values(by = 'nums_player_traits', ascending = False)
    i = n
    while tmp['nums_player_traits'].head(i).sort_values().head(1).values == tmp['nums_player_traits'].head(i+1).sort_values().head(1).values:
        i+=1

    fig, ax = plt.subplots(figsize=(10,i/2))
    sns.barplot(y = 'short_name' ,x = 'nums_player_traits', data = fifa.sort_values(by = 'nums_player_traits', ascending = False).head(i)[['short_name','nums_player_traits']], orient = 'h', ax = ax)
    ax.set_xlim(fifa.sort_values(by = 'nums_player_traits', ascending = False).head(i)['nums_player_traits'].min() - 2,fifa.sort_values(by = 'nums_player_traits', ascending = False).head(i)['nums_player_traits'].max()+1)
    ax.set_title('Top ' + str(n)+ ' players with the largest number of player traits(including tied)')
    ax.set_ylabel('Player')
    ax.set_xlabel('Number of player traits')
    ax.set_yticklabels(fifa.sort_values(by = 'nums_player_traits', ascending = False).head(i).short_name)
    plt.show()
 
## 10 players with the largest number of player_traits(including tied)
plot_players_with_largest_number_traits(10)





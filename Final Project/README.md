
 
# Project Repository

Walkthrough video link: https://www.youtube.com/watch?v=xsGXSDU3p8E

## Step by step instruction
1. Change the directory /copy command /Users/Downloads/players_20.csv of the project_database.sql (in src folder) to the place you store your player_20.csv file, where you can download it in data file of this repository.  
2. Launch psql shell and run the project_database.sql file. 
3. Change the the sql server information to your own sql server information in main.py, where you can find the file in src folder of this repostiory. 
4. Run the main.py file with user-input arguments. 

## Task-I: Database
### Database Constraints
1. age, height_cm, and weight_kg must > 0 

### Table infrastructure
![table infrastructure](https://github.com/36-650-Fall-2021/course-project-weiyut/blob/master/docs/table%20infrastructure%20?raw=true)

## Task-II/Task-III: Python Functions/Documentation
### 1. List the x players who achieved highest improvement across all skillsets
Step 1: Calculate the average skillset for each player.

Step 2: Calculate the difference between the each player's average skillset value the average of all players' average skillsets.

Step 3: Obtained x players with highest differences among the data.

<img width="242" alt="Screen Shot 2021-10-31 at 4 22 59 PM" src="https://user-images.githubusercontent.com/89482675/139600061-a30d5081-3ae6-4d1f-baa5-5a690c3e0219.png">

### 2. What are the y clubs that have largest number of players with contracts ending in 2021?
Filter the data to the players with contracts ending in year(default =  2021), group the data by clubs, and count the number of data in each group, and print out the top y clubs with the largest number of players with contracts ending in that year.

<img width="337" alt="Screen Shot 2021-10-31 at 4 26 28 PM" src="https://user-images.githubusercontent.com/89482675/139600196-8f685b9c-4f91-4ad4-b9d7-c2404f67e8fa.png">

### 3. List the z clubs with largest number of players in the dataset where z >= 5
Reminder: Since z must >=5, if z is smaller than 5, it returns a value error message.

Group the data first by club and count the numbers of players in each club, then return the top z clubs with largest number of players in the dataset.
        
<img width="314" alt="Screen Shot 2021-10-31 at 4 32 46 PM" src="https://user-images.githubusercontent.com/89482675/139600312-a7877728-4bc7-40e4-a70f-db1b37875ed8.png">

### 4. What is the most popular nation_position and team_position in the dataset? (list the most popular for each)
Reminder: we only want to know the most popular position in nation_position and team_position,so if the input isn't either of these two categories, we return an error.

Also, since SUB and RES are not the actual positions in soccer, we filter them out.

<img width="372" alt="Screen Shot 2021-10-31 at 4 35 17 PM" src="https://user-images.githubusercontent.com/89482675/139600364-b4da5aa4-b89e-4ccc-b9f8-f831cfb33eb3.png">

### 5. What is the most popular nationality for the players in the dataset?
Group the data first by nationality and count the numbers of players in each club, then return the top n nationality with largest number of players in the dataset. 
    
<img width="336" alt="Screen Shot 2021-10-31 at 4 36 45 PM" src="https://user-images.githubusercontent.com/89482675/139600412-289a2597-c2b6-4f4f-ad0c-b0d005b39825.png">




## Task-IV: Unit-Testing
### 1. List the x players who achieved highest improvement across all skillsets
<img width="952" alt="Screen Shot 2021-11-20 at 4 14 15 PM" src="https://user-images.githubusercontent.com/89482675/142741145-21abe830-d4fc-47db-a2b3-4099f3d14c80.png">

### 2. What are the y clubs that have largest number of players with contracts ending in 2021?
<img width="1383" alt="Screen Shot 2021-11-20 at 4 16 26 PM" src="https://user-images.githubusercontent.com/89482675/142741176-b63acc83-b21d-4ae5-a3eb-c93cc62f04ab.png">

### 3. List the z clubs with largest number of players in the dataset where z >= 5
<img width="1397" alt="Screen Shot 2021-11-20 at 4 18 44 PM" src="https://user-images.githubusercontent.com/89482675/142741230-6e422f25-10c7-4a40-985f-88d9ef93cb5a.png">

### 4. What is the most popular nation_position and team_position in the dataset? (list the most popular for each)
<img width="1179" alt="Screen Shot 2021-11-20 at 4 20 01 PM" src="https://user-images.githubusercontent.com/89482675/142741256-c611697c-b7bf-48f8-866a-78f9f966cb4b.png">

### 5. What is the most popular nationality for the players in the dataset?
<img width="1364" alt="Screen Shot 2021-11-20 at 4 21 02 PM" src="https://user-images.githubusercontent.com/89482675/142741276-f034e002-ddbe-41c6-b3a6-e1a4bcae73b6.png">



# Task V: Seaborn graphs
### 1. 10 players who have achieved the highest improvement across all skillsets. 
![1](https://user-images.githubusercontent.com/89482675/142741355-3ba8ebd9-d53e-4ee8-9ebe-5bff3832d5dc.png)

### 2. 5 players with highest value
![image](https://user-images.githubusercontent.com/89482675/142741392-b6c2c872-dfb0-4fd0-b5b7-241638c21042.png)


### 3. 10 players with the largest number of player_traits(including tied)
![image](https://user-images.githubusercontent.com/89482675/142741399-ca37d87e-2b79-4fe7-89b7-9afac96e98a1.png)










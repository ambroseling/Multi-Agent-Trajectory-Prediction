
import numpy 
import pickle
import pandas as pd
import os
import time
# game_name = '0021500009.pkl'

# game = pd.read_pickle('/Users/ambroseling/Desktop/raptors/data/'+game_name)
# print(game.keys())
# print(game['events'][0].keys())
# print(game['events'][0]['moments'][0].keys())

data_path = '/Users/ambroseling/Desktop/DeepHoopers/Raptors/data'
data_list = []

start = time.time()
for dir in os.listdir(data_path):
    game = pd.read_pickle(os.path.join(data_path,dir))
    game_id = game['gameid']
    for i in range(len(game['events'])):
        home_id = game['events'][i]['home']['teamid']
        visitor_id = game['events'][i]['visitor']['teamid']
        for j in range(len(game['events'][i]['moments'])):
            moment = game['events'][i]['moments'][j]
            data =  {
                'Game_ID':game_id,
                'Event_ID':i,
                'Moment_ID':j,
                'Moment_Time':moment[1],
                'Ball_X':moment[5][0][-3],
                'Ball_Y':moment[5][0][-2],
                'Ball_Z':moment[5][0][-1],
            }
            for k,player in enumerate(moment[5][1:]):
                team_side = 'H' if player[0]==home_id else 'V'
                data[f'Player_{team_side}_{k%5}_X'] = player[2] 
                data[f'Player_{team_side}_{k%5}_Y'] = player[2] 
            data_list.append(data)
    break
stop = time.time()
pd.set_option('display.max_columns', None)
df = pd.DataFrame(data_list)
print(df.head())
print('Time to load 1 game: ',stop-start, '. We have ',len(os.listdir(data_path)) , 'games so it would take ',len(os.listdir(data_path))*(stop-start)/60., ' minutes ',)
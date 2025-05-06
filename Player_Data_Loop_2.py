# This script was written after the raw data from the API was examined.
# Before compiling the data into tables, I wanted to create an additional data set with 'counting stats' only
from sportsipy.nba.roster import Player
import pandas as pd
from datetime import datetime
startTime = datetime.now()


active_player_list = ['playerid1','playerid2','playerid3']
player_name_file_list = ['FirstName1_LastName1_','FirstName1_LastName2_','FirstName3_LastName3_']



x_ = 0

while x_ <= (len(active_player_list)):
    
    next_file = player_name_file_list[x_]
    # we used the pandas 
    df = pd.read_csv( "'" + next_file + "'" + '.csv')
    raw_df = df[["player_id","season","games_played","minutes_played","points","total_rebounds","assists","steals","blocks","turnovers","field_goals","field_goal_attempts","two_pointers","two_point_attempts","three_pointers","three_point_attempts","free_throws","free_throw_attempts","offensive_rebounds","defensive_rebounds","personal_fouls"]]

 
#_________________________________________________   

    # '_rs_' here just refers to the fact that this data set is 'raw stats'
    raw_df.to_csv('_rs_' + str(player_name_file_list[x_]) + ".csv")
    x_ = x_ + 1

print(datetime.now() - startTime)
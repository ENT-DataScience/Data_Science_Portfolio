from sportsipy.nba.roster import Player
#raw stats from -source written to individual csv files


active_player_list = ['playerid1','playerid2','playerid3']
player_name_file_list = ['FirstName1_LastName1_','FirstName2_LastName2_','FirstName3_LastName3_']


x_ = 0

while x_ <= len(player_name_file_list):
    player_selection = str(active_player_list[x_])
    current_player = Player(player_selection)  
    


    print(player_selection) 


##___________________________________________________
    df = current_player.dataframe
    df.to_csv("'" + str(player_name_file_list[x_]) + "'.csv")
    x_ = x_ + 1


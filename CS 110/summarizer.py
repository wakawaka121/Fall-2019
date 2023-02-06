####
#### Author: Derek Tominaga
#### Description: Read a text file
#### and extract, team, player, and points scored.
#### print summary of, Winning team, team scores, #of
#### players that scored, player who scored first and last
####

def player_list(line_info,players):
    '''
    This function takes two parameters
    line_info = list of [team, player, points]
    players = list of players who scored in the game
    adds player to list if not in player list
    '''
    if line_info[1] not in players:
        players.append(line_info[1])
def get_team_index(line_info, teams, points_made):
    '''
    This fnction takes three parameters
    line_info = list of [team, player, points]
    teams = list of teams, if team not in teams list
    add to list.
    points_made = list of team score with indexs corrosponding
    to teams list
    returns the team index
    '''
    if line_info[0] not in teams:
        teams.append(line_info[0])
        points_made.append(0)
    return teams.index(line_info[0])

def main():
    file_name = input("enter gamelog file name: \n")
    game_stats = open(file_name, "r")
    string_list = game_stats.readlines()
    teams = []
    players = []
    points_made = []
    for line in string_list:
        line_info = line.split(" ")
        team_index = get_team_index(line_info, teams, points_made)
        points_made[team_index] += int(line_info[2])
        player_list(line_info, players)
        last_player_scored = line_info[1]
    game_stats.close()
    if points_made[0] > points_made[1]:
        winner = teams[0]
    else:
        winner = teams[1]
    first_team_score = teams[0] + " scored " + str(points_made[0]) + " points."
    second_team_score = teams[1] + " scored " + str(points_made[1]) + " points."
    print(winner + " won!")
    print(first_team_score)
    print(second_team_score)
    print(str(len(players)) + " players scored.")
    print(players[0] +  " scored first.")
    print(last_player_scored + " scored last.")
main()
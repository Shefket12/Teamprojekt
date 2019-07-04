import csv

def writeTeamIDs():
    Teams = {79: '1.FC Nürnberg', 81: 'Mainz 05', 6: 'Levverkusen', 7: 'BVB', 87: 'BMG', 
        91: 'Frankfurt', 95: 'Augsburg', 40: 'FC Bayern', 9: 'FC Schalke', 185: 'Düsseldorf', 
        55: 'Hannover 96', 54: 'Hertha BSC', 1635: 'RB Leipzig', 112: 'Freiburg', 123: 'TSG', 
        16: 'Stuttgart', 131: 'Wolfsburg', 134: 'Bremen'}
    download_dir = "TeamIDs.csv"
    csv = open(download_dir, 'w')
    for i in Teams:
        wholeTeam = str(i) + ',' + Teams[i] + '\n'
        csv.write(wholeTeam)
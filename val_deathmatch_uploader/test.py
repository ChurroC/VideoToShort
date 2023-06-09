import os
from dotenv import load_dotenv
import valorant

load_dotenv()

KEY = os.getenv("VALPY-KEY")
client = valorant.Client(KEY, region="na", locale="en-US")

player = client.get_user_by_name("Churro#MMM")

# Find their most recent Ranked match.:
# This will raise an error if your API Key does not have match access.
match = player.matchlist().history.find(queueId="competitive")

# Check if the match exists.
if match == None:
    print("No Ranked match in recent history!")
    exit(1)
else:
    match = match.get()

# Print everyone's ranks.
for team in match.teams:
    print(f"{team.teamId} Team's Ranks: ")

    # Find all the players on the same team.
    players = match.players.get_all(teamId=team.teamId)

    for player in players:
        print(f"\t{player.gameName} - {player.rank}")

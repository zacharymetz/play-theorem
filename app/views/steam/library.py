"""

"""

import json
import urllib.request
from . import STEAM_API_KEY

class SteamLibrary:
    'Class to hold all the information related to a users steam library'

    def __init__(self, steam_id):
        self.id = steam_id #keep track of the id of the user
        self.library = get_steam_library(steam_id) #get the raw data and the game count
        self.games = []
        self.games_last_two_weeks = apps_used_last_two_weeks(self.library)

        for game in self.library[0]:
            self.games.append(game['appid'])
             #where the info for all the games go



    #call this function to get all the info for the games in the library
    def get_app_info(self):
        for app in self.library[0]:
            app_data = get_steam_app_data(app['appid'])
            print(app['appid'])
            self.games.append(app)


#returns a json object with the seatm ids of all the
#games along with the total play time and the last 2 weeks per element and
#and the game count
def get_steam_library(steam_id):
    print(steam_id)
    api_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+STEAM_API_KEY+"&steamid="+str(steam_id)+"&format=json"
    api_response = urllib.request.urlopen(api_url)
    print(api_response.getcode())
    return_json = json.loads(api_response.read().decode("utf-8"))
    return return_json['response']['games'], return_json['response']['game_count']


#retuns a json object with information relating to the game including screen shots
# this api request does not require a key
def get_steam_app_data(app_id):
    api_url = "http://store.steampowered.com/api/appdetails?appids=" + str(app_id)
    api_response = urllib.request.urlopen(api_url)
    print(api_response.getcode())
    return json.loads(api_response.read().decode("utf-8"))


#returns the name of the app (DOSENT WORK)
def get_app_name(app_data,app_id):
	#error catch
	if app_data[app_id]["success"] == True:
		return app_data[app_id]["data"]["name"] # additionaly in data is generes and categories

def get_steam_id(steam_name):
    """
    Uses steam api to find the 64 bit steamid for a user and only takes in their
    username
    """

    api_url = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key="+STEAM_API_KEY+ "&vanityurl=" + steam_name
    print(api_url)
    api_response = urllib.request.urlopen(api_url)

    print(api_response.getcode())
    return json.loads(api_response.read().decode("utf-8"))

def apps_used_last_two_weeks(steam_library):
	played_last_two_weeks = []

	#loop thorugh the library and add all the dicts for the games that have been played in the last 2 weeks
	for app in steam_library[0]:
		if 'playtime_2weeks' in app.keys():
			played_last_two_weeks.append(app)
	return played_last_two_weeks
# gives you a list of app ids based on a max play time
def apps_never_used(steam_library,max_play_time):
	return_games =[]
	for app in steam_library[0]:
		if app["playtime_forever"] <= max_play_time:
			return_games.append(app)
	return return_games

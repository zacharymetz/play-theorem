STEAM_API_KEY = "" #blank steam key for the app to use

def init_steam_connection():
    """
    Methods is called loads the steam key in steamkey.txt
    """
    try:
        key_file = open("steamkey.txt",'rt')
        global STEAM_API_KEY
        STEAM_API_KEY = key_file.read()
        key_file.close()
        print("Steam Key Loaded successfully")
    except:
        print("ERROR LOADING STEAM API KEY, Connection to steam service cannot be established")


def get_steam_key():
    global STEAM_API_KEY
    return STEAM_API_KEY.strip('\n')

from . import create_app
from flask import request
import time



def main():
    print("CREATING DUMMY APP FOR DB SEEDING")
    app = create_app() #create new app object
    time.sleep(1)
    

main()

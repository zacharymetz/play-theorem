from flask import Blueprint, render_template, redirect, url_for, request
from app.views.forms.search_forms import SteamidForm
from app.views.steam.library import get_steam_id

search = Blueprint('search', __name__)



@search.route('/', methods=["GET","POST"])
def landing_page():
    error = None
    form = SteamidForm(request.form)
    if request.method == "POST":
        print("finding steam id")
        steam_id = get_steam_id(form.steamid.data)
        print(steam_id)
        return "  "


    return render_template('search/main.html',form=form,error=error)

@search.route('/search', methods=["POST"])
def results():


    return render_template('/search/results.html')

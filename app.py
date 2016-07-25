from flask import Flask, render_template, request, redirect
from geopy import geocoders

import dill
dill.settings["recurse"] = True

import requests
from bokeh.plotting import figure
from bokeh.embed import components

import pandas as pd

app = Flask(__name__)

app.vars = {}
with open("knn_model.pkl", "rb") as f:
    app.model = dill.load(f)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        app.vars["street"] = request.form["street"]
        app.vars["city"] = request.form["city"]
        app.vars["state"] = request.form["state"]
        app.vars["numberofblightviolationtickets"] = request.form["numberofblightviolationtickets"]
        app.vars["numberofcrimes"] = request.form["numberofcrimes"]
        app.vars["numberof311calls"] = request.form["numberof311calls"]

        return redirect('/graph') #redirect('/graph')

def get_lat_lon(x):
    geolocator = geocoders.Nominatim()
    try:
        location = geolocator.geocode(x, timeout=8, exactly_one=True)
        lat = location.latitude
        lon = location.longitude
    except:
        lat = 0
        lon = 0
    return [lat, lon]

@app.route('/graph')
def graph():
    # Search for the geocoordinates (latitude, Longitude)
    address = app.vars["street"] + ", " + app.vars["city"] + ", " + app.vars["state"]
    latlon = get_lat_lon(address)
    column_names=["Latitude", "Longitude", "Violation_Count", "Crime_Count", "311_Count"]
    values = [latlon[0], latlon[1], app.vars["numberofblightviolationtickets"], \
            app.vars["numberofcrimes"], app.vars["numberof311calls"]]
    # create a datafram which is the input default of model
    xx = {x : y for x, y in zip(column_names, values)}
    df = pd.DataFrame(columns = column_names)
    for i in range(5):
        df.set_value(0, column_names[i], float(values[i]))

    # Predict the value with the model
    try:
        if app.model.predict(df)[0]:
            div =  '%s' % ("YES")
        else:
            div = '%s' % ("NO")
    except:
        div="Error"
    #print div
    #script = "aa"

    street = '%s' % app.vars['street']
    return render_template('graph.html', div=div, subtitle=street) #, script=script

if __name__ == '__main__':
    #app.run(port=33507, debug=True)
    app.run(host='0.0.0.0') # The operating system listens on all public IPs.

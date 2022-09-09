# #create a new flask instance
# #import your dependencies
import datetime as dt
from sys import prefix
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#create our engine
engine = create_engine("sqlite:///hawaii.sqlite", connect_args={"check_same_thread":False})

#reflect the database into the classes
Base = automap_base()

Base.prepare(engine, reflect = True)

#create class references
Measurement = Base.classes.measurement
Station = Base.classes.station

#create the session
session = Session(engine)

#Setup flask
app = Flask(__name__, template_folder = 'template')


#create a root for our first route
@app.route('/')

#create a function to provide users with text to the other routes on the homepage
def welcome():
    return('''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')

#create the new routes

##precipitation route
@app.route("/api/v1.0/precipitation")

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

##Stations route
@app.route("/api/v1.0/stations")

def stations():

    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations = stations)

## tobs route
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017,8,23)- dt.timedelta(days = 365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps = temps)

## statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


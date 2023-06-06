# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt

# SQLAlchemy tools
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect

#################################################
# Database Setup        
#################################################   

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(engine, reflect=True)

# Save references to each table- turns db tables into python classes
measurement = base.classes.measurement
station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

# Create an app, being sure to pass __name__

app = Flask(__name__)

# #################################################
# # Flask Routes
# #################################################

# Homeppage-define all routes
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Welcome to my Hawai'ian Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")   
def precipitation():

     # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation data"""
    # Query all precipitation data
    results = session.query(measurement.date, measurement.prcp).all()

    # Convert list of tuples into normal list
    all_precipitation = list(np.ravel(results))

    return jsonify(all_precipitation)

@app.route('/api/v1.0/stations')
def stations():

    """Return a list of stations"""
     # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # return a json list of stations  
    stations = session.query(station.station).all()

    return jsonify(stations)
    
@app.route('/api/v1.0/tobs')
def tobs():

    """List of temperature observations for the previous year from the most active station."""
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # dates and temp observations of most active station for last year.
    most_active_station = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
    filter(measurement.station == 'USC00519281').all()

     # Convert list of tuples into normal list
    all_precipitation = list(np.ravel(most_active_station))

    return jsonify(all_precipitation)
                   
@app.route('/api/v1.0/start')
def start():

    """List min/max/avg temps for a given start date."""
       # Create our session (link) from Python to the DB
    session = Session(engine)

    # return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    start_date = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
    filter(measurement.date >= '2016-08-23').all()

    return jsonify(start_date)


@app.route('/api/v1.0/start-end')

def start_end():
    """List min/max/avg temps for a given start/end date range."""
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    start_end_date = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
    filter(measurement.date >= '2016-08-23').\
    filter(measurement.date <= '2017-08-23').all()

    return jsonify(start_end_date)

if __name__ == '__main__':
    app.run(debug=True)

    session.close()



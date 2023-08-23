import numpy as np
from flask import Flask, request
import geopandas as gpd
from shapely.geometry import Point

app = Flask(__name__)

try:
    shape_file = gpd.read_file("tz_world/tz_world.shp")
except:
    print("There was an error opening the shape file")

@app.route("/timezones", methods = ['GET'])
def get_timezones():
    latitude = float(request.args.get("lat"))
    longitude = float(request.args.get("lon"))

    # in case we have the arguments "lon" and "lat" present, return a specific time zone
    if (latitude and longitude):
        coordinates = Point(longitude, latitude)

        # compute the nearest time zone for any given point
        # in case it is from 'uninhibited' area, get closest available time zone
        nearest_timezone = None
        min_distance = np.Inf

        for _, row in shape_file.iterrows():
            if row['TZID'] != 'uninhabited':
                # measure the distance between given Point and all available polygons
                distance = coordinates.distance(row['geometry'])
                if distance < min_distance:
                    min_distance = distance
                    nearest_timezone = row['TZID']

        return {"timezone": nearest_timezone}
    else:
        # if there are no arguments present, return default respone: all time zones
        unique_timezones = shape_file['TZID'].unique()
        return {"timezones": list(unique_timezones)}

if __name__ == '__main__':
    app.run(debug=True)
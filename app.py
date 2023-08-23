from flask import Flask, request, Response, jsonify
import geopandas as gpd

app = Flask(__name__)

try:
    shape_file = gpd.read_file("tz_world/tz_world.shp")
except:
    print("There was an error opening the shape file")

@app.route("/timezones", methods = ['GET'])
def get_timezones():
    # get all unique values in the TZID
    timezones = shape_file['TZID'].unique()
    return {"timezones": list(timezones)}

if __name__ == '__main__':
    app.run(debug=True)
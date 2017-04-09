import json
import sys
import math
import os.path
from pprint import pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    return max(data, key=lambda d: d['SeatsCount'])    

def get_smallest_bar(data):
    return min(data, key=lambda d: d['SeatsCount'])

def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda d: math.hypot(longitude - float(d["Longitude_WGS84"]), latitude - float(d["Latitude_WGS84"])))

if __name__ == '__main__':
    fpath  = input("Enter json filepath:")
    bars_data = load_data(fpath)
    if bars_data is None:
        print ("File '%s' not found" % (fpath)) 
        sys.exit()
    mylat  = float(input("Enter your latitude:"))
    mylong = float(input("Enter your longitude:"))
    print("\nBiggest bar: \n") 
    pprint (get_biggest_bar(bars_data))
    print("\nSmallest bar: \n") 
    pprint (get_smallest_bar(bars_data))
    print("\nClosest bar: \n") 
    pprint (get_closest_bar(bars_data,mylong,mylat))
    

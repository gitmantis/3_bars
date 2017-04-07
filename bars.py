import json
import math
import os.path
from operator import itemgetter, attrgetter
from pprint import pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    return max([bar for bar in data], key=lambda d: d['SeatsCount'])    

def get_smallest_bar(data):
    return min([bar for bar in data], key=lambda d: d['SeatsCount'])

def get_closest_bar(data, longitude, latitude):
    distance = 0    
    closest_bar = {}
    earthradius = 6372795    
    distance_min = 2*math.pi*earthradius
   
    for bar in data:
        bar_longitude = bar["geoData"]["coordinates"][0]
        bar_latitude  = bar["geoData"]["coordinates"][1]
 
        #перевести координаты в радианы
        lat1  = bar_latitude * math.pi / 180;
        long1 = bar_longitude * math.pi / 180;
        lat2  = latitude * math.pi / 180;
        long2 = longitude * math.pi / 180;
 
        #косинусы и синусы широт и разницы долгот
        cl1 = math.cos(lat1);
        cl2 = math.cos(lat2);
        sl1 = math.sin(lat1);
        sl2 = math.sin(lat2);
        delta = long2 - long1;
        cdelta = math.cos(delta);
        sdelta = math.sin(delta);
 
        #вычисления длины большого круга
        y = math.sqrt(math.pow(cl2 * sdelta, 2) + math.pow(cl1 * sl2 - sl1 * cl2 * cdelta, 2));
        x = sl1 * sl2 + cl1 * cl2 * cdelta;
 
        ad = math.atan2(y, x);
        distance = ad * earthradius;
        
        if distance < distance_min:
            distance_min = distance
            closest_bar = bar    
 
    return closest_bar
   

if __name__ == '__main__':
    fpath  = input("Enter json filepath:")
    mylat  = float(input("Enter your latitude:"))
    mylong = float(input("Enter your longitude:"))

    bars_data = load_data(fpath)
    print("\nBiggest bar: \n") 
    pprint (get_biggest_bar(bars_data))
    print("\nSmallest bar: \n") 
    pprint (get_smallest_bar(bars_data))
    print("\nClosest bar: \n") 
    pprint (get_closest_bar(bars_data,mylong,mylat))
    

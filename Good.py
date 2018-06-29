
import random 
import json
class Coord : 
    def __init__(self, lat, long): 
        self.lat = lat 
        self.long = long 
# type  = 0 --> land without house 
# 1 --> villa
# 2 --> appart 
class Land : 
    def __init__(self, id, lat, long, address, boundries, surface, type  ): 
        self.id = id
        self.coord = Coord(lat, long)
        self.address = address
        self.boundries = boundries
        self.surface = surface
        self.estimatedPrice =50000
        self.type = type 
    
    def __str__(self): 
        return "Land : id = " + str(self.id)  + " address : " + self.address
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


class Vehicle: 
    def __init__(self, id, type, immatriculation, color, marque ): 
        self.id = id
        self.type =type
        self.immatriculation = immatriculation
        self.color = color
        self.marque = marque
        self.estimatedPrice =50000

    def __str__(self): 
        return "Voiture : id = " + str(self.id)  + " color : " + self.color
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

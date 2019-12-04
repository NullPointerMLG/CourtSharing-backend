from math import radians, sin, cos, sqrt, atan2

class Distance:

    @staticmethod
    def calc_distance(lat1, lon1, lat2, lon2):
        #Earth radius in meters
        R = 6372800

        #slat, slon - starts coords ---- elat, elon - end cords
        slat = radians(float(lat1))
        slon = radians(float(lon1))
        elat = radians(float(lat2))
        elon = radians(float(lon2))

        dphi = elat - slat
        dlambda = elon - slon

        a = sin(dphi/2)**2 + cos(slat)*cos(elat)*sin(dlambda/2)**2

        dist = (2*R*atan2(sqrt(a), sqrt(1 - a)))/1000

        return dist
      
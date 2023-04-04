class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance
    def mTOcm(self):
        return self.__distance*100
    def mTOkm(self):
        return self.__distance/1000
    def mTOinch(self):
        return self.__distance*39.37
    def display(self):
        print(f"Your distance in Centimeter is: {self.mTOcm()}")
        print(f"Your distance in Kilometer is: {self.mTOkm()}")
        print(f"Your distance in inch is: {self.mTOinch()}")
Meters = DistanceConversion(float(input("Input a distance in meter:")))
Meters.display()
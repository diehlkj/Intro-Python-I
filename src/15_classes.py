# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# * https://www.programiz.com/python-programming/methods/built-in/super
# * https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance

# YOUR CODE HERE
class LatLon():
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

        # print(f"LatLon > Lat: {lat}")
        # print(f"LatLon > lon: {lon}")
    def __str__(self):
        lat = self.lat.format(self=self)
        lon = self.lon.format(self=self)
        return f"{lat} {lon}"

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        # self.lat = lat
        # self.lon = lon

        # print(f"Waypoint > name: {name}")
        # print(f"Waypoint > lat: {lat}")
        # print(f"Waypoint > lon: {lon}")
    def __str__(self):
        name = self.name.format(self=self)
        lat = self.lat
        lon = self.lon
        return f"{name} {lat} {lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        # ? The values of 'name', 'lat', and 'lon' are being created by Waypoint and LatLon.
        # ? They are defined here but created in different classes to share with others.

        # self.name = name
        self.difficulty = difficulty
        self.size = size
        # self.lat = lat
        # self.lon = lon

        # print(f"Geocache > name: {name}")
        # print(f"Geocache > difficulty: {difficulty}")
        # print(f"Geocache > size: {size}")
        # print(f"Geocache > lat: {lat}")
        # print(f"Geocache > lon: {lon}")
    def __str__(self):
        name = self.name.format(self=self)
        diff = self.difficulty.format(self=self)
        size = self.size.format(self=self)
        lat = self.lat
        lon = self.lon
        return f"{name} {diff} {size} {lat} {lon}"
        # output = ""
        # for i in dir(self): 
        #     if not i.startswith('__'):
        #         output += f"{i}: {self.i.format(self=self)} \n"
        # return output


Geocache('place', 'super hard', 'very large', 45, 135)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
a = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# * https://stackoverflow.com/questions/11637293/iterate-over-object-attributes-in-python
print(a)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
b = Geocache("Newberry Views", "diff 1.5", "size 2", 44.052137, -121.41556)

# Print it--also make this print more nicely
print(b)

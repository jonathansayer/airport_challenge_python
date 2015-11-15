class Airport:

    def __init__(self):
        self.capacity = 20
        self.planes = []

    def land_plane(self, plane):
        plane.land()
        self.planes.append(plane)

    def release_plane(self,plane,weather):
        if weather.stormy == True:
            return "Weather is Stormy"
        plane.take_off()
        self.planes.remove(plane)

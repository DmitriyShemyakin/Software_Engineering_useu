from get_datetime import get_datetime
get_datetime()

class Planet:
    def __init__(self, name, mass, distance):
        self._name = name
        self._mass = mass
        self._distance = distance

    def get_name(self):
        return self._name

    def set_mass(self, mass):
        self._mass = mass
        print(f"Mass of {self._name} updated to {self._mass}")

    def get_info(self):
        return f"{self._name} | Mass: {self._mass} | Distance: {self._distance}"

class HabitablePlanet(Planet):
    def __init__(self, name, mass, distance, water_presence, atmosphere):
        super().__init__(name, mass, distance)
        self._water_presence = water_presence
        self._atmosphere = atmosphere

    def get_habitable_features(self):
        return f"Water: {self._water_presence}, Atmosphere: {self._atmosphere}"

mars = Planet("Mars", "6.39 × 10^23 kg", "227.9 million km")
print(mars.get_info())

mars.set_mass("6.41 × 10^23 kg")
print(mars.get_info())

kepler = HabitablePlanet("Kepler-22b", "Unknown", "600 light years", "Yes", "Likely")
print(kepler.get_info())
print(kepler.get_habitable_features())
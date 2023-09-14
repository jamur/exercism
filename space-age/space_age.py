PLANETS = {'Mercury': 0.2408467, 'Venus': 0.61519726, 'Earth': 1,
           'Mars': 1.8808158, 'Jupiter': 11.862615, 'Saturn': 29.447498,
           'Uranus': 84.016846, 'Neptune': 164.79132}

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        for planet, year in PLANETS.items():
            setattr(self, f'on_{planet.casefold()}',
                    lambda seconds=seconds, year=year:
                    round(seconds / 31557600 / year, 2))

from classes.turret import Turret
from classes.api import API

turret = Turret(21,15)

api = API(on_aim=turret.aim)

api.run()
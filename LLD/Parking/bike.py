from vehicle import Vehicle
from vehicle_type import VehicleType


class Bike(Vehicle):

  def __init__(self,vehicle_no):
    super().__init__(vehicle_no, VehicleType.BIKE)

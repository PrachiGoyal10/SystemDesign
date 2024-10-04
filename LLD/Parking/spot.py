from vehicle_type import VehicleType
from vehicle import Vehicle

# class SpotAvailableStatus(Enum):
#   RESERVED=1
#   AVAILABLE=2
#   PARKED=3

class Spot:

  def __init__(self, spot_no : int , type_of_vehicle: VehicleType ): 
    self.spot_no = spot_no
    self.type_of_vehicle = type_of_vehicle
    self.vehicle = None

  def park_vehicle(self, vehicle : Vehicle):
    if self.is_availble() and vehicle.type ==  self.type_of_vehicle: 
      self.vehicle = vehicle
      
    return not self.is_availble()

  def unpark_vehicle(self):
    return self.vehicle = None

  def is_availble(self,):
    return self.vehicle == None

  def get_spot_no(self):
    return self.spot_no

  def get_type_of_vehicle(self):
    return self.type_of_vehicle

  def get_vehicle(self):
    return self.vehicle
    
    

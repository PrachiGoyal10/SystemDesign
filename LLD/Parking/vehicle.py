from abc import ABC

class Vehicle(ABC):

  def __init__(self,vehcile_no, type):
    self.vehcile_no = vehcile_no
    self.type = type
    self.color = None


  def get_vehicle_type(self):
    return self.type

  




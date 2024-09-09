from commands.park_vehicle import ParkVehicle
from commands.leave_vehicle import LeaveVehicle
from commands.create_parking import CreateParking
from commands.status_parking import StatusParking
from commands.slot_with_color import SlotWithColor
from commands.slot_with_number import SlotWithNumber
from commands.registeration_with_color import RegisterationWithColor

class CommandFactory():
    
    def __init__(self,parking,name,args):
        
        if name == "create_parking_lot":
            CreateParking(parking,args)
        elif name == "park":
            ParkVehicle(parking,args)
        elif name == "leave":
            LeaveVehicle(parking,args)
        elif name == "status":
            StatusParking(parking)
        elif name == "registration_numbers_for_cars_with_colour":
            RegisterationWithColor(parking,args)
        elif name == "slot_numbers_for_cars_with_colour":
            SlotWithColor(parking,args)
        elif name == "slot_number_for_registration_number":
            SlotWithNumber(parking,args)
        else:
            print("Invalid Command Passed")
        
        
        
        
        
from models.cars import Cars

class ParkVehicle():
    
    def __init__(self,parking_slot,args):
        if not parking_slot.check_vacancy():
            print("Sorry no space left to park")
            return
        
        if not parking_slot.check_car_in_registration(args[0]):
            print("Car with same registeration already exists")
            return 
            
        slot = parking_slot.check_availalble_slot()
        car = Cars(args[0],args[1])
        parking_slot.assign_car_to_slot(car,slot)
        print(f"Allocated Slot number {slot.number}")
        return
    
    
        
    
    
from models.cars import Cars

class LeaveVehicle():
    
    def __init__(self,parking_slot,args):
        slot  = slot(args[0])
        if slot not in parking_slot.keys():
            print("Sorry the slot is invalid")
            return
        
        parking_slot.remove_car_from_slot(slot)
        print(f"Slot number {slot.number} is free.")
        return
    
    
        
    
    
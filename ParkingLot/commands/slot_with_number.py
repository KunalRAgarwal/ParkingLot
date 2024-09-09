class SlotWithNumber():
    
    def __init__(self,parking_slot,args):
        number  = args[0]
        for slot in parking_slot:
            car  = parking_slot.db_mp [slot]
            if car.registration == number:
                print("Car with registration {number} is in slot {slot.number}")
                return

        print("The car with the registration {number} is not present.")
        return
        
        
    
    
        
    
    
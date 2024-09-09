class StatusParking():
    
    def __init__(self,parking_slot):
        for slot in parking_slot:
            car  = parking_slot.db_mp [slot]
            print(f"{slot.number} {car.registration} {car.color}")
        
            
    
    
        
    
    
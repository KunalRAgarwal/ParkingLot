from models.slot import slots

class ParkingSlot():
    db_mp = {}
    occupied_slots = None
    size = None
    cars_registered = []
    
    def create_parking(self,size):
        self.size = size
        for i in range(1,size+1):
            slot = slots(i)
            self.db_mp[slot] = None
        
        self.occupied_slots = 0
    
    def assign_car_to_slot(self,car,slot):
        self.db_mp[slot] = car
        self.occupied_slots +=1
        self.cars_registered.append(car.registration)
    
    def remove_car_from_slot(self,slot):
        car  = self.db_mp[slot]
        self.db_mp[slot] = None
        self.occupied_slots -=1
        self.cars_registered.remove(car.registration)
    
    def check_vacancy(self):
        return self.size - self.occupied_slots>0
    
    def check_availalble_slot(self):
        for i in range(1,self.size+1):
            slot = slots(i)
            
            if not self.db_mp[slot]:
                return slot
    
    def check_car_in_registration(self,car):
        return car.registration in self.cars_registered
            
    
            
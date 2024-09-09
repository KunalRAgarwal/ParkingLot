class SlotWithColor():
    
    def __init__(self,parking_slot,args):
        color  = args[0]
        slots_list = []
        for slot in parking_slot:
            car  = parking_slot.db_mp [slot]
            if car.color == color:
                slots_list.append(slot.number)
        
        if not slots_list:
            print("There is no car with the color {color}")
        
        slots_list =", ".join(slots_list)
        print("The slots with the color {color} are {slots_list}")
        return
        
        
    
    
        
    
    
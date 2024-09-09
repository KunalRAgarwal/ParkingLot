class RegisterationWithColor():
    
    def __init__(self,parking_slot,args):
        color  = args[0]
        registration_list = []
        for slot in parking_slot:
            car  = parking_slot.db_mp [slot]
            if car.color == color:
                registration_list.append(car.registration)
        
        if not registration_list:
            print("There is no car with the color {color}")
        
        registration_list =", ".join(registration_list)
        print("The cars with the color {color} are {registration_list}")
        return
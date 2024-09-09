from models.parking_slot import ParkingSlot
from parking_stratergy.parking_stratergy import ParkingStratergy

parking = ParkingSlot()
parking_stratergy = ParkingStratergy()

while True:
    command = input().strip().split()
    ParkingStratergy.execute(parking,command)
    
    
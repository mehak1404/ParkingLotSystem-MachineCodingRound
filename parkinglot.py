"""
-> floors
-> slots
-> parking lot
-> vehicle 
(park, unpark)
"""
from copy import deepcopy
from enum import Enum, auto

class VehicleType(Enum):

    CAR = auto()
    TRUCK = auto()
    BIKE = auto()

class Slots:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.status = 1
        self.vehicle = None
        return
    def park_vehicle(self, vehicle):
        self.status = 0
        self.vehicle = vehicle
        return

    def unpark_vehicle(self):
        self.status = 1
        self.vehicle = None
        return 

class Floors:
    def __init__(self, id):
        self.id = id
        self.slots = []

    def add_slots(self, slot):
        slot = Slots(slot["id"], slot["type"])
        self.slots.append(slot)
        return
                
    def get_available_slots(self, type = None):

        if type:
            return [slot for slot in self.slots if slot.status==1 and slot.type == VehicleType.__getitem__(type)]
        return [slot for slot in self.slots if slot.status == 1]
    def get_occupied_slots(self, type = None):

        if type:
            return [slot for slot in self.slots if slot.status==0 and slot.type == VehicleType.__getitem__(type)]
        return [slot for slot in self.slots if slot.status == 0]


class ParkingLot:

    def __init__(self, id):
        self.id = id
        self.floors = {}
        return
    
    def add_floors(self, floor_nums, slots):
        for floor_id  in range(1, int(floor_nums) +1):

            floor = Floors(floor_id)
            for id in range(1, int(slots) +1):
                if id == 1:
                    floor.add_slots({"id": id, "type": VehicleType.TRUCK})
                elif id == 2 or id == 3:
                    floor.add_slots({"id": id, "type": VehicleType.BIKE})
                else:
                    floor.add_slots({"id": id, "type": VehicleType.CAR})
            self.floors[floor_id] = floor

    def get_floor(self, floor_id):
        return self.floors.get(floor_id)
    
   
    
                     
class Vehicle:
    def __init__(self, reg_no, color, type):
        self.reg_no =  reg_no
        self.color = color
        self.type = VehicleType.__getitem__(type)

class Ticket:
    @staticmethod
    def generate_ticket(parkinglot, floor, slot):
        return f"{parkinglot}_{floor}_{slot}"
    
class ParkinglotManager:

    def __init__(self):
        self.parking_lots = {}

    def create_parking_lot(self, parking_lot_id, floors, slots):
        parking_lot = ParkingLot(parking_lot_id)
        parking_lot.add_floors(floors, slots)
        self.parking_lots[parking_lot_id] = parking_lot
        
        return f"Created parking lot with {floors} floors and {slots} slots per floor"
    
    def park_vehicle(self, type, reg_num, color):
        
        for parkinglot_it, parking_lot in self.parking_lots.items():
            for floor_id, floor in parking_lot.floors.items():
                if slots := floor.get_available_slots(type):
                    vehicle = Vehicle(reg_no=reg_num, color=color, type=type)
                    slots[0].park_vehicle(vehicle)
                    ticket =  Ticket.generate_ticket(parkinglot_it, floor_id, slots[0].id)
                    return f"Parked vehicle. Ticket ID: {ticket}"
            
        return "Parking Lot Full"
    
    def unpark_vehicle(self, ticket):

        p_id, floor_id, slot_id = ticket.split("_")
        
        if parking_lot := self.parking_lots.get(p_id):
            if floor := parking_lot.get_floor(int(floor_id)):
                
                if int(slot_id) <= len(floor.slots):
                    slot = floor.slots[int(slot_id)-1]
                    vehicle = deepcopy(slot.vehicle)
                    if vehicle:
                        slot.unpark_vehicle()
                        return f"Unparked vehicle with Registration Number: {vehicle.reg_no} and Color: {vehicle.color}"

        return "Invalid Ticket"

    def free_count(self, type):
        
        for p_id, parking_lot in self.parking_lots.items():

            for f_id, floor in parking_lot.floors.items():

                slots = floor.get_available_slots(type = type)
                print(f"No. of free slots for {type} on Floor {f_id}: {len(slots)}")

    def free_slots(self, type):
        for p_id, parking_lot in self.parking_lots.items():

            for f_id, floor in parking_lot.floors.items():

                slots = floor.get_available_slots(type = type)
                slot_ids = [str(slot.id) for slot in slots]
                print(f'Free slots for {type} on Floor {f_id}: {",".join(slot_ids)}')


    def occupied_slots(self, type):
        for p_id, parking_lot in self.parking_lots.items():

            for f_id, floor in parking_lot.floors.items():

                slots = floor.get_occupied_slots(type = type)
                slot_ids = [str(slot.id) for slot in slots]
                print(f'Occupied slots for {type} on Floor {f_id}: {",".join(slot_ids)}')



if __name__ == "__main__":

    parkingManager = ParkinglotManager()
    while(cmd := input()):
        if cmd == "exit":
            break
            
        cmd = cmd.split()

        if cmd[0] == "create_parking_lot":
            print(parkingManager.create_parking_lot(cmd[1], cmd[2], cmd[3]))

        elif cmd[0] == "park_vehicle":
            print(parkingManager.park_vehicle(cmd[1], cmd[2], cmd[3]))

        elif cmd[0] == "unpark_vehicle":
            print(parkingManager.unpark_vehicle(cmd[1]))

        else:
            
            if cmd[1] == "free_count":
                parkingManager.free_count(cmd[2])

            elif cmd[1] == "free_slots":
                parkingManager.free_slots(cmd[2])

            elif cmd[1] == "occupied_slots":
                parkingManager.occupied_slots(cmd[2])



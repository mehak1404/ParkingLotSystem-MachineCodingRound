# Parking Lot System

## Overview
This project implements a command-line application for managing a parking lot system. The system allows for creating a parking lot, adding floors and slots, parking and unparking vehicles, and displaying the status of parking slots.

## Features
- **Create Parking Lot:** Initialize a parking lot with a specified number of floors and slots per floor.
- **Park Vehicle:** Finds the first available slot for a vehicle, books it, and returns a ticket.
- **Unpark Vehicle:** Frees the parking slot for a given ticket.
- **Display Slot Details:** Provides details on free, occupied, or total slots per floor by vehicle type.
- **Vehicle and Slot Types:** Supports cars, bikes, and trucks, with designated slots for each type. First slot on each floor is for truck, 2 , and 3rd for bikes, rest for cars.

## Details
### Parking slot
Details about the Parking Slots:
- Each type of slot can park a specific type of vehicle.
- No other vehicle should be allowed by the system.
- Finding the first available slot should be based on:
- The slot should be of the same type as the vehicle.
- The slot should be on the lowest possible floor in the parking lot.
- The slot should have the lowest possible slot number on the floor.
- Numbered serially from 1 to n for each floor where n is the number of parking slots on that floor.

### Vehicle
- Every vehicle will have a type, registration number, and color.
- Different Types of Vehicles:
 - Car
 - Bike
 - Truck

### Floors
- Numbered serially from 1 to n where n is the number of floors.
- Might contain one or more parking lot slots of different types.
- We will assume that the first slot on each floor will be for a truck, the next 2 for bikes, and all the other slots for cars.

### Tickets
- The ticket id would be of the following format:
`<parking_lot_id>_<floor_no>_<slot_no>`
- Example: PR1234_2_5 (denotes 5th slot of 2nd floor of parking lot PR1234)


## Commands
The application supports the following commands:

### 1. `create_parking_lot`
**Syntax:** `create_parking_lot <parking_lot_id> <no_of_floors> <no_of_slots_per_floor>`  
**Example:** `create_parking_lot PR1234 2 6`  
**Output:**  
`Created parking lot with 2 floors and 6 slots per floor`

### 2. `park_vehicle`
**Syntax:** `park_vehicle <vehicle_type> <reg_no> <color>`  
**Example:** `park_vehicle CAR KA-01-DB-1234 black`  
**Output:**  
`Parked vehicle. Ticket ID: PR1234_1_4`  
If no slot is available: `Parking Lot Full`

### 3. `unpark_vehicle`
**Syntax:** `unpark_vehicle <ticket_id>`  
**Example:** `unpark_vehicle PR1234_1_4`  
**Output:**  
`Unparked vehicle with Registration Number: KA-01-DB-1234 and Color: black`  
If the ticket is invalid or the slot is already empty: `Invalid Ticket`

### 4. `display`
**Syntax:** `display <display_type> <vehicle_type>`  
- `display_type`: `free_count`, `free_slots`, `occupied_slots`  
**Examples:**  
`display free_count CAR`  
`display free_slots BIKE`  
`display occupied_slots TRUCK`

**Outputs:**  
- `free_count`:  
`No. of free slots for <vehicle_type> on Floor <floor_no>: <count>`  
- `free_slots`:  
`Free slots for <vehicle_type> on Floor <floor_no>: <slot_numbers>`  
- `occupied_slots`:  
`Occupied slots for <vehicle_type> on Floor <floor_no>: <slot_numbers>`

### 5. `exit`
Stops taking input and exits the application.

## Input/Output Examples
### Input:
```plaintext
create_parking_lot PR1234 2 6
display free_count CAR
park_vehicle CAR KA-01-DB-1234 black
unpark_vehicle PR1234_1_4
```

### Output:
```plaintext
Created parking lot with 2 floors and 6 slots per floor
No. of free slots for CAR on Floor 1: 3
Parked vehicle. Ticket ID: PR1234_1_4
Unparked vehicle with Registration Number: KA-01-DB-1234 and Color: black

```

### Command to run:
` python3 parkinglot.py < input.txt > output.txt`
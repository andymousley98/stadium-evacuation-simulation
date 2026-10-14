# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:12:47 2026

@author: andym
"""

# STAGE 1: Basic evacuation calculation
# Calculates theoretical evacuation time using fixed exit capacity.


def calculate_evacuation_time(total_people, number_of_doors, door_capacity):
    # Calculate total exit capacity and evacuation time
    total_capacity = number_of_doors * door_capacity
    evacuation_time = total_people / total_capacity

    return evacuation_time
    # End of evacuation calculation


# Test the function with different stadium populations

for pop in range(500, 3500, 500):

    time = calculate_evacuation_time(
        total_people=pop,
        number_of_doors=2,
        door_capacity=60
    )

    print(f"{pop} people: {time:.2f} minutes")
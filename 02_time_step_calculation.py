# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:16:30 2026

@author: andym
"""

# STAGE 2: Discrete time-step evacuation simulation
# Simulates the evacuation minute-by-minute.


def simulate_evacuation(total_people, number_of_doors, door_capacity):
    # Simulate people leaving each minute until everyone has left
    people_remaining = total_people
    time = 0
    total_capacity = number_of_doors * door_capacity

    while people_remaining > 0:

        people_leaving = min(total_capacity, people_remaining)
        people_remaining = people_remaining - people_leaving
        time += 1

        print(f"Minute {time}: {people_remaining} people remaining")

    return time
    # End of evacuation simulation


# Run the simulation

evacuation_time = simulate_evacuation(
    total_people=1000,
    number_of_doors=2,
    door_capacity=60
)

print(f"Total evacuation time: {evacuation_time} minutes")
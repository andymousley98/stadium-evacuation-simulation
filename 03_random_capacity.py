# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:01:47 2026

@author: andym
"""

# STAGE 3: Random exit capacity
# Adds randomness to the number of people leaving each minute.

import random


def simulate_evacuation(total_people, number_of_doors, min_capacity, max_capacity):
    # Simulate an evacuation with variable exit capacity

    people_remaining = total_people
    time = 0

    while people_remaining > 0:

        # Each door gets a random capacity for this minute
        door_capacity = random.randint(min_capacity, max_capacity)

        total_capacity = number_of_doors * door_capacity

        people_leaving = min(total_capacity, people_remaining)

        people_remaining = people_remaining - people_leaving
        time += 1

        print(
            f"Minute {time}: "
            f"{people_leaving} left, "
            f"{people_remaining} remaining"
        )

    return time
    # End of evacuation simulation


# Run the simulation

evacuation_time = simulate_evacuation(
    total_people=1000,
    number_of_doors=2,
    min_capacity=50,
    max_capacity=70
)

print(f"Total evacuation time: {evacuation_time} minutes")
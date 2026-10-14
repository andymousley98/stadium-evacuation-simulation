# STAGE 4: Monte Carlo simulation
# Runs the evacuation model many times to explore uncertainty.

import random


def simulate_evacuation(total_people, number_of_doors, min_capacity, max_capacity):
    # Simulate one evacuation with variable exit capacity

    people_remaining = total_people
    time = 0

    while people_remaining > 0:

        door_capacity = random.randint(min_capacity, max_capacity)
        total_capacity = number_of_doors * door_capacity

        people_leaving = min(total_capacity, people_remaining)

        people_remaining = people_remaining - people_leaving
        time += 1

    return time
    # End of evacuation simulation


# Run the simulation many times

results = []

for i in range(1000):

    evacuation_time = simulate_evacuation(
        total_people=1000,
        number_of_doors=2,
        min_capacity=50,
        max_capacity=70
    )

    results.append(evacuation_time)


# Calculate some basic results

average_time = sum(results) / len(results)
fastest_time = min(results)
slowest_time = max(results)


print(f"Average evacuation time: {average_time:.2f} minutes")
print(f"Fastest evacuation: {fastest_time} minutes")
print(f"Slowest evacuation: {slowest_time} minutes")

print(f"The evacuation was done in 8 minutes {results.count(8)} times")
print(f"The evacuation was done in 9 minutes {results.count(9)} times")
print(f"The evacuation was done in 10 minutes {results.count(10)} times")

#Plotting this as a bar chart

import matplotlib.pyplot as plt

times = sorted(set(results))
counts = [results.count(time) for time in times]

plt.bar(times, counts)

plt.xlabel("Evacuation time (minutes)")
plt.ylabel("Number of simulations")
plt.title("Evacuation time distribution")

plt.show()
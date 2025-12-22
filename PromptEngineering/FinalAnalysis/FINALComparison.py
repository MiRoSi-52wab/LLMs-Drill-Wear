SingleAgent_TIME = {
    "EASY": 54.508140563964844,
    "MEDIUM": 48.43189024925232,
    "HARD": 61.496365547180176
}

MultiAgent_TIME = {
    "EASY": 61.62889361381531,
    "MEDIUM": 125.5024926662445,
    "HARD": 172.38211846351624
}

accuracy = {
    "Single Agent": [1.0, 0.5, 2.0/3.0],
    "Multi Agent": [0.0, 0.5, 1.0]
}

import matplotlib.pyplot as plt
import numpy as np

difficulty_levels = ["EASY", "MEDIUM", "HARD"]
single_agent_times = [54.5, 48.4, 61.5]
multi_agent_times = [61.6, 125.5, 172.4]


accuracy_single_agent = [1.0, 0.5, 2.0/3.0]
accuracy_multi_agent = [1.0/3.0, 0.5, 1.0]

bar_width = 0.35
index = np.arange(len(difficulty_levels))

plt.bar(index, single_agent_times, bar_width, label='Single Agent')
plt.bar(index + bar_width, multi_agent_times, bar_width, label='Multi Agent')

plt.xlabel('Difficulty Level')
plt.ylabel('Time (seconds)')
plt.title('Time to Answer Questions by Model and Difficulty Level')
plt.xticks(index + bar_width / 2, difficulty_levels)
plt.legend()

plt.show()

# Bar width and index for positioning
bar_width = 0.35
index = np.arange(len(difficulty_levels))

# Bar plot for accuracy (ignoring time data)
plt.bar(index, accuracy_single_agent, bar_width, label='Single Agent', color='lightblue')
plt.bar(index + bar_width, accuracy_multi_agent, bar_width, label='Multi Agent', color='salmon')

# Labeling the axes and title
plt.xlabel('Difficulty Level')
plt.ylabel('Accuracy')
plt.title('Accuracy by Model and Difficulty Level')

# Adjusting the x-axis to show difficulty levels properly
plt.xticks(index + bar_width / 2, difficulty_levels)

# Adding a legend
plt.legend()

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Difficulty levels
difficulty_levels = ["EASY", "MEDIUM", "HARD"]

# Accuracy values for each model and difficulty level
accuracy_single_agent = [1.0, 0.5, 2.0/3.0]
accuracy_multi_agent = [1.0/3.0, 0.5, 1.0]

# Number of difficulty levels
N = len(difficulty_levels)

# Calculate angle for each axis (equal spacing)
angles = [n / float(N) * 2 * pi for n in range(N)]

# Close the circle by repeating the first value at the end
accuracy_single_agent += accuracy_single_agent[:1]
accuracy_multi_agent += accuracy_multi_agent[:1]
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(6, 6), dpi=120, subplot_kw=dict(polar=True))

# Plotting the accuracy for Single Agent and Multi Agent
ax.plot(angles, accuracy_single_agent, linewidth=2, linestyle='solid', label='Single Agent', color='blue')
ax.fill(angles, accuracy_single_agent, color='blue', alpha=0.4)

ax.plot(angles, accuracy_multi_agent, linewidth=2, linestyle='solid', label='Multi Agent', color='red')
ax.fill(angles, accuracy_multi_agent, color='red', alpha=0.4)

# Set the labels for each difficulty level
ax.set_yticklabels([])  # Hide radial axis labels
ax.set_xticks(angles[:-1])  # Set x-ticks to be the angles corresponding to difficulty levels
ax.set_xticklabels(difficulty_levels)  # Label each difficulty level

# Add a title and a legend
ax.set_title('Accuracy Comparison by Model and Difficulty Level', size=14, color='black', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Add values to the isolines (the concentric circles)
# Define the isoline values (for example: 0, 0.25, 0.5, 0.75, 1)
isolines = np.linspace(0, 1, 5)  # From 0 to 1, with 5 isolines

for isoline in isolines:
    ax.plot(angles, [isoline] * len(angles), linestyle='--', color='gray', alpha=0.5)  # Draw isoline
    # Annotate the isoline value
    ax.annotate(f'{isoline:.2f}', xy=(angles[0], isoline), 
                horizontalalignment='center', verticalalignment='center', 
                color='black', fontsize=10)

# Show the plot
plt.show()

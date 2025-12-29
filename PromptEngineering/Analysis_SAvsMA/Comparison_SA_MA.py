import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Data for plots
difficulty_levels = ["EASY", "MEDIUM", "HARD"]
single_agent_times = [54.5, 48.4, 61.5]
multi_agent_times = [61.6, 125.5, 172.4]
accuracy_single_agent = [1.0, 0.5, 2.0/3.0]
accuracy_multi_agent = [1.0/3.0, 0.5, 1.0]

# 1. Bar plot for time
bar_width = 0.35
index = np.arange(len(difficulty_levels))

# Create the first bar plot for time
plt.bar(index, single_agent_times, bar_width, label='Single Agent')
plt.bar(index + bar_width, multi_agent_times, bar_width, label='Multi Agent')

plt.xlabel('Difficulty Level')
plt.ylabel('Time (seconds)')
plt.title('Time to Answer Questions by Model and Difficulty Level')
plt.xticks(index + bar_width / 2, difficulty_levels)
plt.legend()

# Save the first plot
plt.savefig("time_to_answer_questions.png", format="png", dpi=300)
plt.close()  # Close the plot to avoid overlap when creating the next one

# 2. Bar plot for accuracy
plt.bar(index, accuracy_single_agent, bar_width, label='Single Agent', color='lightblue')
plt.bar(index + bar_width, accuracy_multi_agent, bar_width, label='Multi Agent', color='salmon')

plt.xlabel('Difficulty Level')
plt.ylabel('Accuracy')
plt.title('Accuracy by Model and Difficulty Level')
plt.xticks(index + bar_width / 2, difficulty_levels)
plt.legend()

# Save the second plot
plt.savefig("accuracy_by_model.png", format="png", dpi=300)
plt.close()  # Close the plot to avoid overlap when creating the next one

# 3. Radar chart for accuracy comparison
N = len(difficulty_levels)
angles = [n / float(N) * 2 * pi for n in range(N)]

accuracy_single_agent += accuracy_single_agent[:1]
accuracy_multi_agent += accuracy_multi_agent[:1]
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(6, 6), dpi=120, subplot_kw=dict(polar=True))

ax.plot(angles, accuracy_single_agent, linewidth=2, linestyle='solid', label='Single Agent', color='blue')
ax.fill(angles, accuracy_single_agent, color='blue', alpha=0.4)

ax.plot(angles, accuracy_multi_agent, linewidth=2, linestyle='solid', label='Multi Agent', color='red')
ax.fill(angles, accuracy_multi_agent, color='red', alpha=0.4)

ax.set_yticklabels([])  # Hide radial axis labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(difficulty_levels)

ax.set_title('Accuracy Comparison by Model and Difficulty Level', size=14, color='black', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

isolines = np.linspace(0, 1, 5)

for isoline in isolines:
    ax.plot(angles, [isoline] * len(angles), linestyle='--', color='gray', alpha=0.5)
    ax.annotate(f'{isoline:.2f}', xy=(angles[0], isoline), 
                horizontalalignment='center', verticalalignment='center', 
                color='black', fontsize=10)

# Save the third plot (radar chart)
plt.savefig("accuracy_comparison_radar.png", format="png", dpi=300)
plt.close()  # Close the plot


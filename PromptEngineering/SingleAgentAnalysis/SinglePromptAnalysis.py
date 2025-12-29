import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Given dictionaries
timeforEASY = {
    "Zero-Shot Prompts": 33.88163113594055,
    "Few-Shot Prompts": 35.244433641433716,
    "Chain-of-Thought Prompts": 47.27047109603882,
    "Plan and Solve Prompts": 45.09834170341492
}

timeforMEDIUM = {
    "Zero-Shot Prompts": 54.613399505615234,
    "Few-Shot Prompts": 56.485573291778564,
    "Chain-of-Thought Prompts": 47.92797327041626,
    "Plan and Solve Prompts": 48.46125149726868
}

timeforHARD = {
    "Zero-Shot Prompts": 73.24371385574341,
    "Few-Shot Prompts": 68.47876000404358,
    "Chain-of-Thought Prompts": 70.21622705459595,
    "Plan and Solve Prompts": 73.32620596885681
}

# Combine data into a format suitable for the heatmap
prompts = list(timeforEASY.keys())  # The prompt types are the same for all difficulties
easy_values = list(timeforEASY.values())
medium_values = list(timeforMEDIUM.values())
hard_values = list(timeforHARD.values())

# Create a matrix with time values for each difficulty level
time_matrix = np.array([easy_values, medium_values, hard_values])

# Create a heatmap using seaborn with a smaller size and larger text
fig, ax = plt.subplots(figsize=(6, 4))  # Smaller figure size
sns.heatmap(time_matrix.T, annot=True, cmap='Reds', xticklabels=["EASY", "MEDIUM", "HARD"], 
            yticklabels=prompts, cbar_kws={'label': 'Time (seconds)'}, ax=ax,
            annot_kws={'size': 14})  # Increase text size of the annotations


ax.set_title("Time to Complete Different Prompt Types at Various Difficulty Levels", fontsize=18)  # Set font size for title


plt.xticks(fontsize=14)  # Set font size for x-tick labels
plt.yticks(fontsize=14)  # Set font size for x-tick labels

plt.tight_layout()
# Save the figure as a PNG file
plt.savefig("prompt_times_SA.png", format="png", dpi=300)

# Show the plot
plt.show()

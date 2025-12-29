import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Given dictionaries
Supervisor = {
    "Zero-Shot Prompts": 97.70771431922913,
    "Few-Shot Prompts": 144.01396584510803,
    "Chain-of-Thought Prompts": 56.276204347610474,
    "Plan and Solve Prompts": 24.600756645202637
}

Wear = {
    "Zero-Shot Prompts": 58.864967823028564,
    "Few-Shot Prompts": 158.15411114692688,
    "Chain-of-Thought Prompts": 55.36191725730896,
    "Plan and Solve Prompts": 57.14752149581909
}

Quality = {
    "Zero-Shot Prompts": 63.43387794494629,
    "Few-Shot Prompts": 125.15679502487183,
    "Chain-of-Thought Prompts": 130.3980269432068,
    "Plan and Solve Prompts": 155.71048402786255
}

# Combine data into a format suitable for the heatmap
prompts = list(Supervisor.keys())  # The prompt types are the same for all models
supervisor_values = list(Supervisor.values())
wear_values = list(Wear.values())
quality_values = list(Quality.values())

# Create a matrix with time values for each model
time_matrix = np.array([supervisor_values, wear_values, quality_values])

# Create a heatmap using seaborn with a smaller size and larger text
fig, ax = plt.subplots(figsize=(6, 4))  # Smaller figure size
sns.heatmap(time_matrix.T, annot=True, cmap='Greens', xticklabels=["Supervisor", "Wear", "Quality"], 
            yticklabels=prompts, cbar_kws={'label': 'Time (seconds)'}, ax=ax,
            annot_kws={'size': 14})  # Increase text size of the annotations

# Set labels and title with custom font sizes
ax.set_title("Time to Complete Different Prompt Types for Various Models", fontsize=18)  # Set font size for title

# Increase size of the xticklabels
plt.xticks(fontsize=14)  # Set font size for x-tick labels
plt.yticks(fontsize=14)  # Set font size for x-tick labels

plt.tight_layout()
# Save the figure as a PNG file
plt.savefig("prompt_times_MA.png", format="png", dpi=300)


# Show the plot
plt.show()

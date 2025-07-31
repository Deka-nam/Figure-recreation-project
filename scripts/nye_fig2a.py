import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("data/mockfile_nyefig2a_genus_counts.csv")

# Sort by count
df = df.sort_values("Count", ascending=True)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 10))
bars = ax.barh(df["Genus"], df["Count"], color="gray", edgecolor="black")

# Add value labels to bars
for bar in bars:
    width = bar.get_width()
    ax.text(width + 2, bar.get_y() + bar.get_height()/2,
            f"{int(width)}", va='center', fontsize=8)

# Styling
ax.set_xlabel("Count", fontsize=12, weight='bold')
ax.set_ylabel("Genus", fontsize=12, weight='bold')
ax.set_title("Genus Detection Count", loc='left', fontsize=12, weight='bold')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.tight_layout()

# Save to results folder
plt.savefig("results/ny_fig2a_output.png", dpi=300)
plt.close()

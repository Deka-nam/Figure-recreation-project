import pandas as pd
import matplotlib.pyplot as plt

# Load the frequency data
csv_path = "/data/mockfile_nyefig2b_genus_frequencies.csv"
df = pd.read_csv(csv_path)

# Convert collection period to string for better plotting
df["CollectionPeriod"] = df["CollectionPeriod"].astype(str)

# Create the dot plot
plt.figure(figsize=(12, 10))
scatter = plt.scatter(
    x=df["CollectionPeriod"],
    y=df["Genus"],
    s=df["Frequency"] * 1000,  # Scale dot size
    c=df["Frequency"],
    cmap="inferno_r",
    edgecolors='black'
)

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label("Freq")

# Styling
plt.xlabel("Collection period", fontsize=12, weight='bold')
plt.ylabel("Genus", fontsize=12, weight='bold')
plt.title("Genus Frequency per Collection Period", fontsize=14, loc='left', weight='bold')
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Save figure
output_path = "/results/nye_fig2b_output_dotplot.png"
plt.savefig(output_path, dpi=300)
plt.close()



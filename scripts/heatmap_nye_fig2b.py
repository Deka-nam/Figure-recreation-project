import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/mockfile_nyefig2b_genus_frequencies.csv")

# Plot
plt.figure(figsize=(12, 10))
pivot = df.pivot("Genus", "CollectionPeriod", "Frequency")
g = sns.heatmap(pivot, cmap="inferno_r", linewidths=0.5, linecolor='gray', 
                cbar_kws={'label': 'Freq'}, square=False)

# Improve aesthetics
plt.title("Genus Frequency per Collection Period", fontsize=14, loc='left', weight='bold')
plt.xlabel("Collection period", fontsize=12, weight='bold')
plt.ylabel("Genus", fontsize=12, weight='bold')
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()

# Save
plt.savefig("results/nye_fig2b_output.png", dpi=300)
plt.close()

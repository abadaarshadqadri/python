# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib_venn import venn3

# # Load the data
# file_path = 'gene_presence_absence.csv'  # Update this with your actual file path
# data = pd.read_csv(file_path)

# # Print column names to identify them
# print("Column names in the DataFrame:")
# print(data.columns.tolist())

# # Display the first few rows of the DataFrame
# print(data.head())

# # Extract gene presence for each genus
# genus_presence = {
#     'Arthrospira': set(data.loc[data['Arthrospira_platensis'].notnull(), 'Gene']),
#     'Limnospira': set(data.loc[data['Limnospira_fusiformis_KN01'].notnull(), 'Gene']),
#     'Spirulina': set(data.loc[data['Spirulina_major_CS-329'].notnull(), 'Gene'])
# }

# # Create the Venn diagram
# venn3([genus_presence['Arthrospira'], genus_presence['Limnospira'], genus_presence['Spirulina']],
#       set_labels=('Arthrospira', 'Limnospira', 'Spirulina'))
# plt.title("Gene Presence/Absence Venn Diagram")
# plt.savefig('venn_diagram.png')  # Save the Venn diagram
# plt.show()

# # Bar plot for gene counts
# gene_counts = {
#     'Arthrospira': len(genus_presence['Arthrospira']),
#     'Limnospira': len(genus_presence['Limnospira']),
#     'Spirulina': len(genus_presence['Spirulina'])
# }

# plt.bar(gene_counts.keys(), gene_counts.values(), color=['blue', 'orange', 'green'])
# plt.ylabel("Number of Unique Genes")
# plt.title("Unique Gene Counts by Genus")
# plt.savefig('gene_counts.png')  # Save the bar plot
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import matplotlib.cm as cm
import numpy as np

# Load the data
file_path = 'gene_presence_absence.csv'  # Update this with your actual file path
data = pd.read_csv(file_path)

# Print column names to identify them
print("Column names in the DataFrame:")
print(data.columns.tolist())

# Extract gene presence for each genus
genus_presence = {
    'Arthrospira': set(data.loc[data['Arthrospira_platensis'].notnull(), 'Gene']),
    'Limnospira': set(data.loc[data['Limnospira_fusiformis_KN01'].notnull(), 'Gene']),
    'Spirulina': set(data.loc[data['Spirulina_major_CS-329'].notnull(), 'Gene'])
}

# Create the Venn diagram
plt.figure(figsize=(10, 8))  # Set figure size

# Define a colormap to generate colors dynamically
num_sets = len(genus_presence)
colors = cm.get_cmap('Pastel1', num_sets)

# Create Venn diagram
venn = venn3([genus_presence['Arthrospira'], genus_presence['Limnospira'], genus_presence['Spirulina']],
              set_labels=('Arthrospira', 'Limnospira', 'Spirulina'),
              alpha=0.7)

# Add colors to the Venn diagram and set font sizes
for idx, patch in enumerate(venn.patches):
    if patch:  # Check if the patch is not None
        patch.set_facecolor(colors(idx))

for label in venn.set_labels:
    label.set_fontsize(12)  # Set fontsize for the set labels

# Title and aesthetics
plt.title("Gene Presence/Absence Venn Diagram", fontsize=16, fontweight='bold')
plt.axis('equal')  # Equal aspect ratio ensures the circles are circular.
plt.grid(False)  # Disable the grid

# Save the enhanced Venn diagram
plt.savefig('enhanced_venn_diagram.png', bbox_inches='tight')  # Save with tight layout
plt.show()

# Bar plot for gene counts
gene_counts = {
    'Arthrospira': len(genus_presence['Arthrospira']),
    'Limnospira': len(genus_presence['Limnospira']),
    'Spirulina': len(genus_presence['Spirulina'])
}

plt.figure(figsize=(10, 6))
plt.bar(gene_counts.keys(), gene_counts.values(), color=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.9)
plt.ylabel("Number of Unique Genes", fontsize=14)
plt.title("Unique Gene Counts by Genus", fontsize=16, fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the enhanced bar plot
plt.savefig('enhanced_gene_counts.png', bbox_inches='tight')
plt.show()

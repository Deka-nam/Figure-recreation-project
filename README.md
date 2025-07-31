# Figure-recreation-project
Recreation of scientific figures using Python for data visualization and reproducibility practice.
# Recreation of Figures from "Microbial co-occurrences on catheters from long-term catheterized patients."

This project recreates key data visualizations from the paper:
> Nye, T.M., Zou, Z., Obernuefemann, C.L.P. et al. Microbial co-occurrences on catheters from long-term catheterized patients. Nat Commun 15, 61 (2024). https://doi.org/10.1038/s41467-023-44095-0

## Figures Recreated
- **Figure 2a**: Bar plot: Count of each genus detected across catheter and urine samples from long-term catheterized patients.
- **Figure 2b**: Dot plot: The frequency of indicated genera detected over sample collection periods for patients with 9 or more collection periods. 

## Tools Used
- Python (pandas, matplotlib, seaborn, numpy)
- Jupyter Notebooks 
- Git for version control

## Project Structure
```bash
paper-figure-recreation/
│
├── data/                    # Cleaned or provided datasets 
│   └── figure1_data.csv
│
├── notebooks/               # Jupyter notebooks 
│   └── figure1_recreation.ipynb
│
├── scripts/                 # Python scripts for reproducible runs
│   └── recreate_figure1.py
│
├── results/                 # Generated output: recreated plots, tables
│   └── figure1_output.png
│
├── original_figures/        # Original figure images (for comparison)
│   └── original_figure1.png
│
├── README.md                # Overview, paper info, steps to reproduce
├── requirements.txt         # List of dependencies 
├── LICENSE
└── .gitignore
```

## Output examples
> <div align="center">
> <img src="/results/nye_fig2a_output.png" alt="2a" width="335" style="margin: 5px;">
> <img src="/results/nye_fig2b_output_dotplot.png" alt="2b" width="500" style="margin: 5px;">
**Recreation of Fig 2a and 2b from Nye_2024**
> </div>

## Notes
*All figures are recreated for educational purposes to practice data visualization and reproducibility. This project does not include raw data extraction or proprietary information from the original paper.*



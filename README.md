# Algorithm to Process and Filter the 7000 Protein Panel from SOMALogic

The algorithm described in this post filters the SOMALogic Protein Sample for uniprotIDs that are associated with bone health. Once the proteins have been filters, the algorithm produces venn diagrams to visualize the overlap between various subgroups within the custom panel. 

The Code will be explained below:

```python
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2
from venn import venn
```

Above are the libraries imported to load in data, compile the data into a dataset, and analyze the data to produce venn diagrams.

```python
SomaLogic = pd.read_csv("~/Desktop/Knight Campus/ML Code/data.csv")
df = pd.read_csv("~/Desktop/Knight Campus/ML Code/data.csv")
SomaLogic = SomaLogic.fillna(0)
SomaLogic = SomaLogic.replace("X", 1)
df = df.fillna(0)
df = df.replace("X", 1)
```

The block of code above reads in the original dataset as a csv file and replaces all the occurances of NA with 0 and all of the occurances of X with 1. The original dataset indicated all of the SOMALogic proteins that correlated with 'Cardiovascular Disease', 'Inflammation and Immune Response', 'Metabolic Disease', 'Oncology', 'Combine Immune and Metabolic', 'Previous association with age', 'Previous association with Sex', 'Drug Targets', 'Bone Related or of interest', 'NIHM Supplemental Data', 'Aging and Longevity pQTLs', 'Rat Cytokine/Chemokine Luminex', 'Known of Interest', and 'Inflammatory Serum Protein Profiling of Patients'.

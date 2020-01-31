#!/usr/bin/env python
from sklearn.decomposition import PCA as PCA
from scipy.sparse.csgraph import connected_components
import umap
import pandas as pd
import sys
prefix = sys.argv[1]
filename = prefix + ".pruned.geno.txt"
pre_data = pd.read_table(filename, delim_whitespace=True, header=None, low_memory=False)
data = pre_data.dropna(how='any', axis=1)
pca_50 = PCA(n_components=50).fit(data)
proj_pca = pca_50.fit_transform(data)
d_embedding = umap.UMAP().fit_transform(proj_pca[:,:50])
outfile = prefix + ".pca50_umap.txt"
pd.DataFrame(d_embedding).to_csv(outfile, sep='\t', header=False, index=True)

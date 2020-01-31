# Dimensionality reduction methods to large-scale genotype data.
This is a repository for a source code to replicate Sakaue S. et al. 2020 (to appear).

## Overview

<div align="center">
<img src="https://raw.githubusercontent.com/saorisakaue/Genotype-dimensionality-reduction/images/fig/new_Figure2_v3.png" width=60%>
</div>

To find finest-scale population substructures, we applied a series of dimensionality reduction methods to large-scale genotype data of Japanese and also worldwide populations. We will introduce the python-based source code for replicationg our results.

## Publication
**Coming soon**

Sakaue S et al. [Dimensionality reduction enlightens the finest-scale genetic, evolutional, and phenotypic structure within the Japanese population.](https://XXX) ***Nat Commun*** 2020 (to appear)

## Requirements

- umap-learn
- scikit-learn
- scipy
- pandas
- TSNE

We would recommend you to install these dependencies using `anaconda`.

## Installation
If you want to download the scripts,
```{bash}
$ git clone https://github.com/saorisakaue/Genotype-dimensionality-reduction
$ cd ./Genotype-dimensionality-reduction
```

## Usage
Two scripts
- 01_prep_genotype.sh
- 02_run_umap.py
are used for performing dimensionality reduction on genotype data provided by the user as plink file. To run the script on the command line, simply

```{bash}
bash 01_prep_genotype.sh {path_to_your_plinkfile_prefix}
python 02_run_umap.py {path_to_your_plinkfile_prefix}
```

can do all the analyses.
Example genotype data of 50 individuals from 1KGPp3v5 is provided in ./data_umap directory.
If you use example dataset, the command line will be as follows;
```
bash 01_prep_genotype.sh ./data_umap/1KG.selected
python 02_run_umap.py ./data_umap/1KG.selected
```



## Contact
Any questions? Saori Sakaue (saori.sakaue\[at\]riken.jp)
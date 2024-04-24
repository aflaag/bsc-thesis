# Notes

## A new correlation clustering method for cancer mutation analysis

The goal of the algorithm is to cluster the vertices of the fully connected graph $G$ defined as follows:
  - each vertex $u \in V(G)$ represents a gene which shows sufficiently large mutation prevalence in cancer patients, and each edge $uv \in E(G)$ has two weights:
    - $w^+_{uv}$: this is the cost of having $u$ and $v$ in different clusters, which means that the higher the value of $w^+_{uv}$, the harder it becomes to have $u$ and $v$ in different clusters
    - $w^-_{uv}$: this is the cost of having $u$ and $v$ in the same cluster, which means that the higher the value of $w^-_{uv}$, the harder it becomes to have $u$ and $v$ in the same cluster; this is chosen to be relatively small if the endpoint genes describing the edge are deemed to be mutually exclusive in cancer patients, and a small $w^-_{uv}$ means encourages placing mutually exclusive genes within the same cluster
  - note that only the top 5% of mutated genes in cancer patients are used as vertices, because
    - low-frequency mutations require specialized statistical and network analysis methods, which are not feasable with the current number of patient samples available
    - from the obtained results it seems to be enough to outperform the state-of-the-art
    - usually only a very small number of driver genes are needed to initiate the proces of tumorigenesis

Thus, the goal of the algorithm is to partition the objects into clusters so that the edges within clusters are mostly positive, and the edges between clusters are mostly negative; this means that each cluster contains mostly mutually exclusive genes. Note that the algorithm seeks _optimal clustering_, minimizing the total number of errors, when a perfect clustering is not possible ("triangle" cases TODO: capire bene il prblema)
We can impose some restrictions on the weights, for example the _probability constraints_ give a natural restriction on the weights such that $w_e^+ + w_e^- = 1$, and the _triangle inequality_ requires that $\forall u, v, z \in V(G) \mid u \neq v \neq z \quad w_{uz}^- \le w^-_{uv} + w^-_{vz}$.

Let $n_p$ be the number of samples (i.e. patient genomes available) and let $n_g$ denote the number of genes. Also, let $A \in \mathrm{Mat}_{n_g \times n_p}(\{0, 1\})$ be the mutation data matrix, such that $a_{i, j} = 1$ if and only if gene $i$ is mutated in patient $j$. Also, let $C \in \mathrm{Mat}_{n_g \times n_p}(\mathbb Z)$ be the CNV (_copy number variation_) matrix, such that $c_{i, j}$ reflects the deviation of the CNV number (CNV is the molecular phenomenon in which sequences of the same genome are repeated, and the number of repeats varies between individuals of the same species) from its baseline. We then define the following matrix $M \in \mathrm{Mat}_{n_g \times n_p}(\{0, 1\})$ such that $m_{i, j} = 0$ if and only if $a_{i, j} = 0$ and $l_{\textrm{cnv}} \lt c_{i, j} \lt h_{\textrm{cnv}}$, where the last two values are user-specified copy number bounds, which determines what is deemed to be a significant CNV change. Finally let TODO manca la matrice Z ma ora non è rilevante

### Clustering ME-CO (Mutual Exclusivity - Coverage)

**Mutual exclusivity**: mutated driver genes in a patient tend to belong to different pathways, and the number of patients with more thatn one mutated driver gene per given pathway is small, in fact very often only one gene in each gene group is mutated at a given time in any given patient; this rule in cancer pathways is supported by the observations that, in general, one mutated gene sufficies to perturb the function of its corresponding pathway, and multiple mutations would require significantly higher energy investments on the part of cancer cell, and are hence selected against.

**Coverage**: it's the number of patients in which the same mutation is observed, hence high coverage postulates that important driver pathway should be mutated in as many patients as possible.

## Databases

- The Cancer Genome Atlas (TCGA)
- Catalogue Of Somatic Mutations In Cancer (COSMIC)
- International Cancer Genome Consortium (ICGC)
- Genomics of Drug Sensitivity in Cancer (GDSC)
- OncoDB
- OncoVar
- Protein Data Bank (PDB)

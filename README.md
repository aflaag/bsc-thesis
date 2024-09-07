# thesis-notes

## Domande

## TODO list

- [use and rework this somewhere](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4590705/)
    Suppose that in a given large set of viable (cancer) cells, a pair of genes exhibits mutual exclusivity with respect to a genetic event – i.e. each gene individually is affected by the genetic event in most large proportions of cells but both genes are simultaneously affected in few or none. We hypothesize that the observed viability of these cells is dependent on, or a consequence of, the mutual exclusivity between the two genes: cells are not viable if the genetic event were to affect both genes simultaneously, and therefore we observe that few if any viable cells in our population carry such an event in both genes (in other words, the mutually exclusive combinations constitute the (clonally) selected combinations amenable to cell survival). Consequently, we infer that the two genes are synthetic lethal with each other.

- consistency nella notazione

- metti inizio/fine chap 3 il perché abbiamo tanti algoritmi (perché?)
- lavoro critico

- CAMBIARE TUTTI GLI ACRONIMI

- passa tutto a ly

- fai tbf e tit per leggibilità

- capire come aumentare lo spazio tra table e caption
- abstract

- check thesis.tex
- check references.bib

## Paper per allungare

- [co-occorrenza e mutua esclusività](https://www.sciencedirect.com/science/article/abs/pii/S2405803321001011) ([sci-hub](https://sci-hub.ru/https://doi.org/10.1016/j.trecan.2021.04.009)))
- [synthetic lethality e hypergeometric test](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4590705/)
- [signaling pathways: target therapy e treatments](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8002322/) (questo paper è molto complesso è quasi solo biologia, si potrebbe usare per allungare prendendo qualcosa dai trafiletti introduttivi)
- [target therapy](https://www.cancer.org/cancer/managing-cancer/treatment-types/targeted-therapy/what-is.html)

Input:
    - G: Set of genes
    - A: Binary matrix of genomic alterations (e.g., mutations, CNAs) across samples (rows = genes, columns = samples)
    - PPI: Protein-Protein Interaction (PPI) network data (as an adjacency list or matrix)
    - K: Number of top gene groups to identify
    - N: Number of permutations for significance estimation
    - alpha: Significance level for p-value threshold

Output:
    - List of significant mutually exclusive gene groups

Step 1: Initialize Data Structures
    - Groups <- empty list to store top mutually exclusive gene groups
    - Scores <- empty dictionary to store exclusivity scores for each gene pair/group
    - NullDistributions <- empty dictionary to store null distribution of scores for significance estimation
    - ObservedPValues <- empty dictionary to store empirical p-values for each group

Step 2: Calculate Observed Mutual Exclusivity Scores
    For each gene pair (g1, g2) in G:
        1. Extract alteration profiles for g1 and g2 from A:
            - Alterations_g1 <- A[g1]
            - Alterations_g2 <- A[g2]
        2. Compute the Mutual Exclusivity (ME) score for the pair (g1, g2):
            - Exclusive_g1 <- (Number of samples with alteration in g1 but not in g2)
            - Exclusive_g2 <- (Number of samples with alteration in g2 but not in g1)
            - Shared <- (Number of samples with alterations in both g1 and g2)
            - ME_Score(g1, g2) <- (Exclusive_g1 + Exclusive_g2) / (Exclusive_g1 + Exclusive_g2 + Shared)
        3. Store ME_Score(g1, g2) in Scores[(g1, g2)]

Step 3: Expand Gene Pairs into Groups Using PPI Network
    For each gene pair (g1, g2) in G:
        1. Identify neighbors in the PPI network:
            - Neighbors_g1 <- PPI[g1]  // genes interacting with g1
            - Neighbors_g2 <- PPI[g2]  // genes interacting with g2
            - Common_neighbors <- Neighbors_g1 ∩ Neighbors_g2
        2. Form candidate groups by adding each common neighbor (g3) to (g1, g2):
            - For each g3 in Common_neighbors:
                - Group <- (g1, g2, g3)
                - Compute ME_Score(Group) using the same method as above
                - Store ME_Score(Group) in Scores[Group]

Step 4: Generate Null Distributions
    For each gene group (Group) in Scores:
        Initialize NullDistributions[Group] as an empty list
        For i = 1 to N (number of permutations):
            1. Permute alterations for the genes in Group across samples in A:
                - For each gene g in Group:
                    - Permuted_Alterations_g <- random.shuffle(A[g])
            2. Compute ME_Score(Group) with permuted alterations:
                - ME_Score_Permuted <- Compute ME Score using permuted alterations
            3. Store ME_Score_Permuted in NullDistributions[Group]

Step 5: Calculate Empirical P-values
    For each gene group (Group) in Scores:
        1. Observed_Score <- Scores[Group]
        2. Count Null_Scores that are greater than or equal to Observed_Score:
            - Null_Count <- number of scores in NullDistributions[Group] >= Observed_Score
        3. Calculate empirical p-value:
            - p-value[Group] <- Null_Count / N
        4. Store p-value in ObservedPValues[Group]

Step 6: Correct for Multiple Hypothesis Testing
    - Sort all p-values in ObservedPValues in ascending order
    - Apply Benjamini-Hochberg correction to adjust p-values:
        - For each p-value p[i] in sorted ObservedPValues:
            - Adjusted_p[i] <- p[i] * (Total number of tests / rank of p[i])
        - Update ObservedPValues with Adjusted_p values

Step 7: Select Significant Mutually Exclusive Groups
    For each gene group in ObservedPValues:
        1. If Adjusted_p[group] < alpha:
            - Add group to the list of significant Groups

Step 8: Return Results
    - Return the list of significant mutually exclusive gene groups


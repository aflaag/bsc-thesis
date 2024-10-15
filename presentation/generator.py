import requests
import os

formulas = [
    r"a_{i, j} = 1 \iff i \ \mathrm{ha \ il \ gene \ } j \ \mathrm{mutato}",
    r"\Gamma(g) := \{i \mid a_{i, j} = 1\}",
    r"\displaystyle \Gamma(M) := \bigcup_{g \in M}{\Gamma(g)}",
    r"\forall g, g' \in M \quad \Gamma(g) \cap \Gamma(g') = \varnothing",
    r"\omega(M) := \sum_{g \in M} |\Gamma(g)| - |\Gamma(M)|",
    r"W(M) := |\Gamma(M)| - \omega(M)",
    r"W(M) := |\Gamma(M)| - 0",
    r"\times",
]

for i in range(len(formulas)):
    r = requests.get(f'https://latex.codecogs.com/svg.image?{formulas[i]}')

    with open(f"out/{i}.svg", "w+") as f:
        print(f"Saved out/{i}.svg")
        f.write(r.text)

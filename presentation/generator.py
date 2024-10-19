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
    r"\textsf{NP-completo}",
    r"I_M(j) = 1 \iff j \in M",
    r"C_i(M) = 1 \iff \exists g \in M \mid i \in \Gamma(g)",
    r"\mathrm{maximize} \sum_{i = 1}^m {\left (2 \cdot C_i(M) - \sum_{j = 1}^n I_M(j) \cdot a_{i, j} \right)},",
    r"\mathrm{subject \ to\ } \sum_{j = 1}^n{I_M(j) = k},",
    r"\sum_{j = 1}^n I_M(j) \cdot {a_{i, j}} \ge C_i(M), \quad 1 \le i \le m.",
    r"W'(M) := \sum_{\rho = 1}^t{W(M_\rho)}",
    r"P(X = \gamma(g, M_g)) = \dfrac{\dbinom{\gamma(g)}{\gamma(g, M_g)}\dbinom{m - \gamma(g)}{\gamma(M_g) - \gamma(g, M_g)}}{\dbinom{m}{\gamma(M_g)}}",
    r"M - \{g_1\}",
    r"\implies",
    r"X \sim H(m, \gamma(g), \gamma(M_g))",
    r"g_n",
    r"w^-_{uv} := w^-_{uv}(\mathrm e)",
    r"w^+_{uv} := w_1 w^+_{uv}(\mathrm c) + w_2 w^+_{uv}(\mathrm n) + w_3 w^+_{uv}(\mathrm x)",
    r"\iff",
    r"= m",
    r"\Gamma(g) \cap \Gamma(M - \{g\})",
    r"X \sim H(m, \Gamma(g), \Gamma(M - \{g\}))",
    r"s_M := \max_{g \in M}{p_g}",
    r"p_g := P(X = \Gamma(g) \cap \Gamma(M - \{g\}))",
]

for i in range(len(formulas)):
    r = requests.get(f'https://latex.codecogs.com/svg.image?{formulas[i]}')

    with open(f"out/{i}.svg", "w+") as f:
        print(f"Saved out/{i}.svg")
        f.write(r.text)

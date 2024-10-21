# Speech

## Prima parte

### Il cancro

Il cancro è un gruppo di malattie caratterizzate dalla crescita incontrollata delle cellule che invadono tessuti ed organi e ne compromettono le funzionalità. Esistono oltre 100 tipi di cancro, come _carcinomi_, _sarcomi_ e _leucemie_, ed ogni anno i decessi per il cancro sono nell'ordine dei milioni. Ciò mostra quanto sia importante trovare trattamenti efficaci contro questa malattia.

### Cure attuali

La ricerca per trovare cure e trattamenti per il cancro è in continua evoluzione, a causa della gravità e della complessità della malattia. Attualmente, le principali tecniche per rimuovere e gestire il cancro includono chirurgia, radioterapia, chemioterapia e terapia ormonale. Ma nonostante i progressi realizzati, tutti questi approcci sono tutt'ora significativamenti limitati, e possono portare a recidive tumorali e numerosi altri effetti collaterali indesiderati.

### Terapia a bersaglio

Le problematiche che caratterizzano gli attuali trattamenti del cancro hanno spinto ad un maggiore interesse per le cosiddette terapie a bersaglio. La terapia a bersaglio è un trattamento per il cancro che si concentra sulle proteine responsabili della crescita e della diffusione delle cellule tumorali. Questo terapie sono vantaggiose in quanto differiscono della chemioterapia standard, che distrugge indiscriminatamente cellule normali e tumorali, poiché sono in grado di attaccare specificamente le proteine anormali prodotte da geni mutati, offrendo dunque maggiore selettività e riducendo gli effetti collaterali.

Naturalmente, l'efficacia delle terapie a bersaglio dipende direttamente dal target considerato. È necessario dunque porsi una domanda: come è possibile trovare target adeguatamente efficaci a scopi terapeutici?

### Il ruolo delle mutazioni nel cancro

Il cancro evolve attraverso un processo multistep in cui le cellule acquisiscono gradualmente caratteristiche maligne tramite una serie di mutazioni. Infatti, lo sviluppo del cancro è come un processo di mutazione e selezione di cellule con capacità sempre maggiori di proliferare, sopravvivere e metastatizzare.

È dunque evidente che le mutazioni ricoprono un ruolo fondamentale per lo sviluppo e la progressione del cancro. Pertanto, per combattere efficacemente questa malattia, è essenziale acquisire una comprensione completa di come queste alterazioni genetiche si verificano e contribuiscono allo sviluppo del tumore.

### Tipi di mutazioni

Non tutte le anomalie presenti in un tumore sono rilevanti per la sua proliferazione. Infatti, le mutazioni del cancro sono generalmente divise in due categorie: le mutazioni _passenger_, che non conferiscono vantaggi diretti alla crescita tumorale, e le mutazioni _driver_, che invece contribuiscono direttamente alla progressione del cancro, fornendo vantaggio evolutivo e promuovendo la proliferazione delle cellule tumorali.

Dunque, poiché sono le più importanti per lo sviluppo del cancro, le mutazioni _driver_ devono essere il target delle terapie a bersaglio. Di conseguenza, riuscire a classificare le mutazioni in queste due categorie è fondamentale, al fine di riuscire a sviluppare terapie sempre più efficaci.

<!-- ### Problemi nel classificare le mutazioni -->
<!---->
<!-- Per classificare le mutazioni in queste due categorie, è essenziale valutare la loro funzione biologica, ma questo rimane tutt'ora difficile da eseguire. Esistono numerosi metodi per prevedere l'impatto funzionale di mutazioni, basati su conoscenze _a priori_. Tuttavia, questi approcci spesso non riescono a integrare le informazioni in modo efficace tra i vari tipi di mutazione e sono limitati dalla loro dipendenza da proteine conosciute, rendendoli meno efficaci per quelle meno studiate. -->
<!---->
<!-- Con la diminuzione del costo del sequenziamento del DNA, è ora possibile categorizzare le mutazioni esaminandone la frequenza, poiché le mutazioni _driver_ sono tipicamente le più ricorrenti nei genomi dei pazienti. -->
<!---->
<!-- Per geni con numero molto elevato di mutazioni, come TP53 o KRAS, la maggior parte dei metodi statistici suggerirà fortemente che questi geni siano _driver_. Tuttavia, i geni con più di una, ma comunque relativamente poche mutazioni, sono molto più comuni, e per questo tipo di geni analisi di frequenza non sono sufficienti per identificare in modo affidabile i geni _driver_. -->
<!---->
<!-- Serve dunque un approccio più efficace per cercare di classificare le mutazioni nelle due tipologie. -->

### Pathway cellulari

Un pathway cellulare è una serie di reazioni chimiche e interazioni molecolari che si verificano all'interno di una cellula. Questi pathway sono essenziali per regolare le funzioni cellulari, come la crescita, il metabolismo, la risposta a segnali esterni e l'apoptosi.

Come mostrato in figura, è possibile rappresentare le catene di reazioni dei pathway attravreso grafi diretti. La ricerca è interessata ai geni che compongono i pathway.

### Cercare i pathway _driver_

I pathway cellulari sono importanti poiché attraverso essi è possibile valutare la ricorrenza di singole mutazioni o geni, e molte considerazioni biologiche supportano questo approccio. In particolare, più mutazioni driver in geni diversi possono portare a simili effetti _downstream_, quindi il vantaggio selettivo è distribuito tra le frequenze delle varie alterazioni genetiche, ed infatti mutazioni diverse possono influenzare lo stesso pathway in vari campioni. Ciò suggerisce che l'attenzione dovrebbe concentrarsi sui pathway _driver_ piuttosto che sulle singole mutazioni driver.

Infatti, negli ultimi anni, l'attenzione si è spostata su tentativi per identificare automaticamente pathway _driver_ e gruppi di geni con mutazioni _driver_, derivandoli direttamente dai dati delle mutazioni somatiche.

### Ricerca di driver pathway

Trovare pathway _driver_ senza criterio è complesso, per via dell'enorme numero di possibili gruppi di geni da testare. Infatti, poiché il genoma umano contiene all'incirca 20,000 geni che codificano proteine, ci sono più di $10^{26}$ gruppi di $7$ geni possibili.

Questo rende necessario trovare proprietà o caratteristiche specifiche per guidare la ricerca in modo efficiente. Fortunatamente, la nostra attuale comprensione dei processi mutazionali somatici nel cancro suggerisce vincoli sui modelli di mutazione.

### Formalizzazione dei pathway _driver_

In primo luogo, gli studi suggeriscono che un pathway importante per il cancro dovrebbe essere alterato in un numero significativo di pazienti, quindi ci si aspetta che la maggior parte dei pazienti presenti aberrazioni in alcuni geni all'interno pathway _driver_.

Pertanto, si presume che i geni _driver_ che costituiscono un pathway driver frequentemente mutati in molti campioni. Questa caratteristica è misurata dalla cosiddetta copertura.

In secondo luogo, la maggior parte delle tecniche sviluppate negli ultimi anni sfrutta una proprietà statistica molto più forte, osservata nei dati dei pazienti oncologici: ogni paziente, in genere, ha un numero relativamente ridotto di mutazioni, le quali colpiscono molteplici pathway, quindi ogni percorso conterrà in media 1 mutazione driver per campione.

Questo concetto viene assiomatizzato sottoforma di mutua esclusività tra mutazioni _driver_ all'interno dello stesso pathway, e viene utilizzato dagli algoritmi di ricerca per identificare mutazioni e pathway _driver_.

Pertanto, un pathway _driver_ è costituito da geni che sono mutati in numerosi pazienti, con mutazioni approssimativamente mutuamente esclusive nel pathway.

Di conseguenza, affinché sia possibile cercare driver pathway, è necessario definire metriche efficaci che siano in grado di modellare e quantificare il livello di copertura e di mutua esclusività di un dato gruppo di geni.

## Seconda parte

### Matrice di mutazione

Una delle prime e più ampiamente utilizzate formalizzazioni matematiche per modellare e quantificare la mutua esclusività è stata introdotta da Vandin. Per illustrarla, è necessario fornire alcune definizioni preliminari.

Questa è una matrice di mutazione, una matrice binaria in cui la cella $(i, j)$ è pari ad $1$ se e solo se il paziente nella riga $i$ ha il gene nella colonna $j$ mutato. Attraverso questa matrice, è possibile dare delle definizioni ulteriori.

### Copertura di un gene

Questa formula rappresenta la copertura del gene $g$, che è data dall'insieme dei pazienti che hanno il gene $g$ mutato. Ad esempio, in figura è mostrata la copertura di $g_3$.

### Copertura di un insieme di geni

Dato un insieme di geni $M$, la copertura di $M$ è l'unione delle coperture dei geni di $M$, come mostrato a schermo. Ad esempio, per l'insieme $M = \{g_2, g_3\}$, la sua copertura è l'insieme $\{p_1, p_2, p_3\}$.

### Mutua eslcusività

Un insieme di geni è detto essere mutuamente esclusivo se le coperture dei geni che lo compongono sono a due a due disgiunte. In altre parole, $M$ è mutuamente esclusivo se non vi sono pazienti con più di una mutazione in $M$, o alternativamente, se ogni riga di $M$ contiene al massimo un $1$.

### Sovrapposizione di un insieme di geni

Per stabilire se un gruppo di geni è mutuamente esclusivo, Vandin ha introdotto la definizione di sovrapposizione di copertura di un set di geni, definita come mostrato.

Notiamo che la prima sommatoria conta tutti gli $1$ all'interno di $M$, e poiché il secondo valore della differenza è la copertura dell'insieme, $\omega(M)$ rappresenta il numero di pazienti che hanno più di una mutazione in $M$. Chiaramente, $M$ è mutuamente esclusivo se e solo se $\omega(M) = 0$.

### Peso di un gruppo di geni

Infine, la metrica principale con la quale viene calcolato il livello di ottimalità di un set di geni è dato dalla formula seguente, che sintetizza il bilanciamento tra quanti geni copre $M$, e quanto sia mutuamente esclusivo. In altre parole, $W(M)$ conta il numero di pazienti che hanno uno ed un solo $1$ all'interno delle righe di $M$.

Notiamo che è opportuno che un set di geni $M$ massimizzi tale peso, poiché maggiore sarà il peso, maggiore sarà la copertura di $M$, e minore sarà la sua sovrapposizione.

### Maximum Weight Submatrix Problem (MWSP)

La rappresentazione matriciale di set di geni $M$ permette di formulare il problema di trovare $M$ tale da massimizzare $W(M)$ come segue.

**Maximum Weight Submatrix Problem** (MWSP): Data una matrice di mutazione $A$ di dimensioni $m \times n$, ed un intero $k > 0$, si trovi una sottomatrice $m \times k$ di $A$ tale da massimizzare $W(M)$.

Questa formulazione permette di valutare la complessità del problema, ed è possibile dimostrare che l'MWSP è $\textsf{NP-completo}$, attraverso una riduzione dall'Independent Set Problem (ISP).

<!-- ### Un ILP per l'MWSP -->
<!---->
<!-- Una delle implementazioni più dirette dell'MWSP è stata fornita da Leiserson, attraverso un Integer Linear Program (ILP). Per introdurlo, è necessario descrivere le seguenti variabili indicatrici: -->
<!--   - $I_M(j)$ è la variabile indicatrice che descrive l'insieme di geni $M$, ed è definita come segue: $I_M(j) = 1 \iff j \in M$, dunque $I_M(j)$ è $1$ se e solo se $j$ appartiene ad $M$; -->
<!--   - $C_i(M)$ è la variabile indicatrice che descrive quali pazienti copre $M$, ed è definita come segue: $C_i(M) = 1 \iff \exists g \in M \mid i \in \Gamma(g)$, dunque $C_i(M)$ è $1$ se e solo se esiste un paziente $i$ che ha un gene di $M$ mutato. -->
<!---->
<!-- Attraverso queste funzioni indicatrici, è possibile formulare l'MWSP come mostrato. In particolare, notiamo che il primo constraint rappresenta $W(M)$, il secondo forza $M$ ad avere dimensione $k$, ed infine il terzo descrive il comportamento di $C_i(M)$. -->

### Multiple Maximum Weight Submatrix Problem (MMWSP)

Sebbene l'identificazione di singoli pathway driver sia fondamentale per la ricerca e il trattamento del cancro, si è osservato che la maggior parte dei pazienti oncologici presenta mutazioni driver in molteplici pathway. Per questo motivo, studi successivi hanno esteso l'MWSP, al fine di trovare più _driver_ pathway contemporaneamente. In particolare, questo problema utilizza $W'(M)$, una metrica permette di valutare il livello di copertura e mutua esclusività di una collezione di insiemi di geni.

**Multiple Maximum Weight Submatrices Problem** (MMWSP): Data una matrice di mutazione $A$ di dimensioni $m \times n$, ed un intero $t > 0$, si trovi la collezione $M = \{M_1, \ldots, M_t\}$ di sottomatrici colonna di $A$ che massimizzi $W'(M) := \sum_{\rho = 1}^t{W(M)}$.

Analogamente al caso $t = 1$, anche questo problema è $\textsf{NP-completo}$.

### Approcci statistici

La metrica sviluppata da Vandin, ossia il peso $W(M)$, ha un'importante limitazione: assume che i pathway _driver_ abbiano i geni esattamente mutuamente esclusivi, ma nei dati somatici reali, l'esatta mutua eslcusività si verifica raremente. Questo significa che risolvere l'MWSP potrebbe non tenere in considerazione di soluzioni subottimali che non necessariamente massimizzano $W(M)$, ma che sono comunque pathway _driver_ nella realtà. Per questo motivo, approcci statistici tendono a performare meglio per questa tipologia di ricerca. Ad esempio, Babur ha sviluppato una metrica basata su una distribuzione ipergeometrica, che verrà ora illustrata.

### Ipotesi nulla

Babur definisce la seguente ipotesi nulla $H_0$: _dato un grupo di geni $M$, un membro del gruppo $g \in M$ è alterato indipendentemente dall'unione delle altre alterazioni del gruppo $\Gamma(M - \{g\})$_.

Ad esempio, se consideriamo il seguente gruppo di geni $M = \{g_1, g_2, g_3, g_4\}$ e le loro rispettive alterazioni nei pazienti. Questa ipotesi nulla assume che qualsiasi pattern osservato all'interno delle alterazioni di $M$ è dovuto al caso.

Per testare $H_0$ è necessario valutare la probabilità di avere $\Gamma(g) \cap \Gamma(M - \{g\})$ pazienti che hanno sia $g$ sia qualsiasi altro gene di $M$ mutato.

### Punteggio di un insieme di geni

Sia $X$ la variabile aleatoria che rappresenta il numero di pazienti aventi sia $g$ che un qualsiasi altro gene di $M - {g}$ mutato. Chiaramente, $X$ segue una distribuzione ipergeometrica.

Dunque, il $p$-value associato ad un gene è proprio la probabilità di avere $X = \Gamma(g) \cap \Gamma(M - \{g\})$, ed il punteggio di un insieme di geni $M$ è dato dal massimo dei $p$-value dei geni di $M$. Viene scelto il massimo per rimanere conservativi sul punteggio ottenuto.

### Algoritmo genetico

Esistono anche molti altri approcci che permettono di trovare pathway _driver_. Un esempio è dato dall'algoritmo genetico di Zhao che utilizza il peso di Vandin come funzione di _fitness_.

Nel suo algoritmo genetico, ogni membro della popolazione è una stringa binaria che rappresenta un possibile insieme di geni $M$: l'$i$-esimo bit è 1 se e solo se l'$i$-esimo gene è in $M$. Dunque, lo spazio dei membri possibili è dato da tutte le stringhe binarie lunghe $n$ aventi $k$ bit pari ad $1$.

Infine, il _crossover_ tra membri della popolazione è definito come mostrato: dati due membri della popolazione, i bit uguali vengono ereditati dalla prole, mentre i bit diversi vengono scelti casualmente.

### Algoritmo di clustering

In ultimo, sono presenti in letteratura anche approcci clustering di vertici su grafi completamente conenssi i cui vertici rappresentano geni, ed i cluster sono i pathway _driver_ cercati.

Un esempio di questo approccio è dato dall'algoritmo di Hou, che dato un grafo di geni come mostrato, assegna ad ogni arco 2 pesi, uno positivo ed uno negativo, e definisce i pesi attraverso combinazioni lineari di componenti di:
  - mutua esclusività
  - copertura
  - informazioni sulla topologia della rete
  - informazioni sull'espressione genomica

### Risultati

TODO DA RISCRIVERE

Il signaling pathway p53 che coinvolge TP53 e CDKN2A è stato identificato da Dendrix, Multi-Dendrix e MDPFinder.

Il signaling pathway RTK/RAS/PI(3)K, che include geni come EGFR, PTEN, PIK3R1 e PIK3CA, appare nei risultati di Dendrix, Multi-Dendrix e MDPFinder.

Il signaling pathway RB, che coinvolge geni come RB1 e CDK4, è stato identificato sia in Dendrix che in Multi-Dendrix, in particolare per il glioblastoma multiforme (GBM).

Infine, geni comuni rilevanti per il GBM, come EGFR, RB1, BRAF e GLI1, sono stati evidenziati nei metodi Dendrix, Multi-Dendrix, MDPFinder e $\mathrm{C}^3$.

### Lavori futuri

L'identificazione dei pathway _driver_ e la capacità di misurare fenomeni genomici chiave offrono prospettive promettenti per migliorare l'efficacia delle terapie a bersaglio, che potrebbero portare a trattamenti più personalizzate ed adattati ai profili genetici unici di ogni paziente.

Future ricerche potrebbero integrare tecnologie emergenti, come il _single-cell sequencing_, per affinare ulteriormente la comprensione dei pathway _driver_. Inoltre, sarebbe interessante provare a sviluppare algoritmi che permettano di tenere in considerazione l'eterogeneità tumorale ed i meccanismi di resistenza adattativa alle terapie a bersaglio.

### Grazie per l'attenzione

Grazie per l'attenzione.

<!-- ## Dendrix -->
<!---->
<!-- - lung adenocarcinoma -->
<!--     - novel triplet (EGFR, KRAS, STK11), only the pair (EGFR, KRAS) was known -->
<!--     - novel pair (ATM, TP53) -->
<!-- - GBM -->
<!--     - novel pair (CDKN2B, CYP27B1) -->
<!--     - novel triplet (CDKN2B, RB1, CDK4), important for the RB1 signaling pathway -->
<!--     - novel pair (TP53, CDKN2A), linked to the p53 tumor suppressor pathway -->
<!--     - novel pair (NF1, EGFR), part of the RTK pathway -->
<!---->
<!-- ## Multi-Dendrix -->
<!---->
<!-- - GBM -->
<!--     - IRF5 -->
<!--     - MSL3 in RB signaling pathway -->
<!--     - IDH1 mutually exclusive with (PTEN,PIK3CA, PIK3R1) in RTK/RAS/PI(3)K pathway -->
<!--     - NPAS3 in p53 signaling pathway -->
<!--     - (EGFR, PDGFRA, RB1) in RTK/RAS/PI(3)K and RB pathways -->
<!-- - BRCA -->
<!--     - 12p in PI(3)K/AKT pathway -->
<!--     - (TP53, CDH1, GATA3, CTCF, GPRIN2) in p53 signaling pathway -->
<!--     - (MAP2K4, MAP3K1, PPEF1, SMARCA4, WWP2) in p38-JNK1 signaling pathway -->
<!--     - (CCDN1, MAP2K4, RB1, GRID1) in cell cycle progression -->
<!---->
<!-- ## MDPFinder -->
<!---->
<!-- - HNSCC -->
<!--     - (ANO4, CDKN2A, NFE2L2, NOTCH1, SYNE1, TP63) linked to squamous epithelia differentiation -->
<!--     - (CDKN2A, NOTCH1, TP63, SYNE1) -->
<!-- - GBM -->
<!--     - novel pair (CDKN2A, TP53) in p53 signaling pathway -->
<!--     - novel 5-tuple (PTEN, EGFR, PIK3R1, PIK3CA, GRIA2) in RTK/RAS/PI(3)K signaling pathway -->
<!-- - ovarian carcinoma -->
<!--     - (KRAS, NF1, MAPK8IP2) linked to MAPK signaling pathway -->
<!---->
<!-- ## Mutex -->
<!---->
<!-- - N/A -->
<!--     - OBSCN -->
<!--     - ARID1 -->
<!--     - RHOC in cancer metastasis -->
<!--     - TRRAP, OBSCN, RIT1, AGAP2, and RORC contain mutation hotspots -->
<!--     - (CERS2, NCSTN) showed CNAs -->
<!---->
<!-- ## C^3 -->
<!---->
<!-- - N/A -->
<!--     - novel cluster (PTEN, HUWE1, CNTNAP2, GRID2, CACNA1B, CYSLTR2, MYH1) -->
<!--     - HUWE1, CNTNAP2, and GLI1 potential drivers -->
<!-- - GBM -->
<!--     - novel cluster (GLI1, WNT2, BRAF, PLCG1, ...) linked to many cell processes -->
<!---->

# Speech

## Prima parte

### Il cancro

Il cancro è un gruppo di malattie caratterizzate dalla crescita incontrollata delle cellule che invadono tessuti ed organi e ne compromettono le funzionalità. Esistono oltre 100 tipi di cancro, come carcinomi, sarcomi e leucemie, ed ogni anno i decessi per il cancro sono nell'ordine dei milioni. Dunque, è fondamentale trovare trattamenti efficaci contro questa malattia.

### Cure attuali

La ricerca per trovare cure e trattamenti per il cancro è in continua evoluzione, a causa della gravità e della complessità della malattia. Attualmente, le principali tecniche per rimuovere e gestire il cancro includono chirurgia, radioterapia, chemioterapia e terapia ormonale. Ma nonostante i progressi realizzati, tutti questi approcci sono attualmente significativamenti limitati, e possono portare a recidive tumorali e numerosi altri effetti collaterali indesiderati.

### Terapia a bersaglio

Le problematiche che caratterizzano gli attuali trattamenti del cancro hanno spinto ad un maggiore interesse per le cosiddette terapie a bersaglio. La terapia a bersaglio è un trattamento per il cancro che si concentra sulle proteine responsabili della crescita e della diffusione delle cellule tumorali. Queste terapie sono vantaggiose in quanto differiscono dai trattamenti standard, che distruggono indiscriminatamente cellule normali e tumorali, poiché sono in grado di attaccare specificamente le proteine anormali prodotte da geni mutati, offrendo dunque maggiore selettività e riducendo gli effetti collaterali.

Naturalmente, l'efficacia delle terapie a bersaglio dipende direttamente dal target considerato. È necessario dunque chiedersi quali target possano massimizzare la resa terapeutica.

### Il ruolo delle mutazioni nel cancro

Il cancro evolve attraverso un processo _multistep_ in cui le cellule acquisiscono gradualmente caratteristiche maligne tramite una serie di mutazioni. Infatti, lo sviluppo del cancro consiste in un processo di mutazione e selezione di cellule con capacità sempre maggiori di proliferare, sopravvivere e metastatizzare.

È dunque evidente che le mutazioni ricoprono un ruolo fondamentale per lo sviluppo e la progressione del cancro. Pertanto, per combattere efficacemente questa malattia, è essenziale acquisire una comprensione completa di come queste alterazioni genetiche si verificano e contribuiscono allo sviluppo del tumore.

### Tipi di mutazioni

Non tutte le anomalie presenti in un tumore sono rilevanti per la sua proliferazione. Infatti, le mutazioni del cancro sono generalmente divise in due categorie: le mutazioni _passenger_, che non conferiscono vantaggi diretti alla crescita tumorale, e le mutazioni _driver_, che invece contribuiscono direttamente alla progressione del cancro, fornendo vantaggio evolutivo e promuovendo la proliferazione delle cellule tumorali.

Dunque, poiché sono le più importanti per lo sviluppo del cancro, le mutazioni _driver_ devono essere il target delle terapie a bersaglio.

Di conseguenza, riuscire a classificare le mutazioni in queste due categorie è fondamentale, al fine di riuscire a sviluppare terapie sempre più efficaci.

### Pathway cellulari

Un pathway cellulare è una serie di reazioni chimiche e interazioni molecolari che si verificano all'interno di una cellula. I pathway cellulari sono essenziali per regolare le funzioni cellulari, come la crescita, il metabolismo, la risposta a segnali esterni e l'apoptosi.

Come mostrato in figura, è possibile rappresentare le catene di reazioni dei pathway attravreso grafi diretti. La ricerca è interessata ai geni che compongono i pathway.

### Cercare i pathway _driver_

I pathway cellulari sono importanti poiché attraverso essi è possibile classificare le mutazioni del cancro, e molte considerazioni biologiche supportano questo approccio.

In particolare, più mutazioni driver in geni diversi possono portare a simili effetti _downstream_, quindi il vantaggio selettivo è distribuito tra le frequenze delle varie alterazioni genetiche, ed infatti mutazioni diverse possono influenzare lo stesso pathway in vari campioni.

Negli ultimi anni, l'attenzione si è spostata su tentativi per identificare automaticamente pathway _driver_ e gruppi di geni con mutazioni _driver_, derivandoli direttamente dai dati delle mutazioni somatiche.

### Problemi nel cercare i pathway

Trovare pathway _driver_ senza criterio è complesso, per via dell'enorme numero di possibili gruppi di geni da testare. Infatti, poiché il genoma umano contiene all'incirca 20,000 geni che codificano proteine, ci sono più di $10^{26}$ gruppi di $7$ geni possibili.

Questo rende necessario trovare proprietà o caratteristiche specifiche per guidare la ricerca in modo efficiente. Fortunatamente, la nostra attuale comprensione dei processi mutazionali somatici nel cancro suggerisce vincoli sui modelli di mutazione.

### Formalizzazione dei pathway _driver_

In primo luogo, gli studi suggeriscono che un pathway importante per il cancro dovrebbe essere alterato in un numero significativo di pazienti, quindi ci si aspetta che la maggior parte dei pazienti presenti aberrazioni in alcuni geni all'interno pathway _driver_. Pertanto, si presume che i geni _driver_ che costituiscono un pathway driver siano frequentemente mutati in molti campioni. Questa caratteristica è misurata dalla cosiddetta copertura.

In secondo luogo, la maggior parte delle tecniche sviluppate negli ultimi anni sfrutta una proprietà statistica molto più forte, osservata nei dati dei pazienti oncologici: ogni paziente, in genere, ha un numero relativamente ridotto di mutazioni, le quali colpiscono molteplici pathway, quindi ogni percorso conterrà in media 1 mutazione driver per campione.' Questo concetto viene assiomatizzato sottoforma di mutua esclusività tra mutazioni _driver_ all'interno dello stesso pathway, e viene utilizzato dagli algoritmi di ricerca per identificare mutazioni e pathway _driver_.

Pertanto, un pathway _driver_ è costituito da geni che sono mutati in numerosi pazienti, con mutazioni approssimativamente mutuamente esclusive nel pathway.

Di conseguenza, affinché sia possibile cercare driver pathway, è necessario definire metriche efficaci che siano in grado di modellare e quantificare il livello di copertura e di mutua esclusività di un dato gruppo di geni.

## Seconda parte

### Matrice di mutazione

Consideriamo la seguente formalizzazione del problema.

Questa è una matrice di mutazione, una matrice binaria in cui la cella $(i, j)$ è pari ad $1$ se e solo se il paziente nella riga $i$ ha il gene nella colonna $j$ mutato. Attraverso questa matrice, è possibile dare delle definizioni ulteriori.

### Copertura di un gene

Questa formula rappresenta la copertura del gene $g$, che è data dall'insieme dei pazienti che hanno il gene $g$ mutato. Ad esempio, in figura è mostrata la copertura di $g_3$.

### Copertura di un insieme di geni

Dato un insieme di geni $M$, la copertura di $M$ è l'unione delle coperture dei geni di $M$, come mostrato a schermo. Ad esempio, per l'insieme $M = \{g_2, g_3\}$, la sua copertura è l'insieme $\{p_1, p_2, p_3\}$.

### Mutua eslcusività

Un insieme di geni è detto essere mutuamente esclusivo se le coperture dei geni che lo compongono sono a due a due disgiunte. In altre parole, $M$ è mutuamente esclusivo se non vi sono pazienti con più di una mutazione in $M$, o alternativamente, se ogni riga di $M$ contiene al massimo un $1$.

### Sovrapposizione di un insieme di geni

Per stabilire se un gruppo di geni è mutuamente esclusivo, possiamo introdurre la definizione di sovrapposizione di copertura di un set di geni, definita come mostrato.

Notiamo che la prima sommatoria conta tutti gli $1$ all'interno di $M$, e poiché il secondo valore della differenza è la copertura dell'insieme, $\omega(M)$ rappresenta il numero di pazienti che hanno più di una mutazione in $M$. Chiaramente, $M$ è mutuamente esclusivo se e solo se $\omega(M) = 0$.

### Peso di un gruppo di geni

Infine, la metrica principale con la quale viene calcolato il livello di ottimalità di un set di geni è dato dalla formula seguente, che sintetizza il bilanciamento tra quanti geni copre $M$, e quanto $M$ sia mutuamente esclusivo. In altre parole, $W(M)$ conta il numero di pazienti che hanno uno ed un solo $1$ all'interno delle righe di $M$.

Notiamo che è opportuno che un set di geni $M$ massimizzi tale peso, poiché maggiore sarà il peso, maggiore sarà la copertura di $M$, e minore sarà la sua sovrapposizione.

### Maximum Weight Submatrix Problem (MWSP)

La rappresentazione matriciale di set di geni $M$ permette di formulare il problema di trovare $M$ tale da massimizzare $W(M)$ come segue.

**Maximum Weight Submatrix Problem** (MWSP): Data una matrice di mutazione $A$ di dimensioni $m \times n$, ed un intero $k > 0$, si trovi una sottomatrice $m \times k$ di $A$ tale da massimizzare $W(M)$.

Questa formulazione permette di valutare la complessità del problema, ed è possibile dimostrare che l'MWSP è $\textsf{NP-completo}$. Ne segue che è necessario sviluppare approcci ulteriori per poter approssimare il problema.

### Approcci alla ricerca dei pathway

Gli studi analizzati adottano principalmente le seguenti 4 tecniche: ILP, approcci statistici, algoritmi genetici ed approcci di clustering.

### Un ILP per l'MWSP

Partendo dalla prima, definendo delle variabili indicatrici, è possibile definire il seguente ILP; in particolare, notiamo che il primo constraint rappresenta $W(M)$, il secondo forza $M$ ad avere dimensione $k$, ed infine il terzo descrive il comportamento di una delle variabili indicatrici.

Questo approccio, sebbene sia molto veloce nella pratica grazie alla velocità degli ILP solver, non riduce la complessità del problema, poiché risolvere gli ILP è anch'esso un problema $\textsf{NP-completo}$.

### Approccio probabilistico

Consideriamo dunque il seguente approccio probabilistico, basato sulla seguente ipotesi nulla: _dato un grupo di geni $M$, un membro del gruppo $g \in M$ è alterato indipendentemente dall'unione delle altre alterazioni del gruppo $\Gamma(M - \{g\})$_.

Ad esempio, se consideriamo il seguente gruppo di geni $M = \{g_1, g_2, g_3, g_4\}$ e le loro rispettive alterazioni nei pazienti. Questa ipotesi nulla assume che qualsiasi pattern osservato all'interno delle alterazioni di $M$ è dovuto al caso.

Per testare tale ipotesi nulla, è necessario valutare la probabilità di avere $\Gamma(g) \cap \Gamma(M - \{g\})$ pazienti che hanno sia $g$ sia qualsiasi altro gene di $M - \{g\}$ mutato.

Sia dunque $X$ la variabile aleatoria che rappresenta il numero di pazienti aventi sia $g$ che un qualsiasi altro gene di $M - {g}$ mutato. Chiaramente, $X$ segue una distribuzione ipergeometrica.

Dunque, il $p$-value associato ad un gene è proprio la probabilità di avere $X = \Gamma(g) \cap \Gamma(M - \{g\})$, ed il punteggio di un insieme di geni $M$ è dato dal massimo dei $p$-value dei geni di $M$. Viene scelto il massimo per rimanere conservativi sul punteggio ottenuto.

### Approccio genetico

Passando all'approccio successivo, l'algoritmo genetico utilizza la stessa funzione di peso $W(M)$ precedentemente definita, ed ogni membro della popolazione è una stringa binaria che rappresenta un possibile insieme di geni $M$: l'$i$-esimo bit è 1 se e solo se l'$i$-esimo gene è in $M$. Dunque, lo spazio dei membri possibili è dato da tutte le stringhe binarie lunghe $n$ aventi $k$ bit pari ad $1$.

Infine, il _crossover_ tra membri della popolazione è definito come mostrato: dati due membri della popolazione, i bit uguali vengono ereditati dalla prole, mentre i bit diversi vengono scelti casualmente.

### Approccio di clustering

In ultimo, sono presenti in letteratura anche approcci clustering di vertici su grafi completamente conenssi i cui vertici rappresentano geni, ed i cluster sono i pathway _driver_ cercati.

Un esempio di questo è descritto come segue, in cui ad ogni arco sono assegnati arco 2 pesi, uno positivo ed uno negativo, e vengono definiti pesi attraverso combinazioni lineari di formule che calcolano:
  - mutua esclusività
  - copertura
  - informazioni sulla topologia della rete
  - informazioni sull'espressione genomica

### Risultati

A schermo sono mostrati gli insiemi dei gruppi di geni che massimizzano copertura e mutua esclusività, trovati dai vari algoritmi analizzati all'interno di questo lavoro.

In particolare, Dendrix è descritto dall'ILP trattato precedentemente, Multi-Dendrix estende l'MWSP per cercare una collezione di insiemi che massimizzi la somma dei pesi, MDPFinder utilizza l'algoritmo genetico, e $\mathrm{C}^3$ sfrutta un algoritmo di clustering descritto attraverso un LP.

### Lavori futuri

L'identificazione dei pathway _driver_ e la capacità di misurare fenomeni genomici chiave offrono prospettive promettenti per migliorare l'efficacia delle terapie a bersaglio, che potrebbero portare a trattamenti più personalizzati ed adattati ai profili genetici unici di ogni paziente.

Future ricerche potrebbero integrare tecnologie emergenti, come il _single-cell sequencing_, per affinare ulteriormente la comprensione dei pathway _driver_.

Inoltre, sarebbe interessante provare a sviluppare algoritmi che permettano di tenere in considerazione l'eterogeneità tumorale ed i meccanismi di resistenza adattativa alle terapie a bersaglio.

### Grazie per l'attenzione

Grazie per l'attenzione.

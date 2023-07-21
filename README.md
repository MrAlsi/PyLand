# PyLand


# CODING RULES

  
**1. Indentazione e formattazione**

Con il tab

  

**2. Nomenclatura**

Variabili con snake_case. Classi con maiuscola. Funzioni o metodi con verbo che descrivono l’azione

  

**3. Commenti**

Funzioni: sopra.
Codice: Prima dei blocchi

  

**4. Gestione degli errori**

Lettura da console per capire la natura dell’errore.

  

**5. Organizzazione dei files**

Da definire in corso d’opera


# Descrizione del progetto

Una breve introduzione che spiega lo scopo e l'obiettivo del progetto.
Lo scopo del progetto è quello di permettere all'utente di esplorare e divertirsi nel mondo di **PyLand**, un luogo pieno di sfide che aspettano solo te!!!

Gli obiettivi base del progetto erano quelli di:
- Creare  un gioco di ruolo multigiocatore online in cui i giocatori possono creare e personalizzare i loro personaggi.
- Creare un mondo con diverse aree da esplorare e missioni da completare sconfiggendo dei mostri.
- Gestione dei combattimenti tra personaggio e mostri, attraverso l'uso di oggetti e abilità a secondo della classe scelta all'inizio del gioco.

Oltre ad essi abbiamo reso l'esperienza del giocatore ancora più divertente attraverso frasi uniche e immagini in ASCII indimenticabili

Inoltre abbiamo già creato una base per implementare le armature, indossabili dall'utente e determinanti in battaglia. in futuro ci aspettiamo di implementare **l'Arena** dove gli utenti possono scontrarsi tra di loro 

# Installation requirements
Abbiamo usato diverse librerie per realizzare questo progetto, quindi prima di utilizzarlo assicurati di averle installate nel tuo ambiente virtuale!

    import time
    import os
    import pymongo
    import random
    import sys
    import math

# Struttura dei file

* **Classi**: Cartella contenente i file .py in cui vengono definite le classi.
* **objects**: Contiene degli script in cui definiamo degli oggetti, che poi importiamo nello script principale
* **DB**: Contiene il file che permette di gestire le operazioni con il DB. Nel DB sono salvati i giocatori.
* **Character_Loading.py**: gestisce il caricamento dei giocatori da DB o la creazione di un nuovo giocatore
* **game.py**: script che gestisce il gioco e l'interazione con i vari personaggi
* **main.py** script che permette di lanciare il gioco (implementa le funzionalità dallo script `game.py` e `Character_Loading.py`)


# Qualche insight sul mondo virtuale che abbiamo creato

Prima di iniziare a giocare, ti verrà chiesto di creare un personaggio o caricarne uno, nel caso avessi già giocato.

Una volta terminata questa prima parte, inizia il gioco vero e proprio. All'utente si presenterà un menù, e potrà scegliere cosa fare all'interno di PyLand interagendo con la Console del proprio IDE.

Di seguito riportiamo il menù che viene stampato, spiegandone i vari punti.

    print("1. Esplora Locations")  
    print("2. Esplora missioni")  
    print("3. Fai una missione (combatti con un mostro)")  
    print("4. Vai dal fabbro")  
    print("5. Vai in locanda")  
    print("6. Vai al lago")  
    print("7. Vai in montagna")  
    print("8. Visualizza stato giocatore")  
    print("9. Esci\n")



**1. Esplora Locations**

Permette all'utente di iniziare a interfacciassi con il mondo di **PyLand**.
Verrà mostrato un menù con tutti i possibili luoghi visitabili. Tramite interazione con console sarà possibile esplorare i luoghi o tornare al menù principale.
Esempio di cosa succede se premiamo `1`:

    Cosa vuoi fare?>? 1
    Ci sono quattro luoghi che puoi visitare! Su quale vorresti avere maggiori info?
    1. Fabbro
    2. Locanda
    3. Lago
    4. Montagna
    5. Premi un tasto a caso per tornare in città
    Entra il numero della location che vuoi visitare: 

**2. Esplora missioni**

Stampa le missioni disponibili. Esistono tre tipi di missione: facile, media e difficile. Nella missione di livello facile si affronta uno a caso fra vari mostri di livello facile, e così anche per gli altri livelli. Quando un giocatore vuole completare una missione, gliene verrà associata una in base al suo livello. In particolare:

* `livello < 3`: missione facile. Combatti contro un mostro di livello facile;
* `3 < livello < 6`: missione media. Combatti contro un mostro di livello medio;
* `livello > 6`: missione difficile. Combatti contro un mostro di livello difficile;

**3. Fai una missione (combatti contro un mostro)**

Permette al giocatore di impegnarsi in una missione. Se il giocatore non sta indossando nessun arma, gli verrà chiesto se vuole equipaggiarne una presente nell'inventario per il combattimento. Se il giocatore non ha armi nell'inventario, allora combatterà a mani nude!

Sono possibili due output:
* Il giocatore sconfigge il mostro, e quindi guadagna esperienza;
* Il giocatore viene sconfitto dal mostro, e quindi `GAME OVER`

**4. Vai dal fabbro** 

Permette di andare a visitare il fabbro. Ti si aprirà un menù tramite il quale potrai scegliere che azione compiere:

    1. Acquista arma
    2. Vendi arma
    3. Upgrade Arma
    4. Visualizza le armi che hai nell'inventario
    5. Saluta il fabbro

1. Acquista arma: mostra una lista di armi acquistabili e permette al giocatore di comprarne una, se ha abbastanza soldi nel portafoglio. 
2. Vendi arma. Permette al giocatore di vendere un'arma al fabbro, ovviamente a un prezzo molto ridotto rispetto a quello di acquisto.
3. Upgrade arma: permette al giocatore di migliorare un'oggetto arma che possiede, aumentandone attacco base e livello..
4. Visualizza le armi che hai nell'inventario: permette al giocatore di visualizzare le armi che ha in inventario
5. Sauta il fabbro: permette al giocatore di tornare al menù principale.

**5. Vai in locanda**

Permette di andare a visitare la locanda. Ti si aprirà un menù tramite il quale potrai scegliere che azione compiere:

    1. Bevi una birra
    2. Affitta una camera
    3. Esci dalla locanda

1. Bevi una birra: chiede al giocatore quante birre vuole bere. Ogni birra ha un prezzo e fa aumentare i punti vita del giocatore
2. Affitta una camera: permette al giocatore di dormire in locanda e recuperare punti vita.
3. Esci dalla locanda: torna al menù principale

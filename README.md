# GNOME battery case using an external plug
v0.1 - just an initial tentative

GNOME Battery Notifier è un'applicazione desktop progettata per prolungare la vita della batteria di un notebook, qualora il firmware del bios non preveda una funzionalità specifiche che possa essere sfruttata da tool quali TLP.
In tal caso, questo progetto offre un workarond avvalendosi di uno smart plug esterno in grado di ricevere delle chiamate REST sulla stessa rete del notebook: quando il livello di carica della batteria supera una determinata soglia (di base il 75%), appare una notifica e lo smart plug viene disattivato. Quando la batteria, scaricandosi, raggiunge il 50% di carica, lo smart plug viene riattivato.

## Requisiti

Assicurati di avere installato Python 3 e i seguenti pacchetti:

- `notify2`: per la gestione delle notifiche.
- `psutil`: per il monitoraggio delle informazioni sulla batteria.
- `requests`: per l'invio delle chiamate http.

Puoi installare le dipendenze eseguendo:

```
pip install -r requirements.txt
```

## Installazione

1. Clona il repository:

   ```
   git clone <URL_DEL_REPOSITORY>
   cd gnome-battery-notifier
   ```

2. Installa il pacchetto:

   ```
   python setup.py install
   ```

## Utilizzo

Per avviare l'applicazione, esegui il seguente comando:

```
python src/main.py
```

L'applicazione inizierà a monitorare il livello della batteria e mostrerà una notifica quando la carica supera il 75%.

## Contribuire

Se desideri contribuire a questo progetto, sentiti libero di aprire una pull request o segnalare problemi.

## Licenza

Questo progetto è concesso in licenza sotto la MIT License. Vedi il file LICENSE per ulteriori dettagli.

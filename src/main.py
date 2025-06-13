import time
import requests
import psutil
import notify2

MAX_THRESHOLD = 75  # percentuale di carica oltre cui spegnere lo smart plug
MIN_THRESHOLD = 45  # percentuale di carica sotto cui accendere lo smart plug

def main():
    notify2.init("GNOME Battery Notifier")
    notified_max = False
    notified_min = False

    while True:
        battery = psutil.sensors_battery()
        if battery is None:
            print("Nessuna batteria rilevata.")
            break

        percent = battery.percent

        if percent >= MAX_THRESHOLD and not notified_max:
            n = notify2.Notification(
                "Batteria quasi carica",
                f"La batteria è al {percent:.0f}%. Spengo lo smart plug",
                "dialog-information"
            )
            response = requests.get("http://192.168.1.73/relay/0?turn=off")
            if response.status_code == 200:
                 print("Risposta ricevuta:", response.text)
            else:
                 print("Errore nella richiesta:", response.status_code)

            n.set_urgency(notify2.URGENCY_NORMAL)
            n.show()
            notified_max = True
            notified_min = False  # resetta l'altro flag
        elif percent < MAX_THRESHOLD:
            notified_max = False

        if percent <= MIN_THRESHOLD and not notified_min:
            n = notify2.Notification(
                "Batteria quasi scarica",
                f"La batteria è al {percent:.0f}%. Accendo lo smart plug",
                "dialog-information"
            )
            response = requests.get("http://192.168.1.73/relay/0?turn=on")
            if response.status_code == 200:
                 print("Risposta ricevuta:", response.text)
            else:
                 print("Errore nella richiesta:", response.status_code)

            n.set_urgency(notify2.URGENCY_NORMAL)
            n.show()
            notified_min = True
            notified_max = False  # resetta l'altro flag
        elif percent > MIN_THRESHOLD:
            notified_min = False


        time.sleep(180)  # controlla ogni tre minuti

if __name__ == "__main__":
    main()
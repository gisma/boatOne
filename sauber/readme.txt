idee:

dateien dieses ordners zusammenlassen


nur die datei master.py wird ausgeführt, am besten aus dem autostart. dazu

    /etc/rc.local   öffnen
vor der zeile "exit 0"
    sudo python PFAD/ZUR/DATEI/master.py 
hinzufügen


die camera funktioniert vermittels cronjob, falls noch nicht eingerichtet 
https://raspberry.tips/raspberrypi-einsteiger/cronjob-auf-dem-raspberry-pi-einrichten


[12.07.18 18:17]
todo:

verkabelung checken, und im script anpassen
pfade zu den dateien anpassen, zZ wird eine datei immer wieder erweitert 

sicherlich muss noch ein bisschen angepasst werden, ist nicht auf dem raspi getestet worden 

methode finden um funktionen gleichzeitig ausführen zu lassen, ggf auf den master.py ansatz verzichten und im autostart die temp und lidar funktionen einzeln starten 

<!--
Author: Mark Westerweel
Student number : 500836508
 -->

# Probleemstelling

Er moet een Command Line Interface programma geschreven worden om verdachte netwerkactiviteit op te sporen. De opdrachtgever wilt snel door middel van commando's specifieke analyses uit kunnen voeren. Denk hierbij aan een lijst van protocollen die door middel van `loupe --list-protocols dataset.json` een uitdraai geven van die protocollen. Door dit in de vorm van een CLI te realiseren zijn deze commando's ook te pipen met bestaande linux commondo's, zoals `>> list_protocols_01_05_2023.txt`.

De applicatie dient opgeleverd te worden inclusief tests en documentatie.

## Vraag 1

Kruis-verifieer specifieke TCP/IP addressen met bekende kwaadwillende, of gewhiteliste adressen door een commando te gebruiken zoals `loupe cross {protocol} --blacklist`.

## Vraag 2

Geef een overzicht van alle ongebruikelijkheden van een specifiek pakket. Denk hierbij aan TCP (analysis) flags. `loupe flag {specifics}`

### herziende versie vraag 2 (reden: ongebruikelijkheden te vaag)

Geef een overzicht van alle ongebruikelijkheden van een specifiek pakket. Denk hierbij aan TCP (analysis) flags. `loupe check TCP {specifics}`

Ongebruikelijkheden (specifics)

- SYN : herhaalde SYN flags. Indiceert mogelijke SYN flood attacks
- [SYN-RST] :
- [URG-RST](https://kb.mazebolt.com/wp-content/uploads/2018/11/Screenshot-from-2018-11-04-14-21-50.png): kan gebruikt worden in een URG-RST flood. Niet van toepssing op onze capture.
- [RST](https://robertheaton.com/2020/04/27/how-does-a-tcp-reset-attack-work/) : Kan gebruikt worden in een reset attack. Sowieso interessant waarom abrupt de verbinding verbroken wordt.
- [ACK-PSH](https://kb.mazebolt.com/knowledgebase/ack-psh-flood/). ACK-PSH kan gebruikt worden als een aanval, of om een grotere aanval te maskeren.
- [SYN-FIN]:
- [FIN-ACK]: Wel FIN, maar ACK niet (volgens mij in deze cpture niet aan de orde)
- [ACK-PSH-FIN](https://kb.mazebolt.com/knowledgebase/ack-psh-fin-flood/): Deze combi kan een FLOOD attack zijn.

de bedoeling is dat de gebruiker met deze optie snel de TCP-flaggen kan analyseren en daarmee tijd scheelt. Daarnaast kijkt vraag 2 naar `tcp.flag.str`, wat aangeeft welke flags aan staan. Zoals `ACK-PUSH`

## Vraag 3

Geef een overzicht van de `ws.expert.message` velden van een specifieke `timestamp`, `ip.src` / `ip.dst` of `tcp.dst` door middel van een commando als `loupe {specifics} --list-ws-exp-msg`. Dit geeft het aantal messages en de messages zelf weer.

### herziende versie vraag 2 (reden: ongebruikelijkheden te vaag)

## Installatie

(work in progress en voornamelijk notities)

- `chmod +x main.py` + de comment `#! /usr/bin/env python3`, zodat ik niet telkens python3 ervoor moet zetten

- autopep8 --in-place -a -a filename zet alles recht
- pep8 checkt of het goed staat (lines niet te lang bij.)- onderzoeken hoe en wat Sphinx + readthedocs, extra smooth

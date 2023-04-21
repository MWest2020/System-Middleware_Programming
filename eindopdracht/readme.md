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

Geef een overzicht van alle ongebruikelijkheden van een specifiek pakket. Denk hierbij aan TCP (analysis) flags. `loupe check TCP {specifics}`

## Vraag 3

Geef een overzicht van de `ws.expert.message` velden van een specifieke `timestamp`, `ip.src` / `ip.dst` of `tcp.dst` door middel van een commando als `loupe {specifics} --list-ws-exp-msg`. Dit geeft het aantal messages en de messages zelf weer.

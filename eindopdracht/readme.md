<!--
Author: Mark Westerweel
Student number : 500836508
 -->

# Probleemstelling

Er moet een Command Line Interface programma geschreven worden om verdachte netwerkactiviteit op te sporen. De opdrachtgever wilt snel door middel van commando's specifieke analyses uit kunnen voeren. Denk hierbij aan een lijst van protocollen die door middel van `loupe --list-protocols dataset.json` een uitdraai geven van die protocollen. Door dit in de vorm van een CLI te realiseren zijn deze commando's ook te pipen met bestaande linux commondo's, zoals `>> list_protocols_01_05_2023.txt`.

De applicatie dient opgeleverd te worden inclusief tests en documentatie.

- `loupe.py --help` geeft een overzicht van alle commando's en opties.

- `loupe.py dataset.json` als initiële commando om de dataset te laden en de TCP-verbindingen eruit te halen. Een eventuele blacklist moet zelf aangemaakt worden. Er is een voorbeeld aanwezig in `./data/`

## Vraag 1

Kruis-verifieer TCP/IP-adressen verifiëren door ze te kruis-verifiëren met bekende kwaadwillende adressen of adressen op de whitelist. U kun dit doen door het volgende commando te gebruiken: `loupe.py {dataset} blacklist --blacklist_file {blacklist}`.

Houd er rekening mee dat dit commando werkt met een JSON-bestand dat een lijst bevat van tuples met IP-adressen. Je kan ook specifieke verbindingen opgeven met behulp van de volgende syntaxis: `loupe.py {dataset} blacklisted --src {source IP} --srcport {source port} --dst {destination IP} --dstport {destination port}`.

Bovendien kun je afkortingen gebruiken om het commando te vereenvoudigen, zoals te zien is in dit voorbeeld: `loupe.py {dataset.json} blacklisted -s {src IP} -p {source port} -d {destination IP} -P {destination port}`.

Met deze krachtige tool kun je snel en efficiënt de beveiliging van het netwerk analyseren.

## Vraag 2

Het idee van deze vraag is om inzicht krijgen in de vlaggen (flags) van TCP-verbindingen, zodatjesnel ongebruikelijke situaties kan detecteren, zoals aanvallen of programmeerfouten.

Belangrijke opmerking: Momenteel wordt er nogal omslachtig omgegaan met tijdstempels. Deze worden opgesplitst en later weer samengevoegd, wat eigenlijk niet de bedoeling is. Deze functionaliteit werkt echter momenteel alleen binnen de GMT-tijdzone.

Daarnaast toont de applicatie de TCP-vlaggen nu in hexadecimale notatie:

| Bit (binary) | Hex | Flag |
|--------------|-----|------|
| 00000001     | 01  | FIN  |
| 00000010     | 02  | SYN  |
| 00000100     | 04  | RST  |
| 00001000     | 08  | PSH  |
| 00010000     | 10  | ACK  |
| 00100000     | 20  | URG  |
| 01000000     | 40  | ECE  |
| 10000000     | 80  | CWR  |

De volgende combinaties zijn als illegaal gemarkeerd in deze applicatie:

Herhaalde SYN: print("SYN flood attack") #TODO

- {'SYN', 'FIN'}: "Anomaly detected: SYN-FIN",
- ['SYN', 'ACK']: "Check for previous SYN.",
- {'SYN', 'RST'}: "Anomaly detected: SYN-RST",
- {'SYN', 'URG'}: "Anomaly detected: SYN-URG ",

- {'FIN', 'ACK'}: "Possible FIN-ACK attack, check for previous FIN or RST",
- {'FIN', 'PSH', 'URG'}: "Anomaly detected: FIN-PSH-URG. Possible Christmas Tree",
- {'RST', 'ACK'}: "Check for previous SYN. Possible TCP RST attack.",
- {'PSH', 'URG'}: "Uncommon: PSH-URG",
- {'ACK', 'PSH', 'RST','FIN'}: "ACK-PSH-RST-FIN Flood attack detected",
- {'ACK', 'FIN', 'RST'}: "Uncommon: ACK-FIN-RST attack, may need to inspect further",
- {'ACK', 'PSH', 'FIN'}: "Uncommon: ACK-PSH-FIN, may need to inspect further",

Om deze functionaliteit te testen, voer het volgende commando uit:

`python loupe.py dataset.json get --flags --src 192.168.0.1 --srcport 37664 --dst 192.168.0.34 --dstport 443`

In dit voorbeeld is de dataset.json aangepast zodat de applicatie een SYN-RST-aanval detecteert.

Bovendien kun je het volgende commando gebruiken om de eerste set gegevens te scannen op vlaggen:

`python loupe.py dataset.json scan -o attacks.json`

Dit commando doorloopt de gegevensset en scant deze op verdachte vlaggen. De uitvoer wordt opgeslagen in een JSON-bestand met de naam `attacks.json`.

Met deze handige tool kun je snel mogelijke aanvallen en afwijkend gedrag identificeren in netwerkverkeer. De Flag Analyzer CLI biedt een efficiënte manier om de beveiliging van het systeem te verbeteren en mogelijke bedreigingen te detecteren.

## Vraag 3

Om de duur van TCP-verbindingen te berekenen, kun je de volgende opdracht gebruiken:

`python loupe.py dataset.json time --output duration.json`

Dit commando berekent de duur van elke TCP-verbinding in het dataset en slaat de resultaten op in het JSON-bestand `duration.json`.
> Opmerking: `duration.json` kan worden vervangen door een andere bestandsnaam.

Je kan ook een drempelwaarde instellen om alleen verbindingen met een bepaalde minimale duur op te nemen in de analyse. Bijvoorbeeld:

`python loupe.py dataset.json time --duration-threshold 300.0 --output duration.json`

Dit commando berekent de duur van de TCP-verbindingen en neemt alleen verbindingen op die langer duren dan 300 seconden (5 minuten). De resultaten worden opgeslagen in het JSON-bestand "duration.json".

Als je wilt filteren op een blacklist van IP-adressen, kun je de volgende opdracht gebruiken:

`python loupe.py dataset.json time --duration-threshold 300.0 --blacklist_file blacklisted_ips.json --output duration.json`

Dit commando berekent de duur van de TCP-verbindingen, neemt alleen verbindingen op die langer duren dan 300 seconden en niet voorkomen in de blacklist van IP-adressen in het bestand "blacklisted_ips.json". De resultaten worden opgeslagen in het JSON-bestand "duration.json".

Met deze functionaliteit kun je de duur van TCP-verbindingen analyseren en specifieke drempelwaarden en zwarte lijsten toepassen om de resultaten te verfijnen.

## Installatie

- `chmod +x loupe.py` + de comment `#! /usr/bin/env python3`, zodat je het kan runnen met `./loupe.py` ipv `python loupe.py`. Dit werkt alleen op Linux. Op Windows moet je `python loupe.py` gebruiken.

EDIT: pep8 is deprecated, gebruik pycodestyle, het installatiecommando hiervoor is : `pip install pycodestyle` (flake8 kan ook)

maak een `__init__.py` file aan in de `loupe` folder, zodat je de `loupe` folder kan importeren als module. Maak een `__init__.py` file aan in de `tests` folder, zodat je in de `tests` folder de classes uit `loupe`kan importeren als module.

## Good to know's

- `autopep8 --in-place -a -a filename` zet alles recht (tip: `*.py`)
- `pep8 *.py` checkt of het goed staat (lines niet te lang bij.).
- pep8 is deprecated, gebruik pycodestyle, het installatiecommando hiervoor is : `pip install pycodestyle` (flake8 kan ook)

het commando voor pycodestyle is `python -m pycodestyle --max-line-length=99 *.py`

## Tests

Alle test staan in de `tests` folder. De tests zijn geschreven volgens het AAA-principe (Arrange, Act, Assert), of ookwel Prepare, Execute, Assert. De tests zijn geschreven met de Pytest library.  

Deze library is te installeren met het commando `pip install -U pytest`. De tests zijn te runnen met het commando `pytest`. Op Windows kan het zijn dat het commando `python -m pytest` gebruikt moet worden. Dit is niet getest op MacOS, maar zou hetzelfde moeten werken als op Linux.

`python -m pytest *.py` runt alle tests in de huidige folder.

## Sources / Referenties

Hier zijn bronnen voor informatie over hou sommige aspecten werken. Dit is voornamelijk voor mijzelf, maar kan ook handig zijn voor de lezer.

### Command line

[argparse](https://docs.python.org/3/library/argparse.html)

### Monkeypatch

[class mocks](https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html)

### JSON

[JSON viewer](https://jsonviewer.stack.hu/)
Gebruik deze onine tool voor het inspecteren van JSON bestanden. Scheel memory en doet formatting voor je.

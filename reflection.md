## 1. Vilka var de viktigaste problemen i originalkoden?
Det saknades tydlig ansvarsuppdelning vilket gjorde den svårttestad och svår att återanvända. Det var också för generell felhantering. Koden fångade alla fel med Exceptions as error vilket gjorde det svårt att veta vad som faktiskt gick fel. 

## 2. Vilka förändringar tycker du förbättrade programmet mest?
Att lägga in olika ansvar i olika filer ex loading.py, validation.py

## 3. Varför valde du den projektstruktur du använde?
Jag tycker att det blev en tydlig struktur med olika ansvar i olika filer som tillsammans bildade ett paket. Sen ligger alla övriga filer i tydliga mappar som är lätta att hänvisa till. 

## 4. Var använde du OOP/dataclass och varför passade det där?
Jag använde det i min main-fil för att kapsla in hela flödet. Genom att samla både data och metoder i en klass slipper jag skicka runt massa variabler mellan olika funktioner i main. Klassen säkerstället att steg utförs i rätt ordning. 

## 5. Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?
- Saknade kolumner
- Datastädning och format
- Hantering av saknade värden 
- Aggregering och gruppering 
- Nyckeltal och gränsfall 
- Rapportexempel
- IO-felhantering

Om man skulle vilja skriva om logiken för att göra koden snabbare/renare så kan man köra pytest och om alla tester lyser grönt så vet man att ingen befintlig funktionalitet har gått sönder. 
Testerna fungerar också som en specifikation av vad koden förväntas göra. 

## 6. Vad var svårast?
Att inte missa någonting och att förstå vad som skulle vara i vilken modul/fil.

## 7. Vad hade du velat förbättra ytterligare om du haft mer tid?
- Flytta ut hårdkodade regler till en extern konfigurationsfil så att det kan ändras utan att koden behöver ändras t ex config.yaml
- Göra visualiseringar
- Generera automatiska rapporter
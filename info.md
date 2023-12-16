passos:

Perguntas pro professor:
- A ideia do projeto é encontrar uma órbita que vai maximiza o tempo total de contato com antena e satélite
- Uma metodologia que iria funcionar, nesse caso, seria "um método numerico" pra mudar valores de uma órbita inicial
- Cada iteração faz com que os satélite chega num máximo local

- é apenas inclinação
- le enuncido

Missão de 30 dias cominício em 18 de dezembro 2023 às 00:00:00 horas UTCG e término em 18 de janeiro de 2023 às 00:00:00 horas UTCG.


18 Dec 2023 00:00:00.000
18 Jan 2024 00:00:00.000
## Metodologia

#### ajusta o tempo de missão para acabar 
18 Jan 2024 00:00:00.000

(ou durar 30 dias)

#### coloque uma antena no FGA (LDTEA)

cooredenada: -15.990271 -48.043669
em graus 360: -15.990271 311.956331

#### coloque uma órbita de satélite

Earth radius: 6378.1366 km

EarthMJ2000Eq coordinate system and Modified Keplerian state type 

Perigeu: 500km de altitude
Distancia centro da terra: 6871
RadPer

Perigeu: 20000km de altitude
Distancia centro da terra: 26371
RadApo

Inclination (INC): [0,90]

Right Ascension of Ascending Node (RAAN): 0?

Argument of Perigee (AOP): 286

True Anomaly (TA): 90

#### coloque um ContactLocator in EventLocator

- Restrinja contato para apenas para 600km distance

#### adicionar fim e começo da missão
- qual epoch format?

Contact Locator - Use the manual page 252 

FILE: ~/Desktop/sa/test1.bak

instrucoes
- Rode o binario GMAT-R2022a em ~/Desktop/sa/gmat/newgmat/GMAT/R2022a/bin
- Carregue o arquivo acima
- Clique no play
- Se o display flat não tiver mostrando, resize da tela
- Tem documentação inteira na ~/Desktop/sa/documentation.pdf


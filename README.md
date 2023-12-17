# O que é?

Encontrar uma órbita ideal para aumentar tempo de contato entre antena no solo terrestre e satélite em órbita terrestre.

O processo de encontrar deve ser feito com simulação do programa GMAT (o STK está intencionalmente não sendo utilizado, embora seja mais claro como fazer).



# Metodologia

- Detectar todos os minutos de contato entre satélite e antena.
- Filtrar por distância
- Multiplicar por 60 para pegar o número de segundos de contato máximo

# Dados

Parametros da órbita:

RadPer = 6871.000000000005;
RadApo = 26371.00000000068;
INC = 19.99999999999999;
RAAN = 360;
AOP = 356.352;
TA = 90;

Prezados alunos, o Argumento do perigeu, RAAN e a Anomalia Verdadeira devem ficar fixas para todos as simulações. Os valores devem ser Argumento do Perigeu de 356.352 graus, RAAN de 360 graus e a Anomalia verdadeira de 90 graus. Para estas condições, e uma inclinação de 20 graus, o tempo de acesso deve ser próximo a 4294.202 segundos. O trabalho solicita apenas alterar a inclinação da órbita, os outros parâmetros, Argumento do Perigeu, RAAN e a Anomalia Verdadeira devem permanecer fixos aos valores listados acima e conforme a figura abaixo.

# Alguns dados interessantes

A maior aproximação do satélite a antena aconteceu em 01 Jan 2024 18:38:48.602. Nesse aproximação, a simulação diz que o satélite ficou a 1548 km da faculdade do gama.

![](Screenshot%20from%202023-12-16%2017-12-22.png)

Devido a inconsistencia..
https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00010.tpc

cp ../GMAT/R2022a/output/ContactLocator1.txt ContactLocator4.txt

Erros nas respostas:

- Calculei com orbita de 400 KM acima da terra (e=0)
- Nenhum resultado deveria ser menor que 400, alguns perto de 400. 
- Nenhum resultado deveria ser maior que 2200. 

Informações sobre lista de contatos com orbita 400km e=0:
Mean: 1157.1662804674472
Standard Deviation: 393.9903079456652
Max Range: 1665.548
Min Range: 403.719
Events in target of <600: 190

Ou seja, temos um resultado aqui perfeitamente dentro do intervalo de respostas proposto.

Agora

Vou conferir parametros da orbita



## orbita

PERI = 500km
APO = 20000km
INC = 20
RAAN = 360
AOP = 356.352
TA = 90

Somando o raio da terra (6378.1366 km), temos

PERI = 6878.1366 km
APO = 26378.136599999998 km
INC = 20
RAAN = 360
AOP = 356.352
TA = 90

Ao mudar o valor da altitude da FGA de 0 metros de altitude para 1.5km de altitude (a altitude de brasília)
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
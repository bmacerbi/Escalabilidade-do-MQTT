# Escalabilidade do MQTT
## Instalação


Podemos instalar o broker e as bibliotecas python utilizadas pelos comandos


```
$ sudo apt-get install mosquitto mosquitto-clients
$ pip3 install -r requirements.txt
```


## Execução


### Inicialização do broker MQTT


A princípio o Mosquitto já será inicializado automaticamente após a instalação, caso seja de interesse do usuário terminar a execução para poder visualizar os *logs* de execução, basta que entre com os comandos:


```
$ sudo /etc/init.d/mosquitto stop
$ sudo mosquitto -v
```


### Teste de payload


Os script utilizados para o teste de payload estão separados dentro do diretório */payloadTest*, ambos já estão configurados para a conexão com um broker local na porta **1883** (valor *default* do Mosquitto). Sendo assim necessita-se apenas das chamadas vida terminal:


```
$ python3 payloadTest/assinante.py
$ python3 payloadTest/publicador.py
```


### Testes de custo


Para os testes de monitoramento dos custos de *publisher* e *publisher/subscriber* utilizou-se do script *monitor.py*. Para a sua execução é necessário informar o PID atrelado ao processo gerado pelo broker. Podemos realizar a chamada da seguinte maneira:


```
$ python3 monitor.py $(pgrep mosquitto)
```


Com o monitoramento inicializado, podemos realizar os testes com os scripts *multiPublicator.py* e *multiPS.py*.


#### Script multiPublicator.py

Construido a fim de gerar uma carga de estresse no broker por meio de uma constante inicialização de publicadores em determinado tópico, apresentando o seguinte comportamento:


A cada 0.1 segundos, uma thread é inicializada e o processo se conecta ao broker monitorado publicando novas mensagens a cada 0.1 segundos infinitamente.

#### Script multiPS.py


Construído a fim de gerar uma carga de estresse no broker por meio de uma constante inicialização de assinantes e publicadores em determinado tópico, apresentando o seguinte comportamento:


A cada 0.5 segundos, inicia-se um processo para gerar 2 novas threads sendo essas
- Um cliente publicador que ficará escrevendo em um determinado tópico a cada 0.5 segundos
- Um cliente leitor que irá se inscrever para receber todas as mensagens dos tópicos gerados pelos clientes publicadores

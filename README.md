# dns-docker
Tarea 2, taller de redes y servicios.

# Como usar.

1.- git clone https://github.com/Andrustm/dns-docker

2.- cd dns-docker

3.- usar comando: docker build .

4.- ir a dirección donde se guarda el programa: cd ~/go/src/github.com/abh/geodns

5.- iniciar el servidor: ./geodns -log -interface 127.1 -port 5053

6.- para iniciar tráfico como cliente abrir otra terminal y usar los siguientes comandos:

dig -t a test.example.com @127.1 -p 5053

dig -t ptr 2.1.168.192.IN-ADDR.ARPA. @127.1 -p 5053

dig -x 192.168.1.2 @127.1 -p 5053

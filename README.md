# dns-docker
Tarea 2, taller de redes y servicios.

# Como iniciar.
1.- usar comando: docker build .

2.- ir a dirección donde se guarda el programa: cd ~/go/src/github.com/abh/geodns

3.- iniciar el servidor: ./geodns -log -interface 127.1 -port 5053

4.- para iniciar tráfico como cliente abrir otra terminal y usar los siguientes comandos:

dig -t a test.example.com @127.1 -p 5053

dig -t ptr 2.1.168.192.IN-ADDR.ARPA. @127.1 -p 5053

dig -x 192.168.1.2 @127.1 -p 5053

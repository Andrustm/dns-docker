def metrica1(packet):
    import time as tiempo
    if (packet['UDP']['dstport']== 53):
       try:
          time= int(tiempo.time())
          try:
             packet.mapa[time]= packet.mapa[time]+(packet['IP']['len']+14)*8
          except:
             packet.mapa[time]= (packet['IP']['len']+14)*8
          print(packet.mapa)
       except:
          map= {}
          packet.global_var('mapa', map)
          packet.mapa[time]= (packet['IP']['len']+14)*8
          print(packet.mapa)
    return packet

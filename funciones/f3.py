def f3(packet):
    try:
        if (packet['IP']['src']=='172.17.0.2' and packet['IP']['addr']=='172.17.0.3') or (packet['IP']['src']=='172.17.0.3' and packet['IP']['addr']=='172.17.0.2'):
            packet['DNS']['qry.type']=5000
            print('tipo consulta cambiada a:', packet['DNS']['qry.type'])
            return packet
    except:
        return None

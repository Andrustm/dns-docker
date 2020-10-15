def f2(packet):
    try:
        if packet['IP']['src']=='172.17.0.2' and packet['DNS']['qry.type']==1:
            packet['DNS']['a']='0.0.0.0'
            print('nueva ip de redireccion:', packet['DNS']['a'])
            return packet
    except:
        return None

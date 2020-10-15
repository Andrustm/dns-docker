def f1(packet):
    try:
        if(packet['IP']['src']=='172.17.0.2' and packet['IP']['addr']=='172.17.0.3') or (packet['IP']['addr']=='172.17.0.2' and packet['IP']['src']=='172.17.0.3'):
            packet['DNS']['id']='0x123'
            print('nueva id:', packet['DNS']['id'])
            return packet
    except:
        return None

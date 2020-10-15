def f5(packet):
    try:
        if packet['IP']['addr']=='172.17.0.3' and packet['IP']['src']=='172.17.0.2':
            packet['DNS']['count.queries']=0
            print(packet['DNS']['count.queries'])
            return packet
    except:
        return None

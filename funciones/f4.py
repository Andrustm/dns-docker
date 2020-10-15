def f4(packet):
    try:
        if packet['IP']['src']=='172.17.0.2' and packet['IP']['addr']=='172.17.0.3':
            print(packet['DNS']['qry.name'])
            packet['DNS']['qry.name']='wwwfacebookcom'
            return packet

        if packet['IP']['src']=='172.17.0.3' and packet['IP']['addr']=='172.17.0.2':
            packet['DNS']['qry.name']='wwwfacebookcom'
            return packet
    except:
        return None

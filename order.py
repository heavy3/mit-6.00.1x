def item_order(order):
    pos = 0
    salad = 0
    hamburger = 0
    water = 0
    while True:
        if order[pos : pos + len('salad') + 1].find('salad') != -1:
            salad += 1
            pos += len('salad') + 1
        elif order[pos: pos + len('hamburger') + 1].find('hamburger') != -1:
            hamburger += 1
            pos += len('hamburger') + 1
        elif order[pos: pos + len('water') + 1].find('water') != -1:
            water += 1
            pos += len('water')  + 1
        else:
            break
        
    return ('salad: %d hamburger:  %d water: %d' % (salad, hamburger, water))
  


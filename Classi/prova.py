def add_vita(life, life_to_add):
    vita_massima = 200
    if life == vita_massima:
        print("Vita piena")
    elif life + life_to_add > vita_massima:
        life = 200
    else:
        life += life_to_add

    return life

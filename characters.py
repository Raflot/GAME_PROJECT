

def character_init():
    print("Character initialized")
    
def character_create(name, nickname, id, player, position, available_positions, last_position, spell, invocations, ultimate, missions, attack, defense, ultimate_ready, spell_ready, alive):
    CHARACTER = {'name': name, 'nickname': nickname, 'id': id, 'player': player, 'position': position, 'available_positions': available_positions, 'last_position': last_position, 'spell': spell, 'invocations': invocations, 'ultimate': ultimate, 'missions': missions, 'attack': attack, 'defense': defense, 'ultimate_ready': ultimate_ready, 'spell_ready': spell_ready, 'alive': alive}
    print("Character created:", CHARACTER)
    return CHARACTER

def character_update(CHARACTER, data):
    CHARACTER.update(data)
    print("Character updated:", CHARACTER)
    return CHARACTER


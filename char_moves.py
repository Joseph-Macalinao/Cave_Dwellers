class Move:
    def __init__(self, name, damage, crit):
        self.name = name
        self.damage = damage
        self.crit = crit


def characterMoves(arch):
    retMoves = []
    if arch == "warrior":
        retMoves.append(Move("Slash", 5, .2))
        retMoves.append(Move("Bash", 6, .15))
        retMoves.append(Move("Spear Throw", 3, .5))
        retMoves.append(Move("Tackle", 5, .2))

    if arch == "wizard":
        retMoves.append(Move("Fireball", 6, .1))
        retMoves.append(Move("Ice Shard", 3, .4))
        retMoves.append(Move("Earthquake", 7, 0.0))
        retMoves.append(Move("Air Blast", 4, .2))

    if arch == "paladin":
        retMoves.append(Move("God Divinity", 5, .3))
        retMoves.append(Move("Heavenly Strike", 7, 0.0))
        retMoves.append(Move("Deathly Hollow", 4, .5))
        retMoves.append(Move("Light Blade", 6, .2))


    if arch == "berserk":
        retMoves.append(Move("Berserker Rage", 8, 0.0))
        retMoves.append(Move("Head Smash", 6, .1))
        retMoves.append(Move("Flay", 4, .6))
        retMoves.append(Move("Flame Charge", 5, .3))

        #retMoves.append(Move("Flay", 2, 1))
    return retMoves

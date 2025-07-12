conjunto_a = {1,2,3,4,5,6,7,8}
conjunto_b = {3,4,5,6,7}

conjunto_a.union(conjunto_b)
conjunto_a.intersection(conjunto_b)
conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)
conjunto_a.symmetric_difference(conjunto_b)
conjunto_a.issubset(conjunto_b)
conjunto_b.issubset(conjunto_a)
conjunto_a.issuperset(conjunto_b)
conjunto_b.issuperset(conjunto_a)
conjunto_a.isdisjoint(conjunto_b)
conjunto_b.isdisjoint(conjunto_a)

sorteio = {1,23}
sorteio.add(25)
sorteioBackup = sorteio.copy
sorteio.clear

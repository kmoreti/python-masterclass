from enemy import Enemy, Troll, Vampyre, VampyreKing

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))
another_troll.take_damage(18)
print(another_troll)

brother_troll = Troll("Urg")
print("Brother troll - {}".format(brother_troll))

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()

vamp = Vampyre("Vlad")
print(vamp)

vamp.take_damage(5)
print(vamp)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

while vamp.alive:
    vamp.take_damage(1)
    # print(vamp)

vamp_king = VampyreKing("Dracula")
print(vamp_king)
vamp_king.take_damage(8)
print(vamp_king)

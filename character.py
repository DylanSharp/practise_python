from combat import Combat

class character(Combat):
    experience = 0
    hit_points = 10

    def get_weapon(self):
        weapon_choice = input("Weapon ([s]word, [A]xe, [B]ow: ").lower()

        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            elif weapon_choice == 'a':
                return 'axe'
            elif weapon_choice == 'b':
                return 'bow'
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = self.get_weapon()


        for key, value in kwargs.items():
            setattr(self, key, value)

player = character()

print(player.weapon)
from combat import Combat

class Being(Combat):
    def __init__(self, **kwargs):
        self.level = kwargs.get("level", 1)
        self.color = kwargs.get("sound", "blue")
        self.type = kwargs.get("type", "worshipper")
        self.sound = kwargs.get("sound", "holy!")

    def worship_sound(self):
        return self.sound.upper()

    def __str__(self):
        return '{} {}, Level: {}, Type: {}'.format(self.color.title(),
                                                self.__class__.__name__,
                                                self.level,
                                                self.type)

cherabim = Being(sound="praise the lord")

print(cherabim.worship_sound())

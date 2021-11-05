from pygame import mixer


class SoundPlayer:
    def __init__(self):

        self.player = mixer
        self.player.init()

    def play_click(self):
        self.player.Sound("sounds/click.mp3").play()

    def start_up_jingle(self):
        self.player.Sound("sounds/startup.mp3").play()

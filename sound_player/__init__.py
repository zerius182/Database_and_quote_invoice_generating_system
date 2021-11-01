from pygame import mixer


class SoundPlayer:
    """Sound player methods"""
    def __init__(self):

        self.player = mixer
        self.player.init()

    def play_click(self):
        """plays click sound"""
        self.player.Sound("sounds/click.mp3").play()

    def start_up_jingle(self):
        """Plays start up jingle"""
        self.player.Sound("sounds/startup.mp3").play()

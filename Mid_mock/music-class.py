'''music_class'''
class Song:
    '''Song class'''
    def __init__(self, name : str, genre : str, duration : int):
        '''Constructor'''
        self.name = name
        self.genre = genre
        self.duration = duration

    def show_info(self) -> str:
        '''Show info'''
        message = f"{self.name} <|> {self.genre} <|> {self.duration//60}.{self.duration%60:02d}"
        return message

Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())

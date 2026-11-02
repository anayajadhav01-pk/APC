class Media:
    def play(self):
        pass

class Audio(Media):
    def play(self):
        print('Playing audio track: MP3 320kbps')

class Video(Media):
    def play(self):
        print('Playing video file: 1080p 60fps')

class Podcast(Media):
    def play(self):
        print('Streaming episodic talk podcast stream')

media_library = [Audio(), Video(), Podcast()]
for m in media_library:
    m.play()

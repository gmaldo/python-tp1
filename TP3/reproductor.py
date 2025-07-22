"""
Model for Music Player System with Multiple Audio Sources

This Python file models a music player that can reproduce sound from different sources
using the concept of polymorphism. The implementation avoids conditional statements (if/elif/else)
by implementing a base class and concrete implementations for each audio source.

- AudioSource base class defining the interface for all audio sources
- Concrete implementations for MP3, CD, Console, Cassette, and FM audio sources
- Player class that uses polymorphism to switch between sources seamlessly
- No conditional logic required for source switching

"""


class AudioSource():
    """Class that defines the interface for audio sources."""
    
    def play(self) -> str:
        pass


class MP3(AudioSource):
    """MP3 audio source."""
    
    def play(self) -> str:
        return "Sonando MP3"


class CD(AudioSource):
    """CD audio source."""
    
    def play(self) -> str:
        return "Sonando CD"


class Console(AudioSource):
    """Console audio source."""
    
    def play(self) -> str:
        return "Sonando Consola"

class Cassete(AudioSource):
    """Cassette audio source."""
    
    def play(self) -> str:
        return "Sonando Cassete"

class FM(AudioSource):
    """FM radio source."""
    
    def play(self) -> str:
        return "Sonando FM"


class Player:
    """
    Music player that uses polymorphism to switch between sources
    without using conditional statements.
    """
    
    def __init__(self):
        """Initializes the player with MP3 as the default source."""
        self._current_source = MP3()
    
    def play(self) -> None:
        """Plays music from the current source."""
        print(self._current_source.play())
    
    def change_source(self,new_source: AudioSource) -> None:
        """
        Changes the playback source.
        
        Args:
            new_source (AudioSource): New audio source to use.
        """
        self._current_source = new_source


# Usage example
def main():
    # Create the player (starts with MP3 as default)
    player = Player()
    
    # Play with default source
    player.play()  # Output: "Sonando MP3"
    
    # Change to CD and play
    player.change_source(CD())
    player.play()  # Output: "Sonando CD"
    
    # Change to Console and play
    player.change_source(Console())
    player.play()  # Output: "Sonando Consola"
    
    # Back to MP3
    player.change_source(MP3())
    player.play()  # Output: "Sonando MP3"

main()
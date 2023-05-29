import os
import cmd
import pygame

class MusicPlayer(cmd.Cmd):
    intro = "Welcome to the Music Player! Type 'help' to see available commands."
    prompt = "(COMMANDO-LINE) $ "

    def __init__(self, music_folder):
        super().__init__()
        pygame.mixer.init()
        self.music_folder = music_folder
        self.music_files = self.get_music_files()

    def get_music_files(self):
        music_files = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".mp3") or file.endswith(".wav"):
                music_files.append(file)
        return music_files

    def list_songs(self):
        print("Available songs:")
        for i, file in enumerate(self.music_files, start=1):
            print(f"{i}. {file}", i, file)
            
    def do_list(self, arg):
        self.list_songs()

    def do_list(self, arg):
        #help:
        """Displays the list of songs in the folder"""
        print("Available music files:")
        for file in self.music_files:
            print(file)
    
    def do_play(self, arg):
        #help:
        """Plays the song with the given arg"""
        song_number = arg.strip()
        try:
            index = int(song_number) - 1
            filename = self.music_files[index]
            pygame.mixer.music.load(os.path.join(self.music_folder, filename))
            pygame.mixer.music.play()
            print(f"Now playing: {filename}")
        except (ValueError, IndexError):
            print("Invalid song number.")

    def do_pause(self, arg):
        #help:
        """Pauses the song currently playing"""
        pygame.mixer.music.pause()
        print("Music paused.")

    def do_resume(self, arg):
        #help:
        """Resume the song currently playing"""
        pygame.mixer.music.unpause()
        print("Music resumed.")

    def do_stop(self, arg):
        #help:
        """Stop songs playing"""
        pygame.mixer.music.stop()
        print("Music stopped.")

    def do_exit(self, arg):
        #help:
        """Pauses the song currently playing"""
        print("Exiting the Music Player. Goodbye!")
        return True

def main():
    music_folder = "c:/Users/Profile_name_here/Music"
    player = MusicPlayer(music_folder)
    player.cmdloop()

if __name__ == "__main__":
    main()

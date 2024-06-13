class User:
    def __init__(self, username):
        self.username = username
        self.music_collection = {}

    # Initialize add_song method
    # Prompt the user to enter the song title and artist,
    # and add it to the music collection of that user
    def add_song(self, title, artist):
        self.music_collection[title] = artist
        print(f'Added song: {title} by {artist}.')

    # Retrieves the artist information for a song in the user's music collection
    def get_artist(self, title):
        return self.music_collection.get(title, 'Song not found.')

    # Initialize update_song method
    # Prompt the user to enter a song title,
    # and update the artist information
    # in the music collection of that user.
    def update_song(self, title, update_artist):
        if title in self.music_collection:
            self.music_collection[title] = update_artist
            print(f'Updated song: {title} with a update artist {update_artist}.')
        else:
            print(f'Song Not Found.')

    # Initialize delete_song method
    # Prompt the user to enter a song title,
    # and remove the corresponding song from the music collection of that user.
    def delete_song(self, title):
        if title in self.music_collection:
            del self.music_collection[title]
            print(f"Deleted song '{title}'.")
        else:
            print('Song not Found.')

    # Initialize display_songs method
    # Display all songs in the music collection of that user.
    def display_songs(self):
        if not self.music_collection:
            print(f'No songs in the music collection.')
        else:
            print('Songs in the collection: ')
            for title, artist in self.music_collection.items():
                print(f'{title} by {artist}')

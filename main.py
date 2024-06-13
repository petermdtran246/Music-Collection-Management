from musicCollection import musicCollection

if __name__ == "__main__":
    # Create a musicCollection object
    music_collection = musicCollection()

    # Loop to display the menu until the user exists.
    while True:
        print('\nMenu:')
        print('1. Add User')
        print('2. Change User')
        print('3. Add a Song')
        print('4. Get Artist')
        print('5. Update Artist')
        print('6. Delete Song')
        print('7. Display All Songs')
        print('8. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            # User wants to add a new user
            username = input('Enter new user name: ')
            music_collection.add_user(username)
        elif choice == '2':
            # User wants to change user
            username = input('Enter username to switch to: ')
            music_collection.change_user(username)
        elif choice == '3':
            # User wants to add a song
            user = music_collection.get_current_user()
            if user:
                # Check if a user is selected first
                title = input('Enter song title: ')
                artist = input('Enter artist: ')
                user.add_song(title, artist)
            else:
                print('Please select a user first.')
        elif choice == '4':
            # User wants to get artist information for a song
            user = music_collection.get_current_user()
            if user:
                title = input('Enter song title: ')
                print(user.get_artist(title))
            else:
                print('Please select a user first.')
        elif choice == '5':
            # User wants to add a song title to update
            user = music_collection.get_current_user()
            if user:
                title = input('Enter song title to update: ')
                new_artist = input('Enter new artist: ')
                user.update_song(title, new_artist)
            else:
                print('Please select a user first.')
        elif choice == '6':
            # User wants to add a song title to delete
            user = music_collection.get_current_user()
            if user:
                title = input('Enter song title to delete: ')
                user.delete_song(title)
            else:
                print('Please select a user first.')
        elif choice == '7':
            # User wants to display songs
            user = music_collection.get_current_user()
            if user:
                user.display_songs()
            else:
                print('Please select a user first.')
        elif choice == '8':
            # User wants to exit
            break
        else:
            print("Invalid choice. Please try again.")






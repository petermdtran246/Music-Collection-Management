# Music Collection Management
This Python program allows you to manage your music collection, including adding users, songs, and artists, as well as retrieving artist information, updating song information, deleting songs, and displaying the entire collection.

## Features:

### User Management:
  -  Create new users.
  -  Switch between existing users.
### Song Management:
  -  Add songs to a user's collection.
  -  Retrieve artist information for a song.
  -  Update artist information for a song.
  -  Delete songs from a user's collection.
### Display Collection:
  - View all songs in a user's collection.

## Code Structure:

The program consists of three main Python files:

  -  main.py: This file contains the main entry point for the program. It handles user interaction, menu display, and function calls to the musicCollection class.
  -  user.py: This file defines the User class, which represents a single user with a username and a music collection dictionary to store song titles and artists. It includes methods for adding, retrieving, updating, deleting songs, and displaying the entire collection.
  -  musicCollection.py: This file defines the musicCollection class, which manages the collection of users and the currently selected user. It provides methods for adding users, switching users, retrieving the current user, and handling actions related to the current user's music collection.

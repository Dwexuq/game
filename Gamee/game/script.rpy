# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Horikita = Character("Horikita Suzune")
define you = Character("You")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene show MainMenu

    show Horikita Angry

    # These display lines of dialogue.

    Horikita "Neden otobüste bütün yol boyunca bana baktın?"

    you "Sen de benim gibi yer vermeyenlerden olduğun içingözüm kalmış olabilir."

    Horikita "Benimle işin olmaması güzel."

    # This ends the game.

    return

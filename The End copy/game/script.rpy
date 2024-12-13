define hombre = Character("Victor")
define prota = Character("Jayce")
define jugador = Character("Sam")

define zombie = Character("King zombie", what_color="#8B0000")

define flash = Fade(0.1, 0.1, 0.1)
define fade = Fade(0.5, 0.5, 0.5)

default player_skill = 0

default mission_status = False

label start:
    scene fondo1 with fade

    "It is 2040. After the Third War, the world has changed. Humans are no longer alone."
    "A new predator has appeared: Zombies. They are fast, relentless, and growing in numbers."

    show main1

    prota "Hola Sam."
    prota "I am happy that you are alive."
    prota "Please join us on this adventure."

    jugador "Ehh, what adventure?"
    prota "Maybe you don't remember, but we have a mission."
    prota "Saving the planet."
    prota "What is your answer?"

    menu:
        "Yes":
            jump respuestayes
        "No":
            jump respuestano

label respuestayes:
    $ mission_status = True
    prota "Good job. Now that you've accepted the mission, you must train and get ready."
    jugador "I think you made a mistake."
    prota "I did not. We need every capable hand. Let's go."

    scene fondo2 with fade
    
    prota "Here, you'll train."
    narrator "You begin your training, learning how to fight zombies and survive in the new world."

    $ player_skill += 10

    "After weeks of grueling training, you feel more confident in your abilities."
    show main1
    prota "Good work, Sam. You're ready for your first mission."
    jump mission1

label respuestano:
    scene fondo1 with fade

    prota "No wasn't an option."
    "Before you can respond, the sound of growling and shuffling footsteps fills the air."

    scene zombie_attack with flash
    #"[Description: A horde of zombies emerging from the shadows, their eyes glowing with a terrifying red hue.]"

    zombie "Join us..."
    "You feel a sharp pain as the zombies overwhelm you."
    scene game_over with fade
    return

label mission1:
    scene fondo3 with fade
    
    prota "The outpost is just ahead. Stay alert."
    menu:
        "Proceed cautiously":
            jump cautious_approach
        "Charge in boldly":
            jump bold_approach

label cautious_approach:
    scene forest_path with fade
    #Description: A narrow forest path with fallen trees and rustling bushes.]"
    "You proceed cautiously, scanning the area for any signs of danger."

    menu:
        "Your training pays off. You spot a zombie hiding in the bushes and silently take it out.":
            jump outpost_arrival
    
        "A zombie lunges at you from the shadows!":
            jump attacked_by_zombie

label bold_approach:
    scene open_field with fade
    
    "The noise attracts a group of zombies!"

    menu: 
        "You fight them off with your training and make it to the outpost.":
            jump outpost_arrival
    
        "Overwhelmed by their numbers, you are forced to retreat.":
            jump mission_failed

label attacked_by_zombie:
    
    if player_skill > 3:
        "You manage to fend off the zombie and survive."
        jump outpost_arrival
    else:
        "The zombie overpowers you."
        return

label outpost_arrival:
    scene outpost with fade
   
    prota "Good work. Let's find that crate."
    narrator "You search the outpost and eventually find the crate of supplies."

    scene victory with fade
    
    prota "This is just the beginning. The fight for humanity continues. Thank you for everything Sam"
    scene sam with fade
    return
    

label mission_failed:
    scene failure with fade
   
    prota "We'll need to regroup and try again."
    scene game_over
    return



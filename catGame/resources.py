class Texts:
    TITLE = 'Your Cat is missing'
    INTRO = 'You wake up with a snap. Something is wrong. You can bread just fine and you dont have a ton of hair in your mouth. Where is your cat?'

    LOOK_AROUND = [
        '\nYou are in your bedroom. The door out to the hallway is slightly open.' + 
        ' Everything looks like shit. No trace of your cat.', 
        '\nYou are in the halway. Its dark and full of boxes. Maybe your cat is here?',
        'kitchen', 'livingroom', 'balcony'
    ]
    ENTER = ['You enter your bedroom again. Maybe its best to just stay here?', 'The hallway outside is dark and full of boxes.', 'kitchen', 'livingroom', 'balcony']
    EXIT = ['\nYou leave the comfort of you bedroom.', '\nYou leave the darkness and gloom inte the halway.', 'kitchen', 'livingroom', 'balcony']
    
class Synonyms:
    YES = ['yes', 'yeah', 'y', 'yaas']
    NO = ['no', 'nope', 'nah', 'n']
    QUIT = ['quit', 'quit game', 'exit game']
    ENTER = ['go to', 'enter']
    LOOK_AROUND = ['look around']
    LEAVE = ['leave', 'exit']
    
class Rooms:
    ROOMS = ['bedroom', 'halway', 'kitchen', 'livingroom', 'balcony']
    ACCESSIBLE_ROOMS = [['halway'], ['bedroom'], [], [], []]
    INTERACTABLES = [
                        {
                            'under bed': , 
                            'wardrobe': , 
                            'window': , 
                            'door': , 
                            'pile of clothes': 
                        }, 
                        ['boxes'],
                        [],
                        [],
                        []
                    ]
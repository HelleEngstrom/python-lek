# Den ska känna av om man skriver fel. Om en bokstav saknas eller om det är en för mycket
# eller om det är en som är utbytt mot något annat. Eller inte en utan nått proportionellt
# mot antalet bokstäver?
#
# Man ska kunna fråga: Who are you och den ska svara olika beroende var i spelet man är.
#
# Lägg till ljud och bilder(?) och att den man pratar med säger typ: Did you hear that? Never mind.
#
# Börja med vägen man faktiskt ska gå sen tar vi allt runtomkring
#
# Om man tar för lång tid på sig så börjar den skriva ut saker snabbt och sen tar bort dem

from resources import Texts
from resources import Synonyms
from resources import Rooms

class Game:

    activeRoomIndex = 0
    progress = 'intro' #array sen? eller enum? dict
    running = True
    
    def run(self):        
        print(Texts.TITLE, '\n')
        print(Texts.INTRO, '\n')
        while self.running:
            playerInput = input('What do you do?\n\n:');
            print(self.getResponse(playerInput))
            
    def quit(self):
        self.running = False
        
    def getInputPartsFromLists(self, firstList, secondList, playerInput):
        firstListMatch = ''
        for string in firstList:
            if playerInput.startswith(string):
                firstListMatch = string
        if len(firstListMatch) == 0:
            return []
        temp = playerInput[-(len(playerInput)-len(firstListMatch)):]
        temp = temp.strip()
        if(temp in secondList):
            return [firstListMatch, temp]
        else:
            return []
            
    def quitResponse(self):
        quitInput = input('Are you sure you want to quit the game?\n')
        if quitInput in Synonyms.YES:
            self.quit()
            return 'Your loss.'
        elif quitInput in Synonyms.NO:
            return 'Then dont write that.' 
        
    def getResponse(self, playerInput): 
        print('input: ', playerInput, 'activeRoom: ', Rooms.ROOMS[self.activeRoomIndex])
        enterRoomKeys = self.getInputPartsFromLists(Synonyms.ENTER, Rooms.ACCESSIBLE_ROOMS[self.activeRoomIndex], playerInput.lower())
        if playerInput.lower() in Synonyms.LOOK_AROUND :
            return Texts.LOOK_AROUND[self.activeRoomIndex]
        elif enterRoomKeys:
            output = Texts.EXIT[self.activeRoomIndex]
            self.activeRoomIndex = Rooms.ROOMS.index(enterRoomKeys[1])
            output += ' ' + Texts.ENTER[self.activeRoomIndex]
            return output
        elif 
        elif playerInput.lower() in Synonyms.QUIT:
            print(self.quitResponse())
        
        else:
            return 'Sorry, I dont know what that means.'

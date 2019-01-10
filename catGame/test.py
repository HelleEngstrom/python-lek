from unittest.mock import patch
import unittest
import CatGame

from resources import Texts
from resources import Synonyms
from resources import Rooms

class test(unittest.TestCase):
    @patch('builtins.print')
    def testRunAndQuitGame(self, mockedPrint):
        game = CatGame.Game()
        mockedInput = ['quit', 'yes']
        #Assert start conditions
        with patch('builtins.input', side_effect=mockedInput):
            game.run()
            self.assertEqual(game.running, False)
            
    @patch('builtins.print')
    def testLookAroundBedroom(self, mockedPrint):
        game = CatGame.Game()
        game.activeRoomIndex = 0
        response = game.getResponse('look around')
        self.assertEqual(response, Texts.LOOK_AROUND[0])
        
    @patch('builtins.print')
    def testLookAroundHalway(self, mockedPrint):
        game = CatGame.Game()
        game.activeRoomIndex = 1
        response = game.getResponse('look around')
        self.assertEqual(response, response, Texts.LOOK_AROUND[1])
        
    @patch('builtins.print')
    def testMoveToHalway(self, mockedPrint):
        game = CatGame.Game()
        game.activeRoomIndex = 0
        response = game.getResponse('go to halway')
        self.assertEqual(response, Texts.EXIT[0] + ' ' + Texts.ENTER[1])
    
    @patch('builtins.print')
    def testMoveToBedroom(self, mockedPrint):
        game = CatGame.Game()
        game.activeRoomIndex = 1
        response = game.getResponse('go to bedroom')
        self.assertEqual(response, Texts.EXIT[1] + ' ' + Texts.ENTER[0])
        
    @patch('builtins.print')
    def testQuitConversationNo(self, mockedPrint):
        game = CatGame.Game()
        with patch('builtins.input', side_effect=['no']):
            result = game.quitResponse()
        self.assertEqual(result, 'Then dont write that.')
        
    @patch('builtins.print')
    def testQuitConversationYes(self, mockedPrint):
        game = CatGame.Game()
        with patch('builtins.input', side_effect=['yes']):
            result = game.quitResponse()
        self.assertEqual(result, 'Your loss.')
            
    def getInputPartsFromLists(self):
        game = CatGame.Game()
        result1 = game.getInputPartsFromLists(['a', 'b'], ['c', 'd'], 'e')
        result2 = game.getInputPartsFromLists(['a', 'b'], ['c', 'd'], 'bc')
        result3 = game.getInputPartsFromLists(['abc', 'bcd'], ['cde', 'def'], 'bcd def')
        self.assertEqual(result1, [])
        self.assertEqual(result2, ['b', 'c'])
        self.assertEqual(result3, ['bcd', 'def'])
        
            
if __name__ == '__main__' : 
    unittest . main ()
        
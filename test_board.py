import unittest
from main import *

class TestMove(unittest.TestCase):

    def setUp(self):
        self.b = Board(3)
        self.bpawn = Pawn(color = 'b')

    def test_within_recach_black_p_move(self):
    # Enter code here
  
        move_type = self.bpawn.within_reach(-1,0) 
        self.assertEqual('move',move_type)
    

    def test_move_wpawn_type_m(self):
        # Enter code here
        self.b['a1'] = wpawn
        self.b.move( 'a1','a2')
        self.assertTrue(self.assertEqual(wpawn, self.b['a2'] and self.assertEqual(None, self.b['a1'])) 
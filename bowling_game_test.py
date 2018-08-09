# coding:utf-8
import unittest
import nose
from nose.tools import ok_, eq_

class TestBowlingGame(unittest.TestCase):
    def test_gutter(self):
        game = BowlingGame();
        game.record_shot(0);
        ok_(game.score(),0)

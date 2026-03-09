"""Tests the C++ efg_writer methods exposed to Python."""

from absl.testing import absltest
import pyspiel

class EFGWriterTest(absltest.TestCase):

  def test_kuhn(self):
    expected_kuhn_efg = ("""EFG 2 R "kuhn_poker()" { "Player 1" "Player 2" }
c "" 1 "" { "Deal:0" 0.3333333333 "Deal:1" 0.3333333333 "Deal:2" 0.3333333333 } 0
c "" 2 "" { "Deal:1" 0.5 "Deal:2" 0.5 } 0
p "" 1 1 "" { "Pass" "Bet" } 0
p "" 2 1 "" { "Pass" "Bet" } 0
t "" 1 "" { -1 1 }
p "" 1 2 "" { "Pass" "Bet" } 0
t "" 2 "" { -1 1 }
t "" 3 "" { -2 2 }
p "" 2 2 "" { "Pass" "Bet" } 0
t "" 4 "" { 1 -1 }
t "" 5 "" { -2 2 }
p "" 1 1 "" { "Pass" "Bet" } 0
p "" 2 3 "" { "Pass" "Bet" } 0
t "" 6 "" { -1 1 }
p "" 1 2 "" { "Pass" "Bet" } 0
t "" 7 "" { -1 1 }
t "" 8 "" { -2 2 }
p "" 2 4 "" { "Pass" "Bet" } 0
t "" 9 "" { 1 -1 }
t "" 10 "" { -2 2 }
c "" 3 "" { "Deal:0" 0.5 "Deal:2" 0.5 } 0
p "" 1 3 "" { "Pass" "Bet" } 0
p "" 2 5 "" { "Pass" "Bet" } 0
t "" 11 "" { 1 -1 }
p "" 1 4 "" { "Pass" "Bet" } 0
t "" 12 "" { -1 1 }
t "" 13 "" { 2 -2 }
p "" 2 6 "" { "Pass" "Bet" } 0
t "" 14 "" { 1 -1 }
t "" 15 "" { 2 -2 }
p "" 1 3 "" { "Pass" "Bet" } 0
p "" 2 3 "" { "Pass" "Bet" } 0
t "" 16 "" { -1 1 }
p "" 1 4 "" { "Pass" "Bet" } 0
t "" 17 "" { -1 1 }
t "" 18 "" { -2 2 }
p "" 2 4 "" { "Pass" "Bet" } 0
t "" 19 "" { 1 -1 }
t "" 20 "" { -2 2 }
c "" 4 "" { "Deal:0" 0.5 "Deal:1" 0.5 } 0
p "" 1 5 "" { "Pass" "Bet" } 0
p "" 2 5 "" { "Pass" "Bet" } 0
t "" 21 "" { 1 -1 }
p "" 1 6 "" { "Pass" "Bet" } 0
t "" 22 "" { -1 1 }
t "" 23 "" { 2 -2 }
p "" 2 6 "" { "Pass" "Bet" } 0
t "" 24 "" { 1 -1 }
t "" 25 "" { 2 -2 }
p "" 1 5 "" { "Pass" "Bet" } 0
p "" 2 1 "" { "Pass" "Bet" } 0
t "" 26 "" { 1 -1 }
p "" 1 6 "" { "Pass" "Bet" } 0
t "" 27 "" { -1 1 }
t "" 28 "" { 2 -2 }
p "" 2 2 "" { "Pass" "Bet" } 0
t "" 29 "" { 1 -1 }
t "" 30 "" { 2 -2 }\n""")
    game = pyspiel.load_game("kuhn_poker")
    efg_text = pyspiel.game_to_efg_string(game, True, True)
    self.assertEqual(efg_text, expected_kuhn_efg)

  def test_ld(self):
    expected_ld_efg = ("""EFG 2 R "liars_dice()" { "Player 1" "Player 2" }
c "" 1 "" { "Roll 1" 0.1666666667 "Roll 2" 0.1666666667 "Roll 3" 0.1666666667 "Roll 4" 0.1666666667 "Roll 5" 0.1666666667 "Roll 6" 0.1666666667 } 0
c "" 2 "" { "Roll 1" 0.1666666667 "Roll 2" 0.1666666667 "Roll 3" 0.1666666667 "Roll 4" 0.1666666667 "Roll 5" 0.1666666667 "Roll 6" 0.1666666667 } 0
p "" 1 1 "" { "1-1" "1-2" "1-3" "1-4" "1-5" "1-6" "2-1" "2-2" "2-3" "2-4" "2-5" "2-6" } 0
p "" 2 1 "" { "1-2" "1-3" "1-4" "1-5" "1-6" "2-1" "2-2" "2-3" "2-4" "2-5" "2-6" "Liar" } 0
p "" 1 2 "" { "1-3" "1-4" "1-5" "1-6" "2-1" "2-2" "2-3" "2-4" "2-5" "2-6" "Liar" } 0
p "" 2 2 "" { "1-4" "1-5" "1-6" "2-1" "2-2" "2-3" "2-4" "2-5" "2-6" "Liar" } 0
p "" 1 3 "" { "1-5" "1-6" "2-1" "2-2" "2-3" "2-4" "2-5" "2-6" "Liar" } 0
p "" 2 3 "" { "1-6" "2-1" "2-2" "2-3" "2-4" "2-5" "2-6" "Liar" } 0
p "" 1 4 "" { "2-1" "2-2" "2-3" "2-4" "2-5" "2-6" "Liar" } 0
p "" 2 4 "" { "2-2" "2-3" "2-4" "2-5" "2-6" "Liar" } 0
p "" 1 5 "" { "2-3" "2-4" "2-5" "2-6" "Liar" } 0
p "" 2 5 "" { "2-4" "2-5" "2-6" "Liar" } 0
p "" 1 6 "" { "2-5" "2-6" "Liar" } 0
p "" 2 6 "" { "2-6" "Liar" } 0
p "" 1 7 "" { "Liar" } 0
t "" 1 "" { 1 -1 }
t "" 2 "" { -1 1 }
p "" 2 7 "" { "Liar" } 0
t "" 3 "" { -1 1 }
t "" 4 "" { 1 -1 }
p "" 1 8 "" { "2-6" "Liar" } 0
p "" 2 8 "" { "Liar" } 0
t "" 5 "" { -1 1 }
t "" 6 "" { 1 -1 }
p "" 1 9 "" { "Liar" } 0
t "" 7 "" { 1 -1 }
t "" 8 "" { -1 1 }
p "" 2 9 "" { "2-5" "2-6" "Liar" } 0
p "" 1 10 "" { "2-6" "Liar" } 0
p "" 2 10 "" { "Liar" } 0
t "" 9 "" { -1 1 }
t "" 10 "" { 1 -1 }
p "" 1 11 "" { "Liar" } 0
t "" 11 "" { 1 -1 }
t "" 12 "" { -1 1 }
p "" 2 11 "" { "2-6" "Liar" } 0
p "" 1 12 "" { "Liar" } 0
t "" 13 "" { 1 -1 }
t "" 14 "" { -1 1 }
p "" 2 12 "" { "Liar" } 0
t "" 15 "" { -1 1 }
t "" 16 "" { 1 -1 }
p "" 1 13 "" { "2-4" "2-5" "2-6" "Liar" } 0
p "" 2 13 "" { "2-5" "2-6" "Liar" } 0
p "" 1 14 "" { "2-6" "Liar" } 0
p "" 2 14 "" { "Liar" } 0
t "" 17 "" { -1 1 }
t "" 18 "" { 1 -1 }\n""")
    game = pyspiel.load_game("liars_dice")
    efg_text = pyspiel.game_to_efg_string(game, True, True)
    efg_text = "\n".join(efg_text.splitlines()[:49]) + "\n" #truncate to first 49 lines for tests (i.e. outcome node t = 18)
    self.assertEqual(efg_text, expected_ld_efg)

  def test_leduc(self):
    expected_leduc_efg = ("""EFG 2 R "leduc_poker()" { "Player 1" "Player 2" }
c "" 1 "" { "Chance outcome:0" 0.1666666667 "Chance outcome:1" 0.1666666667 "Chance outcome:2" 0.1666666667 "Chance outcome:3" 0.1666666667 "Chance outcome:4" 0.1666666667 "Chance outcome:5" 0.1666666667 } 0
c "" 2 "" { "Chance outcome:1" 0.2 "Chance outcome:2" 0.2 "Chance outcome:3" 0.2 "Chance outcome:4" 0.2 "Chance outcome:5" 0.2 } 0
p "" 1 1 "" { "Call" "Raise" } 0
p "" 2 1 "" { "Call" "Raise" } 0
c "" 3 "" { "Chance outcome:2" 0.25 "Chance outcome:3" 0.25 "Chance outcome:4" 0.25 "Chance outcome:5" 0.25 } 0
p "" 1 2 "" { "Call" "Raise" } 0
p "" 2 2 "" { "Call" "Raise" } 0
t "" 1 "" { 0 0 }
p "" 1 3 "" { "Fold" "Call" "Raise" } 0
t "" 2 "" { -1 1 }
t "" 3 "" { 0 0 }
p "" 2 3 "" { "Fold" "Call" } 0
t "" 4 "" { 5 -5 }
t "" 5 "" { 0 0 }
p "" 2 4 "" { "Fold" "Call" "Raise" } 0
t "" 6 "" { 1 -1 }
t "" 7 "" { 0 0 }
p "" 1 4 "" { "Fold" "Call" } 0
t "" 8 "" { -5 5 }
t "" 9 "" { 0 0 }
p "" 1 5 "" { "Call" "Raise" } 0
p "" 2 5 "" { "Call" "Raise" } 0
t "" 10 "" { 0 0 }
p "" 1 6 "" { "Fold" "Call" "Raise" } 0
t "" 11 "" { -1 1 }
t "" 12 "" { 0 0 }
p "" 2 6 "" { "Fold" "Call" } 0
t "" 13 "" { 5 -5 }
t "" 14 "" { 0 0 }
p "" 2 7 "" { "Fold" "Call" "Raise" } 0
t "" 15 "" { 1 -1 }
t "" 16 "" { 0 0 }
p "" 1 7 "" { "Fold" "Call" } 0
t "" 17 "" { -5 5 }
t "" 18 "" { 0 0 }
p "" 1 8 "" { "Call" "Raise" } 0
p "" 2 8 "" { "Call" "Raise" } 0
t "" 19 "" { 0 0 }
p "" 1 9 "" { "Fold" "Call" "Raise" } 0
t "" 20 "" { -1 1 }
t "" 21 "" { 0 0 }\n""")
    game = pyspiel.load_game("leduc_poker")
    efg_text = pyspiel.game_to_efg_string(game, True, True)
    efg_text = "\n".join(efg_text.splitlines()[:42]) + "\n" #truncate to first 42 lines for tests (i.e. outcome node t = 21)
    self.assertEqual(efg_text, expected_leduc_efg)

  def test_tiny_hanabi(self):
    expected_tiny_hanabi_efg = ("""EFG 2 R "tiny_hanabi()" { "Player 1" "Player 2" }
c "" 1 "" { "d0" 0.5 "d1" 0.5 } 0
c "" 2 "" { "d0" 0.5 "d1" 0.5 } 0
p "" 1 1 "" { "p0a0" "p0a1" "p0a2" } 0
p "" 2 1 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 1 "" { 10 10 }
t "" 2 "" { 0 0 }
t "" 3 "" { 0 0 }
p "" 2 2 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 4 "" { 4 4 }
t "" 5 "" { 8 8 }
t "" 6 "" { 4 4 }
p "" 2 3 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 7 "" { 10 10 }
t "" 8 "" { 0 0 }
t "" 9 "" { 0 0 }
p "" 1 1 "" { "p0a0" "p0a1" "p0a2" } 0
p "" 2 4 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 10 "" { 0 0 }
t "" 11 "" { 0 0 }
t "" 12 "" { 10 10 }
p "" 2 5 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 13 "" { 4 4 }
t "" 14 "" { 8 8 }
t "" 15 "" { 4 4 }
p "" 2 6 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 16 "" { 0 0 }
t "" 17 "" { 0 0 }
t "" 18 "" { 10 10 }
c "" 3 "" { "d0" 0.5 "d1" 0.5 } 0
p "" 1 2 "" { "p0a0" "p0a1" "p0a2" } 0
p "" 2 1 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 19 "" { 0 0 }
t "" 20 "" { 0 0 }
t "" 21 "" { 10 10 }
p "" 2 2 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 22 "" { 4 4 }
t "" 23 "" { 8 8 }
t "" 24 "" { 4 4 }
p "" 2 3 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 25 "" { 0 0 }
t "" 26 "" { 0 0 }
t "" 27 "" { 0 0 }
p "" 1 2 "" { "p0a0" "p0a1" "p0a2" } 0
p "" 2 4 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 28 "" { 10 10 }
t "" 29 "" { 0 0 }
t "" 30 "" { 0 0 }
p "" 2 5 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 31 "" { 4 4 }
t "" 32 "" { 8 8 }
t "" 33 "" { 4 4 }
p "" 2 6 "" { "p1a0" "p1a1" "p1a2" } 0
t "" 34 "" { 10 10 }
t "" 35 "" { 0 0 }
t "" 36 "" { 0 0 }\n""")
    game = pyspiel.load_game("tiny_hanabi")
    efg_text = pyspiel.game_to_efg_string(game, True, True)
    self.assertEqual(efg_text, expected_tiny_hanabi_efg)

if __name__ == "__main__":
  absltest.main()

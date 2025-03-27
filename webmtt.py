from treys import Evaluator, Card
import random
from template import *

class PokerBot:
    def __init__(self, hole_cards, community_cards, chips, pot):
        self.hole_cards = [Card.new(card) for card in hole_cards]
        self.community_cards = [Card.new(card) for card in community_cards]
        self.chips = chips
        self.pot = pot
        self.evaluator = Evaluator()

    def evaluate_hand(self):
        """Menilai kekuatan kartu saat ini"""
        if len(self.community_cards) < 3:
            return None  # Tidak bisa mengevaluasi sebelum flop
        return self.evaluator.evaluate(self.community_cards, self.hole_cards)

    def simulate_odds(self, trials=3000):
        """Simulasi odds menang dengan Monte Carlo"""
        deck = [Card.new(rank+suit) for rank in '23456789TJQKA' for suit in 'shdc']
        used_cards = set(self.hole_cards + self.community_cards)
        deck = [card for card in deck if card not in used_cards]

        win_count = 0
        for _ in range(trials):
            random.shuffle(deck)
            opponent_hand = deck[:2]
            remaining_board = deck[2:7-len(self.community_cards)] + self.community_cards

            my_score = self.evaluator.evaluate(remaining_board, self.hole_cards)
            opp_score = self.evaluator.evaluate(remaining_board, opponent_hand)

            if my_score < opp_score:
                win_count += 1

        return win_count / trials

    def make_decision(self):
        """Membuat keputusan berdasarkan odds dan ukuran pot"""
        if len(self.community_cards) < 3:
            return "CHECK/FOLD"  # Preflop tanpa informasi lebih lanjut

        hand_strength = self.evaluate_hand()
        win_odds = self.simulate_odds()

        pot_odds = self.pot / (self.pot + self.chips)

        # Jika odds menang sangat tinggi atau chip hampir habis → ALL IN
        if win_odds > 0.8 or self.chips < (self.pot * 0.5):
            return "ALL IN"
        elif win_odds > pot_odds + 0.1:
            return "RAISE"
        elif win_odds > pot_odds:
            return "CALL"
        else:
            return "FOLD"

# Contoh Input
hole_cards = ['As', 'Ks']
community_cards = ['2h', '7d', 'Jc']
chips = 30  # Simulasi chip kecil untuk uji ALL IN
pot = 500

bot = PokerBot(hole_cards, community_cards, chips, pot)
decision = bot.make_decision()
print(f"Keputusan Bot: {decision}")



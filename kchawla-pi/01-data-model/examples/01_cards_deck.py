import collections

Card = collections.namedtuple('Card', 'rank suite')

class FrenchDeck(object):
    ranks = [str(rank) for rank in range(1,11)] + list('JKQA')
    suites = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank=rank_, suite=suite_) for rank_ in self.ranks
                                                     for suite_ in self.suites]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __str__(self):
        print( '\n'.join(sorted(['\t'.join([str(card_) for card_ in self._cards if card_.rank == rank_]) for rank_ in self.ranks])))
        return 'a'
    
    

    
deck0 = FrenchDeck()
print(deck0)
print(repr(deck0))

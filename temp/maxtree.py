import random
from anytree import Node, RenderTree, LevelOrderGroupIter

class SimGame:
    self.in_combat = False
    self.player = None
    self.monsters = []
    self.draw_pile = []
    self.discard_pile = []
    self.exhaust_pile = []
    self.hand = []
    self.limbo = []
    self.card_in_play = None
    self.turn = 0
    self.cards_discarded_this_turn = 0
    self.barricade = False


def getstate:
    n = SimGame()
    n.player = Game.player

#return a random evaluation number for given game state
def eval_function(gamestate):
    #eval is a number between -50 and 50
    eval = random.randrange(-50, 51)
    return eval


#return new list of available cards after playing one
def get_next_game_state(card, cards):
    remaining_cards = cards.copy() #copy list of cards

    #remove the card being played from list of cards
    remaining_cards.remove(card)
    return remaining_cards #return remaining list of cards

#builds a tree using current game
def build_tree(gamestate):
        for x in gamestate.name.card_list:
            temp = Game_State() #new child game state
            temp.card_list = gamestate.name.card_list #copy card list
            temp.card_list = get_next_game_state(x, temp.card_list) #get next game state
            if len(temp.card_list) == 1: #if this is a leaf assign evaluation
                temp.grade = eval_function(1)
            if temp.card_list: #if card list is not empty
                child = Node(temp, parent=gamestate) #create child node
                build_tree(child) #recursively build tree

def tree_search(r):
    if not r.children: #if node is a leaf
        return
    max = -51
    for children in LevelOrderGroupIter(r, maxlevel=2):
        for node in children:
            if node in r.children:
                tree_search(node)
                if node.name.grade > max:
                    max = node.name.grade
    r.name.grade = max #set current node's eval to max of children

cards = ['card1', 'card2', 'card3']

class Game_State:
    card_list = []
    grade = 0

a = Game_State()
a.card_list = cards.copy()
root = Node(a, parent=None)
build_tree(root)
for pre, fill, node in RenderTree(root):
    print("%s%s%s" % (pre, node.name.card_list, node.name.grade))
tree_search(root)
print()
print()
print()
print()
for pre, fill, node in RenderTree(root):
    print("%s%s%s" % (pre, node.name.card_list, node.name.grade))
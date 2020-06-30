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
    #--------- Additional
    self.energy = 3
    #--------- Card switches needed for combat
    self.Barricade = False
    self.Battle_Trace = False
    self.Blood_For_Blood = False
    self.Combust = False
    self.Corruption = False
    self.Dark_Embrace = False
    self.Demon_Form = False
    self.Double_Tap = False
    self.Evolve = False
    self.Feel_No_Pain = False
    self.Fire_Breathing = False
    self.Flame_Barrier = False
    self.Flex = False
    self.Juggernaut = False
    self.Metallicize = False
    self.Rage = False
    self.Rupture = False




def getstate:
    n = SimGame()
    n.player = Game.player
    n.monsters = Game.monsters
    n.draw_pile = Game.draw_pile
    n.discard_pile = Game.discard_pile
    n.exhaust_pile = Game.exhaust_pile
    n.hand = Game.hand
    n.limbo = Game.limbo
    n.card_in_play = Game.card_in_play
    n.turn = Game.turn
    n.cards_discarded_this_turn = Game.cards_discarded_this_turn


#---------------

# Effect at end of turn
def end_of_turn(gamestate):
    newstate = gamestate
    #deal poison damage
    #ethereal check, if card is ethereal, exhaust it
    return newstate

def start_of_turn(gamestate):
    newstate = gamestate
    #reset energy/mana
    return newstate
#Need to Helper Function
#Cost,

#example pseudocode
for cardname, card in Game.hand:
    x = cards[card]
    #check if enough energy to play card
    #might have to add energy to game state
    if SimGame.energy >= x[0]:
        SimGame.energy = Game.energy - x[0]
        #somehow play card/call card function from dict
        #PROBLEM: how are monsters stores in gamestate?'
        #since some cards don't need targets, the card function will loop through the targets if needed?
        if x[1] = False:
            x[2](SimGame)
            SimGame = SimGame.hand.remove(cardname)
            SimGame = SimGame.discard_pile.append(cardname)
        else:
            for target in SimGame.Monsters:
                x[2](SimGame, target)
                SimGame = SimGame.hand.remove(cardname)
                SimGame = SimGame.discard_pile.append(cardname)

#will need to evaluate the new gamestate the card function returns?

#---------------

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

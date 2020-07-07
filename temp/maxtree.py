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




def getstate():
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
    return n


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

#will need to evaluate the new gamestate the card function returns?

#---------------

#return a random evaluation number for given game state
def eval_function(gamestate):
    #eval is a number between -100 and 100
    eval = random.randrange(-100, 101)
    return eval

root_node.state = getstate()
newstate = root_node.state
for cardname, card in newstate.hand:
    x = cards[card]
    #check if enough energy to play card
    #might have to add energy to game state
    if newstate.energy >= x[0]:
        newstate.energy = newstate.energy - x[0]
        #somehow play card/call card function from dict
        #PROBLEM: how are monsters stores in gamestate?'
        #since some cards don't need targets, the card function will loop through the targets if needed?
        if x[1] = False:
            x[2](newstate)
            newstate = newstate.hand.remove(cardname)
            newstate = newstate.discard_pile.append(cardname)
        else:
            for target in newstate.Monsters:
                x[2](newstate, target)
                newstate = newstate.hand.remove(cardname)
                newstate = newstate.discard_pile.append(cardname)



def get_next_game_state(card, enough_energy, state_node):
        gs = SimGame()
        x = cards[card]
        if state_node.name.energy >= x[0]:
            gs.hand = state_node.name.hand.copy()
            gs.hand.remove(card)
            gs.discard_pile = state_node.name.discard_pile.copy()
            gs.discard_pile.append(card)
            gs.energy = state_node.name.energy
            gs.energy -= x[0]
            gs = x[2](state_node)
        else:
            enough_energy = False
        return gs

#builds a tree using current game
def build_tree(gamestate):
        for x in gamestate.name.hand:
            temp = SimGame()
            can_play = True
            temp = get_next_game_state(x, can_play, gamestate)
            if can_play and temp.hand: #if card list is not empty
                child = Node(temp, parent=gamestate) #create child node
                build_tree(child) #recursively build tree

def eval_tree(r):
    for children in LevelOrderGroupIter(r):
        for node in children:
            if not node.children:
                node.name.grade = eval_function(1)

def tree_search(r):
    if not r.children: #if node is a leaf
        return
    max = -101
    for children in LevelOrderGroupIter(r, maxlevel=2):
        for node in children:
            if node in r.children:
                tree_search(node)
                if node.name.grade > max:
                    max = node.name.grade
    r.name.grade = max #set current node's eval to max of children

#returns card played
def return_move(hand1, hand2):
    for x in hand1:
        if x not in hand2:
            return x

#returns path to max gamestate
def return_path(r):
    move_list = []
    for children in LevelOrderGroupIter(r, maxlevel=2):
        for node in children:
            if node in r.children:
                if node.name.grade == r.name.grade:
                    move = return_move(r.name.hand, node.name.hand)
                    move_list.append(move)
                    move_list += return_path(node)
    return move_list





cards = ['health', 'potion', 'attack']

a = SimGame()
a.hand = cards.copy()
root = Node(a, parent=None)
build_tree(root)
for pre, fill, node in RenderTree(root):
    print("%s%s%s" % (pre, node.name.hand, node.name.grade))
eval_tree(root)
print()
print()
print()
print()
for pre, fill, node in RenderTree(root):
    print("%s%s%s" % (pre, node.name.hand, node.name.grade))
tree_search(root)
print()
print()
print()
print()
for pre, fill, node in RenderTree(root):
    print("%s%s%s" % (pre, node.name.hand, node.name.grade))
print()
print()
print()
print()
print(return_path(root))

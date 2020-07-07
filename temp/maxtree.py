import random
from anytree import Node, RenderTree, LevelOrderGroupIter



#will need to evaluate the new gamestate the card function returns?

#---------------

#return a random evaluation number for given game state
def eval_function(gamestate):
    #eval is a number between -100 and 100
    eval = random.randrange(-100, 101)
    return eval


#return new list of available cards after playing one
def get_next_game_state(card, enough_energy, gamestate):
        gs = SimGame()
        x = 0
        if card == 'health':
           x = 1 
        if card == 'potion':
           x = 2 
        if card == 'health':
           x = 3 
        if gamestate.name.energy >= x:
            gs.hand = gamestate.name.hand.copy()
            gs.hand.remove(card)
            gs.discard_pile = gamestate.name.discard_pile.copy()
            gs.discard_pile.append(card)
            gs.energy = gamestate.name.energy
            gs.energy -= x
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


class SimGame:
    in_combat = False
    player = None
    monsters = []
    draw_pile = []
    discard_pile = []
    exhaust_pile = []
    hand = []
    limbo = []
    card_in_play = None
    turn = 0
    cards_discarded_this_turn = 0
    grade = 0 #evaluation grade
    #--------- Additional
    energy = 3
    #--------- Card switches needed for combat
    Barricade = False
    Battle_Trace = False
    Blood_For_Blood = False
    Combust = False
    Corruption = False
    Dark_Embrace = False
    Demon_Form = False
    Double_Tap = False
    Evolve = False
    Feel_No_Pain = False
    Fire_Breathing = False
    Flame_Barrier = False
    Flex = False
    Juggernaut = False
    Metallicize = False
    Rage = False
    Rupture = False

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

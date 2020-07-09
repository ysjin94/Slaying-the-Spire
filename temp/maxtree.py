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
    self.Berserk = False
    self.Brutality = False
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



def get_next_game_state(card, state):
        x = cards[card]
        if state.energy >= x[0]:
            state.hand.remove(card)
            state.discard_pile.append(card)
            #state.energy -= x[0]
            return True
        else:
            return False

#builds a tree using current game
def build_tree(gamestate):
        for x in gamestate.name.hand:
            next_state = copy.deepcopy(gamestate.name)
            can_play = get_next_game_state(x, next_state)
            #if can_play and x == 'armament':
            #    child2 = Node(temp, parent=gamestate) #create child node
            #    for i in range(len(temp.hand)):
            #        temp2 = copy.deepcopy(temp)
            #        temp2.hand[i] += ' upgrade' 
            #        child3 = Node(temp2, parent=child2)
            #        build_tree(child3) #recursively build tree
            #else:
            if can_play:
                child = Node(next_state, parent=gamestate) #create child node
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
def find_path(r):
    move_list = []
    for children in LevelOrderGroupIter(r, maxlevel=2):
        for node in children:
            if node in r.children:
                if node.name.grade == r.name.grade:
                    move = return_move(r.name.hand, node.name.hand)
                    move_list.append(move)
                    move_list += find_path(node)
    return move_list 

def return_path(r):
    moves = find_path(r)
    for i in range(len(moves)):
        #if moves[i-1] == 'play armament':
        #    moves[i] = 'upgrade ' + moves[i]
        #else:
        moves[i] = 'play ' + moves[i]
    print(moves)





cards = ['health', 'potion', 'attack']

a = getstate()
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

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
    self.decisions = []
    #--------- Card switches needed for combat
    # self.Barricade = False
    # self.Battle_Trace = False
    # self.Blood_For_Blood = False
    # self.Berserk = False
    # self.Brutality = False
    # self.Combust = False
    # self.Corruption = False
    # self.Dark_Embrace = False
    # self.Demon_Form = False
    # self.Double_Tap = False
    # self.Evolve = False
    # self.Feel_No_Pain = False
    # self.Fire_Breathing = False
    # self.Flame_Barrier = False
    # self.Flex = False
    # self.Juggernaut = False
    # self.Metallicize = False
    # self.Rage = False
    # self.Rupture = False




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
    n.decisions = []
    return n

#---------------

# Effect at end of turn
# def end_of_turn(gamestate):
#     newstate = gamestate
#     #deal poison damage
#     #ethereal check, if card is ethereal, exhaust it
#     return newstate
#
# def start_of_turn(gamestate):
#     newstate = gamestate
#     #reset energy/mana
#     return newstate
#Need to Helper Function
#Cost,

#will need to evaluate the new gamestate the card function returns?

#----------------

#return a random evaluation number for given game state
def eval_function(gamestate):
    eval = 0

    return eval

# root_node.state = getstate()
# newstate = root_node.state
# for cardname, card in newstate.hand:
#     x = cards[card]
#     #check if enough energy to play card
#     #might have to add energy to game state
#     if newstate.energy >= x[0]:
#         newstate.energy = newstate.energy - x[0]
#         #somehow play card/call card function from dict
#         #PROBLEM: how are monsters stores in gamestate?'
#         #since some cards don't need targets, the card function will loop through the targets if needed?
#         if x[1] = False:
#             x[2](newstate)
#             newstate = newstate.hand.remove(cardname)
#             newstate = newstate.discard_pile.append(cardname)
#         else:
#             for target in newstate.Monsters:
#                 x[2](newstate, target)
#                 newstate = newstate.hand.remove(cardname)
#                 newstate = newstate.discard_pile.append(cardname)



# returns the next game state after updating a copy of current state
# @param decision: the decision chosen for the next game state
# decision is either the card to be played or the end turn function
# @param state: the current state to be copied and modified
def get_next_game_state(play, state, target = False):

    # copy current state
    next_state = copy.deepcopy(state)

    decisionlist = []
    if play == 'End_Turn':
        next_state = end_of_turn(next_state)
        next_state = start_of_turn(next_state)
        decisionlist.append['End_Turn']

    elif target == False
        card = play.name
        next_state = cards[card](next_state, upgrades = play.upgrades)
        decisionlist.append[play]

    elif target == True:
        card = play.name
        next_state = cards[card](next_state, hitmonster = target, upgrades = play.upgrades)
        decisionlist.append[play]
        decisionlist.append[target]


    next_state.decision.append(decisionlist)
    return next_state

# recursively builds a decision tree using current gamestate
# @param gamestate: the node containing the current game state
# when the function is first called this is the root node
def build_tree(gamestate):
    for x in gamestate.name.decisions:
        # card energy cost
        card = cards[cardname]
        card_cost = card[0]
        if x == 'END TURN':
            card_cost = 0

        # if there is enough energy to play this card
        if gamestate.name.energy >= card_cost:
            # next game state
            next_state = get_next_game_state(x, gamestate.name)
            # create child node
            child = Node(next_state, parent=gamestate)
            # do not create children for end turn
            if x != 'END TURN':
                build_tree(child) #recursively build tree

            #################
           # if x == 'armament':
           #     for i in range(len(next_state.hand)):
           #         temp = copy.deepcopy(next_state)
           #         for j in range(len(temp.decisions)):
           #             if temp.hand[i] == temp.decisions[j]:
           #                 temp.decisions[j] += ' upgrade'
           #         temp.hand[i] += ' upgrade'
           #         child2 = Node(temp, parent=child)
           #         build_tree(child2) #recursively build tree
           # else:
            #################

def build_tree(gamestate):
    for c in gamestate.name.hand:
        if gamestate.name.energy >= c.cost:
            #get_next_game_state needs to append the decision to gamestate.decisions

            #checks if needs target
            card = c.name
            if cards[card][1] == True:
                for monsterindex in range(len(gamestate.name.monsters)):
                    next_state = get_next_game_state(c, gamestate.name, target = monsterindex)
                    child = Node(next_state, parent = gamestate)
                    build_tree(child)

            #don't need target
            else:
                next_state = get_next_game_state(c, gamestate.name)
                child = Node(next_state, parent = gamestate)
                build_tree(child)

    #end turn
    next_state = get_next_game_state('End_Turn', gamestate.name)
    child = Node(next_state, parent = gamestate)
    build_tree(child)


# assigns evaluation values to the leaves of the tree only
# @param r: the root node of the tree
def eval_tree(r):
    for children in LevelOrderGroupIter(r):
        for node in children:
            if not node.children:
                node.name.grade = eval_function(1)

# percolates the max evaluation value up to the root of the tree
# @param r: the root node of the tree
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

# returns the choice made between a parent node and its child
# @param list1: the list of decisions belonging to parent node
# @param list2: the list of decisions belonging to child node
def return_move(list1, list2):
    for x in list1:
        if x not in list2:
            return x

# returns path to gamestate with max evaluation value
# @param r: the root node
def find_path(r):
    move_list = []
    for children in LevelOrderGroupIter(r, maxlevel=2):
        for node in children:
            if node in r.children:
                if node.name.grade == r.name.grade:
                    move = return_move(r.name.decisions, node.name.decisions)
                    move_list.append(move)
                    move_list += find_path(node)
    return move_list

# returns the list of decisions to obtain max evaluation value
# @param node: the root node
# @param state: the game state
def return_path(node, state):
    moves = find_path(node)



def get_decision(self):
    #newstate is type simgame
    simstate = getstate()
    root = Node(simstate, parent=None)
    build_tree(root)
    eval_tree(root)
    tree_search(root)
    return_path(root, simstate)

get_decision(1)

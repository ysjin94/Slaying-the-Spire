import random
from anytree import Node, RenderTree, LevelOrderGroupIter
from sys import stdout

from spirecomm.spire.game import Game
from spirecomm.spire.character import Intent, PlayerClass
import spirecomm.spire.card
from spirecomm.communication.action import *

class SimGame():
    def __init__(self):
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

#returns a SimGame that includes the gamestate stuff but also desisions
def getstate(gamestate):
    n = SimGame()
    n.player = gamestate.player
    n.monsters = gamestate.monsters
    n.draw_pile = gamestate.draw_pile
    n.discard_pile = gamestate.discard_pile
    n.exhaust_pile = gamestate.exhaust_pile
    n.hand = gamestate.hand
    n.limbo = gamestate.limbo
    n.card_in_play = gamestate.card_in_play
    n.turn = gamestate.turn
    n.cards_discarded_this_turn = gamestate.cards_discarded_this_turn
    n.decisions = []
    return n

#return a random evaluation number for given game state
def eval_function(gamestate):
    #eval out of 1000 or so, can be more or less
    eval = 0
    #hp
    eval += (gamestate.current_hp * 2)
    eval += gamestate.gold
    if gamestate.monsters == []:
        eval += 200
    else:
        for m in gamestate.monsters:
            eval -= m.current_hp
            eval -= (m.move_adjusted_damage * m.move_hits)
            for mpower in gamestate.player.powers:
                if mpower.name == 'Strength':
                    eval -= mpower.amount
                if mpower.name == 'Weakened':
                    eval += mpower.amount
                if mpower.name == 'Vulnerable':
                    eval += mpower.amount
                if mpower.name == 'Rage':
                    eval -= mpower.amount
                if mpower.name == 'Double Tap':
                    eval -= (mpower.amount * 25)
                if mpower.name == 'Flame Barrier':
                    eval -= mpower.amount
                if mpower.name == 'Dexterity':
                    eval -= mpower.amount
                if mpower.name == 'Juggernaut':
                    eval -= mpower.amount
                if mpower.name == 'Dark Embrace':
                    eval -= mpower.amount
                if mpower.name == 'Feel No Pain':
                    eval -= mpower.amount
                if mpower.name == 'Sentinel':
                    eval -= mpower.amount
                if mpower.name == 'No Draw':
                    eval += mpower.amount
                if mpower.name == 'Evolve':
                    eval -= mpower.amount
                if mpower.name == 'Fire Breathing':
                    eval -= mpower.amount
                if mpower.name == 'Combust':
                    eval -= mpower.amount
                if mpower.name == 'Rupture':
                    eval -= mpower.amount
                if mpower.name == 'Flex':
                    eval -= mpower.amount
                if mpower.name == 'Metallicize':
                    #number of block in the end
                    eval -= (mpower.amount*(mpower.amount + 1))/2
                if mpower.name == 'Poison':
                    #number of damage in the end
                    eval += (mpower.amount*(mpower.amount + 1))/2
                if mpower.name == 'Energized':
                    eval -= 100
                if mpower.name == 'Barricade':
                    eval -= (gamestate.player.block * 2)
                if mpower.name == 'Demon Form':
                    eval -= (mpower.amount * 100)
                if mpower.name == 'Brutality':
                    eval -= (mpower.amount * 25)
                if mpower.name == 'Rupture':
                    eval -= (mpower.amount * 25)
            #have to do monster powers

    #have to do player powers
    for ppower in gamestate.player.powers:
        if ppower.name == 'Strength':
            eval += ppower.amount
        if ppower.name == 'Weakened':
            eval -= ppower.amount
        if ppower.name == 'Vulnerable':
            eval -= ppower.amount
        if ppower.name == 'Rage':
            eval += ppower.amount
        if ppower.name == 'Double Tap':
            eval += (ppower.amount * 25)
        if ppower.name == 'Flame Barrier':
            eval += ppower.amount
        if ppower.name == 'Dexterity':
            eval += ppower.amount
        if ppower.name == 'Juggernaut':
            eval += ppower.amount
        if ppower.name == 'Dark Embrace':
            eval += ppower.amount
        if ppower.name == 'Feel No Pain':
            eval += ppower.amount
        if ppower.name == 'Sentinel':
            eval += ppower.amount
        if ppower.name == 'No Draw':
            eval -= ppower.amount
        if ppower.name == 'Evolve':
            eval += ppower.amount
        if ppower.name == 'Fire Breathing':
            eval += ppower.amount
        if ppower.name == 'Combust':
            eval += ppower.amount
        if ppower.name == 'Rupture':
            eval += ppower.amount
        if ppower.name == 'Flex':
            eval += ppower.amount
        if ppower.name == 'Metallicize':
            #number of block in the end
            eval += (ppower.amount*(ppower.amount + 1))/2
        if ppower.name == 'Poison':
            #number of damage in the end
            eval -= (ppower.amount*(ppower.amount + 1))/2
        if ppower.name == 'Energized':
            eval += 100
        if ppower.name == 'Barricade':
            eval += (gamestate.player.block * 2)
        if ppower.name == 'Demon Form':
            eval += (ppower.amount * 100)
        if ppower.name == 'Brutality':
            eval += (ppower.amount * 25)
        if ppower.name == 'Rupture':
            eval += (ppower.amount * 25)
    #have to do potions

    #print all the powers for troubleshooting later
    original_stdout = sys.stdout # Save a reference to the original standard output

    with open('powers .txt', 'a') as f:
        sys.stdout = f # Change the standard output to the file we created.
        powerout = ['Player Powers']
        for p in gamestate.player.powers:
            powerout = []
            powerout.append('power_id = ' + p.power_id)
            powerout.append('power_name = ' + p.power_name)
            powerout.append('amount = ' + p.amount)
            powerout.append('damage = ' + p.damage)
            powerout.append('misc = ' + p.misc)
            powerout.append('just_applied' + p.just_applied)
            powerout.append('card' + p.card)
        print(powerout)

        #Monster powers
        mpowerout = ['Monster Powers']
            for m in gamestate.monsters:
                for p in gamestate.monster.powers:
                    mpowerout = []
                    mpowerout.append('power_id = ' + p.power_id)
                    mpowerout.append('power_name = ' + p.power_name)
                    mpowerout.append('amount = ' + p.amount)
                    mpowerout.append('damage = ' + p.damage)
                    mpowerout.append('misc = ' + p.misc)
                    mpowerout.append('just_applied' + p.just_applied)
                    mpowerout.append('card' + p.card)
        print(mpowerout)
        sys.stdout = original_stdout # Reset the standard output to its original value
    return eval


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
        decisionlist.append('End_Turn')

    elif target == False:
        card = play.name
        next_state.hand.remove(play)
        next_state = cards[card](next_state, upgrades = play.upgrades)
        if play.exhausts == True:
            addcard(newstate, play.name, 'exhaust_pile')
        else:
            addcard(newstate, play.name, 'discard_pile')
        decisionlist.append(play)

    elif target == True:
        card = play.name
        next_state.hand.remove(play)
        next_state = cards[card](next_state, hitmonster = target, upgrades = play.upgrades)
        if play.exhausts == True:
            addcard(newstate, play.name, 'exhaust_pile')
        else:
            addcard(newstate, play.name, 'discard_pile')
        decisionlist.append(play)
        decisionlist.append(target)


    next_state.decision.append(decisionlist)
    return next_state

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

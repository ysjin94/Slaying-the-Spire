import random
from anytree import Node, RenderTree, LevelOrderGroupIter

#return a random evaluation number for given game state
def eval_function(gamestate):
    #eval is a number between -100 and 100
    eval = random.randrange(-100, 101)
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
                    move = return_move(r.name.card_list, node.name.card_list)
                    move_list.append(move)
                    move_list += return_path(node)
    return move_list 

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

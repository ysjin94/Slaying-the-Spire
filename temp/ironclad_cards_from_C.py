#THIS IS PARTLY PSEUDOCODE
#problems:upgrading a card not implemented

#dict of cards
#cost, target, function
#target true = card can target enemy
#target false = card just gets played
cards = {
    #after burning pact
    'Carnage' : [12, True, Carnage],
    'Clash' : [13, True, Clash ],
    'Cleave' : [14, True, Cleave],
    'Clothsline' : [15, True, Clothsline],
    'Combust' :[16, True, Combust],
    'Corruption' : [17, False, Corruption],
    'Dark Embrace' : [18, False, Dark_Embradce],
    'Defend' : [19, False, Defend],
    'Disarm' : [20, True, Disarm],
    'Double Tap' : [21, False, Double_Tap],
    'Dropkick' : [22, True, Dropkick],
    'Dual' : [23, False, Dual],
    'Entrench' :[24, False, Entrench],
    'Evolve' : [25, False, Evolve],
    'Exhume' : [26, False, Exhume],
    
    
}
#States
class Temp_State:
    def __init__(self, My_Strength, Monster_Strength,check_start_of_turn, weak, check_end_of_turn, current_cost, attacknum):
        self.weak = weak
        self.My_Strength = My_Strength
        self.Monster_Strength = Monster_Strength
        self.check_start_of_turn =check_start_of_turn
        self.check_end_of_turn = check_end_of_turn
        self.current_cost =current_cost
        self.attacknum = attacknum
        
        
#helper functions
#deal damage to monster
def dealdmg(gamestate, damage, monster, attacknum):
    newstate = gamestate
    for p in newstate.Player.Power:
        if p.power_name = Strength:
            newstate.Monsters[monster].current_hp -= (damage + p.amount) * attacknum
            return newstate
    else:
        newstate.Monsters[monster].current_hp -= damage * attacknum
        return newstate

#Need to Helper Function
#Cost,

#example pseudocode
for card in Game.hand:
    x = cards[card]
    #check if enough energy to play card
    #might have to add energy to game state
    if Game.energy >= x[0]:
        game.energy = game.energy - x[0]
        #somehow play card/call card function from dict
        #PROBLEM: how are monsters stores in gamestate?'
        #since some cards don't need targets, the card function will loop through the targets if needed?
        if x[1] = False:
            x[2](gamestate)
        else:
            for target in Game.Monsters:
                x[2](gamestate, target)

#will need to evaluate the new gamestate the card function returns?
        


#carnage 2 cost	Ethereal. Deal 20(28) damage : Ethereal removed until end of combat.
def Carnage (gamestate, hitmonster, Temp_State):
    newstate = gamestate
    # deal 20 damage
    newstate = dealdmg(newstate, 20, newstate.Monster[hitmonster], Temp_State.attacknum)
    #do not newstate.discard_pile.append('Carnage'), it is Ethereal.
    return newstate
    
#clash 0 cost Can only be played if every card in your hand is an Attack. Deal 14 damage.
def Clash (gmaestate, hitmonster, is_all_attack_in_hand, Temp_State):
    #Check = is_all_attack_in_hand , if every card in your hand is an Attack.
    newstate = gmaestate
    if is_all_attack_in_hand:
        newstate = dealdmg(newstate, 20, newstate.Monster[hitmonster], Temp_State.attacknum)
        newstate.discard_pile.append['Clash']
        return newstate
    else:
        newstate.discard_pile.append['Clash']
        return  newstate

#cleave 1 cost Deal 8 damage to ALL enemies.
def Cleave (gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #hitmonster is list such as monster = [moster1, moster2, moster3]
    #attack monster1, monster2, and monster3
    for num in len(hitmonster):
        newstate = dealdmg(newstate, 8, newstate.Monster[hitmonster[num]], Temp_State.attacknum)
    newstate.discard_pile.append('Cleave')
    return newstate

#clothsline 2 cost Deal 12 damage. Apply 2 Weak. weak : Target deals 25% less attack damage.
#need to apply weak
def Clothsline (gamestate, hitmonster, Temp_State):

    newstate = gamestate
    newstate = Monster[hitmonster].current_hp = newstate.Monsters[hitmonster].current_hp - 12
    newstate = newstate.discard_pile.append['Clothsline']
    return newstate

#combust 1 cost At the end of your turn, lose 1 HP and deal 5 damage to ALL enemies.
#How to apply At the end of your turn?
def Combust(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    # attack monster1, monster2, and monster3
    for attack in len(hitmonster):
        newstate = dealdmg(newstate, 5, newstate.Monsters[hitmonster[attack]], Temp_State.attacknum)

    newstate.discard_pile.append('Combust')

    return newstate

#corruption 3 cost Skills cost 0. Whenever you play a Skill, Exhaust it.
# Need to modify
def Corruption(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#dark embrace 2 cost Whenever a card is Exhausted, draw 1 card.
#Need to modify
def Dark_Embrace(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.discard_pile.append('Dark Embrace')
    return newstate

#defend 1 cost Gain 5 Block.
def Defend (gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #add 5 block
    newstate.player.block = newstate.player.block + 5
    newstate.discard_pile.append('Defend')
    return newstate
    
#demon form 3 cost At the start of each turn, gain 2 Strength.
#How to apply start of each turn?
def Demon Form(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    if State.check_start_of_turn
        State.My_Strength = State.My_Strength + 2
        newstate.discard_pile.append('Demon Form')
        return newstate
    else:
        newstate.discard_pile.append('Demon Form')
        return newstate
    
#disarm 1 cost Enemy loses 2 Strength. Exhaust.
def Disarm(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #add Enemy loses 2 Strength.
    newstate.exhaust_pile.append('Disarm')
    return newstate

#double tap 1 cost This turn, your next Attack is played twice.
def Double_Tap(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #need to modifiy
    Temp_State.attacknum = Temp_State.attacknum + 1
    return newstate

#dropkick 1 cost Deal 5 damage. If the enemy is Vulnerable, gain 1 energy and draw 1 card.
#
def Dropkick(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate
    
#dual wield 1 cost Create a copy of an Attack or Power card in your hand.
def Dual_Wield(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#entrench 2 cost Double your current Block.
def Entrench(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.player.block = newstate.player.block * 2
    newstate.discard_pile['Entrench']
    return newstate
    
#evolve 1 cost Whenever you draw a Status, draw 1 card.
def Evolve(gamestate, hitmonster, Temp_State):
    newstate =  gmaestate
    return newstate

#exhume 1 cost Place a card from your Exhaust pile into your hand. Exhaust.
#how to pick the card form exhaust pile
def Exhume(gmaestate, hitmonster, Temp_State):
    newstate = gamestate
    #add Place a card from your Exhaust pile
    newstate.exhaust_pile['Exhume']
    return newstate


#Modify here

"""

To do list:
    Debug
    Modify dealdmg : lose block first, than lose hp
    Make helper function : Gain Strangth
    Modify Monsters -> Monster (e.g newstate.Monsters[hitmonster] -> .. Monster[hitmonster] )
    Modify Start_of_turn : Add reset monster block = 0
    Need to Update Some functions that contains switch, example: Feel_No_Pain
    Convert boolean to int e.g) Feel_No_Pain

    <Data From AI>:
     Sending message:{
     "combat_state":{"draw_pile":[{"exhausts":false,"is_playable":true,"cost":1,"name":"Strike","id":"Strike_G","type":"ATTACK","uuid":"b0f7e30e-ad01-4f7b-998d-bea4c8078703","upgrades":0,"rarity":"BASIC","has_target":true},
                                  {"exhausts":false,"is_playable":true,"cost":1,"name":"Strike","id":"Strike_G","type":"ATTACK","uuid":"efa253c0-0c03-4229-8bcf-16e1b2f14257","upgrades":0,"rarity":"BASIC","has_target":true},
                                  {"exhausts":false,"is_playable":true,"cost":1,"name":"Defend","id":"Defend_G","type":"SKILL","uuid":"721e873c-b829-4a31-ad52-6b6a6c9422b2","upgrades":0,"rarity":"BASIC","has_target":false}]

                    "discard_pile":[{"exhausts":false,"is_playable":true,"cost":1,"name":"Strike","id":"Strike_G","type":"ATTACK","uuid":"29397503-e3d0-4e84-813a-a47e7d382c99","upgrades":0,"rarity":"BASIC","has_target":true},
                                   {"exhausts":false,"is_playable":true,"cost":1,"name":"Survivor","id":"Survivor","type":"SKILL","uuid":"7a683fef-6192-4745-95e2-1514759386d3","upgrades":0,"rarity":"BASIC","has_target":false}]
                    "exhaust_pile":[]
                    "hand":[{"exhausts":false,"is_playable":true,"cost":1,"name":"Defend","id":"Defend_G","type":"SKILL","uuid":"3d5fb93d-9340-44cd-aec3-99428a972eb3","upgrades":0,"rarity":"BASIC","has_target":false},
                            {"exhausts":false,"is_playable":true,"cost":0,"name":"Neutralize","id":"Neutralize","type":"ATTACK","uuid":"f3efc536-de1a-466a-85a2-100dcc0e6b95","upgrades":0,"rarity":"BASIC","has_target":true}]

                    "player":{"orbs":[],"current_hp":70,"block":8,"max_hp":70,"powers":[],"energy":1}},

                    "deck":[{"exhausts":false,"is_playable":true,"cost":1,"name":"Strike","id":"Strike_G","type":"ATTACK","uuid":"b0f7e30e-ad01-4f7b-998d-bea4c8078703","upgrades":0,"rarity":"BASIC","has_target":true}]

                    "relics":[{"name":"Ring of the Snake","id":"Ring of the Snake","counter":-1}]

                    "potions":[{"requires_target":false,"can_use":false,"can_discard":false,"name":"Potion Slot","id":"Potion Slot"},
                               {"requires_target":false,"can_use":false,"can_discard":false,"name":"Potion Slot","id":"Potion Slot"},
                               {"requires_target":false,"can_use":false,"can_discard":false,"name":"Potion Slot","id":"Potion Slot"}],]

                    "monsters":[{"is_gone":false,"move_hits":1,"move_base_damage":11,"half_dead":false,"move_adjusted_damage":11,"max_hp":41,"intent":"ATTACK","move_id":1,"name":"Jaw Worm","current_hp":35,"block":0,"id":"JawWorm","powers":[]}]
                    }
         }
       how to call the dictionary
       print(message["combat_state"]["draw_pile"][0]["name"]) # print out " Strike"
       Im not sure the name of dictionary", check the dictionary_name
"""

import random
from maxtree import SimGame
#THIS IS PARTLY PSEUDOCODE
#problems:upgrading a card not implemented

#helper functions
#need add energy/mana function
#deal damage to monster
#added checks for Strength and Vulnerable
#NEED WEAK and other powers
#WEAK AND VULNERABLE APPLIES AFTER STRENGTH
def dealdmg(gamestate, damage, monster, attacknum = 1):
    newstate = gamestate
    for pplayer in newstate.Player.power:
        if pplayer.power_name == 'Strength':
            damage += p.amount
    for pplayer in newstate.Player.power:
        if pplayer.power_name == 'Weak':
            damage = damage * 0.75
    for pmonster in newstate.Monsters[monster].power:
        if pmonster.power_name == 'Vulnerable':
            damage = damage * 1.5
    #need to check block. if block is existed, reduce block. Not the HP
    newstate.Monsters[monster].current_hp -= (damage * attacknum)
    if newstate.Monsters[Monster].current_hp <= 0:
        del newstate.Monsters[Monster]
    return newstate

def addblock(gamestate, block):
    newstate = gamestate
    newstate.player.block = newstate.player.block + block
    # if Juggernaut:
    # dealdmg to random monster
    return newstate

#Will need to figure out what power_id is
def dealvulnerable(gamestate, amount, monster):
    newstate = gamestate
    for pmonster in newstate.Monsters[monster].power:
        if pmonster.power_name == 'Vulnerable':
            pmonster.amount = pmonster.amount + amount
            return newstate
    newvulnerable = Power('Vulnerable', 'Vulnerable', amount)
    newvulnerable.just_applied = True
    newstate.Monsters[monster].power.append(newvulnerable)
    return newstate

def dealweak(gamestate, amount, monster):
    newstate = gamestate
    for pmonster in newstate.Monsters[monster].power:
        if pmonster.power_name == 'Weak':
            pmonster.amount = pmonster.amount + amount
            return newstate
    newweak = Power('Weak', 'Weak', amount)
    newweak.just_applied = True
    newstate.Monsters[monster].power.append(newweak)
    return newstate

    # for p in newstate.Player.Power:
    #     if p.power_name = Strength:
    #         newstate.Monsters[monster].current_hp -= (damage + p.amount) * attacknum
    #         return newstate
    # else:
    #     newstate.Monsters[monster].current_hp -= damage * attacknum
    #     return newstate

def upgrade(card):
    if card.name == 'Searing Blow':
        card.upgrades += 1
    elif card.upgrades == 0:
        card.upgrades = 1
    return card

# def changestrength(gamestate, amount, character):
#     newstate = gamestate
#     character

# Effect at end of turn
def end_of_turn(gamestate, monster):
    newstate = gamestate

    # lose 1 HP and deal 5 damage to ALL enemies.
    # Warning : even if player has block, lose 1 HP.
    if Combust :
        newstate.player.current_hp = newstate.player.current_hp - 1
        for x in len(monster):
                newstate = dealdmg(newstate, 5, newstate.Monsters[monster[x]])

    # At the end of your turn, lose 2 Strength.
    if newstate.Flex :
        # lose 2 Strength.
        newstate.Flex = False

    #  At the end of your turn, gain 3 Block.
    if newstate.Metallicize:
        # need to modify, when metallicize used N times, gain (3 * N) block every turn.
        newstate.player.block = newstate.player.block + 3

    #deal poison damage, reduces poison stack
    for pmonster in newstate.Monsters[monster].power:
        if pmonster.power_name == 'Poison':
           # if moster has block reduce block, instead of current HP
            if hitmonster.block == 0 :
                newstate.Monsters[monster].current_hp -= pmonster.amount
                newvulnerable = Power('Poison', 'Poison', amount - 1)
                newvulnerable.just_applied = True
                newstate.Monsters[monster].power.append(newvulnerable)
            else :
                newstate.Monsters[monster].block -= pmonster.amount
                newvulnerable = Power('Poison', 'Poison', amount - 1)
                newvulnerable.just_applied = True
                newstate.Monsters[monster].power.append(newvulnerable)

    #ethereal check, if card is ethereal, exhaust it
    #ethereal : If you manage to discard the card from your hand, it won't get Exhausted.
    for cardname,card in newstate.hand:
        x = cards[card]
        # if x is ethereal
            # exhaust it
        # else:
            # newstate.hand.remove(cardname)
            # newstate.discard_pile.append(cardname)


    return newstate

def start_of_turn(gamestate):
    newstate = gamestate
    #reset energy/mana
    if newstate.Berserk :
        # need to modify here, if Upgrade Berserk, Gain 2 engergy
        newstate.energy = 3 + 1
    else :
        newstate.energy = 3

    #At the start of your turn, lose 1 HP and draw 1 card.
    if newstate.Brutality:
        newstate.player.current_hp = newstate.player.current_hp - 1
        #Draw 1 Card

    #at the start of your turn, Block no longer expires
    if newstate.Barricade:
        # do not reset the block if Barricade is played
        newstate.player.block = gamestate.player.block
    else:
        # else do reset the block
        newstate.player.block = 0

    # Lose moster blocks

    #Draw Cards

    return newstate

#Need to Helper Function
#Cost,

#example pseudocode
#for cardname, card in Game.hand:
 #   x = cards[card]
 #   check if enough energy to play card
    #might have to add energy to game state
    # if SimGame.energy >= x[0]:
    #    SimGame.energy = Game.energy - x[0]
        #somehow play card/call card function from dict
        #PROBLEM: how are monsters stores in gamestate?'
        #since some cards don't need targets, the card function will loop through the targets if needed?
    #    if x[1] == False:
     #       x[2](gamestate)
     #       gamestate = gamestate.hand.remove(cardname)
     #       gamestate = gamestate.discard_pile.append(cardname)
     #   else:
     #       for target in Game.Monsters:
     #           x[2](gamestate, target)
     #           gamestate = gamestate.hand.remove(cardname)
     #           gamestate = gamestate.discard_pile.append(cardname)

#will need to evaluate the new gamestate the card function returns?

#anger 0 cost Deal 6 damage. Add a copy of this card to your discard pile.
def Anger(gamestate, hitmonster, Upgrade):
    #gamestate class = Game
    #hitmonster class = Monster
    newstate = gamestate
    if Upgrade :
        #deal 8 damge
        newstate = dealdmg(newstate, 8, newstate.Monster[hitmonster])
        newstate.discard_pile.append('anger')
        return newstate
    else :
        #deal 6 damage
        newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster])
        #add a copy of this card to your discard pile
        newstate.discard_pile.append('anger')
        return newstate

#armaments 1 cost Gain 5 Block. Upgrade a card in your hand for the rest of combat.
def Armaments(gamestate, cardtoupgrade, Upgrade,):
    newstate = gamestate
    #add 5 block
    newstate = addblock(newstate, 5)
    if Upgrade:
        #upgrade all card in your hand for the rest of combat
        for card in newstate.hand:
            newstate.hand[card] = upgrade(newstate.hand[card])
        return newstate
    else:

        return newstate
        #somehow return a new gamestate for every card which can be upgraded

    #not sure if this return is correct

#barricade 3 cost Block no longer expires at the start of your turn.
def Barricade(gamestate, Upgrade):
    #NEW Gamestate bool needed for barricade, do not lose block at turn end
    newstate = gamestate
    if Upgrade:
        #cost is 2
        #Block no longer expires at the start of your turn.
        newstate.Barricade = True
        return newstate
    else:
        #cost is 3
        newstate.Barricade = True
        return newstate

#bash 2 cost Deal 8damage. Apply 2 Vulnerable.
def Bash(gamestate, hitmonster, Upgrade):
    newstate = gamestate

    if Upgrade:
        #deal 10 damage
        newstate = dealdmg(newstate, 10, newstate.Monster[hitmonster])
        #apply 3 vulnerable, write function for add vulnerable
        newstate = dealvulnerable(newstate, 3, hitmonster)
        return newstate
    else:
        #deal 8 damage
        newstate = dealdmg(newstate, 8, newstate.Monster[hitmonster])
        #apply 2 vulnerable, write function for add vulnerable
        newstate = dealvulnerable(newstate, 2, hitmonster)
        return newstate

#battle trance 0 cost Draw 3 cards. You cannot draw additional cards this turn.
def Battle_Trance(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        #Draw 4 Cards
    # else:
        #Draw 3 Cards

    #Cannot draw additional Cards this turn
    gamestate.Battle_Trance = True
    return newstate

#berserk 0 cost Gain 2 Vulnerable. Gain 1 Energy at the start of your turn.
def Berserk(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        #Gain 1 Vulnerable
    #else :
        #Gain 2 Vulnerable
    newstate.Berserk = True
    return newstate

#blood for blood 4 cost Cost 1 less energy for each time you lose HP in combat. Deal 18 damage.
def Blood_For_Blood(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if lose HP in combat
    if Upgrade:
        #cost is 3, Cost 1 less energy for each time you lose HP in combat
        newstate.Blood_For_Blood = True
        #Cost 1 less energy for each time
        #Deal 22 damage
        newstate = dealdmg(newstate, 22, newstate.Monster[hitmonster])
    else :
        #cost is 4, Cost 1 less energy for each time you lose HP in combat
        newstate.Blood_For_Blood = True
        #Cost 1 less energy for each time
        #Deal 18 damage
        newstate = dealdmg(newstate, 18, newstate.Monster[hitmonster])

    return newstate

#bloodletting 0 cost Lose 3 HP. Gain 1 Energy.
def Bloodletting(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        # lose 3 HP
        newstate.player.current_hp = newstate.player.current_hp - 3
        # Gain 2 Energy.
        newstate.energy += 2
    else:
        # lose 3 HP
        newstate.player.current_hp = newstate.player.current_hp - 3
        # Gain 1 Energy.
        newstate.energy += 1

    return newstate

#bludgeon 3 cost Deal 32 damage.
def Bludgeon(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        #deal 42 damage
        newstate = dealdmg(newstate, 42, newstate.Monster[hitmonster])
    else:
        #deal 32 damage
        newstate = dealdmg(newstate, 32, newstate.Monster[hitmonster])
    return newstate

#body slam 1 cost	Deal damage equal to your current Block.
def Body_Slam(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #cost is 0,
        #deal damage equal to your current Block.
        newstate = dealdmg(newstate, newstate.player.block, newstate.Monster[hitmonster])
    else:
        #cost is 1,
        #deal damage equal to your current Block.
        newstate = dealdmg(newstate, newstate.player.block, newstate.Monster[hitmonster])

    return newstate

#brutality 0 cost (Innate.) At the start of your turn, lose 1 HP and draw 1 card.
#It is not different between Upgraded or not.
def Brutality(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    newstate.Brutality = True
    return newstate

#burning pact 1 cost Exhaust 1 card. Draw 2 cards.
def Burning_Pact(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #Exhaust 1 card
    #newstate.exhaust_pile.append('chosen_card_name')
    # if Upgrade :
    #     #Draw 3 cards
    # else :
    #     #Draw 2 cards
    return newstate

#carnage 2 cost	Ethereal. Deal 20(28) damage : Ethereal removed at end of combat.
def Carnage (gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        # deal 20 damage
        newstate = dealdmg(newstate, 28, newstate.Monster[hitmonster])
    else:
        # deal 20 damage
        newstate = dealdmg(newstate, 20, newstate.Monster[hitmonster])
    return newstate

#clash 0 cost Can only be played if every card in your hand is an Attack. Deal 14 damage.
def Clash (gamestate, hitmonster, Upgrade):
    #Check = is_all_attack_in_hand , if every card in your hand is an Attack.
    newstate = gamestate
    #if is_an_attack_in_hand:
        #if Upgrade:
        #deal 18 damage
        #    newstate = dealdmg(newstate, 18, newstate.Monster[hitmonster])

        #else :
        #deal 14 damage
        #    newstate = dealdmg(newstate, 18, newstate.Monster[hitmonster])
    return newstate

#cleave 1 cost Deal 8 damage to ALL enemies.
def Cleave (gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #hitmonster is list such as monster = [moster1, moster2, moster3]
    #attack monster1, monster2, and monster3
    if Upgrade :
        for num in len(hitmonster):
            #deal 11 damage to ALL enemies
            newstate = dealdmg(newstate, 11, newstate.Monster[hitmonster[num]])
    else :
        for num in len(hitmonster):
            #deal 8 damgae to ALL enemies
            newstate = dealdmg(newstate, 8, newstate.Monster[hitmonster[num]])

    return newstate

#clothsline 2 cost Deal 12 damage. Apply 2 Weak. weak : Target deals 25% less attack damage.
def Clothesline (gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        #deal 14 damage
        newstate = dealdmg(newstate, 14, newstate.Monsters[hitmonster[x]])
        #apply 3 weak
        newstate = dealweak(newstate, 3, hitmonster)

    else:
        #deal 12 damage
        newstate = dealdmg(newstate, 12, newstate.Monsters[hitmonster[x]])
        #apply 2 weak
        newstate = dealweak(newstate, 2, hitmonster)

    return newstate

#combust 1 cost At the end of your turn, lose 1 HP and deal 5 damage to ALL enemies.
#How to apply At the end of your turn?
def Combust(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    # At the end of your turn
    newstate.Combust = True
    #Upgrade
    #combust 1 cost At the end of your turn, lose 1 HP and deal 7 damage to ALL enemies.
    return newstate

#corruption 3 cost Skills cost 0. Whenever you play a Skill, Exhaust it.
# Need to modify
def Corruption(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade :
        #cost is 2
    #else Upgrade :
        #cost is 3
    # Set the skill cost 0
    newstate.Corruption = True
    # When you play the skill
    # Exhaust it

    return newstate

#dark embrace 2 cost Whenever a card is Exhausted, draw 1 card.
def Dark_Embrace(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade :
        #cost is 1
    #else :
        #cost is 2

    #whenever a card is Exhausted,
    newstate.Dark_Embrace = True
    #Draw 1 Card.

    return newstate

#defend 1 cost Gain 5 Block.
def Defend (gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        #add 8 block
        newstate = addblock(newstate, 8)
    else:
        #add 5 block
        newstate = addblock(newstate, 5)
    return newstate

#demon form 3 cost At the start of each turn, gain 2 Strength.
#How to apply start of each turn?
def Demon_Form(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        #at the start of each turn, gain 3 Strength
    #else:
        #at the start of each turn, gain 2 Strength
    newstate.Demon_Form = True
    return newstate

#disarm 1 cost Enemy loses 2 Strength. Exhaust.
def Disarm(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        #Enemy loses 3 Strength
    else :
        #Enemy loses 2 Strength.
    #Exhaust
    return newstate

#double tap 1 cost This turn, your next Attack is played twice.
def Double_Tap(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade :
        # your next 2 Attack are played twice
    #else:
        # your next Attack is played twice
    newstate.Double_Tap = True
    return newstate

#dropkick 1 cost Deal 5 damage. If the enemy is Vulnerable, gain 1 energy and draw 1 card.
#
def Dropkick(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #deal 8 damage
        newstate =dealdmg(newstate,8,newstate.Monster[hitmonster])
    else:
        #deal 5 damage
        newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster])
    #if the enemy is Vulnerable
        #Gain 1 energy, and draw 1 card
    return newstate

#dual wield 1 cost Create a copy of an Attack or Power card in your hand.
def Dual_Wield(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        #add Create two copy of an Attack or Power Card.
    #else:
        #add Create a copy of an Attack or Power Card.
    return newstate

#entrench 2 cost Double your current Block.
def Entrench(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade :
        #cost is 1
    #else :
        #cost is 2
    newstate.player.block = newstate.player.block * 2
    return newstate

#evolve 1 cost Whenever you draw a Status, draw 1 card.
#Add draw
def Evolve(gamestate, hitmonster, Upgrade):
    #if Upgrade:
        # Draw 2 cards, if you draw a Status
    #else:
        #add Draw card, if you draw a Status
    newstate =  gamestate
    newstate.Evolve = True
    return newstate

#exhume 1 cost Place a card from your Exhaust pile into your hand. Exhaust.
#how to pick the card form exhaust pile
def Exhume(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade
        # cost is 0
    #else
        # cost is 1
    #add Place a card from your Exhaust pile
    newstate.exhaust_pile.append('Exhume')
    return newstate

#feed 1 cost Deal 10 damage. If this kills a non-minion enemy, gain 3 permanent Max HP. Exhaust.
def Feed(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        # deal 12 damage
        newstate = dealdmg(newstate, 12, newstate.Monsters[hitmonster])
        # if monster is dead
        if newstate.is_dead_monster:
            # gain 4 permanent Max HP
            newstate.player.max_hp =newstate.player.max_hp + 4
            newstate.exhaust_pile.append('Feed')

    else :
        # deal 14 damage
        newstate = dealdmg(newstate, 10, newstate.Monsters[hitmonster])
        # if monster is dead
        if newstate.is_dead_monster:
            # gain 3 permanent Max HP
            newstate.player.max_hp =newstate.player.max_hp + 3
            newstate.exhaust_pile.append('Feed')

    return newstate

#feel no pain 1 cost Whenever a card is Exhausted, gain 3 Block.
def Feel_No_Pain(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        #check if a card is Exhausted, whenever after playing Feel No pain
        #gain 4 Block
        newstate.Feel_No_Pain = True
    else:
        #check if a card is Exhausted, whenever after playing Feel No pain
        #gain 3 Block
        newstate.Feel_No_Pain = True
    return newstate

#fiend fire 2 cost Exhaust your hand. Deal 7(10) damage for each Exhausted card. Exhaust.
def Fiend_Fire(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    # if This card is played, turn on(True) the "Exhaust" helper function if not turn off(False)
    newstate.exhaust_pile.append('Fiend Fire')
    return newstate

#fire breathing 1 cost Whenever you draw a Status or Curse card, deal 6(10) damage to all enemies.

def Fire_Breathing(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    newstate.Fire_Breathing = True
    # Whenever you draw a Status or Curse card
    #if draw_State_or_Curse
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster[x]])
    return newstate

#flame barrier 2 cost Gain 12 Block. Whenever you are attacked this turn, deal 4 damage to the attacker.
def Flame_Barrier(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        #Gain 16 Block
        newstate = addblock(newstate, 16)
        newstate.Flame_Barrier = True
        #whenever you are attacked this turn
        newstate.Flame_Barrier = True
            #how to represent attacker?
            #how to represent this turn?
            #newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster], 1)

    else:
        #Gain 12 Block
        newstate = addblock(newstate, 12)
        newstate.Flame_Barrier = True
            #whenever you are attacked this turn
            newstate.Flame_Barrier = True
            #how to represent attacker?
            #how to represent this turn?
            #newstate = dealdmg(newstate, 4, newstate.Monster[hitmonster], 1)

    return newstate

#flex 0 cost 2 Strength. At the end of your turn, lose 2 Strength.
def Flex(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        #gain 2 Strength
        #end_of_turn lose 2 Strength
        newstate.Flex = True
    else:
        #gain 2 Strength
        #end_of_turn lose 2 Strength
        newstate.Flex = True
    return newstate

#ghostly armor 1 cost Ethereal. Gain 10 Block.
#add if you do not use this card, Ethereal.
def Ghostly_Armor(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        #Gain 13 Block
        newstate = addblock(newstate,13)
    else :
        #Gain 10 Block
        newstate = addblock(newstate, 10)
    return newstate

#havoc 1 cost Play the top card of your draw pile and Exhaust it.
def Havoc(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        # cost is 0
    # else:
        # cost is 1
    #Play the top card of your draw pile
    # Exhaust it
    return newstate

#headbutt 1 cost Deal 9 damage. Place a card from your discard pile on top of your draw pile.
def Headbutt(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #deal 12 damage
        newstate = dealdmg(newstate,12, newstate.Monster[hitmonster])
        #add Place a card from your discard pile on top of your draw pile.
    else :
        #deal 9 damage
        newstate = dealdmg(newstate, 9, newstate.Monster[hitmonster])
        #add  Place a card from your discard pile on top of your draw pile.
    return newstate

#heavy blade 2 cost Deal 14 damage. Strength affects Heavy Blade 3 times.
def Heavy_Blade(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        newstate = dealdmg(newstate, 14, newstate.Monster[hitmonster])
        #add  Strength affects Heavy Blade 5 times
    else:
        newstate = dealdmg(newstate, 14, newstate.Monster[hitmonster])
        #add  Strength affects Heavy Blade 3 times

    return newstate

#hemokinesis 1 cost Lose 3 HP. Deal 14 damage.
def Hemokinesis(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        # lose 2 HP
        newstate.current_hp =newstate.current_hp - 2
        # Deal 18 Damage
        newstate = dealdmg(newstate, 18, newstate.Monster[hitmonster])
    else:
        # lose 3 HP
        newstate.current_hp =newstate.current_hp - 3
        # Deal 14 Damage
        newstate = dealdmg(newstate, 14, newstate.Monster[hitmonster])

    return newstate

#immolate 2 cost Deal 21 damage to ALL enemies. Add a Burn to your discard pile.
def Immolate(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        for x in len(hitmonster):
            # Deal 28 Damage
            newstate = dealdmg(newstate, 28, newstate.Monster[hitmonster[x]])
        newstate.discard_pile.append('Burn')
    else:
        for x in len(hitmonster):
            # Deal 21 Damage
            newstate = dealdmg(newstate, 21, newstate.Monster[hitmonster[x]])
        newstate.discard_pile.append('Burn')
    return newstate

#impervious 2 cost Gain 30 Block. Exhaust.
def Impervious(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #gain 40 Block
        newstate = addblock(newstate, 40)
        newstate.exhaust_pile.append('Impervious')
    else:
        #gain 30 Block
        newstate = addblock(newstate, 30)
        newstate.exhaust_pile.append('Impervious')
    return newstate

#infernal blade 1 cost Add a random Attack to your hand. It costs 0 this turn. Exhaust.
def Infernal_Blade(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        # cost is 0
        #add a random Attack to your hand
        #set the Attack costs 0 this turn
        newstate.exhaust_pile.append('Infernal_Blade')
    else :
        # cost is 1
        #add a random Attack to your hand
        #set the Attack costs 0 this turn
        newstate.exhaust_pile.append('Infernal_Blade')
    return newstate

#inflame 1 cost Gain 2 Strength.
def Inflame(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        # Gain 3 Strength
    #else :
        # Gain 2 Strength
    return newstate

#intimidate 0 cost Apply 1 Weak to ALL enemies. Exhaust.
def Intimidate(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #add apply 2 weeak to All enemies.
        for x in len(hitmonster):
            newstate = dealweak(newstate, 2, hitmonster[x])
        newstate.exhaust_pile.append('intimidate')
    else:
        #add apply 1 weeak to All enemies.
        for x in len(hitmonster):
            newstate = dealweak(newstate, 1, hitmonster[x])
        newstate.exhaust_pile.append('intimidate')

    return newstate

#iron wave 1 cost Gain 5 Block. Deal 5 damage.
def Iron_wave(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade :
        #Gain 7 Block
        newstate = addblock(newstate, 7)
        #Deal 7 Damage
        newstate = dealdmg(newstate, 7, newstate.Monster[hitmonster])

    else:
        #Gain 5 Block
        newstate = addblock(newstate, 5)
        #Deal 5 Damage
        newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster])
    return newstate

#juggernaut 2 cost Whenever you gain Block, deal 5 damage to a random enemy.
def Juggernaut(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #Whenever you Gain Block,
    #if Upgrade:
        #deal 7 damage to a random enemy
    #else:
        #deal 5 damage to a random enemy
    newstate.Juggernaut = True
    #deal 5 Damage to a random enemy.
        #x = randomrange(len(hitmonster))
        #newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster[x]])
    return newstate

#limit break 1 cost Double your Strength. Exhaust.
def Limit_Break(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        # Double your Strength
        # Do not Exhaust
    #else:
        #add double your Strength
        #newstate.exhaust_pile.append('Limit Break')
    return newstate

#metallicize 1 cost At the end of your turn, gain 3 Block.
def Metallicize(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        # gain 4 Blocks at the end of your turn
    #else:
        # gain 3 blocks, at the end of your turn
    newstate.Metallicize = True
    return newstate

#offering 0 cost Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.
def Offering(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        newstate.player.current_hp = newstate.player.current_hp - 6
        #add Draw 5 Cards
        #Gain 2 energy
        newstate.energy = newstate.energy + 2
        newstate.exhaust_pile.append('Offering')
    else:
        newstate.player.current_hp = newstate.player.current_hp - 6
        #add Draw 3 Cards
        #Gain 2 energy
        newstate.energy = newstate.energy + 2
        newstate.exhaust_pile.append('Offering')

    return newstate

#perfected strike 2 cost Deal 6 damage. Deals an additional 2 damage for ALL of your cards containing "Strike".
def Perfected_Strike(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        newstate =dealdmg(newstate, 6, newstate.Monster[hitmonster])
        #add Deal an additional 3 damage for All of your cards containing "Strike"
    else:
        newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster])
        #add Deals an additional 2 damage for ALL of your cards containing "Strike".
    return newstate

#pommel strike 1 cost Deal 9 damage. Draw 1 card(s).
def Pommel_Strike(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        # Deal 10 damage
        newstate =dealdmg(newstate, 10, newstate.Monster[hitmonster])
        # Add Draw 2 Cards
    else:
        # Deal 9 damage
        newstate = dealdmg(newstate, 9, newstate.Monster[hitmonster])
        #add draw 1 card

    return newstate

#power through 1 cost Add 2 Wounds to your hand. Gain 15 Block.
def Power_Through(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        newstate = addblock(newstate, 20)
        newstate.hand.append('Wound')
        newstate.hand.append('Wound')
    else:
        newstate = addblock(newstate, 15)
        newstate.hand.append('Wound')
        newstate.hand.append('Wound')

    return newstate

#pummel 1 cost Deal 2 damage 4 times. Exhaust.
def Pummel(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        # Deal 2 damage 5 times
        newstate = dealdmg(newstate, 2, newstate.Monster[hitmonster], 5)
    else:
        # Deal 2 damage 4 times
        newstate = dealdmg(newstate, 2, newstate.Monster[hitmonster], 4)
        newstate.exhaust_pile.append('Pummel')
    return newstate

#rage 0 cost Whenever you play an Attack this turn, gain 3 Block
def Rage(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        # whenever player play an Attack this turn, gain 5 Block
    #else:
        # whenever player play an Attack this turn, gain 3 Block
    newstate.Rage = True
    return newstate

#rampage 1 cost Deal 5 damage. Every time this card is played, increase its damage by 8 for this combat.
def Rampage(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #deal 8 damage
        newstate = dealdmg(newstate, 8, newstate.Monster[hitmonster[x]])
        #Every time this card is played, increase its damage by 8 for this combat.
    else:
        newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster[x]])
        #Every time this card is played, increase its damage by 8 for this combat.
    return newstate

#reaper 2 cost Deal 4 damage to ALL enemies. Heal for unblocked damage dealt. Exhaust.
def Reaper(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #deal 5 damage to All enemies
        for x in len(hitmonster):
            newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster[x]])
        newstate.exhaust_pile.append('Reaper')

    else:
        # Deal 4 damage to All enemies
        for x in len(hitmonster):
            newstate = dealdmg(newstate, 4, newstate.Monster[hitmonster[x]])
        newstate.exhaust_pile.append('Reaper')

    return newstate

#reckless charge 0 cost Deal 7 damage. Shuffle a Dazed into your draw pile
def Reckless_Charge(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        # deal 10 damage
        newstate = dealdmg(gamestate, 10, newstate.Monster[hitmonster])
        newstate.draw_pile.append('Dazed')
    else:
        # deal 7 damage
        newstate = dealdmg(gamestate, 7, newstate.Monster[hitmonster])
        newstate.draw_pile.append('Dazed')

    return newstate

#rupture 1 cost Whenever you lose HP from a card, gain 1 Strength.
def Rupture(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        # cost is 0
    #else:
        # cost is 1
    #whenevr player lose Hp from a cards
    newstate.Rupture = True
    #gain 1 Strength
    return newstate

#searing blow 2 cost Deal 12 damage. Can be upgraded any number of times.
def Searing_Blow(gamestate, hitmonster, Upgrade):
    newstate = gamestate

    #if Upgrade:
        # if upgrade n times, deal n(n+7)/2 + 12 Damage (https://slay-the-spire.fandom.com/wiki/Searing_Blow)
        # newstate = newstate dealdmg(newstate, n(n+7)/2 + 12, newstate.Monster[hitmonster])
    #else:
        #deal 12 Damage
        #newstate =  dealdmg(newstate, 12, newstate.Monster[hitmonster])

    return newstate

#second wind 1 cost Exhaust all non-Attack cards in your hand and gain 5 Block for each.
def Second_Wind(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        #Exhaust all non-Attack Cards in your hand.
        #Gain 7 Block for each
    #else:
        #Exhaust all non-Attack Cards in your hand.
        #Gain 5 Block for each
    return newstate

#seeing red 1 cost Gain 2 energy. Exhaust.
def Seeing_Red(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        # cost is 0
        # Gain 2 energy/cost
        newstate.energy = newstate.energy + 2
        newstate.exhaust_pile.append('Seeing_Red')
    else:
        #Gain 2 energy/cost
        newstate.energy = newstate.energy + 2
        newstate.exhaust_pile.append('Seeing Red')

    return newstate

#sentinel 1 cost Gain 5 Block. If this card is Exhausted, gain 2 energy.
def Sentinel(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        newstate = addblock(newstate, 8)
        #add If this card is exhuasted
            #Gain 3 energy/cost
    #else:
        #Gain 5 Block
        newstate = addblock(newstate, 5)
        #add If this card is Exhausted
            #Gain 2 energy/cost
    return newstate

#sever soul 2 cost Exhaust all non-Attack cards in your hand. Deal 16 damage.
def Sever_Soul(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        #add exhaust all non-Attack Cards in your hand
        #Deal 20 Damage
        newstate = dealdmg(newstate, 20, newstate.Monster[hitmonster])
    #else:
        # add exhaust all non-Attack Cards in your hand
        # Deal 16 damage.
        newstate = dealdmg(newstate, 16, newstate.Monster[hitmonster])
    return newstate

#shock wave 2 cost Apply 3 Weak and Vulnerable to ALL enemies. Exhaust.
def Shockwave(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
    #add apply 5 Weak and Vulnerable to All enemies
        for x in len(hitmonster):
            newstate = dealweak(newstate, 5, hitmonster[x])
            newstate = dealvulnerable(newstate, 5, hitmonster[x])
        newstate.exhaust_pile.append('Shock Wave')

    else:
        #add apply 3 Weak and Vulnerable to All enemies
        for x in len(hitmonster):
            newstate = dealweak(newstate, 3, hitmonster[x])
            newstate = dealvulnerable(newstate, 3, hitmonster[x])
        newstate.exhaust_pile.append('Shock Wave')

    return newstate

#shrug it off 1 cost Gain 8 Block. Draw 1 card.
def Shrug_It_Off(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        #gain 11 block
        newstate = addblock(newstate, 11)
        #add Draw 1 card
    #else:
        #gain 8 Block
        newstate = addblock(newstate, 8)
        #add Draw 1 Card
    return newstate

#spot weakness 1 cost If an enemy intends to attack, gain 3 Strength.
def Spot_Weakness(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    #if Upgrade:
        #if an enemy intends to attack
        #gain 4 Strength
    #else:
        #if an enemy intends to attack
        #gain 3 Strength
    return newstate

#strike 1 cost Deal 6 damage.
def Strike(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        # deal 9 damage
        newstate = dealdmg(newstate, 9, newstate.Monster[hitmonster])
    else:
        # deal 6 damage
        newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster])
    return newstate

#sword boomerang 1 cost Deal 3 damage to a random enemy 3 times.
def Sword_Boomerang(gamestate, hitmonster, Upgrade):
    newstate = gamestate

    if Upgrade:
        # a random enemy.
        x = randomrange(len(hitmonster))
        # deal 3 damage, 4 times
        newstate = dealdmg(newstate, 3, newstate.Monster[hitmonster[x]], 4)

    else:
        # a random enemy.
        x = randomrange(len(hitmonster))
        # deal 3 damage, 3 times
        newstate = dealdmg(newstate, 3, newstate.Monster[hitmonster[x]], 3)

    return newstate

#thunderclap 1 cost Deal 4damage and apply 1 Vulnerable to ALL enemies.
def Thunderclap(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        for x in len(hitmonster):
        #deal 7 demage to All enemies
            newstate = dealdmg(newstate, 7, newstate.Monster[hitmonster[x]])
        #add apply 1 Vulnerable to All enemies
        for x in len(hitmonster):
            newstate = dealvulnerable(newstate, 1, hitmonster[x])

    else:
        for x in len(hitmonster):
        #deal 4 demage to All enemies
            newstate = dealdmg(newstate, 4, newstate.Monster[hitmonster[x]])
        #add apply 1 Vulnerable to All enemies
        for x in len(hitmonster):
            newstate = dealvulnerable(newstate, 1, hitmonster[x])

    return newstate

#true grit 1 cost Gain 7 Block. Exhaust a random card from your hand.
def True_Grit(gamestate, hitmonster, Upgrade):
    newstate = gamestate

    if Upgrade:
        #Gain 9 Block
        newstate = addblock(newstate, 9)
        #add Exhaust a random card from your hand
        #select Random Card from hand
        x = randomrange(len(hand))
        newstate.exhaust_pile.append(hand[x])
    else:
        #Gain 7 Block
        newstate = addblock(newstate, 7)
        #add Exhaust a random card from your hand
        #select Random Card from hand
        x = randomrange(len(hand))
        #Exhaust the it.
        newstate.exhaust_pile.append(hand[x])

    return newstate

#twin strike 1 cost Deal 5 damage twice.
def Twin_Strike(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #Deal 7 damage twice
        newstate = dealdmg(newstate, 7, newstate.Monster[hitmonster], 2)
    else:
        #Deal 5 Damage twice
        newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster], 2)

    return newstate

#uppercut 2 cost Deal 13 damage. Apply 1 Weak. Apply 1 Vulnerable.
def Uppercut(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #deal 13 Damage
        newstate = dealdmg(newstate, 13, newstate.Monster[hitmonster])
        #apply 2 weak, and 2 Vulnerable
        newstate = dealweak(newstate, 2, hitmonster)
        newstate = dealvulnerable(newstate, 2, hitmonster)

    else:
        #deal 13 Damage
        newstate = dealdmg(newstate, 13, newstate.Monster[hitmonster])
        #apply 1 weak, and 1 Vulnerable
        newstate = dealweak(newstate, 1, hitmonster)
        newstate = dealvulnerable(newstate, 1, hitmonster)

    return newstate

#warcry 0 cost Draw 1 card. Place a card from your hand on top of your draw pile. Exhaust.
def Warcry(gamestate, hitmonster, Upgrade):
    newstate = gamestate

    if Upgrade:
        #Draw 2 Card
        #Place a Card from your hand on top of your draw pile.
        newstate.exhaust_pile.append('Warcry')

    else:
        #Draw 1 Card
        #Place a Card from your hand on top of your draw pile.
        newstate.exhaust_pile.append('Warcry')

    return newstate

#whirlwind X cost Deal 5 damage to ALL enemies X times.
def Whirlwind(gamestate, hitmonster, Upgrade):
    newstate = gamestate
    if Upgrade:
        #repaet X times, X is cost, deal 8 damage
        for x in len(hitmonster):
            newstate = dealdmg(newstate, 8, newstate.Monster[hitmonster[x]])
    else:
        #repaet X times, X is cost, deal 5 damage
        for x in len(hitmonster):
            newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster[x]])

    return newstate

#wildstrike 1 cost Deal 12 damage. Shuffle a Wound into your draw pile.
def Wildstrike(gamestate, hitmonster, Upgrade):
    newstate = gamestate

    if Upgrade:
        #deal 17 damage
        newstate = dealdmg(newstate, 17, newstate.Monster[hitmonster])
        #Shuffle a Wound into draw pile
        newstate.draw_pile.append('Wound')
    else:
        #deal 12 damage
        newstate = dealdmg(newstate, 12, newstate.Monster[hitmonster])
        #Shuffle a Wound into draw pile
        newstate.draw_pile.append('Wound')

    return newstate


#dict of cards
#cost, target, function, type
#target true = card can target enemy
#target false = card just gets played
#type = A for Attack,  P for Power, S for Skill

#will need new type for status like the card wound

#WILL NEED MORE FIELD IN ARRAY
#Ethereal, exhaust, etc.
#type of card also important
#need ignore discard field

cards = {
    'Anger' : [0, True, Anger, 'A'],
    'Armaments' : [1, False, Armaments, 'S'], #need upgrade function
    'Barricade' : [3, False, Barricade, 'P'], #Barricade needs to be a game state field, do not lose block at turn end
    'Bash' : [2, True, Bash, 'A'],
    'Battle Trance' : [0, False, Battle_Trance, 'S'], # gamestate, You cannot draw additional cards this turn.
    'Berserk' : [0, False, Berserk, 'P'], #somehow figure out energy
    'Blood For Blood' : [4, True, Blood_For_Blood, 'A'],#gamestate, 1 less energy for each time you lose HP in combat
    'Bloodletting' : [0, False, Bloodletting, 'S'],
    'Bludgeon' : [3, True, Bludgeon, 'A'],
    'Body Slam' : [1, True, Body_Slam, 'A'],
    'Brutality' : [0, True, Brutality, 'P'],
    'Burning Pact' : [1, False, Burning_Pact, 'S'], #need draw function
    'Carnage' : [2, True, Carnage, 'A'],
    'Clash' : [0, True, Clash, 'A'], #Clash does not play if not all cards are attacks, SHOULD IGNORE DISCARD, card itself will handle discard
    'Cleave' : [1, True, Cleave, 'A'],
    'Clothesline' : [2, True, Clothesline,'A'],
    'Combust' :[1, True, Combust, 'P'], # gamestate, At the end of your turn
    'Corruption' : [3, False, Corruption, 'P'], # gamestate, Whenever you play a Skill, Exhaust it
    'Dark Embrace' : [2, False, Dark_Embrace,'P'], #gamestate, Whenever a card is Exhausted, draw 1 card.
    'Defend' : [1, False, Defend, 'S'],
    'Disarm' : [3, True, Disarm, 'S'], #exhaust
    'Double Tap' : [1, False, Double_Tap, 'D'], #gamestate, This turn, your next Attack is played twice.
    'Dropkick' : [1, True, Dropkick, 'A'], #draw if conditions are met
    'Dual Wield' : [1, False, Dual_Wield,'S'],
    'Demon Form' : [3, False, Demon_Form, 'P'], # gamestate, at the start of each turn, gain 2 strength
    'Entrench' :[2, False, Entrench, 'S'],
    'Evolve' : [1, False, Evolve, 'P'], # gamestate, Whenever you draw a Status, draw 1 card.
    'Exhume' : [1, False, Exhume, 'S'], #exhaust
    'Feed' :[1, True, Feed, 'A'], #exhaust
    'Feel No Pain' : [1, False, Feel_No_Pain, 'P'],#gamestate, Whenever a card is Exhausted, gain 3 Block.
    'Fiend Fire' : [2, True, Fiend_Fire, 'A'], #exhaust
    'Fire Breathing' : [1, True, Fire_Breathing, 'P'],#gamestate,  Whenever you draw a Status or Curse card,
    'Flame Barrier' : [2, False, Flame_Barrier, 'S'], #gamestate,  Whenever you are attacked this turn
    'Flex' : [0, False, Flex,'S'], #gamestate, lose 2 strength at end of turn
    'Ghostly Armor' : [1, False, Ghostly_Armor,'S'],
    'Havoc' : [1, False, Havoc, 'S'],
    'Headbutt' : [1, True, Headbutt,'A'], #need new function to return card from discard pile
    'Heavy Blade' : [2, True, Heavy_Blade, 'A'], #Strength affects heavy blade 3 times
    'Hemokinesis' : [1, True, Hemokinesis, 'A'],
    'Immolate' : [2, True, Immolate, 'A'],
    'Impervious' : [2, False, Impervious, 'S'], #exhaust
    'Infernal Blade' : [1, False, Infernal_Blade,'S'],
    'Inflame' : [1, True, Inflame, 'P'],
    'Intimidate' : [0, True, Intimidate,'S'], # exhaust
    'Iron wave' : [1, True, Iron_wave,'A'],
    'Juggernaut' : [2, True, Juggernaut, 'P'], # gamstate, Whenever you gain Block,
    'Limit Break' : [1, False, Limit_Break, 'S'], #exhaust
    'Metallicize' : [1, False, Metallicize,'P'], #gamestate,At the end of your turn, gain 3 Block.
    'Offering' : [0, False, Offering, 'S'], #need add energy/mana function, exhaust
    'Perfected Strike' : [2, True, Perfected_Strike, 'A'],
    'Pommel Strike' : [1, True, Pommel_Strike, 'A'], #draw
    'Power Through' : [1, False, Power_Through, 'S'], #add 2 wounds to hand
    'Pummel' : [1, True, Pummel, 'A'], #exhaust
    'Rage' : [0, False, Rage, 'S'], # gamestate, Whenever you play an Attack this turn, gain 3 Block
    'Rampage' : [1, True, Rampage, 'A'], #need ability to track unique cards of rampage
    'Reaper' : [2, True, Reaper, 'A'], #exhaust
    'Reckless Charge' : [0, True, Reckless_Charge, 'A'], #shuffle daze in draw pile
    'Rupture' : [1, False, Rupture, 'P'], #gamestate, Whenever you lose HP from a card, gain 1 Strength.
    'Searing Blow' : [2, True, Searing_Blow, 'A'], #can be upgraded nay number of times
    'Seeing Red' : [0, False, Seeing_Red, 'S'], #exhaust
    'Sentinel' : [1, False, Sentinel, 'S'], #check gamestate for exhaust skills when used
    'Sever Soul' : [2, False, Sever_Soul, 'A'],
    'Shockwave' : [2, False, Shockwave, 'S'], # exhaust
    'Shrug It Off' : [1, False, Shrug_It_Off, 'S'], #draw
    'Spot Weakness' : [1, False, Spot_Weakness, 'S'], #check enemy intent
    'Strike' : [1, True, Strike, 'A'],
    'Second Wind' : [1, False, Second_Wind, 'S'], # #Exhaust all non-Attack Cards in your hand.
    #Gain 5 Block for each
    'Sword Boomerang' : [1, True, Sword_Boomerang, 'A'], #some way to handle probability
    'Thunderclap' : [1, True,Thunderclap, 'A'],
    'True grit' : [1, False, True_Grit, 'S'], #need some way to randomly handle probability
    'Twin Strike' : [1, True, Twin_Strike, 'A'],
    'Uppercut' : [2, True, Uppercut, 'A'],
    'Warcry' : [0, False, Warcry, 'S'],
    'Whirlwind' : ['Whirlwind', True, Whirlwind, 'A'], #COST IS VARIABLE PAY ATTENTION
    'Wild Strike' : [1, True, Wildstrike,'A'], #shuffle wound to draw pile

}
#call the dictionary
#print(cards['Anger'][0])
#print(cards['Anger'][1])
#newstate = cards['Anger'][2](gamestate,hitmonster)
#print(cards['Anger'][3])

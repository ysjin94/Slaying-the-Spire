from spirecomm.spire.character.py import Character
import random
#THIS IS PARTLY PSEUDOCODE
#problems:upgrading a card not implemented

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
    'Battle Trance' : [0, False, Battle_Trance, 'S'], #Need new gamestate disable drawing
    'Berserk' : [0, False, Berserk, 'P'], #somehow figure out energy
    'Blood For Blood' : [4, True, Blood_For_Blood, 'A'], #need new gamestate
    'Bloodletting' : [0, False, Bloodletting, 'S'],
    'Bludgeon' : [3, True, Bludgeon, 'A'],
    'Body Slam' : [1, True, Body_Slam, 'A'],
    'Brutality' : [0, True, Brutality, 'P'],
    'Burning Pact' : [1, False, Burning_Pact, 'S'], #need draw function
    'Carnage' : [2, True, Carnage, 'A'],
    'Clash' : [0, True, Clash. 'A'], #Clash does not play if not all cards are attacks, SHOULD IGNORE DISCARD, card itself will handle discard
    'Cleave' : [1, True, Cleave, 'A'],
    'Clothesline' : [2, True, Clothsline,'A'],
    'Combust' :[1, True, Combust, 'P'], #Need gamestate
    'Corruption' : [3, False, Corruption, 'P'], #new gamestate
    'Dark Embrace' : [2, False, Dark_Embrace,'P'], #Needs new gamestate field
    'Defend' : [1, False, Defend, 'S'],
    'Disarm' : [3, True, Disarm, 'S'], #exhaust
    'Double Tap' : [1, False, Double_Tap, 'D'], #gamestate
    'Dropkick' : [1, True, Dropkick, 'A'], #draw if conditions are met
    'Dual Wield' : [1, False, Dual_Wield,'S'],
    'Entrench' :[2, False, Entrench, 'S'],
    'Evolve' : [1, False, Evolve, 'P'], #new gamestate
    'Exhume' : [1, False, Exhume, 'S'], #exhaust
    'Feed' :[1, True, Feed, 'A'], #exhaust
    'Feel No Pain' : [1, False, Feel_No_Pain, 'P'], #gamestate
    'Fiend Fire' : [2, True, Fiend_Fire, 'A'], #exhaust
    'Fire Breathing' : [1, True, Fire_Breathing, 'P'], #gamestate
    'Flame Barrier' : [2, False, Flame_Barrier, 'S'], #gamestate
    'Flex' : [0, False, Flex,'S'], #gamestate lose 2 strength at end of turn
    'Ghostly Armor' : [1, False, Ghostly_Armor,'S'],
    'Havoc' : [1, False, Havoc, 'S'],
    'Headbutt' : [1, True, Headbutt,'A'], #need new function to return card from discard pile
    'Heavy Blade' : [2, True, Heavy_Blade, 'A'], #Strength affects heavy blad 3 times
    'Hemokinesis' : [1, True, Hemokinesis, 'A'],
    'Immolate' : [2, True, Immolate, 'A'],
    'Impervious' : [2, False, Impervious, 'S'], #exhaust
    'Infernal Blade' : [1, False, Infernal_Blade,'S'],
    'Inflame' : [1, True, Inflame, 'P'],
    'Intimidate' : [0, True, Intimidate,'S'], # exhaust
    'Iron wave' : [1, True, Iron_wave,'A'],
    'Juggernaut' : [2, True, Juggernaut, 'P'], #gamestate, to work with block
    'Limit Break' : [1, False, Limit_Break, 'S'], #exhaust
    'Metallicize' : [1, False, Metallicize,'P'], #gamestate
    'Offering' : [0, False, Offering, 'S'], #need add energy/mana function, exhaust
    'Perfected Strike' : [2, True, Perfected_Strike, 'A'],
    'Pommel Strike' : [1, True, Pommel_Strike, 'A'], #draw
    'Power Through' : [1, False, Power_Through, 'S'], #add 2 wounds to hand
    'Pummel' : [1, True, Pummel, 'A'], #exhaust
    'Rage' : [0, False, Rage, 'S'], #gamestate
    'Rampage' : [1, True, Rampage, 'A'], #need ability to track unique cards of rampage
    'Reaper' : [2, True, Reaper, 'A'], #exhaust
    'Reckless Charge' : [0, True, Reckless_Charge, 'A'], #shuffle daze in draw pile
    'Rupture' : [1, False, Rupture, 'P'], #gamestate
    'Searing Blow' : [2, True, Searing_Blow, 'A'], #can be upgraded nay number of times
    'Seeing Red' : [0, False, Seeing_Red, 'S'], #exhaust
    'Sentinel' : [1, False, Sentinel, 'S'], #check gamestate for exhaust skills when used
    'Sever Soul' : [2, False, Sever_Soul, 'A'],
    'Shockwave' : [2, False, Shockwave, 'S'], # exhaust
    'Shrug It Off' : [1, False, Shrug_It_Off, 'S'], #draw
    'Spot Weakness' : [1, False, Spot_Weakness, 'S'], #check enemy intent
    'Strike' : [1, True, Strike, 'A'],
    'Sword Boomerang' : [1, True, Sword_Boomerang, 'A'], #some way to handle probability
    'Thunderclap' : [1, True,Thunderclap, 'A'],
    'True grit' : [1, False, True_Grit, 'S'], #need some way to randomly handle probability
    'Twin Strike' : [1, True, Twin_Strike, 'A'],
    'Uppercut' : [2, True, Uppercut, 'A'],
    'Warcry' : [0, False, Warcry, 'S'],
    'Whirlwind' : [3, True, Whirlwind, 'A'], #COST IS VARIABLE PAY ATTENTION
    'Wild Strike' : [1, True, WildStrike,'A'], #shuffle wound to draw pile

}

#helper functions
#need add energy/mana function
#deal damage to monster
#added checks for Strength and Vulnerable
#NEED WEAK and other powers
#WEAK AND VULNERABLE APPLIES AFTER STRENGTH
def dealdmg(gamestate, damage, monster, attacknum = 1):
    newstate = gamestate
    for pplayer in newstate.Player.power:
        if pplayer.power_name = 'Strength':
            damage += p.amount
    for pplayer in newstate.Player.power:
        if pplayer.power_name = 'Weak':
            damage = damage * 0.75
    for pmonster in newstate.Monsters[monster].power:
        if pmonster.power_name = 'Vulnerable':
            damage = damage * 1.5
    newstate.Monsters[monster].current_hp -= (damage * attacknum)
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
        if pmonster.power_name = 'Vulnerable':
            pmonster.amount = pmonster.amount + amount
            return newstate
    newvulnerable = Power('simtemp', 'Vulnerable', amount)
    newstate.Monsters[monster].power.append(newvulnerable)
    return newstate

def dealweak(gamestate, amount, monster):
    newstate = gamestate
    for pmonster in newstate.Monsters[monster].power:
        if pmonster.power_name = 'Weak':
            pmonster.amount = pmonster.amount + amount
            return newstate
    newweak = Power('simtemp', 'Weak', amount)
    newstate.Monsters[monster].power.append(newweak)
    return newstate

    # for p in newstate.Player.Power:
    #     if p.power_name = Strength:
    #         newstate.Monsters[monster].current_hp -= (damage + p.amount) * attacknum
    #         return newstate
    # else:
    #     newstate.Monsters[monster].current_hp -= damage * attacknum
    #     return newstate

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
    if Game.energy >= x[0]:
        Game.energy = Game.energy - x[0]
        #somehow play card/call card function from dict
        #PROBLEM: how are monsters stores in gamestate?'
        #since some cards don't need targets, the card function will loop through the targets if needed?
        if x[1] = False:
            x[2](gamestate)
            gamestate = gamestate.hand.remove(cardname)
            gamestate = gamestate.discard_pile.append(cardname)
        else:
            for target in Game.Monsters:
                x[2](gamestate, target)
                gamestate = gamestate.hand.remove(cardname)
                gamestate = gamestate.discard_pile.append(cardname)

#will need to evaluate the new gamestate the card function returns?

#anger 0 cost Deal 6 damage. Add a copy of this card to your discard pile.
def anger(gamestate, hitmonster):
    #gamestate class = Game
    #hitmonster class = Monster
    newstate = gamestate

    #deal 6 damage
    newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster])

    #add a copy of this card to your discard pile
    newstate.discard_pile.append('anger')
    return newstate

#armaments 1 cost Gain 5 Block. Upgrade a card in your hand for the rest of combat.
def armaments(gamestate):
    newstate = gamestate

    #add 5 block
    newstate = addblock(newstate, 5)

    #upgrade a card in your hand for the rest of combat
    for card in newstate.hand:
        newstate.hand.upgrade(card)

    #somehow return a new gamestate for every card which can be upgraded

    return newstate
    #not sure if this return is correct

#barricade 3 cost Block no longer expires at the start of your turn.
def barricade(gamestate):
    #NEW Gamestate bool needed for barricade, do not lose block at turn end
    newstate = gamestate

    #Block no longer expires at the start of your turn.
    newstate.barricade = true;

    return newstate

#bash 2 cost Deal 8damage. Apply 2 Vulnerable.
def bash(gamestate, hitmonster):
    newstate = gamestate

    #deal 8 damage
    newstate = dealdmg(newstate, 8, newstate.Monster[hitmonster])

    #apply 2 vulnerable, write function for add vulnerable
    newstate = dealvulnerable(newstate, 2, hitmonster)
    return newstate
#battle trance 0 cost Draw 3 cards. You cannot draw additional cards this turn.
def Battle_Trance(gamestate, hitmonster):
    newstate = gamestate
    #Draw 3 Cards
    #Cannot draw additional Cards this turn
    return newstate

#berserk 0 cost Gain 2 Vulnerable. Gain 1 Energy at the start of your turn.
def Berserk(gamestate, hitmonster):
    newstate = gamestate
    #Gain 2 Vulnerable
    newstate = dealvulnerable(newstate, 2, hitmonster)
    #If at start of you turn
        #Gain 2 Energy
    return newstate

#blood for blood 4 cost Cost 1 less energy for each time you lose HP in combat. Deal 18 damage.
def Blood_For_Blood(gamestate, hitmonster):
    newstate = gamestate
    #if lose HP in combat
        #Cost 1 less energy for each time
    #Deal 18 damage
    newstate = dealdmg(newstate, 18, newstate.Monster[hitmonster])

    return newstate

#bloodletting 0 cost Lose 3 HP. Gain 1 Energy.
def Bloodletting(gamestate, hitmonster):
    newstate = gamestate
    # lose 3 HP
    newstate.player.current_hp = newstate.player.current_hp - 3
    # Gain 1 Energy.
    return newstate

#bludgeon 3 cost Deal 32 damage.
def Bludgeon(gamestate, hitmonster):
    newstate = gamestate
    #deal 32 damage
    newstate = dealdmg(newstate, 32, newstate.Monster[hitmonster])
    return newstate

#body slam 1 cost	Deal damage equal to your current Block.
def Body_Slam(gamestate, hitmonster):
    newstate = gamestate
    #deal damage equal to your current Block.
    newstate = dealdmg(newstate, newstate.player.block, newstate.Monster[hitmonster])

    return newstate

#brutality 0 cost (Innate.) At the start of your turn, lose 1 HP and draw 1 card.
def Brutality(gamestate, hitmonster):
    newstate = gamestate
    # At start of turn
        # newstate.player.current_hp = newsate.player.current_hp - 1
        # draw 1 card
    return newstate

#burning pact 1 cost Exhaust 1 card. Draw 2 cards.
def Burning_Pact(gamestate, hitmonster):
    newstate = gamestate
    #Exhaust 1 card
    #newstate.exhuast_pile.append('chosen_card_name')
    #Draw 2 cards
    return newstate

#carnage 2 cost	Ethereal. Deal 20(28) damage : Ethereal removed at end of combat.
def Carnage (gamestate, hitmonster):
    newstate = gamestate
    # deal 20 damage
    newstate = dealdmg(newstate, 20, newstate.Monster[hitmonster])
    return newstate

#clash 0 cost Can only be played if every card in your hand is an Attack. Deal 14 damage.
def Clash (gamestate, hitmonster, is_all_attack_in_hand):
    #Check = is_all_attack_in_hand , if every card in your hand is an Attack.
    newstate = gamestate
    if is_all_attack_in_hand:
        newstate = dealdmg(newstate, 20, newstate.Monster[hitmonster])
        newstate.hand.remove('Clash')
        newstate.discard_pile.append('Clash')
    return newstate
    #Card remains in hand for next round if not played.
    #How to represent?
    #else:
        #newstate.discard_pile.append['Clash']
        #return  newstate

#cleave 1 cost Deal 8 damage to ALL enemies.
def Cleave (gamestate, hitmonster):
    newstate = gamestate
    #hitmonster is list such as monster = [moster1, moster2, moster3]
    #attack monster1, monster2, and monster3
    for num in len(hitmonster):
        newstate = dealdmg(newstate, 8, newstate.Monster[hitmonster[num]])
    return newstate

#clothsline 2 cost Deal 12 damage. Apply 2 Weak. weak : Target deals 25% less attack damage.
def Clothesline (gamestate, hitmonster):

    newstate = gamestate
    #deal 12 damage
    newstate = dealdmg(newstate, 12, newstate.Monsters[hitmonster[x]])
    #apply 2 weak
    newstate = dealweak(newstate, 2, hitmonster)
    return newstate

#combust 1 cost At the end of your turn, lose 1 HP and deal 5 damage to ALL enemies.
#How to apply At the end of your turn?
def Combust(gamestate, hitmonster):
    newstate = gamestate
    # attack monster1, monster2, and monster3
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 5, newstate.Monsters[hitmonster[x]])
     


    return newstate

#corruption 3 cost Skills cost 0. Whenever you play a Skill, Exhaust it.
# Need to modify
def Corruption(gamestate, hitmonster):
    newstate = gamestate
    # Set the skill cost 0
    # When you play the skill
    # Exhaust it

    return newstate

#dark embrace 2 cost Whenever a card is Exhausted, draw 1 card.
def Dark_Embrace(gamestate, hitmonster):
    newstate = gamestate
    #whenever a card is Exhausted,
    #Draw 1 Card.

    return newstate

#defend 1 cost Gain 5 Block.
def Defend (gamestate, hitmonster):
    newstate = gamestate
    #add 5 block
    newstate = addblock(newstate, 5)
    return newstate

#demon form 3 cost At the start of each turn, gain 2 Strength.
#How to apply start of each turn?
def Demon_Form(gamestate, hitmonster):
    newstate = gamestate
        #gain 2 Strength
    #if at the start of each turn,
    #gain 2 Strength
    return newstate

#disarm 1 cost Enemy loses 2 Strength. Exhaust.
def Disarm(gamestate, hitmonster):
    newstate = gamestate
    #add Enemy loses 2 Strength.

    return newstate

#double tap 1 cost This turn, your next Attack is played twice.
def Double_Tap(gamestate, hitmonster):
    newstate = gamestate
    #need to modifiy
    return newstate

#dropkick 1 cost Deal 5 damage. If the enemy is Vulnerable, gain 1 energy and draw 1 card.
#
def Dropkick(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster])
    #if the enemy is Vulnerable
    if is_Vulnerable:
        #Gain 1 energy, and draw 1 card
    return newstate

#dual wield 1 cost Create a copy of an Attack or Power card in your hand.
def Dual_Wield(gamestate, hitmonster):
    newstate = gamestate
    #add Create a copy of an Attack or Power Card.
    return newstate

#entrench 2 cost Double your current Block.
def Entrench(gamestate, hitmonster):
    newstate = gamestate
    #doulbe your current Block
    #need helper function for double it?
    newstate.player.block = newstate.player.block * 2
    return newstate

#evolve 1 cost Whenever you draw a Status, draw 1 card.
#Add draw
def Evolve(gamestate, hitmonster):
    #add Draw card, if you draw a Status
    newstate =  gamestate
    return newstate

#exhume 1 cost Place a card from your Exhaust pile into your hand. Exhaust.
#how to pick the card form exhaust pile
def Exhume(gamestate, hitmonster):
    newstate = gamestate
    #add Place a card from your Exhaust pile
    newstate.exhaust_pile.append('Exhume')
    return newstate

#feed 1 cost Deal 10 damage. If this kills a non-minion enemy, gain 3 permanent Max HP. Exhaust.
def Feed(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 10, newstate.Monsters[hitmonster])
    # if monster is dead
    if newstate.is_dead_monster:
        # gain 3 permanent Max HP
        newstate.player.max_hp =newstate.player.max_hp + 3
        newstate.exhaust_pile.append('Feed')
        return newstate
    else:
        #Remain the card if it is not played
        return newstate

#feel no pain 1 cost Whenever a card is Exhausted, gain 3 Block.
def Feel_No_Pain(gamestate, hitmonster):
    newstate = gamestate
    #check if a card is Exhausted, whenever after playing Feel No pain
    #how to represent?
    newstate = addblock(newstate, 3)
    return newstate

#fiend fire 2 cost Exhaust your hand. Deal 7 damage for each Exhausted card. Exhaust.
def Fiend_Fire(gamestate, hitmonster):
    newstate = gamestate
    # if This card is played, turn on(True) the "Exhaust" helper function if not turn off(False)
    newstate.exhaust_pile.append('Fiend Fire')
    return newstate

#fire breathing 1 cost Whenever you draw a Status or Curse card, deal 6 damage to all enemies.
#need to update
def Fire_Breathing(gamestate, hitmonster):
    newstate = gamestate
    # Whenever you draw a Status or Curse card
    if draw_State_or_Curse
        for x in len(hitmonster):
            newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster[x]])
    return newstate

#flame barrier 2 cost Gain 12 Block. Whenever you are attacked this turn, deal 4 damage to the attacker.
def Flame_Barrier(gamestate, hitmonster):
    newstate = gamestate
    newstate = addblock(newstate, 12)
    #whenever you are attacked this turn
    if is_attacked:
        #how to represent attacker?
        #how to represent this turn?
        #newstate = dealdmg(newstate, 4, newstate.Monster[hitmonster], Temp_State.attacknum)
    return newstate

#flex 0 cost 2 Strength. At the end of your turn, lose 2 Strength.
def Flex(gamestate, hitmonster):
    newstate = gamestate
    #gain 2 Strength
    #end_of_turn lose 2 Strength
    return newstate

#ghostly armor 1 cost Ethereal. Gain 10 Block.
#add if you do not use this card, Ethereal.
def Ghostly_Armor(gamestate, hitmonster):
    newstate = gamestate
    newstate = addblock(newstate, 10)
    return newstate

#havoc 1 cost Play the top card of your draw pile and Exhaust it.
def Havoc(gamestate, hitmonster):
    newstate = gamestate
    #Play the top card of your draw pile
    # Exhaust it
    return newstate

#headbutt 1 cost Deal 9 damage. Place a card from your discard pile on top of your draw pile.
def Headbutt(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 9, newstate.Monster[hitmonster])
    #add  Place a card from your discard pile on top of your draw pile.
    return newstate

#heavy blade 2 cost Deal 14 damage. Strength affects Heavy Blade 3 times.
def Heavy_Blade(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 14, newstate.Monster[hitmonster])
    #add  Strength affects Heavy Blade 3 times
    return newstate

#hemokinesis 1 cost Lose 3 HP. Deal 14 damage.
def Hemokinesis(gamestate, hitmonster):
    newstate = gamestate
    newstate.current_hp =newstate.current_hp - 3
    newstate = dealdmg(newstate, 14, newstate.Monster[hitmonster])
    return newstate

#immolate 2 cost Deal 21 damage to ALL enemies. Add a Burn to your discard pile.
def Immolate(gamestate, hitmonster):
    newstate = gamestate
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 21, newstate.Monsters[hitmonster[x]])
    newstate.discard_pile.append('Burn')
    return newstate

#impervious 2 cost Gain 30 Block. Exhaust.
def Impervious(gamestate, hitmonster):
    newstate = gamestate
    newstate = addblock(newstate, 30)
    newstate.exhaust_pile.append('Impervious')
    return newstate

#infernal blade 1 cost Add a random Attack to your hand. It costs 0 this turn. Exhaust.
def Infernal_Blade(gamestate, hitmonster):
    newstate = gamestate
    #add a random Attack to your hand
    newstate.exhaust_pile.append('Infernal_Blade')
    return newstate

#inflame 1 cost Gain 2 Strength.
def Inflame(gamestate, hitmonster):
    newstate = gamestate
    return newstate

#intimidate 0 cost Apply 1 Weak to ALL enemies. Exhaust.
def Intimidate(gamestate, hitmonster):
    newstate = gamestate
    #add apply 1 weeak to All enemies.
    for x in len(hitmonster):
        newstate = dealweak(newstate, 1, hitmonster[x])
    newstate.exhuast_pile.append('Exhaust')
    return newstate

#iron wave 1 cost Gain 5 Block. Deal 5 damage.
def Iron_wave(gamestate, hitmonster):
    newstate = gamestate
    newstate = addblock(newstate, 5)
    newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster])
    return newstate

#juggernaut 2 cost Whenever you gain Block, deal 5 damage to a random enemy.
def Juggernaut(gamestate, hitmonster):
    newstate = gamestate
    #Whenever you Gain Block,
    #deal 5 Damage to a random enemy.
        #x = randomrange(len(hitmonster))
        #newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster[x]])
    return newstate

#limit break 1 cost Double your Strength. Exhaust.
def Limit_Break(gamestate, hitmonster):
    newstate = gamestate
    #add double your Strength
    newstate.exhaust_pile.append('Limit Break')
    return newstate

#metallicize 1 cost At the end of your turn, gain 3 Block.
def Metallicize(gamestate, hitmonster):
    newstate = gamestate
    #add helper function for at end of your turn
    return newstate

#offering 0 cost Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.
def Offering(gamestate, hitmonster):
    newstate = gamestate
    newstate.player.current_hp = newstate.player.current_hp - 6
    #add Draw 3 Cards
    #add 2 energy
    newstate.exhaust_pile.append('Offering')
    return newstate

#perfected strike 2 cost Deal 6 damage. Deals an additional 2 damage for ALL of your cards containing "Strike".
def Perfected_Strike(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 6, newstate.Monsters[hitmonster])
    #add Deals an additional 2 damage for ALL of your cards containing "Strike".
    return newstate

#pommel strike 1 cost Deal 9 damage. Draw 1 card(s).
def Pommel_Strike(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 9, newstate.Monsters[hitmonster])
    #add draw 1 card
    return newstate

#power through 1 cost Add 2 Wounds to your hand. Gain 15 Block.
def Power_Through(gamestate, hitmonster):
    newstate = gamestate
    newstate = addblock(newstate, 15)
    newstate.hand.append('Wound')
    newstate.hand.append('Wound')
    return newstate

#pummel 1 cost Deal 2 damage 4 times. Exhaust.
def Pummel(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 4, newstate.Monsters[hitmonster], 4)
    newstate.exhaust_pile.append('Pummel')
    return newstate

#rage 0 cost Whenever you play an Attack this turn, gain 3 Block
def Rage(gamestate, hitmonster):
    newstate = gamestate
    # whenever player play an Attack this turn
    newstate = addblock(newstate, 3)
    return newstate

#rampage 1 cost Deal 8 damage. Every time this card is played, increase its damage by 8 for this combat.
def Rampage(gamestate, hitmonster):
    newstate = gamestate
        newstate = dealdmg(newstate, 8, newstate.Monsters[hitmonster[x]])
    #Every time this card is played, increase its damage by 8 for this combat.
    return newstate

#reaper 2 cost Deal 4 damage to ALL enemies. Heal for unblocked damage dealt. Exhaust.
def Reaper(gamestate, hitmonster):
    newstate = gamestate
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 4, newstate.Monsters[hitmonster[x]])
    newstate.exhuast_pile.append('Reaper')
    return newstate

#reckless charge 0 cost Deal 7 damage. Shuffle a Dazed into your draw pile
def Reckless_Charge(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(gamestate, 7, newstate.Monsters[hitmonster])
    newstate.draw_pile.append('Dazed')
    return newstate

#rupture 1 cost Whenever you lose HP from a card, gain 1 Strength.
def Rupture(gamestate, hitmonster):
    newstate = gamestate
    #whenevr player lose Hp from a cards
    #gain 1 Strength
    return newstate

#searing blow 2 cost Deal 12 damage. Can be upgraded any number of times.
def Searing_Blow(gamestate, hitmonster):
    newstate = gamestate
    #deal 12 Damage
    newstate = newstate = dealdmg(newstate, 12, newstate.Monsters[hitmonster])

    return newstate

#second wind 1 cost Exhaust all non-Attack cards in your hand and gain 5 Block for each.
def Second_Wind(gamestate, hitmonster):
    newstate = gamestate
    #Exhaust all non-Attack Cards in your hand.
    #Gain 5 Block for each
    return newstate

#seeing red 1 cost Gain 2 energy. Exhaust.
def Seeing_Red(gamestate, hitmonster):
    newstate = gamestate
    #Gain 2 energy/cost
    newstate.exhaust_pile.append('Seeing Red')
    return newstate

#sentinel 1 cost Gain 5 Block. If this card is Exhausted, gain 2 energy.
def Sentinel(gamestate, hitmonster):
    newstate = gamestate
    #Gain 5 Block
    newstate = addblock(newstate, 5)
    #add If this card is Exhausted
    #Gain 2 emergy/cost
    return newstate

#sever soul 2 cost Exhaust all non-Attack cards in your hand. Deal 16 damage.
def Sever_Soul(gamestate, hitmonster):
    newstate = gamestate
    #add exhuast all non-Attack Cards in your hand
    # Deal 16 damage.
    newstate = dealdmg(newstate, 16, newstate.Monsters[hitmonster])
    return newstate

#shock wave 2 cost Apply 3 Weak and Vulnerable to ALL enemies.Exhaust.
def Shockwave(gamestate, hitmonster):
    newstate = gamestate
    #add apply 3 Weak and Vulnerable to All enemies
    for x in len(hitmonster):
        newstate = dealweak(newstate, 3, hitmonster[x])
        newstate = dealvulnerable(newstate, 3, hitmonster[x])
    newstate.exhaust_pile.append('Shock Wave')
    return newstate

#shrug it off 1 cost Gain 8 Block. Draw 1 card.
def Shrug_It_Off(gamestate, hitmonster):
    newstate = gamestate
    #gain 8 Block
    newstate = addblock(newstate, 8)
    #add Draw 1 Card
    return newstate

#spot weakness 1 cost If an enemy intends to attack, gain 3 Strength.
def Spot_Weakness(gamestate, hitmonster):
    newstate = gamestate
    #if an enemy intends to attack
    #gain 3 Strength
    return newstate

#strike 1 cost Deal 6 damage.
def Strike(gamestate, hitmonster):
    newstate = gamestate
    # deal 6 damage
    newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster])
    return newstate

#sword boomerang 1 cost Deal 3 damage to a random enemy 3 times.
def Sword_Boomerang(gamestate, hitmonster):
    newstate = gamestate
    # a random enemy.
    x = randomrange(len(hitmonster))
    # deal 3 damage, 3 times
    newstate = dealdmg(newstate, 3, newstate.Monsters[hitmonster[x]], 3)
    return newstate

#thunderclap 1 cost Deal 4damage and apply 1 Vulnerable to ALL enemies.
def Thunderclap(gamestate, hitmonster):
    newstate = gamestate
    for x in len(hitmonster):
        #deal 4 demage to All enemies
        newstate = dealdmg(newstate, 4, newstate.Monsters[hitmonster[x]])
        #add apply 1 Vulnerable to All enemies
        for x in len(hitmonster):
            newstate = dealvulnerable(newstate, 1, hitmonster[x])

    return newstate

#true grit 1 cost Gain 7 Block. Exhaust a random card from your hand.
def True_Grit(gamestate, hitmonster):
    newstate = gamestate
    #Gain 7 Block
    newstate = addblock(newstate, 7)
    #add Exhuast a random card from your hand

    #select Random Card from hand
    x = randomrange(len(hand))

    #Exhuast the it.
    newstate.exhuast_pile.append(hand[x])
    return newstate

#twin strike 1 cost Deal 5 damage twice.
def Twin_Strike(gamestate, hitmonster):
    newstate = gamestate
    #Deal 5 Damage twice
    newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster], 2 )
    return newstate

#uppercut 2 cost Deal 13 damage. Apply 1 Weak. Apply 1 Vulnerable.
def Uppercut(gamestate, hitmonster):
    newstate = gamestate
    #deal 13 Damage
    newstate = dealdmg(newstate, 13, newstate.Monster[hitmonster])
    #apply 1 weak, and 1 Vulnerable
    newstate = dealweak(newstate, 1, hitmonster)
    newstate = dealvulnerable(newstate, 1, hitmonster)
    return newstate

#warcry 0 cost Draw 1 card. Place a card from your hand on top of your draw pile. Exhaust.
def Warcry(gamestate, hitmonster):
    newstate = gamestate
    #Draw 1 Card
    #Place a Card from your hand on top of your draw pile.
    newstate.exhaust_pile.append('Warcry')
    return newstate

#whirlwind X cost Deal 5 damage to ALL enemies X times.
def Whirlwind(gamestate, hitmonster):
    newstate = gamestate
    #repaet X times, X is cost
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 5, newstate.Monsters[hitmonster[x]])
    return newstate

#wildstrike 1 cost Deal 12 damage. Shuffle a Wound into your draw pile.
def Wildstrike(gamestate, hitmonster):
    newstate = gamestate
    #deal 12 damage
    newstate = dealdmg(newstate, 12, newstate.Monster[hitmonster])
    #Shuffle a Wound into draw pile
    newstate.draw_pile.append('Wound')
    return newstate

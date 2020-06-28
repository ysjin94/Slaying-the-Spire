from spirecomm.spire.character.py import Character
import random
#THIS IS PARTLY PSEUDOCODE
#problems:upgrading a card not implemented

#dict of cards
#cost, target, function
#target true = card can target enemy
#target false = card just gets played

#WILL NEED MORE FIELD IN ARRAY
#Ethereal, exhaust, etc. 
cards = {
    'Anger' : [0, True, Anger],
    'Armaments' : [1, False, Armaments],
    'Barricade' : [3, False, Barricade], #Barricade needs to be a game state field, do not lose block at turn end
    'Bash' : [2, True, Bash],
    'Battle Trance' : [0, False, Battle_Trance],
    'Berserk' : [0, False, Berserk],
    'Blood For Blood' : [4, True, Blood_For_Blood],
    'Bloodletting' : [0, False, Bloodletting],
    'Bludgeon' : [3, True, Bludgeon],
    'Body Slam' : [1, True, Body_Slam],
    'Brutality' : [0, True, Brutality],
    'Burning Pact' : [1, false, Burning_Pact],
    'Carnage' : [2, True, Carnage],
    'Clash' : [0, True, Clash ],
    'Cleave' : [1, True, Cleave],
    'Clothsline' : [2, True, Clothsline],
    'Combust' :[1, True, Combust],
    'Corruption' : [3, False, Corruption],
    'Dark Embrace' : [2, False, Dark_Embrace],
    'Defend' : [1, False, Defend],
    'Disarm' : [3, True, Disarm],
    'Double Tap' : [1, False, Double_Tap],
    'Dropkick' : [1, True, Dropkick],
    'Dual Wield' : [1, False, Dual_Wield],
    'Entrench' :[2, False, Entrench],
    'Evolve' : [1, False, Evolve],
    'Exhume' : [1, False, Exhume],
    'Feed' :[1, True, Feed],
    'Feel No Pain' : [1, False, Feel_No_Pain],
    'Fiend Fire' : [2, True, Fiend_Fire],
    'Fire Breathing' : [1, True, Fire_Breathing],
    'Flame Barrier' : [2, False, Flame_Barrier],
    'Flex' : [0, False, Flex],
    'Ghostly Armor' : [1, False, Ghostly_Armor],
    'Havoc' : [1, False, Havoc],
    'Headbutt' : [1, True, Headbutt],
    'Heavy Blade' : [2, True, Heavy_Blade],
    'Hemokinesis' : [1, True, Hemokinesis],
    'Immolate' : [2, True, Immolate],
    'Impervious' : [2, False, Impervious],
    'Infernal Blade' : [1, False, Infernal_Blade],
    'Inflame' : [1, True, Inflame],
    'Intimidate' : [0, True, Intimidate],
    'Iron wave' : [1, True, Iron_wave],
    'Juggernaut' : [2, True, Juggernaut],
    'Limit Break' : [1, False, Limit_Break],
    'Metallicize' : [1, False, Metallicize],
    'Offering' : [0, False, Offering],
    'Perfected Strike' : [2, True, Perfected_Strike],
    'Pommel Strike' : [1, True, Pommel_Strike],
    'Power Through' : [1, False, Power_Through],
    'Pummel' : [1, True, Pummel],
    'Rage' : [0, False, Rage],
    'Rampage' : [1, True, Rampage],
    'Reaper' : [2, True, Reaper],
    'Reckless Charge' : [0, True, Reckless_Charge],
    'Rupture' : [1, False, Rupture],
    'Searching Blow' : [2, True, Searching_Blow],
    'Seeing Red' : [0, False, Seeing_Red],
    'Sentinel' : [1, False, Sentinel],
    'Sever Soul' : [2, False, Sever_Soul],
    'Shock Wave' : [2, False, Shock_Wave],
    'Shrug It Off' : [1, False, Shrug_It_Off],
    'Spot Weakness' : [1, False, Spot_Weakness],
    'Strike' : [1, True, Strike],
    'Sword Boomerang' : [1, True, Sword_Boomerang],
    'Thunderclap' : [1, True,Thunderclap],
    'True grit' : [1, False, True_Grit],
    'Twin Strike' : [1, True, Twin_Strike],
    'Uppercut' : [2, True, Uppercut],
    'Warcry' : [0, False, Warcry],
    'Whirlwind' : [3, True, Whirlwind], # X cost Deal 5 damage to ALL enemies X times. initial is 3
    'WildStrike' : [1, True, WildStrike], #72

}

#helper functions
#deal damage to monster
#added checks for Strength and Vulnerable
def dealdmg(gamestate, damage, monster, attacknum = 1):
    newstate = gamestate
    newstate.Monsters[monster].current_hp -= (damage * attacknum)
    for p in newstate.Player.power:
        if p.power_name = 'Strength':
            newstate.Monsters[monster].current_hp -= (p.amount * attacknum)
    for p2 in newstate.Monsters[monster].power:
        if p2.power_name = 'Vulnerable':
            newstate.Monsters[monster].current_hp -= (p2.amount * attacknum)
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
        game.energy = game.energy - x[0]
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
    newstate.player.block = newstate.player.block + 5

    #upgrade a card in your hand for the rest of combat
    for card in newstate.hand:
        newstate.hand.upgrade(card)

    #somehow return a new gamestate for every card which can be upgraded

    newstate.discard_pile.append('armaments')
    return newstate
    #not sure if this return is correct

#barricade 3 cost Block no longer expires at the start of your turn.
def barricade(gamestate):
    #NEW Gamestate bool needed for barricade, do not lose block at turn end
    newstate = gamestate

    #Block no longer expires at the start of your turn.
    newstate.barricade = true;

    newstate.discard_pile.append('barricade')
    return newstate

#bash 2 cost Deal 8damage. Apply 2 Vulnerable.
def bash(gamestate, hitmonster):
    newstate = gamestate

    #deal 8 damage
    newstate = dealdmg(newstate, 8, newstate.Monster[hitmonster])

    #apply 2 vulnerable, write function for add vulnerable
    newstate.discard_pile.append('bash')
    return newstate

#carnage 2 cost	Ethereal. Deal 20(28) damage : Ethereal removed until end of combat.
def Carnage (gamestate, hitmonster):
    newstate = gamestate
    # deal 20 damage
    newstate = dealdmg(newstate, 20, newstate.Monster[hitmonster])
    #do not newstate.discard_pile.append('Carnage'), it is Ethereal.
    return newstate

#clash 0 cost Can only be played if every card in your hand is an Attack. Deal 14 damage.
def Clash (gamestate, hitmonster, is_all_attack_in_hand):
    #Check = is_all_attack_in_hand , if every card in your hand is an Attack.
    newstate = gamestate
    if is_all_attack_in_hand:
        newstate = dealdmg(newstate, 20, newstate.Monster[hitmonster])
        newstate.discard_pile.append['Clash']
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
    newstate.discard_pile.append('Cleave')
    return newstate

#clothsline 2 cost Deal 12 damage. Apply 2 Weak. weak : Target deals 25% less attack damage.
def Clothsline (gamestate, hitmonster):

    newstate = gamestate
    newstate = dealdmg(newstate, 12, newstate.Monsters[hitmonster[x]])
    #apply 2 weak
    newstate = newstate.discard_pile.append['Clothsline']
    return newstate

#combust 1 cost At the end of your turn, lose 1 HP and deal 5 damage to ALL enemies.
#How to apply At the end of your turn?
def Combust(gamestate, hitmonster):
    newstate = gamestate
    # attack monster1, monster2, and monster3
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 5, newstate.Monsters[hitmonster[x]])

    newstate.discard_pile.append('Combust')

    return newstate

#corruption 3 cost Skills cost 0. Whenever you play a Skill, Exhaust it.
# Need to modify
def Corruption(gamestate, hitmonster):
    newstate = gamestate
    # Set the skill cost 0
    # When you play the skill
    # Exhaust it
    newstate.discard_pile.append('Corruption')
    return newstate

#dark embrace 2 cost Whenever a card is Exhausted, draw 1 card.

def Dark_Embrace(gamestate, hitmonster):
    newstate = gamestate
    #whenever a card is Exhausted,
    #Deaw 1 Card.
    newstate.discard_pile.append('Dark Embrace')
    return newstate

#defend 1 cost Gain 5 Block.
def Defend (gamestate, hitmonster):
    newstate = gamestate
    #add 5 block
    newstate.player.block = newstate.player.block + 5
    newstate.discard_pile.append('Defend')
    return newstate

#demon form 3 cost At the start of each turn, gain 2 Strength.
#How to apply start of each turn?
def Demon Form(gamestate, hitmonster):
    newstate = gamestate
        #gain 2 Strength
    #if at the start of each turn,
    #gain 2 Strength
    newstate.discard_pile.append('Demon Form')
    return newstate

#disarm 1 cost Enemy loses 2 Strength. Exhaust.
def Disarm(gamestate, hitmonster):
    newstate = gamestate
    #add Enemy loses 2 Strength.
    newstate.exhaust_pile.append('Disarm')
    return newstate

#double tap 1 cost This turn, your next Attack is played twice.
def Double_Tap(gamestate, hitmonster):
    newstate = gamestate
    #need to modifiy
    newstate.discard_pile.append('Double Tap')
    return newstate

#dropkick 1 cost Deal 5 damage. If the enemy is Vulnerable, gain 1 energy and draw 1 card.
#
def Dropkick(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster])
    #if the enemy is Vulneralble
    if is_Vulnerable:
        #Gain 1 energy, and draw 1 card
    newstate.discard_pile.append('Dropkick')
    return newstate

#dual wield 1 cost Create a copy of an Attack or Power card in your hand.
def Dual_Wield(gamestate, hitmonster):
    newstate = gamestate
    #add Create a copy of an Attack or Power Card.
    newstate.discard_pile.append('Dual Wield')
    return newstate

#entrench 2 cost Double your current Block.
def Entrench(gamestate, hitmonster):
    newstate = gamestate
    #doulbe your current Block
    newstate.player.block = newstate.player.block * 2
    newstate.discard_pile.append('Entrench')
    return newstate

#evolve 1 cost Whenever you draw a Status, draw 1 card.
#Add draw
def Evolve(gamestate, hitmonster):
    #add Draw card, if you draw a Status
    newstate =  gamestate
    newstate.discard_pile.append('Evolve')
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
    newstate.player.block = newstate.player.block+3
    newstate.discard_pile.append('Fell No Pain')
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
    newstate.discard_pile.append('Fire Breathing')
    return newstate

#flame barrier 2 cost Gain 12 Block. Whenever you are attacked this turn, deal 4 damage to the attacker.
def Flame_Barrier(gamestate, hitmonster):
    newstate = gamestate
    newstate.player.block =  newstate.player.block + 12
    #whenever you are attacked this turn
    if is_attacked:
        #how to represent attacker?
        #how to represent this turn?
        #newstate = dealdmg(newstate, 4, newstate.Monster[hitmonster], Temp_State.attacknum)
    newstate.discard_pile.append('Flame_Barrier')
    return newstate

#flex 0 cost 2 Strength. At the end of your turn, lose 2 Strength.
def Flex(gamestate, hitmonster):
    newstate = gamestate
    #gain 2 Strength
    #end_of_turn lose 2 Strength
    newstate.discard_pile.append('Flex')
    return newstate

#ghostly armor 1 cost Ethereal. Gain 10 Block.
#add if you do not use this card, Ethereal.
def Ghostly_Armor(gamestate, hitmonster):
    newstate = gamestate
    newstate.player.block =newstate.player.block + 10
    newstate.discard_pile.append('Ghostly Armor')
    return newstate

#havoc 1 cost Play the top card of your draw pile and Exhaust it.
def Havoc(gamestate, hitmonster):
    newstate = gamestate
    #Play the top card of your draw pile
    # Exhaust it
    newstate.discard_pile.append('Havoc')
    return newstate

#headbutt 1 cost Deal 9 damage. Place a card from your discard pile on top of your draw pile.
def Headbutt(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 9, newstate.Monster[hitmonster])
    #add  Place a card from your discard pile on top of your draw pile.
    newstate.discard_pile.append('Headbutt')
    return newstate

#heavy blade 2 cost Deal 14 damage. Strength affects Heavy Blade 3 times.
def Heavy_Blade(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 14, newstate.Monster[hitmonster])
    #add  Strength affects Heavy Blade 3 times
    newstate.discard_pile.append('Heavy Blade')
    return newstate

#hemokinesis 1 cost Lose 3 HP. Deal 14 damage.
def Hemokinesis(gamestate, hitmonster):
    newstate = gamestate
    newstate.current_hp =newstate.current_hp - 3
    newstate = dealdmg(newstate, 14, newstate.Monster[hitmonster])
    newstate.discard_pile.append('Hemokinesis')
    return newstate

#immolate 2 cost Deal 21 damage to ALL enemies. Add a Burn to your discard pile.
def Immolate(gamestate, hitmonster):
    newstate = gamestate
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 21, newstate.Monsters[hitmonster[x]])
    newstate.discard_pile.append('Burn')
    newstate.discard_pile.append('Immolate')
    return newstate

#impervious 2 cost Gain 30 Block. Exhaust.
def Impervious(gamestate, hitmonster):
    newstate = gamestate
    newstate.player.block =newstate.player.block + 10
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
    newstate.exhuast_pile.append('Exhaust')
    return newstate

#iron wave 1 cost Gain 5 Block. Deal 5 damage.
def Iron_wave(gamestate, hitmonster):
    newstate = gamestate
    newstate.player.block = newstate.player.block +5
    dealdmg(newstate, 5, newstate.Monster[hitmonster])
    newstate.discard_pile.append('Iron Wave')
    return newstate

#juggernaut 2 cost Whenever you gain Block, deal 5 damage to a random enemy.
def Juggernaut(gamestate, hitmonster):
    newstate = gamestate
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
    newstate.discard_pile.append('Perfected Strike')
    return newstate

#pommel strike 1 cost Deal 9 damage. Draw 1 card(s).
def Pommel_Strike(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 9, newstate.Monsters[hitmonster])
    #add draw 1 card
    newstate.discard_pile.append('Pommel Strike')
    return newstate

#power through 1 cost Add 2 Wounds to your hand. Gain 15 Block.
def Power_Through(gamestate, hitmonster):
    newstate = gamestate
    newstate.player.block = newstate.player.block + 15
    newstate.discard_pile.append('Power Through')
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
    newstate.player.block = newstate.player.block + 3
    return newstate

#rampage 1 cost Deal 8 damage. Every time this card is played, increase its damage by 8 for this combat.
def Rampage(gamestate, hitmonster):
    newstate = gamestate
        newstate = dealdmg(newstate, 8, newstate.Monsters[hitmonster[x]])
    #Every time this card is played, increase its damage by 8 for this combat.
    newstate.discard_pile.append('Rampage')
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
    newstate.discard_pile.append('Reckless Charge')
    return newstate

#rupture 1 cost Whenever you lose HP from a card, gain 1 Strength.
def Rupture(gamestate, hitmonster):
    newstate = gamestate
    #whenevr player lose Hp from a cards
    #gain 1 Strength
    newstate.discard_pile.append('Rupture')
    return newstate

#searing blow 2 cost Deal 12 damage. Can be upgraded any number of times.
def Searing_Blow(gamestate, hitmonster):
    newstate = gamestate
    #deal 12 Damage
    newstate = newstate = dealdmg(newstate, 12, newstate.Monsters[hitmonster])

    newstate.discard_pile.append('Searching Blow')
    return newstate

#second wind 1 cost Exhaust all non-Attack cards in your hand and gain 5 Block for each.
def Second_Wind(gamestate, hitmonster):
    newstate = gamestate
    #Exhaust all non-Attack Cards in your hand.
    #Gain 5 Block for each
    newstate.discard_pile.append('Second Wind')
    return newstate

#seeing red 1 cost Gain 2 energy. Exhaust.
def Seeing_Red(gamestate, hitmonster):
    newstate = gamestate
    #Gain 2 energy
    newstate.exhaust_pile.append('Seeing Red')
    return newstate

#sentinel 1 cost Gain 5 Block. If this card is Exhausted, gain 2 energy.
def Sentinel(gamestate, hitmonster):
    newstate = gamestate
    newstate.player.block = newstate.player.block + 5
    #add If this card is Exhausted
    #Gain 2 emergy/cost
    return newstate

#sever soul 2 cost Exhaust all non-Attack cards in your hand. Deal 16 damage.
def Sever_Soul(gamestate, hitmonster):
    newstate = gamestate
    #add exhuast all non-Attack Cards in your hand
    newstate = dealdmg(newstate, 16, newstate.Monsters[hitmonster])
    newstate.discard_pile.append('Sever Soul')
    return newstate

#shock wave 2 cost Apply 3 Weak and Vulnerable to ALL enemies.Exhaust.
def Shock_Wave(gamestate, hitmonster):
    newstate = gamestate
    #add apply 3 Weak and Vulneralble to All enemies
    newstate.exhaust_pile.append('Shock Wave')
    return newstate

#shrug it off 1 cost Gain 8 Block. Draw 1 card.
def Shrug_It_Off(gamestate, hitmonster):
    newstate = gamestate
    newstate.player.block = newstate.player.block + 8
    #add Draw 1 Card
    newstate.discard_pile.append('Strug It Off')
    return newstate

#spot weakness 1 cost If an enemy intends to attack, gain 3 Strength.
def Spot_Weakness(gamestate, hitmonster):
    newstate = gamestate
    #if an enemy intends to attack
    #gain 3 Strength
    newstate.discard_pile.append('Spot Weakness')
    return newstate

#strike 1 cost Deal 6 damage.
def Strike(gamestate, hitmonster):
    newstate = gamestate
    # deal 6 damage
    newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster])
    newstate.discard_pile('Strike')
    return newstate

#sword boomerang 1 cost Deal 3 damage to a random enemy 3 times.
def Sword_Boomerang(gamestate, hitmonster):
    newstate = gamestate
    # a random enemy.
    x = randomrange(len(hitmonster))
    # deal 3 damage
    newstate = dealdmg(newstate, 3, newstate.Monsters[hitmonster[x]], 3)
    newstate.discard_pile.append('Sword Boomerang')
    return newstate

#thunderclap 1 cost Deal 4damage and apply 1 Vulnerable to ALL enemies.
def Thunderclap(gamestate, hitmonster):
    newstate = gamestate
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 4, newstate.Monsters[hitmonster[x]])
        #add apply 1 Vulnerable to All enemies
    newstate.discard_pile.append('Thunderclap')
    return newstate

#true grit 1 cost Gain 7 Block. Exhaust a random card from your hand.
def True_Grit(gamestate, hitmonster):
    newstate = gamestate
    newstate.player.block = newstate.player.block + 7
    #add Exhuast a random card from your hand
    x = randomrange(len(hand))
    newstate.discard_pile.append('True Grit')
    return newstate

#twin strike 1 cost Deal 5 damage twice.
def Twin_Strike(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster], 2 )
    newstate.discard_pile.append('Twin Strike')
    return newstate

#uppercut 2 cost Deal 13 damage. Apply 1 Weak. Apply 1 Vulnerable.
def Uppercut(gamestate, hitmonster):
    newstate = gamestate
    newstate = dealdmg(newstate, 13, newstate.Monster[hitmonster])
    #apply 1 weak, and 1 Vulnerable
    newstate.discard_pile.append('Uppercut')
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
    newstate.discard_pile('Whirlwind')
    return newstate

#wildstrike 1 cost Deal 12 damage. Shuffle a Wound into your draw pile.
def Wildstrike(gamestate, hitmonster):
    newstate = gamestate
    #deal 12 damage
    newstate = dealdmg(newstate, 12, newstate.Monster[hitmonster])
    newstate.discard_pile.append('Wildstrike')
    newstate.draw_pile.append('Wound')
    return newstate

from spirecomm.spire.character.py import Character

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
    'Feel No Pain' : [27, False, Feel_No_Pain],
    'Fiend Fire' : [28, True, Fiend_Fire],
    'Fire Breathing' : [29, True, Fire_Breathing],
    'Flame Barrier' : [30, False, Flame_Barrier],
    'Flex' : [31, False, Flex],
    'Ghostly Armor' : [32, False, Ghostly_Armor],
    'Havoc' : [33, False, Havoc],
    'Headbutt' : [34, True, Headbutt],
    'Heavy Blade' : [35, True. Heavy_Blade],
    'Hemokinesis' : [36, True, Hemokinesis],
    'Immolate' : [37, True, Immolate],
    'Impervious' : [38, False, Impervious],
    'Infernal Blade' : [39, False, Infernal_Blade],
    'Inflame' : [40, True, Inflame],
    'Intimidate' : [41, True, Intimidate],
    'Iron wave' : [42, True, Iron_wave],
    'Juggernaut' : [43, True, Juggernaut],
    'Limit Break' : [44, False, Limit_Break],
    'Metallicize' : [45, False, Metallicize],
    'Offering' : [46, False, Offering],
    'Perfected Strike' : [47, True, Perfected_Strike],
    'Pommel Strike' : [48, True, Pommel_Strike],
    'Power Through' : [49, False, Power_Through],
    'Pummel' : [50, True, Pummel],
    'Rage' : [51, False, Rage],
    'Rampage' : [52, True, Rampage],
    'Reaper' : [53, True, Reaper],
    'Reckless Charge' : [54, True, Reckless_Charge],
    'Rupture' : [55, False, Rupture],
    'Searching Blow' : [56, True, Searching_Blow],
    'Seeing Red' : [57, False, Seeing_Red],
    'Sentinel' : [58, False, Sentinel],
    'Sever Soul' : [59, False, Sever_Soul],
    'Shock Wave' : [60, False, Shock_Wave],
    'Shrug It Off' : [61, False, Shrug_It_Off],
    'Spot Weakness' : [62, False, Spot_Weakness],
    'Strike' : [63, True, Strike],
    'Sword Boomerang' : [64, True, Sword_Boomerang],
    'Thunderclap' : [65, True,Thunderclap],
    'True grit' : [66, False, True_Grit],
    'Twin Strike' : [67, True, Twin_Strike],
    'Uppercut' : [68, True, Uppercut],
    'Warcry' : [69, False, Warcry],
    'Whirlwind' : [70, True, Whirlwind],
    'WildStrike' : [71, True, WildStrike],

}
#States
class Temp_State:
    def __init__(self, My_Strength, Monster_Strength, weak, current_cost, attacknum):
        self.weak = weak
        self.My_Strength = My_Strength
        self.Monster_Strength = Monster_Strength
        self.current_cost =current_cost
        # This is for #double tap 1 cost This turn, your next Attack is played twice.
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

# Effect at end of turn
def end_of_turn(gamestate,Temp_State):
    
    
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
    #Card remains in hand for next round if not played.
    #How to represent?
    #else:
        #newstate.discard_pile.append['Clash']
        #return  newstate

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
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 5, newstate.Monsters[hitmonster[x]], Temp_State.attacknum)
  
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
    if Temp_State.check_start_of_turn
        Temp_State.My_Strength = Temp_State.My_Strength + 2
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
    newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster], Temp_State.attacknum)
    if is_Vulnerable: 
        #Gain 1 energy, and draw 1 card
    newstate.discard_pile.append('Dropkick')
    return newstate
    
#dual wield 1 cost Create a copy of an Attack or Power card in your hand.
def Dual_Wield(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #add Create a copy of an Attack or Power Card.
    newstate.discard_pile.append('Dual Wield')
    return newstate

#entrench 2 cost Double your current Block.
def Entrench(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #doulbe your current Block
    newstate.player.block = newstate.player.block * 2
    newstate.discard_pile.append('Entrench')
    return newstate
    
#evolve 1 cost Whenever you draw a Status, draw 1 card.
#Add draw 
def Evolve(gamestate, hitmonster, Temp_State):
    #add Draw card, if you draw a Status
    newstate =  gmaestate
    newstate.discard_pile.append('Evolve')
    return newstate

#exhume 1 cost Place a card from your Exhaust pile into your hand. Exhaust.
#how to pick the card form exhaust pile
def Exhume(gmaestate, hitmonster, Temp_State):
    newstate = gamestate
    #add Place a card from your Exhaust pile
    newstate.exhaust_pile.append('Exhume')
    return newstate

#feed 1 cost Deal 10 damage. If this kills a non-minion enemy, gain 3 permanent Max HP. Exhaust.
def Feed(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate = dealdmg(newstate, 10, newstate.Monsters[hitmonster], Temp_State.attacknum)
    # if monster is dead
    if newstate.is_dead:
        # gain 3 permanent Max HP
        newstate.max_hp =newstate.max_hp + 3
        newstate.exhaust_pile.append('Feed')
        return newstate
    else:
        #Remain the card if it is not played
        return newstate

#feel no pain 1 cost Whenever a card is Exhausted, gain 3 Block.
def Feel_No_Pain(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #check if a card is Exhausted, whenever after playing Feel No pain
    #how to represent?
    newstate.player.block = newstate.player.block+3
    return newstate

#fiend fire 2 cost Exhaust your hand. Deal 7 damage for each Exhausted card. Exhaust.
def Fiend_Fire(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    # if This card is played, turn on(True) the "Exhaust" helper function if not turn off(False)
    newstate.exhaust_pile.append('Fiend Fire')
    return newstate

#fire breathing 1 cost Whenever you draw a Status or Curse card, deal 6 damage to all enemies.
#need to update
def Fire_Breathing(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    # Whenever you draw a Status or Curse card
    if draw_State_or_Curse
        for x in len(hitmonster):
            newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster[x]], Temp_State.attacknum)
    newstate.discard_pile.append('Fire Breathing')
    return newstate

#flame barrier 2 cost Gain 12 Block. Whenever you are attacked this turn, deal 4 damage to the attacker.
def Flame_Barrier(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.player.block =  newstate.player.block + 12
    #if you are attacked this turn
    if is_attacked:
        #how to represent attacker?
        #how to represent this turn?
        #newstate = dealdmg(newstate, 4, newstate.Monster[hitmonster], Temp_State.attacknum)
    newstate.discard_pile.append('Flame_Barrier')   
    return newstate

#flex 0 cost 2 Strength. At the end of your turn, lose 2 Strength.
def Flex(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#ghostly armor 1 cost Ethereal. Gain 10 Block.
#add if you do not use this card, Ethereal.
def Ghostly_Armor(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.player.block =newstate.player.block + 10
    newstate.discard_pile.append('Ghostly_Armor')
    return newstate

#havoc 1 cost Play the top card of your draw pile and Exhaust it.
def Havoc(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#headbutt 1 cost Deal 9 damage. Place a card from your discard pile on top of your draw pile.
def Headbutt(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#heavy blade 2 cost Deal 14 damage. Strength affects Heavy Blade 3 times.
def Heavy_Blade(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#hemokinesis 1 cost Lose 3 HP. Deal 14 damage.
def Hemokinesis(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.current_hp =newstate.current_hp - 3
    newstate = dealdmg(newstate, 14, newstate.Monster[hitmonster], Temp_State.attacknum)
    newstate.discard_pile.append('Hemokinesis')
    return newstate

#immolate 2 cost Deal 21 damage to ALL enemies. Add a Burn to your discard pile.
def Immolate(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 21, newstate.Monsters[hitmonster[x]], Temp_State.attacknum)
    newstate.discard_pile.append('Burn')
    newstate.discard_pile.append('Immolate')
    return newstate

#impervious 2 cost Gain 30 Block. Exhaust.
def Impervious(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.player.block =newstate.player.block + 10
    newstate.exhaust_pile.append('Impervious')
    return newstate

#infernal blade 1 cost Add a random Attack to your hand. It costs 0 this turn. Exhaust.
def Infernal_Blade(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #add a random Attack to your hand
    newstate.exhaust_pile.append('Infernal_Blade')
    return newstate

#inflame 1 cost Gain 2 Strength.
def Inflame(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#intimidate 0 cost Apply 1 Weak to ALL enemies. Exhaust.
def Intimidate(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#iron wave 1 cost Gain 5 Block. Deal 5 damage.
def Iron_wave(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.player.block = newstate.player.block +5
    dealdmg(newstate, 5, newstate.Monster[hitmonster], Temp_State.attacknum)
    newstate.discard_pile.append('Iron Wave')
    return newstate
    
#juggernaut 2 cost Whenever you gain Block, deal 5 damage to a random enemy.
def Juggernaut(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#limit break 1 cost Double your Strength. Exhaust.
def Limit_Break(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #add double your Strength
    newstate.exhaust_pile.append('Limit Break')
    return newstate

#metallicize 1 cost At the end of your turn, gain 3 Block.
def Metallicize(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#offering 0 cost Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.
def Offering(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#perfected strike 2 cost Deal 6 damage. Deals an additional 2 damage for ALL of your cards containing "Strike".
def Perfected_Strike(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#pommel strike 1 cost Deal 9 damage. Draw 1 card(s).
def Pommel_Strike(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#power through 1 cost Add 2 Wounds to your hand. Gain 15 Block.
def Power_Through(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#pummel 1 cost Deal 2 damage 4 times. Exhaust.
def Pummel(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#rage 0 cost Whenever you play an Attack this turn, gain 3 Block
def Rage(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#rampage 1 cost Deal 8 damage. Every time this card is played, increase its damage by 8 for this combat.
def Rampage(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#reaper 2 cost Deal 4 damage to ALL enemies. Heal for unblocked damage dealt. Exhaust.
def Reaper(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#reckless charge 0 cost Deal 7 damage. Shuffle a Dazed into your draw pile
def Reckless_Charge(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#rupture 1 cost Whenever you lose HP from a card, gain 1 Strength.
def Rupture(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#searing blow 2 cost Deal 12 damage. Can be upgraded any number of times.
def Searing_Blow(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate = newstate = dealdmg(newstate, 12, newstate.Monsters[hitmonster], Temp_State.attacknum)
    return newstate

#second wind 1 cost Exhaust all non-Attack cards in your hand and gain 5 Block for each.
def Second_Wind(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#seeing red 1 cost Gain 2 energy. Exhaust.
def Seeing_Red(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #add Gain 2 energy
    newstate.exhaust_pile.append('Seeing Red')
    return newstate

#sentinel 1 cost Gain 5 Block. If this card is Exhausted, gain 2 energy.
def Sentinel(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.player.block = newstate.player.block + 5
    #add If this card is Exhausted, gain 2 energy
    return newstate

#sever soul 2 cost Exhaust all non-Attack cards in your hand. Deal 16 damage.
def Sever_Soul(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #add exhuast all non-Attack Cards in your hand
    newstate = dealdmg(newstate, 16, newstate.Monsters[hitmonster], Temp_State.attacknum)
    return newstate

#shock wave 2 cost Apply 3 Weak and Vulnerable to ALL enemies.Exhaust.
def Shock_Wave(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #add apply 3 Weak and Vulneralble to All enemies
    newstate.exhaust_pile.append('Shock Wave')
    return newstate

#shrug it off 1 cost Gain 8 Block. Draw 1 card.
def Shrug_It_Off(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.player.block = newstate.player.block + 8
    #add Draw Card
    newstate.discard_pile.append('Strug It Off')
    return newstate

#spot weakness 1 cost If an enemy intends to attack, gain 3 Strength.
def Spot_Weakness(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#strike 1 cost Deal 6 damage.
def Strike(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster], Temp_State.attacknum)
    newstate.discard_pile('Strike')
    return newstate

#sword boomerang 1 cost Deal 3 damage to a random enemy 3 times.
def Sword_Boomerang(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    # a random enemy.
    x = randomrange(len(hitmonster))
    # deal 3 damage
    newstate = dealdmg(newstate, 3, newstate.Monsters[hitmonster[x]], Temp_State.attacknum)
    newstate = dealdmg(newstate, 3, newstate.Monsters[hitmonster[x]], Temp_State.attacknum)
    newstate = dealdmg(newstate, 3, newstate.Monsters[hitmonster[x]], Temp_State.attacknum)
    return newstate

#thunderclap 1 cost Deal 4damage and apply 1 Vulnerable to ALL enemies.
def Thunderclap(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    for x in len(hitmonster):
        newstate = dealdmg(newstate, 4, newstate.Monsters[hitmonster[x]], Temp_State.attacknum)
        #add apply 1 Vulnerable
    newstate.discard_pile.append('Thunderclap')
    return newstate

#true grit 1 cost Gain 7 Block. Exhaust a random card from your hand.
def True_Grit(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate.player.block = newstate.player.block + 7
    #add Exhuast a random card from your hand
    newstate.discard_pile.append('True Grit')
    return newstate

#twin strike 1 cost Deal 5 damage twice.
def Twin_Strike(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster], Temp_State.attacknum)
    newstate = dealdmg(newstate, 5, newstate.Monster[hitmonster], Temp_State.attacknum)
    newstate.discard_pile.append('Twin Strike')
    return newstate

#uppercut 2 cost Deal 13 damage. Apply 1 Weak. Apply 1 Vulnerable.
def Uppercut(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate = dealdmg(newstate, 13, newstate.Monster[hitmonster], Temp_State.attacknum)
    #apply 1 weak, and 1 Vulnerable
    newstate.discard_pile.append('Uppercut')
    return newstate

#warcry 0 cost Draw 1 card. Place a card from your hand on top of your draw pile. Exhaust.
def Warcry(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    #Draw 1 Card
    #Place a Card from your hand on top of your draw pile.
    newstate.exhaust_pile.append('Warcry')
    return newstate

#whirlwind X cost Deal 5 damage to ALL enemies X times.
def Whirlwind(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    return newstate

#wildstrike 1 cost Deal 12 damage. Shuffle a Wound into your draw pile.
def Wildstrike(gamestate, hitmonster, Temp_State):
    newstate = gamestate
    newstate = newstate = dealdmg(newstate, 12, newstate.Monster[hitmonster], Temp_State.attacknum)
    newstate.discard_pile.append('Wildstrike')
    newstate.draw_pile.append('Wound')
    return newstate


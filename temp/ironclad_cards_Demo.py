#THIS IS PARTLY PSEUDOCODE
#problems:upgrading a card not implemented

#dict of cards
#cost, target, function
#target true = card can target enemy
#target false = card just gets played
cards = {
    'anger' : [0, true, anger],
    'armaments' : [1, false, armaments],
    'barricade' : [3, false, barricade],
}


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
        if x[1] = false:
            x[2](gamestate)
        else:
            for target in Game.Monsters:
                x[2](gamestate, target)

#will need to evaluate the new gamestate the card function returns?
                
#helper functions
                
#deal damage to monster
#attacknum is the number of times you attack
def dealdmg(gamestate, damage, monster, attacknum = 1):
    newstate = gamestate
    for p in newstate.Player.Power:
        if p.power_name = Strength:
            newstate.Monsters[monster].current_hp -= (damage + p.amount) * attacknum
            return newstate
    else:
        newstate.Monsters[monster].current_hp -= damage * attacknum
        return newstate
    
        
#anger 0 cost Deal 6 damage. Add a copy of this card to your discard pile.
def anger(gamestate, hitmonster):
    #gamestate class = Game
    #hitmonster class = Monster
    newstate = gamestate
    
    #deal 6 damage    
    newstate = dealdmg(newstate, 6, newstate.Monster[hitmonster])
    
    #add a copy of this card to your discard pile
    newstate.discard_pile.append('anger')
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
    
    #apply 2 vulnerable
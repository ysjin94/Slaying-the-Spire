#This is status_card
#Unplayed : cannot be played in your hand

#Burn :Unplayable. At the end of your turn, take 2(4) damage
def Burn(gamastate, upgrade):
  newstate = gamestate
  return newstate

#Dazed : Unplayable. Ethereal
def Dazed(gamastate, upgrade):
  newstate = gamestate
  return newstate

#Wound : Unplayable
def Wound(gamastate, upgrade):
  newstate = gamestate
  return newstate

#Slimed : Exhuast
def Slimed(gamastate, upgrade):
  newstate = gamestate
  return newstate

#Void : Unplayable. When this card is drawn, lose 1 Energy. Ethereal.
def Void(gamastate, upgrade):
  newstate = gamestate
  return newstate

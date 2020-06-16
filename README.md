# Slaying the Spire
# Hunter College CSCI 49900 Capstone Project

This project is built using ForgottenArbiter's spirecomm which communicates with Slay the Spire through his Communication Mod.

Goals: improvements of existing ai based on certain categories like clear rate, and speed by using Minimax algorithm.

Website : Empty for now



|  | | 
| ---- | --- | 
|![draftbot card](utilities/draftbot.png)| <h2>Tech Used</h2><h3><br/><ul><li>Python</li><li>Website</li></li><li>Simple AI</li><li>Minimax algorithm</li></ul></h3>|

# SetUp :
1. Install three mods
   * Install [Communication Mod](https://github.com/ForgottenArbiter/CommunicationMod)
   * ModTheSpire - Steam Workshop version
   * BaseMod - Steam Workshop versio
2. Update Communication Mod config
  * Windows: `%LOCALAPPDATA%\ModTheSpire\CommunicationMod\config.properties` 
  * Linux: `~/.config/ModTheSpire/config.properties` 
  * Mac: `~/Library/Preferences/ModTheSpire/config.properties` 
3. Set command=python3 Location where is the main.py
  * e.g) `command=python3 path_to_script/main.py`
4. Launch Slay The Spire with mods and go to communication mods setting and click "Start External Process"


If the mod does not run correctly
* check the `communication_mod_errors.log`
You can find it Steam->select "Slay the Spire" -> click "Manage"-> "Browes localfile"->"Resource"


# Building Deck :
![card_choice_screen](utilities/Building_deck_.png)
  
  We are using the data form (https://spirelogs.com/stats/silent/tierlist.php) as a base data. 
  
  The AI always going to select the highest overall score cards.(The Top one is overall, Bottom is upgrade Bonuce ) 
  
  If AI does not has enough money to buy the highest overall score cards, select the next overall cards. If there are same overall cards, Select the highest upgrade bonuce.
  
  If upgrade bounce is greater than overall socre cards in a store, select the upgrades Bonuce.
  
![shop_screen](utilities/shop.png)

 We are also useing the purchased item data as a base data. (https://spirelogs.com/stats/shop-items.php)
 
The Upper cards is the class cards, and bottom one is item and potion.

The priority "Class card" -> "shop card" -> "potion" for now (It could be changed) 

It will be chosen by the winrates base on the data. 

we need to convert postion winrate to overall points
* 0% ~ 10% winrate for shop card = 30 overall points
* 10% ~ 20% winrate for shop card = 60 overall points
* 20% ~ 40% winrate for shop card = 100 overall points
* 40% ~ 50% winrate for shop card = 130 overall points
* 50% ~ 100% winrate for shop card = 200 overall points


# Theory : 
  * Run the AI with the base data.
  * Modify the base data, bese on the Result of Run.
  * The data will be more accurately.
  
# Overview :

# Future Improvements:
 * Develop the website
 * Improve the sample AI by using Minimax algorithm
 * spirelog.com is updated, check the new table, and the Deck Building will be changed.
 (https://dev.spirelogs.com/ironclad/shop.php)

[Presentation Link - Has more diagrams and info](https://docs.google.com/presentation/d/1RxQuOPTGZf5BejvV4l8MaKA3IbAYYN19-rI9gjpSf4s/edit#slide=id.p)

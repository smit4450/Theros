---
title: Rat
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Rat"]
---
# Rat
*Source: Monster Manual (2024) p. 367, Player's Handbook (2024) p. 355. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![An adventurer underestimat...](Compendium/bestiary/beast/img/rats.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Rat (XMM)"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "1"
"hit_dice": "1d4 - 1"
"modifier": !!int "0"
"stats":
  - !!int "2"
  - !!int "11"
  - !!int "9"
  - !!int "2"
  - !!int "10"
  - !!int "4"
"speed": "20 ft., climb 20 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+2"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 30 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The rat doesn't provoke [Opportunity Attacks](Compendium/rules/actions.md#Opportunity%20Attack)\
      \ when it moves out of an enemy's reach."
    "name": "Agile"
"actions":
  - "desc": "*Melee Attack Roll:* +2, reach 5 ft. *Hit:* 1 Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
  - "XPHB"
"image": "Compendium/bestiary/beast/token/rat-xmm.webp"
```
^statblock
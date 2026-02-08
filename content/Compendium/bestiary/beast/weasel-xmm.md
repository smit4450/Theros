---
title: Weasel
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Weasel"]
---
# Weasel
*Source: Monster Manual (2024) p. 372, Player's Handbook (2024) p. 359. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/weasel.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Weasel (XMM)"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "1"
"hit_dice": "1d4 - 1"
"modifier": !!int "3"
"stats":
  - !!int "3"
  - !!int "16"
  - !!int "8"
  - !!int "2"
  - !!int "12"
  - !!int "3"
"speed": "30 ft., climb 30 ft."
"skillsaves":
  - "name": "[Acrobatics](Compendium/rules/skills.md#Acrobatics)"
    "desc": "+5"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "0"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 1 Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
  - "XPHB"
"image": "Compendium/bestiary/beast/token/weasel-xmm.webp"
```
^statblock
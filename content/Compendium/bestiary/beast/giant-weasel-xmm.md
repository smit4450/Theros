---
title: Giant Weasel
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-8
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Weasel"]
---
# Giant Weasel
*Source: Monster Manual (2024) p. 361, Player's Handbook (2024) p. 351. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/weasel.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Weasel (XMM)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "9"
"hit_dice": "2d8"
"modifier": !!int "3"
"stats":
  - !!int "11"
  - !!int "17"
  - !!int "10"
  - !!int "4"
  - !!int "12"
  - !!int "5"
"speed": "40 ft., climb 30 ft."
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
"cr": "1/8"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 5 (1d4 + 3) Piercing\
      \ damage."
    "name": "Bite"
"source":
  - "XMM"
  - "XPHB"
"image": "Compendium/bestiary/beast/token/giant-weasel-xmm.webp"
```
^statblock
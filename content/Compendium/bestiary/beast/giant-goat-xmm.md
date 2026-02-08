---
title: Giant Goat
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Goat"]
---
# Giant Goat
*Source: Monster Manual (2024) p. 357, Player's Handbook (2024) p. 350. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/giant-goat.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Goat (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "19"
"hit_dice": "3d10 + 3"
"modifier": !!int "1"
"stats":
  - !!int "17"
  - !!int "13"
  - !!int "12"
  - !!int "3"
  - !!int "12"
  - !!int "6"
"speed": "40 ft., climb 30 ft."
"saves":
  - "strength": !!int "5"
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "1/2"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 6 (1d6 + 3) Bludgeoning\
      \ damage. If the target is a Large or smaller creature and the goat moved 20+\
      \ feet straight toward it immediately before the hit, the target takes an extra\
      \ 5 (2d4) Bludgeoning damage and has the [Prone](Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Ram"
"source":
  - "XMM"
  - "XPHB"
"image": "Compendium/bestiary/beast/token/giant-goat-xmm.webp"
```
^statblock
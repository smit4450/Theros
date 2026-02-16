---
title: Lion
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Lion"]
---
# Lion
*Source: Monster Manual (2024) p. 364, Player's Handbook (2024) p. 352, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/lion.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Lion (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "22"
"hit_dice": "4d10"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "15"
  - !!int "11"
  - !!int "3"
  - !!int "12"
  - !!int "8"
"speed": "50 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "1"
"traits":
  - "desc": "The lion has [[advantage-xphb|Advantage]]\
      \ on an attack roll against a creature if at least one of the lion's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [[conditions#Incapacitated|Incapacitated]]\
      \ condition."
    "name": "Pack Tactics"
  - "desc": "With a 10-foot running start, the lion can [[long-jump-xphb|Long Jump]]\
      \ up to 25 feet."
    "name": "Running Leap"
"actions":
  - "desc": "The lion makes two Rend attacks. It can replace one attack with a use\
      \ of Roar."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 7 (1d8 + 3) Slashing\
      \ damage."
    "name": "Rend"
  - "desc": "*Wisdom Saving Throw:* DC 11, one creature within 15 feet. *Failure:*\
      \ The target has the [[conditions#Frightened|Frightened]]\
      \ condition until the start of the lion's next turn."
    "name": "Roar"
"source":
  - "XMM"
  - "XPHB"
  - "FRHoF"
"image": "Compendium/bestiary/beast/token/lion-xmm.webp"
```
^statblock
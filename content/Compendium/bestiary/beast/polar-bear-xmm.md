---
title: Polar Bear
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Polar Bear"]
---
# Polar Bear
*Source: Monster Manual (2024) p. 367. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/polar-bear.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Polar Bear (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "42"
"hit_dice": "5d10 + 15"
"modifier": !!int "2"
"stats":
  - !!int "20"
  - !!int "14"
  - !!int "16"
  - !!int "2"
  - !!int "13"
  - !!int "7"
"speed": "40 ft., swim 40 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
"damage_resistances": "cold"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 15"
"languages": ""
"cr": "2"
"actions":
  - "desc": "The bear makes two Rend attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 9 (1d8 + 5) Slashing\
      \ damage."
    "name": "Rend"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/polar-bear-xmm.webp"
```
^statblock
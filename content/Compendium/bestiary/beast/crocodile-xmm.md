---
title: Crocodile
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Crocodile"]
---
# Crocodile
*Source: Monster Manual (2024) p. 352, Player's Handbook (2024) p. 348. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/crocodile.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Crocodile (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "13"
"hit_dice": "2d10 + 2"
"modifier": !!int "0"
"stats":
  - !!int "15"
  - !!int "10"
  - !!int "13"
  - !!int "2"
  - !!int "10"
  - !!int "5"
"speed": "20 ft., swim 30 ft."
"saves":
  - "constitution": !!int "3"
"skillsaves":
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "The crocodile can hold its breath for 1 hour."
    "name": "Hold Breath"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 6 (1d8 + 2) Piercing\
      \ damage. If the target is a Medium or smaller creature, it has the [Grappled](Compendium/rules/conditions.md#Grappled)\
      \ condition (escape DC 12). While [Grappled](Compendium/rules/conditions.md#Grappled),\
      \ the target has the [Restrained](Compendium/rules/conditions.md#Restrained)\
      \ condition."
    "name": "Bite"
"source":
  - "XMM"
  - "XPHB"
"image": "Compendium/bestiary/beast/token/crocodile-xmm.webp"
```
^statblock
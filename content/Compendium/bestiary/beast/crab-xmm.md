---
title: Crab
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Crab"]
---
# Crab
*Source: Monster Manual (2024) p. 351, Player's Handbook (2024) p. 348. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/crab.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Crab (XMM)"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "3"
"hit_dice": "1d4 + 1"
"modifier": !!int "0"
"stats":
  - !!int "6"
  - !!int "11"
  - !!int "12"
  - !!int "1"
  - !!int "8"
  - !!int "2"
"speed": "20 ft., swim 20 ft."
"skillsaves":
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+2"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 30 ft., passive Perception\
  \ 9"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The crab can breathe air and water."
    "name": "Amphibious"
"actions":
  - "desc": "*Melee Attack Roll:* +2, reach 5 ft. *Hit:* 1 Bludgeoning damage."
    "name": "Claw"
"source":
  - "XMM"
  - "XPHB"
"image": "Compendium/bestiary/beast/token/crab-xmm.webp"
```
^statblock
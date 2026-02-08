---
title: Reef Shark
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Reef Shark"]
---
# Reef Shark
*Source: Monster Manual (2024) p. 368, Player's Handbook (2024) p. 356. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/reef-shark.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Reef Shark (XMM)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "22"
"hit_dice": "4d8 + 4"
"modifier": !!int "2"
"stats":
  - !!int "14"
  - !!int "15"
  - !!int "13"
  - !!int "1"
  - !!int "10"
  - !!int "4"
"speed": "5 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+2"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 30 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "The shark has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on an attack roll against a creature if at least one of the shark's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
      \ condition."
    "name": "Pack Tactics"
  - "desc": "The shark can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 7 (2d4 + 2) Piercing\
      \ damage."
    "name": "Bite"
"source":
  - "XMM"
  - "XPHB"
"image": "Compendium/bestiary/beast/token/reef-shark-xmm.webp"
```
^statblock
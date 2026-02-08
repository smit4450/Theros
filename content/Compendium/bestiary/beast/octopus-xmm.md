---
title: Octopus
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Octopus"]
---
# Octopus
*Source: Monster Manual (2024) p. 365, Player's Handbook (2024) p. 353. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/octopus.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Octopus (XMM)"
"size": "Small"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "3"
"hit_dice": "1d6"
"modifier": !!int "2"
"stats":
  - !!int "4"
  - !!int "15"
  - !!int "11"
  - !!int "3"
  - !!int "10"
  - !!int "4"
"speed": "5 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+2"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+6"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 30 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The octopus can move through a space as narrow as 1 inch without expending\
      \ extra movement to do so."
    "name": "Compression"
  - "desc": "The octopus can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 1 Bludgeoning damage."
    "name": "Tentacles"
"reactions":
  - "desc": "Trigger: A creature ends its turn within 5 feet of the octopus while\
      \ underwater. _Response:_ The octopus releases ink that fills a 5-foot [Cube](Compendium/rules/variant-rules/cube-area-of-effect-xphb.md)\
      \ centered on itself, and the octopus moves up to its [Swim Speed](Compendium/rules/variant-rules/swim-speed-xphb.md).\
      \ The [Cube](Compendium/rules/variant-rules/cube-area-of-effect-xphb.md) is\
      \ [Heavily Obscured](Compendium/rules/variant-rules/heavily-obscured-xphb.md)\
      \ for 1 minute or until a strong current or similar effect disperses the ink."
    "name": "Ink Cloud (1/Day)"
"source":
  - "XMM"
  - "XPHB"
"image": "Compendium/bestiary/beast/token/octopus-xmm.webp"
```
^statblock
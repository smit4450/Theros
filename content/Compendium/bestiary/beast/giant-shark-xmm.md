---
title: Giant Shark
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Shark"]
---
# Giant Shark
*Source: Monster Manual (2024) p. 359, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/hunter-shark.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Shark (XMM)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "92"
"hit_dice": "8d12 + 40"
"modifier": !!int "3"
"stats":
  - !!int "23"
  - !!int "11"
  - !!int "21"
  - !!int "1"
  - !!int "10"
  - !!int "5"
"speed": "5 ft., swim 60 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 60 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "5"
"traits":
  - "desc": "The shark can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "The shark makes two Bite attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +9 (with [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
      \ if the target doesn't have all its [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)),\
      \ reach 5 ft. *Hit:* 22 (3d10 + 6) Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/beast/token/giant-shark-xmm.webp"
```
^statblock
---
title: Tyrannosaurus Rex
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast/dinosaur
statblock: inline
aliases: ["Tyrannosaurus Rex"]
---
# Tyrannosaurus Rex
*Source: Monster Manual (2024) p. 372. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/tyrannosaurus-rex.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Tyrannosaurus Rex (XMM)"
"size": "Huge"
"type": "beast"
"subtype": "dinosaur"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "136"
"hit_dice": "13d12 + 52"
"modifier": !!int "3"
"stats":
  - !!int "25"
  - !!int "10"
  - !!int "19"
  - !!int "2"
  - !!int "12"
  - !!int "9"
"speed": "50 ft."
"saves":
  - "strength": !!int "10"
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"senses": "passive Perception 14"
"languages": ""
"cr": "8"
"actions":
  - "desc": "The tyrannosaurus makes one Bite attack and one Tail attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +10, reach 10 ft. *Hit:* 33 (4d12 + 7) Piercing\
      \ damage. If the target is a Large or smaller creature, it has the [Grappled](Compendium/rules/conditions.md#Grappled)\
      \ condition (escape DC 17). While [Grappled](Compendium/rules/conditions.md#Grappled),\
      \ the target has the [Restrained](Compendium/rules/conditions.md#Restrained)\
      \ condition and can't be targeted by the tyrannosaurus's Tail."
    "name": "Bite"
  - "desc": "*Melee Attack Roll:* +10, reach 15 ft. *Hit:* 25 (4d8 + 7) Bludgeoning\
      \ damage. If the target is a Huge or smaller creature, it has the [Prone](Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Tail"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/tyrannosaurus-rex-xmm.webp"
```
^statblock
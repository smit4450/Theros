---
title: Camel
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-8
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Camel"]
---
# Camel
*Source: Monster Manual (2024) p. 351, Player's Handbook (2024) p. 347. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/camel.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Camel (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "17"
"hit_dice": "2d10 + 6"
"modifier": !!int "-1"
"stats":
  - !!int "15"
  - !!int "8"
  - !!int "17"
  - !!int "2"
  - !!int "11"
  - !!int "5"
"speed": "50 ft."
"saves":
  - "constitution": !!int "5"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "1/8"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 4 (1d4 + 2) Bludgeoning\
      \ damage."
    "name": "Bite"
"source":
  - "XMM"
  - "XPHB"
"image": "Compendium/bestiary/beast/token/camel-xmm.webp"
```
^statblock
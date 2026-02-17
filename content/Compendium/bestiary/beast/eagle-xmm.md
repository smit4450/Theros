---
title: Eagle
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/0
- monster/environment/coastal
- monster/environment/grassland
- monster/environment/hill
- monster/environment/mountain
- monster/size/small
- monster/type/beast
statblock: inline
aliases: ["Eagle"]
---
# Eagle
*Source: Monster Manual (2024) p. 353. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/celestial/img/eagle.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Eagle (XMM)"
"size": "Small"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "4"
"hit_dice": "1d6 + 1"
"modifier": !!int "2"
"stats":
  - !!int "6"
  - !!int "15"
  - !!int "12"
  - !!int "2"
  - !!int "14"
  - !!int "7"
"speed": "10 ft., fly 60 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
"senses": "passive Perception 16"
"languages": ""
"cr": "0"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 feet. *Hit:* 4 (1d4 + 2) Slashing\
      \ damage."
    "name": "Talons"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/eagle-xmm.webp"
```
^statblock
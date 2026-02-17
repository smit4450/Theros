---
title: Giant Fire Beetle
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/0
- monster/environment/underdark
- monster/size/small
- monster/type/beast
statblock: inline
aliases: ["Giant Fire Beetle"]
---
# Giant Fire Beetle
*Source: Monster Manual (2024) p. 357. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/giant-fire-beetle.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Fire Beetle (XMM)"
"size": "Small"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "4"
"hit_dice": "1d6 + 1"
"modifier": !!int "0"
"stats":
  - !!int "8"
  - !!int "10"
  - !!int "12"
  - !!int "1"
  - !!int "7"
  - !!int "3"
"speed": "30 ft., climb 30 ft."
"damage_resistances": "fire"
"senses": "[[senses#Blindsight|Blindsight]] 30 ft., passive Perception\
  \ 8"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The beetle sheds [[bright-light-xphb|Bright Light]]\
      \ in a 10-foot radius and [[dim-light-xphb|Dim Light]]\
      \ for an additional 10 feet."
    "name": "Illumination"
"actions":
  - "desc": "*Melee Attack Roll:* +1, reach 5 ft. *Hit:* 1 Fire damage."
    "name": "Bite"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/giant-fire-beetle-xmm.webp"
```
^statblock
---
title: Giant Centipede
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1-4
- monster/environment/underdark
- monster/environment/urban
- monster/size/small
- monster/type/beast
statblock: inline
aliases: ["Giant Centipede"]
---
# Giant Centipede
*Source: Monster Manual (2024) p. 355. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/giant-centipede.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Centipede (XMM)"
"size": "Small"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "9"
"hit_dice": "2d6 + 2"
"modifier": !!int "2"
"stats":
  - !!int "5"
  - !!int "14"
  - !!int "12"
  - !!int "1"
  - !!int "7"
  - !!int "3"
"speed": "30 ft., climb 30 ft."
"senses": "[[senses#Blindsight|Blindsight]] 30 ft., passive Perception\
  \ 8"
"languages": ""
"cr": "1/4"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 4 (1d4 + 2) Piercing\
      \ damage, and the target has the [[conditions#Poisoned|Poisoned]]\
      \ condition until the start of the centipede's next turn."
    "name": "Bite"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/giant-centipede-xmm.webp"
```
^statblock
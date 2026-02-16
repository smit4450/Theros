---
title: Rhinoceros
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Rhinoceros"]
---
# Rhinoceros
*Source: Monster Manual (2024) p. 368. Available in the <span title='Systems Reference Document (5.2)'>SRD</span>*  

![](Compendium/bestiary/beast/img/rhinoceros.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Rhinoceros (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "45"
"hit_dice": "6d10 + 12"
"modifier": !!int "-1"
"stats":
  - !!int "21"
  - !!int "8"
  - !!int "15"
  - !!int "2"
  - !!int "12"
  - !!int "6"
"speed": "40 ft."
"senses": "passive Perception 11"
"languages": ""
"cr": "2"
"actions":
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 14 (2d8 + 5) Piercing\
      \ damage. If target is a Large or smaller creature and the rhinoceros moved\
      \ 20+ feet straight toward it immediately before the hit, the target takes an\
      \ extra 9 (2d8) Piercing damage and has the [[conditions#Prone|Prone]]\
      \ condition."
    "name": "Gore"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/rhinoceros-xmm.webp"
```
^statblock
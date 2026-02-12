---
title: Giant Boar
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Boar"]
---
# Giant Boar
*Source: Monster Manual (2024) p. 355. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/boar.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Boar (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "42"
"hit_dice": "5d10 + 15"
"modifier": !!int "0"
"stats":
  - !!int "17"
  - !!int "10"
  - !!int "16"
  - !!int "2"
  - !!int "7"
  - !!int "5"
"speed": "40 ft."
"saves":
  - "strength": !!int "5"
"senses": "passive Perception 8"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The boar has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on melee attack rolls while it is [Bloodied](Compendium/rules/conditions.md#Bloodied)."
    "name": "Bloodied Fury"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 10 (2d6 + 3) Piercing\
      \ damage. If the target is a Large or smaller creature and the boar moved 20+\
      \ feet straight toward it immediately before the hit, the target takes an extra\
      \ 7 (2d6) Piercing damage and has the [Prone](Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Gore"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/giant-boar-xmm.webp"
```
^statblock
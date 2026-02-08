---
title: Flying Snake
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-8
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Flying Snake"]
---
# Flying Snake
*Source: Monster Manual (2024) p. 353, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/monstrosity/img/flying-snake.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Flying Snake (XMM)"
"size": "Tiny"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "5"
"hit_dice": "2d4"
"modifier": !!int "2"
"stats":
  - !!int "4"
  - !!int "15"
  - !!int "11"
  - !!int "2"
  - !!int "12"
  - !!int "5"
"speed": "30 ft., fly 60 ft., swim 30 ft."
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 10 ft., passive Perception\
  \ 11"
"languages": ""
"cr": "1/8"
"traits":
  - "desc": "The snake doesn't provoke an Opportunity Attack when it flies out of\
      \ an enemy's reach."
    "name": "Flyby"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 1 Piercing damage plus\
      \ 5 (2d4) Poison damage."
    "name": "Bite"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/monstrosity/token/flying-snake-xmm.webp"
```
^statblock
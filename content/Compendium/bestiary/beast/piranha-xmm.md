---
title: Piranha
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Piranha"]
---
# Piranha
*Source: Monster Manual (2024) p. 366. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/piranha.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Piranha (XMM)"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "1"
"hit_dice": "1d4 - 1"
"modifier": !!int "3"
"stats":
  - !!int "2"
  - !!int "16"
  - !!int "9"
  - !!int "1"
  - !!int "7"
  - !!int "2"
"speed": "5 ft., swim 40 ft."
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 8"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The piranha can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "*Melee Attack Roll:* +5 (with [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
      \ if the target doesn't have all its [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)),\
      \ reach 5 ft. *Hit:* 1 Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/piranha-xmm.webp"
```
^statblock
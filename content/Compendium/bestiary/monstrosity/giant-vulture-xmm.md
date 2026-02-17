---
title: Giant Vulture
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1
- monster/environment/desert
- monster/environment/grassland
- monster/environment/hill
- monster/size/large
- monster/type/monstrosity
statblock: inline
aliases: ["Giant Vulture"]
---
# Giant Vulture
*Source: Monster Manual (2024) p. 361. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/vulture.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Vulture (XMM)"
"size": "Large"
"type": "monstrosity"
"alignment": "Neutral Evil"
"ac": !!int "10"
"hp": !!int "25"
"hit_dice": "3d10 + 9"
"modifier": !!int "0"
"stats":
  - !!int "15"
  - !!int "10"
  - !!int "16"
  - !!int "6"
  - !!int "12"
  - !!int "7"
"speed": "10 ft., fly 60 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"damage_resistances": "necrotic"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 13"
"languages": "understands Common but can't speak"
"cr": "1"
"traits":
  - "desc": "The vulture has [[advantage-xphb|Advantage]]\
      \ on an attack roll against a creature if at least one of the vulture's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [[conditions#Incapacitated|Incapacitated]]\
      \ condition."
    "name": "Pack Tactics"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 9 (2d6 + 2) Piercing\
      \ damage, and the target has the [[conditions#Poisoned|Poisoned]]\
      \ condition until the end of its next turn."
    "name": "Gouge"
"source":
  - "XMM"
"image": "Compendium/bestiary/monstrosity/token/giant-vulture-xmm.webp"
```
^statblock
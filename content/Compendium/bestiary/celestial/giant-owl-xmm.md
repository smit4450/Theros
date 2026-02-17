---
title: Giant Owl
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1-4
- monster/environment/arctic
- monster/environment/forest
- monster/environment/hill
- monster/size/large
- monster/type/celestial
statblock: inline
aliases: ["Giant Owl"]
---
# Giant Owl
*Source: Monster Manual (2024) p. 358. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/celestial/img/owl.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Owl (XMM)"
"size": "Large"
"type": "celestial"
"alignment": "Neutral"
"ac": !!int "12"
"hp": !!int "19"
"hit_dice": "3d10 + 3"
"modifier": !!int "2"
"stats":
  - !!int "13"
  - !!int "15"
  - !!int "12"
  - !!int "10"
  - !!int "14"
  - !!int "10"
"speed": "5 ft., fly 60 ft."
"saves":
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+6"
"damage_resistances": "necrotic, radiant"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception\
  \ 16"
"languages": "Celestial; understands Common, Elvish, and Sylvan but can't speak them"
"cr": "1/4"
"traits":
  - "desc": "The owl doesn't provoke an Opportunity Attack when it flies out of an\
      \ enemy's reach."
    "name": "Flyby"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 7 (1d10 + 2) Slashing\
      \ damage."
    "name": "Talons"
  - "desc": "The owl casts one of the following spells, requiring no spell components\
      \ and using Wisdom as the spellcasting ability:\n\n**At will:** [[detect-evil-and-good-xphb|Detect Evil\
      \ and Good]], [[detect-magic-xphb|Detect Magic]]\n\
      \n**1/day:** [[clairvoyance-xphb|Clairvoyance]]"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/celestial/token/giant-owl-xmm.webp"
```
^statblock
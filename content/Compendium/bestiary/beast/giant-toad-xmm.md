---
title: Giant Toad
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1
- monster/environment/coastal
- monster/environment/forest
- monster/environment/swamp
- monster/environment/underdark
- monster/size/large
- monster/type/beast
statblock: inline
aliases: ["Giant Toad"]
---
# Giant Toad
*Source: Monster Manual (2024) p. 360. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/giant-toad.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Toad (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "39"
"hit_dice": "6d10 + 6"
"modifier": !!int "1"
"stats":
  - !!int "15"
  - !!int "13"
  - !!int "13"
  - !!int "2"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., swim 30 ft."
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "1"
"traits":
  - "desc": "The toad can breathe air and water."
    "name": "Amphibious"
  - "desc": "The toad's [[long-jump-xphb|Long Jump]]\
      \ is up to 20 feet and its [[high-jump-xphb|High Jump]]\
      \ is up to 10 feet with or without a running start."
    "name": "Standing Leap"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 5 (1d6 + 2) Piercing\
      \ damage plus 5 (2d4) Poison damage. If the target is a Medium or smaller\
      \ creature, it has the [[conditions#Grappled|Grappled]] condition\
      \ (escape DC 12)."
    "name": "Bite"
  - "desc": "The toad swallows a Medium or smaller target it is grappling. While swallowed,\
      \ the target isn't [[conditions#Grappled|Grappled]] but has\
      \ the [[conditions#Blinded|Blinded]] and [[conditions#Restrained|Restrained]]\
      \ conditions, and it has [[cover-table-xphb|Total Cover]]\
      \ against attacks and other effects outside the toad. In addition, the target\
      \ takes 10 (3d6) Acid damage at the end of each of the toad's turns. The toad\
      \ can have only one target swallowed at a time, and it can't use Bite while\
      \ it has a swallowed target. If the toad dies, a swallowed creature is no longer\
      \ [[conditions#Restrained|Restrained]] and can escape from\
      \ the corpse using 5 feet of movement, exiting with the [[conditions#Prone|Prone]]\
      \ condition."
    "name": "Swallow"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/giant-toad-xmm.webp"
```
^statblock
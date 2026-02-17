---
title: Treeshaker Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvi
- monster/cr/7
- monster/size/h
- monster/type/monstrosity
statblock: inline
aliases: ["Treeshaker Chimera"]
---
# Treeshaker Chimera
*Source: Theros Bestiary TBVI*  

<blockquote>The wisdom of the past is written on the bones of ancients.</blockquote>
The treeshaker chimera is a massive five-legged beast with three heads. Its left side is a wolf, its right side is a kudu, and its middle is a lion. In the front, it has one paw, one claw, and one hoof. It is a trophy animal among hunters.

![Treeshaker Chimera](Compendium/bestiary/monstrosity/img/treeshaker-chimera.webp#right|850)  

```statblock
"name": "Treeshaker Chimera (TBVI)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "80"
"hit_dice": "10d12 + 20"
"modifier": !!int "0"
"stats":
  - !!int "19"
  - !!int "10"
  - !!int "14"
  - !!int "7"
  - !!int "14"
  - !!int "10"
"speed": "40 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": ""
"cr": "7"
"traits":
  - "desc": "The chimera can’t be surprised, and it has [[advantage-xphb|Advantage]] on saving throws against being knocked [[conditions#Unconscious|unconscious]]."
    "name": "Multiheaded"
  - "desc": "The chimera has [[advantage-xphb|Advantage]] on Wisdom (Perception) checks that rely on hearing or smell."
    "name": "Keen Hearing and Smell"
"actions":
  - "desc": "The chimera makes three attacks: its lion head uses its bite, its wolf head uses its bite, and its antelope head uses its gore attack."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 30 (4d12 + 4) piercing damage. If the target is a Medium or smaller creature, it is [[conditions#Grappled|grappled]] (escape DC 17). Until this grapple ends, the target is [[conditions#Restrained|restrained]], and the head grappling the target can't bite another target."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 21 (4d8 + 4) piercing damage."
    "name": "Gore"
  - "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one [[conditions#Prone|prone]] creature. Hit: 20 (3d10 + 4) bludgeoning damage."
    "name": "Hoof"
"source":
  - "TBVI"
"image": "Compendium/bestiary/monstrosity/token/treeshaker-chimera-tbvi.webp"
```
^statblock
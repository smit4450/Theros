---
title: Prescient Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvi
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Prescient Chimera"]
---
# Prescient Chimera
*Source: Theros Bestiary TBVI*  

The prescient chimera has the head and wings of an owl, the body of a lion, and the tail of a dragon.

![Prescient Chimera](https://img.scryfall.com/cards/art_crop/front/f/9/f9342aba-e3aa-4210-ad72-e609c7c027b8.jpg?1562838669#right)  

```statblock
"name": "Prescient Chimera (TBVI)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "12"
"ac_class": "natural armor"
"hp": !!int "72"
"hit_dice": "12d10 + 12"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "15"
  - !!int "13"
  - !!int "2"
  - !!int "12"
  - !!int "7"
"speed": "50 ft., fly 60 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+4"
"senses": "darkvision 120 ft., passive Perception 10"
"languages": ""
"cr": "1"
"traits":
  - "desc": "The chimera doesn't provoke opportunity attacks when it flies out of an enemy's reach."
    "name": "Flyby"
  - "desc": "The chimera has advantage on Wisdom (Perception) checks that rely on hearing or sight."
    "name": "Keen Hearing and Sight"
  - "desc": "If the lion moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the lion can make one bite attack against it as a bonus action."
    "name": "Pounce"
"actions":
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."
    "name": "Claws"
"source":
  - "TBVI"
"image": "Compendium/bestiary/monstrosity/token/prescient-chimera-tbvi.webp"
```
^statblock
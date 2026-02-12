---
title: Shrieking Titan Head
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvx
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Shrieking Titan Head"]
---
# Shrieking Titan Head
*Source: Theros Bestiary TBVX*  

The hydra is a reptilian horror with a crocodilian body and multiple heads on long, serpentine necks. Although its heads can be severed, the hydra magically regrows them in short order.

![Shrieking Titan Head](https://img.scryfall.com/cards/art_crop/front/4/4/44ef6754-b611-4e52-a04b-dc2c794d2cb8.jpg?1562639773#right)  

```statblock
"name": "Shrieking Titan Head (TBVX)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "88"
"hit_dice": "8d12 + 40"
"modifier": !!int "1"
"stats":
  - !!int "22"
  - !!int "12"
  - !!int "20"
  - !!int "2"
  - !!int "9"
  - !!int "8"
"speed": "20 ft., swim 20 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "When the head dies, the number of heads the hydra would regain from it is three instead of two."
    "name": "Elite Head"
"actions":
  - "desc": "The head makes two attacks: one with its bite and one with its shriek."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 6 piercing damage and 5 (2d4) necrotic damage."
    "name": "Bite"
  - "desc": "Each non-head creature within 30 ft. of the head that can hear it takes 3 (1d6) psychic damage."
    "name": "Shriek"
"source":
  - "TBVX"
"image": "Compendium/bestiary/monstrosity/token/shrieking-titan-head-tbvx.webp"
```
^statblock
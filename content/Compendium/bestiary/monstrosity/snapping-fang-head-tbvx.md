---
title: Snapping Fang Head
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvx
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Snapping Fang Head"]
---
# Snapping Fang Head
*Source: Theros Bestiary TBVX*  

The hydra is a reptilian horror with a crocodilian body and multiple heads on long, serpentine necks. Although its heads can be severed, the hydra magically regrows them in short order.

![Snapping Fang Head](https://img.scryfall.com/cards/art_crop/front/1/1/11decc7a-58e7-43f3-acc5-9ec94cce858d.jpg?1562639681#right)  

```statblock
"name": "Snapping Fang Head (TBVX)"
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
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": ""
"cr": "5"
"traits":
  - "desc": "When the head dies, the number of heads the hydra would regain from it is three instead of two."
    "name": "Elite Head"
"actions":
  - "desc": "The head makes two attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 6 piercing damage and 5 (2d4) fire damage."
    "name": "Bite"
"source":
  - "TBVX"
"image": "Compendium/bestiary/monstrosity/token/snapping-fang-head-tbvx.webp"
```
^statblock
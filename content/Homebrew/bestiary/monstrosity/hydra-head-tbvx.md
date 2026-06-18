---
title: Hydra Head
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvx
- monster/cr/2
- monster/size/h
- monster/type/monstrosity
statblock: inline
aliases: ["Hydra Head"]
---
# Hydra Head
*Source: Theros Bestiary TBVX*  

The hydra is a reptilian horror with a crocodilian body and multiple heads on long, serpentine necks. Although its heads can be severed, the hydra magically regrows them in short order.

![Hydra Head](Homebrew/bestiary/monstrosity/img/hydra-head.webp#right)  

```statblock
"name": "Hydra Head (TBVX)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "33"
"hit_dice": "3d12 + 15"
"modifier": !!int "1"
"stats":
  - !!int "20"
  - !!int "12"
  - !!int "20"
  - !!int "2"
  - !!int "10"
  - !!int "7"
"speed": "20 ft., swim 20 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": ""
"cr": "2"
"actions":
  - "desc": "Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) piercing damage."
    "name": "Bite"
"source":
  - "TBVX"
"image": "Homebrew/bestiary/monstrosity/token/hydra-head-tbvx.webp"
```
^statblock
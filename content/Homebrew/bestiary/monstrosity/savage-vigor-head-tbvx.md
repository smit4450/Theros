---
title: Savage Vigor Head
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvx
- monster/cr/3
- monster/size/h
- monster/type/monstrosity
statblock: inline
aliases: ["Savage Vigor Head"]
---
# Savage Vigor Head
*Source: Theros Bestiary TBVX*  

The hydra is a reptilian horror with a crocodilian body and multiple heads on long, serpentine necks. Although its heads can be severed, the hydra magically regrows them in short order.

![Savage Vigor Head](Homebrew/bestiary/monstrosity/img/savage-vigor-head.webp#right)  

```statblock
"name": "Savage Vigor Head (TBVX)"
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
"cr": "3"
"traits":
  - "desc": "When the head dies, the number of heads the hydra would regain from it is three instead of two."
    "name": "Elite Head"
"actions":
  - "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 11 (1d10 + 6) piercing damage."
    "name": "Bite"
"source":
  - "TBVX"
"image": "Homebrew/bestiary/monstrosity/token/savage-vigor-head-tbvx.webp"
```
^statblock
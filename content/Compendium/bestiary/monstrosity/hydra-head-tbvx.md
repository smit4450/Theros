---
title: Hydra Head
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvx
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Hydra Head"]
---
# Hydra Head
*Source: Theros Bestiary TBVX*  

The hydra is a reptilian horror with a crocodilian body and multiple heads on long, serpentine necks. Although its heads can be severed, the hydra magically regrows them in short order.

![Hydra Head](https://img.scryfall.com/cards/art_crop/front/2/7/27d772a9-7542-4ffe-9cd4-e144d129f342.jpg?1562639721#right)  

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
"image": "Compendium/bestiary/monstrosity/token/hydra-head-tbvx.webp"
```
^statblock
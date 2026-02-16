---
title: Nemesis of Mortals
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Nemesis of Mortals"]
---
# Nemesis of Mortals
*Source: Theros Bestiary TBVIV*  

A gigantic 6-eyed snake with a mouth chock-full of fangs.

![Nemesis of Mortals](Compendium/bestiary/monstrosity/img/nemesis-of-mortals.webp#right|850)  

```statblock
"name": "Nemesis of Mortals (TBVIV)"
"size": "Huge"
"type": "monstrosity"
"subtype": "snake"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "75"
"hit_dice": "5d20 + 25"
"modifier": !!int "1"
"stats":
  - !!int "20"
  - !!int "12"
  - !!int "20"
  - !!int "1"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+2"
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., passive Perception 10"
"languages": ""
"cr": "4"
"traits":
  - "desc": "If the nemesis is reduced to 0 [[hit-points-xphb|Hit Points]], it doesn’t die or fall [[conditions#Unconscious|unconscious]]. Instead, it sheds its skin, regains 57 (5d20+5) [[hit-points-xphb|Hit Points]], and moves up to its speed without provoking opportunity attacks."
    "name": "Shed Skin (Mythic Trait; Recharges after a Short or Long Rest)"
"actions":
  - "desc": "Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 32 (5d10 + 5) piercing damage."
    "name": "Bite"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/monstrosity/token/nemesis-of-mortals-tbviv.webp"
```
^statblock
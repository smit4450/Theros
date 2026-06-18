---
title: Nessian Asp
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbviv
- monster/cr/2
- monster/size/m
- monster/type/beast
statblock: inline
aliases: ["Nessian Asp"]
---
# Nessian Asp
*Source: Theros Bestiary TBVIV*  

<small><blockquote>It’s not the two heads you should fear. It’s the four fangs.</blockquote></small>

![Nessian Asp](Homebrew/bestiary/beast/img/nessian-asp.webp#right|850)  

```statblock
"name": "Nessian Asp (TBVIV)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "25"
"hit_dice": "5d8 + 5"
"modifier": !!int "4"
"stats":
  - !!int "10"
  - !!int "18"
  - !!int "13"
  - !!int "2"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., climb 30 ft., swim 30 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+2"
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., passive Perception 10"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The asp has [[advantage-xphb|Advantage]] on Wisdom (Perception) checks and on saving throws against being [[conditions#Blinded|blinded]], [[conditions#Charmed|charmed]], [[conditions#Deafened|deafened]], [[conditions#Frightened|frightened]], [[conditions#Stunned|stunned]], or knocked [[conditions#Unconscious|unconscious]]."
    "name": "Two Heads"
  - "desc": "If the asp is reduced to 0 [[hit-points-xphb|Hit Points]], it doesn’t die or fall [[conditions#Unconscious|unconscious]]. Instead, it sheds its skin, regains 19 (4d8+1) [[hit-points-xphb|Hit Points]], and moves up to its speed without provoking opportunity attacks."
    "name": "Shed Skin (Mythic Trait; Recharges after a Short or Long Rest)."
"actions":
  - "desc": "The asp makes two bite attacks on either one or two targets that are within 5 feet of each other."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +2 to hit, reach 10 ft., one target. Hit: 6 (1d4 + 4) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one."
    "name": "Bite"
"source":
  - "TBVIV"
"image": "Homebrew/bestiary/beast/token/nessian-asp-tbviv.webp"
```
^statblock
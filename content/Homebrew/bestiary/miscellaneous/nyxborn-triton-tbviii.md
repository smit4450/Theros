---
title: Nyxborn Triton
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbviii
- monster/cr/3
- monster/size/m
- monster/type/miscellaneous
statblock: inline
aliases: ["Nyxborn Triton"]
---
# Nyxborn Triton
*Source: Theros Bestiary TBVIII*  

<blockquote><small>"He is Thassa's. I could not sway him." - Kiora</small></blockquote>
A triton created from nyx by Thassa.

![Nyxborn Triton](Homebrew/bestiary/miscellaneous/img/nyxborn-triton.webp#right)  

```statblock
"name": "Nyxborn Triton (TBVIII)"
"size": "Medium"
"type": "3rd-level transmutation humanoid"
"subtype": "triton"
"alignment": "Neutral Evil"
"ac": !!int "14"
"hp": !!int "30"
"hit_dice": "5d8 + 10"
"modifier": !!int "3"
"stats":
  - !!int "11"
  - !!int "16"
  - !!int "14"
  - !!int "10"
  - !!int "15"
  - !!int "11"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[[skills#Nature|Nature]]"
    "desc": "+4"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"damage_resistances": "cold"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": "Common, Primordial"
"cr": "3"
"traits":
  - "desc": "The triton can breathe air and water."
    "name": "Amphibious"
  - "desc": "The triton’s spellcasting ability is Wisdom (spell save DC 12). It can innately cast the following spells, requiring no material components: 1/day each: [[fog-cloud-xphb|Fog Cloud]], [[gust-of-wind-xphb|Gust Of Wind]]"
    "name": "Innate Spellcasting"
  - "desc": "The triton's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The triton can take the Disengage or Hide actions as a bonus action on each of its turns."
    "name": "Nimble Escape"
  - "desc": "In addition to being a creature, the triton is a 3rd-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The triton glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (2d4 + 0) piercing damage."
    "name": "Anchor Pierce"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (2d4 + 0) bludgeoning damage."
    "name": "Anchor Bash"
"source":
  - "TBVIII"
"image": "Homebrew/bestiary/miscellaneous/token/nyxborn-triton-tbviii.webp"
```
^statblock
---
title: Nighthowler
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxiii
- monster/cr/5
- monster/size/m
- monster/type/miscellaneous
statblock: inline
aliases: ["Nighthowler"]
---
# Nighthowler
*Source: Theros Bestiary TBVXXIII*  

The nighthowler is a merging of several undead spirits into one. Its form is a chimeric conglomeration of those souls. It absorbs the souls of those it kills with its shadowy breath.

![Nighthowler](Homebrew/bestiary/miscellaneous/img/nighthowler.webp#right)  

```statblock
"name": "Nighthowler (TBVXXIII)"
"size": "Medium"
"type": "3rd-level transmutation undead"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"hp": !!int "70"
"hit_dice": "10d8 + 30"
"modifier": !!int "1"
"stats":
  - !!int "17"
  - !!int "12"
  - !!int "17"
  - !!int "6"
  - !!int "13"
  - !!int "6"
"speed": "30 ft., fly 30 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
"damage_resistances": "necrotic"
"damage_immunities": "fire"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": ""
"cr": "5"
"traits":
  - "desc": "The nighthowler's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "In addition to being a creature, the nighthowler is a 3rd-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The nighthowler glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
  - "desc": "While in sunlight, the nighthowler has [[disadvantage-xphb|Disadvantage]] on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
    "name": "Sunlight Sensitivity"
"actions":
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 7 (1d8 + 3) piercing damage plus 7 (2d6) necrotic damage."
    "name": "Bite"
  - "desc": "The nighthowler exhales shadowy fire in a 15-foot cone. Each creature in that area must make a DC 12 Dexterity saving throw, taking 21 (6d6) necrotic damage on a failed save, or half as much damage on a successful one. A humanoid reduced to 0 [[hit-points-xphb|Hit Points]] by this damage dies, and that creature's spirit leaves its body and becomes part of the nighthowler. The nighthowler's Strength is increased by 1, and its [[hit-points-xphb|Hit Points]] and maximum [[hit-points-xphb|Hit Points]] are increased by 4 (1d8)."
    "name": "Shadow Breath (Recharge 5-6)"
"source":
  - "TBVXXIII"
"image": "Homebrew/bestiary/miscellaneous/token/nighthowler-tbvxxiii.webp"
```
^statblock
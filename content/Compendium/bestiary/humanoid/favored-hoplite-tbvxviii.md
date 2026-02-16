---
title: Favored Hoplite
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxviii
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Favored Hoplite"]
---
# Favored Hoplite
*Source: Theros Bestiary TBVXVIII*  



![Favored Hoplite](https://img.scryfall.com/cards/art_crop/front/2/5/251015ed-9408-4941-894a-158551ed2613.jpg?1562815791#right)  

```statblock
"name": "Favored Hoplite (TBVXVIII)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "breastplate, shield"
"hp": !!int "6"
"hit_dice": "1d8 + 2"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "16"
  - !!int "14"
  - !!int "11"
  - !!int "14"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "strength": !!int "5"
  - "dexterity": !!int "5"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "4"
"traits":
  - "desc": "While the hoplite is holding a spear, other creatures provoke an opportunity attack from the hoplite when they move within 5 feet of it. When the hoplite hits a creature with an opportunity attack using its spear, the creature takes an extra 4 (1d8) piercing damage, and the creature’s speed becomes 0 for the rest of the turn."
    "name": "Hold the Line"
"actions":
  - "desc": "The hoplite makes three melee attacks or two ranged attacks."
    "name": "Multiattack"
  - "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft., or range 20/60 ft., one target. Hit: 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing damage if used with two hands to make a melee attack."
    "name": "Spear"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 13 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Shield Bash"
"reactions":
  - "desc": "Whenever a spell targets the hoplite, that spell's caster chooses whether the following happens: - Until the end of combat, the hoplite gains a +1 bonus to damage rolls and Strength and Dexterity checks, and it gains 4 (1d8) temporary [[hit-points-xphb|Hit Points]]. The hoplite becomes immune to all types of damage until its next turn."
    "name": "Heroic"
"source":
  - "TBVXVIII"
"image": "Compendium/bestiary/humanoid/token/favored-hoplite-tbvxviii.webp"
```
^statblock
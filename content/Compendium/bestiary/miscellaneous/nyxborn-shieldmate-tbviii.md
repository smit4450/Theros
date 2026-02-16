---
title: Nyxborn Shieldmate
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviii
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Nyxborn Shieldmate"]
---
# Nyxborn Shieldmate
*Source: Theros Bestiary TBVIII*  

<blockquote><small>In Meletis, the walls have ears. In Akros, they have blades.</small></blockquote>
An Akroan mosaic of a hoplite springs to life.

![Nyxborn Shieldmate](Compendium/bestiary/miscellaneous/img/nyxborn-shieldmate.webp#right|850)  

```statblock
"name": "Nyxborn Shieldmate (TBVIII)"
"size": "Medium"
"type": "1st-level transmutation human"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "breastplate, shield"
"hp": !!int "48"
"hit_dice": "8d8 + 16"
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
"cr": "1"
"traits":
  - "desc": "While the shieldmate is holding a spear, other creatures provoke an opportunity attack from the shieldmate when they move within 5 feet of it. When the shieldmate hits a creature with an opportunity attack using its spear, the creature takes an extra 4 (1d8) piercing damage, and the creature’s speed becomes 0 for the rest of the turn."
    "name": "Hold the Line"
  - "desc": "The shieldmate's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "In addition to being a creature, the shieldmate is a 1st-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The shieldmate glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "The shieldmate makes three melee attacks or two ranged attacks."
    "name": "Multiattack"
  - "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft., or range 20/60 ft., one target. Hit: 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing damage if used with two hands to make a melee attack."
    "name": "Spear"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 13 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Shield Bash"
"source":
  - "TBVIII"
"image": "Compendium/bestiary/miscellaneous/token/nyxborn-shieldmate-tbviii.webp"
```
^statblock
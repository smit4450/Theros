---
title: Reckless Reveler
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxiii
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Reckless Reveler"]
---
# Reckless Reveler
*Source: Theros Bestiary TBVXIII*  

<small><blockquote>“The gods of Theros are born of the expectations and beliefs of mortals. If I have found godhood, what does that say about their true desires?”

—Xenagos, god of revels</blockquote></small>

![Reckless Reveler](https://img.scryfall.com/cards/art_crop/front/1/8/188adefd-a808-4991-80be-53249c24df8f.jpg?1593092327#right)  

```statblock
"name": "Reckless Reveler (TBVXIII)"
"size": "Medium"
"type": "fey"
"subtype": "satyr"
"alignment": "Chaotic Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "5"
"hit_dice": "1d8 + 1"
"modifier": !!int "3"
"stats":
  - !!int "15"
  - !!int "16"
  - !!int "13"
  - !!int "12"
  - !!int "10"
  - !!int "16"
"speed": "40 ft."
"skillsaves":
  - "name": "[Acrobatics](Compendium/rules/skills.md#Acrobatics)"
    "desc": "+5"
  - "name": "[Performance](Compendium/rules/skills.md#Performance)"
    "desc": "+7"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": "Common, Sylvan"
"cr": "2"
"traits":
  - "desc": "While the satyr bears a lit torch, its ram attacks deal an extra 4 (1d8) fire damage per lit torch."
    "name": "Careless Ramming"
  - "desc": "If the celebrant moves at least 15 feet straight toward a target and then hits it with its ram attack on the same turn, the target takes an extra 5 (2d4) slashing damage. If the target is a creature, it must succeed on a DC 12 Strength saving throw or be knocked [prone](Compendium/rules/conditions.md#Prone)."
    "name": "Charge"
  - "desc": "The satyr has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "Whenever the celebrant makes a long or high jump, it can cover an additional 1d8 feet, even when making a standing jump. This extra distance costs movement as normal."
    "name": "Mirthful Leaps"
  - "desc": "The celebrant deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "Magic can’t put the satyr to sleep."
    "name": "Sleepless Reveler"
  - "desc": "As a bonus action, the reveler can ignite itself. Any objects within 5 feet also ignite, and the reveler drops to 0 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Hedonism"
"actions":
  - "desc": "The satyr makes two ram attacks or two torch attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) bludgeoning damage."
    "name": "Ram"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 12 (2d8 + 3) fire damage."
    "name": "Torch"
"source":
  - "TBVXIII"
"image": "Compendium/bestiary/fey/token/reckless-reveler-tbvxiii.webp"
```
^statblock
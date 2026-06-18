---
title: Returned Reveler
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxii
- monster/cr/2
- monster/size/m
- monster/type/undead
statblock: inline
aliases: ["Returned Reveler"]
---
# Returned Reveler
*Source: Theros Bestiary TBVXXII*  

<small><blockquote>The flesh is dead and the life forgotten, but old habits persist.</blockquote></small>

![Returned Reveler](Homebrew/bestiary/undead/img/returned-reveler.webp#right)  

```statblock
"name": "Returned Reveler (TBVXXII)"
"size": "Medium"
"type": "undead fey"
"subtype": "returned, satyr"
"alignment": "Chaotic Neutral"
"ac": !!int "13"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "1"
"stats":
  - !!int "13"
  - !!int "13"
  - !!int "16"
  - !!int "11"
  - !!int "10"
  - !!int "11"
"speed": "40 ft."
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+3"
  - "name": "[[skills#Performance|Performance]]"
    "desc": "+7"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+3"
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "passive Perception 10"
"languages": "Common, Sylvan"
"cr": "2"
"traits":
  - "desc": "While the satyr bears a lit torch, its ram attacks deal an extra 4 (1d8) fire damage per lit torch."
    "name": "Careless Ramming"
  - "desc": "If the celebrant moves at least 15 feet straight toward a target and then hits it with its ram attack on the same turn, the target takes an extra 5 (2d4) slashing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Charge"
  - "desc": "As a bonus action, the reveler can ignite itself. Any objects within 5 feet also ignite, and the reveler drops to 0 [[hit-points-xphb|Hit Points]]."
    "name": "Hedonism"
  - "desc": "The satyr has [[advantage-xphb|Advantage]] on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "Whenever the celebrant makes a long or high jump, it can cover an additional 1d8 feet, even when making a standing jump. This extra distance costs movement as normal."
    "name": "Mirthful Leaps"
  - "desc": "The Returned doesn't need food or sleep. It thinks and speaks and even feels emotions based on its new experiences, but given its circumstances, those emotions tend to be muted."
    "name": "Returned Nature"
  - "desc": "The celebrant deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "Magic can’t put the satyr to sleep."
    "name": "Sleepless Reveler"
  - "desc": "The Returned has [[advantage-xphb|Advantage]] on saving throws against any effect that turns undead."
    "name": "Turn Resistance"
  - "desc": "The Returned is immune to any effect that would sense its emotions or read its thoughts. Wisdom (Insight) checks to ascertain the Returned’s intentions or sincerity are made with [[disadvantage-xphb|Disadvantage]]."
    "name": "Unreadable Face"
"actions":
  - "desc": "The satyr makes two ram attacks or two torch attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) bludgeoning damage."
    "name": "Ram"
  - "desc": "_Melee Weapon Attack:_ +3 to hit, reach 5 ft., one target. _Hit:_ 10 (2d8 + 1) fire damage."
    "name": "Torch"
"source":
  - "TBVXXII"
"image": "Homebrew/bestiary/undead/token/returned-reveler-tbvxxii.webp"
```
^statblock
---
title: Oracle of Bones
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxx
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Oracle of Bones"]
---
# Oracle of Bones
*Source: Theros Bestiary TBVXX*  

<b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more cultists might be nearby who will pay tribute to the oracle.
<li>A quest goal might involve helping the oracle as an advance payment for its service.
<li>A quest goal might involve vanquishing the oracle.
<li>A quest goal might involve protecting a creature that is near the oracle.

![Oracle of Bones](Compendium/bestiary/humanoid/img/oracle-of-bones.webp#right)  

```statblock
"name": "Oracle of Bones (TBVXX)"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "blessings of the gods"
"hp": !!int "5"
"hit_dice": "1d8 + 1"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "14"
  - !!int "13"
  - !!int "13"
  - !!int "16"
  - !!int "15"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "5"
  - "charisma": !!int "4"
"skillsaves":
  - "name": "[Insight](Compendium/rules/skills.md#Insight)"
    "desc": "+5"
  - "name": "[Persuasion](Compendium/rules/skills.md#Persuasion)"
    "desc": "+4"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+5"
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": "Celestial, Common, Minotaur"
"cr": "1"
"traits":
  - "desc": "The oracle has advantage on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "While the oracle is wearing no armor and wielding no shield, its AC includes its Wisdom modifier. In addition, a creature that hits the oracle with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Just the oracle seeks insights from interpreting the divine, so too do the gods occasionally seek to manipulate the world through the oracle. Sometimes the gods might speak directly, be it with dramatic manifestations or direct possession of the oracle. Although the gods' words might be steeped in metaphors, should they wish to make their intentions clear, they often find dramatic ways to make their thoughts known."
    "name": "Divine Influence"
  - "desc": "Immediately after the oracle uses the Dash action on its turn and moves at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "The oracle possesses unparalleled experience in divining godly whims from cryptic visions and mundane forces"
    "name": "Interpreter of Signs"
  - "desc": "The oracle of bones is a 9th-level spellcaster. The oracle of bones's spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). The oracle of bones has the following cleric spells prepared: Cantrip (at will): _guidance_, _sacred flame_, _spare the dying_ 2nd level (3 slots): _augury_ 4th level (3 slots): _divination_ 5th level (1 slots): _commune_"
    "name": "Spellcasting"
"actions":
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6 + 3) piercing damage, and the oracle can use a bonus action to attempt to shove that target with its horns. The target must be within 5 feet of the oracle and no more than one size larger than it. Unless the target succeeds on a DC 13 Strength saving throw, the oracle pushes it up to 10 feet away from the oracle."
    "name": "Horns"
"reactions":
  - "desc": "When the oracle or a creature it can see makes an attack roll, a saving throw, or an ability check, the oracle can cause the roll to be made with advantage or disadvantage."
    "name": "Divine Insight (3/Day)"
  - "desc": "Immediately after initiative rolls in which the oracle participates, it demands tribute from a creature it can see. That creature may bow, genuflect, salute, or perform a similar gesture as a bonus action. If tribute is paid: Until the end of combat, the oracle gains a +2 bonus to damage rolls and Strength and Dexterity checks, and 9 (2d8) temporary hit points. If tribute isn't paid: The oracle casts a _sacred flame_ on that creature."
    "name": "Demand Tribute"
"source":
  - "TBVXX"
"image": "Compendium/bestiary/humanoid/token/oracle-of-bones-tbvxx.webp"
```
^statblock
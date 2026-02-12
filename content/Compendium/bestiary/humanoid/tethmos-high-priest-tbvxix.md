---
title: Tethmos High Priest
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxix
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Tethmos High Priest"]
---
# Tethmos High Priest
*Source: Theros Bestiary TBVXIX*  

<small><blockquote>“Death is tyranny. Like all tyranny, it must be opposed.”</blockquote></small>

![Tethmos High Priest](https://img.scryfall.com/cards/art_crop/front/d/9/d901b9d7-6af9-40ce-afb7-d3c9f9143c18.jpg?1593095373#right)  

```statblock
"name": "Tethmos High Priest (TBVXIX)"
"size": "Medium"
"type": "humanoid"
"subtype": "leonin"
"alignment": "Lawful Evil"
"ac": !!int "11"
"ac_class": "padded"
"hp": !!int "126"
"hit_dice": "18d8 + 54"
"modifier": !!int "0"
"stats":
  - !!int "15"
  - !!int "10"
  - !!int "16"
  - !!int "11"
  - !!int "15"
  - !!int "13"
"speed": "35 ft."
"saves":
  - "constitution": !!int "5"
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+3"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+2"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Common, Leonin, Any one language"
"cr": "3"
"traits":
  - "desc": "As a bonus action, the priest can let out an especially menacing roar. Creatures of it chooses within 10 feet of itself that can hear it must succeed on a DC 13 Wisdom saving throw or become frightened of it until the end of the priest's next turn."
    "name": "Daunting Roar (Recharges after a Short or Long Rest)"
  - "desc": "Whenever the priest becomes targeted by a spell, that spell's caster chooses whether the priest may use a bonus action to cast _raise dead_ targeting a leonin, requiring no components or spell slots."
    "name": "Heroic"
  - "desc": "The priest is a 9th-level spellcaster. The priest's spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). The priest has the following cleric spells prepared: Cantrip (at will): _light_, _mending_, _sacred flame_, _spare the dying_ 1st level (4 slots): _divine favor_, _guiding bolt_, _healing word_, _shield of faith_ 2nd level (3 slots): _lesser restoration_, _magic weapon_, _prayer of healing_, _silence_, _spiritual weapon_ 3rd level (3 slots): _beacon of hope_, _crusader's mantle_, _dispel magic_, _revivify_, _spirit guardians_, _wall of water_ 4th level (3 slots): _banishment_, _freedom of movement_, _guardian of faith_, _stoneskin_ 5th level (1 slots): _flame strike_, _mass cure wounds_, _hold monster_"
    "name": "Spellcasting"
"actions":
  - "desc": "The priest makes two melee attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."
    "name": "Claws"
  - "desc": "_Melee Weapon Attack:_ +6 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) bludgeoning damage."
    "name": "Quarterstaff"
"reactions":
  - "desc": "The priest grants a +10 bonus to an attack roll made by itself or another creature within 30 feet of it. The priest can make this choice after the roll is made but before it hits or misses."
    "name": "Guided Strike (1/Rest)"
"source":
  - "TBVXIX"
"image": "Compendium/bestiary/humanoid/token/tethmos-high-priest-tbvxix.webp"
```
^statblock
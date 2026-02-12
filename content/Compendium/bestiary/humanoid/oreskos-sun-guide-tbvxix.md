---
title: Oreskos Sun Guide
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxix
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Oreskos Sun Guide"]
---
# Oreskos Sun Guide
*Source: Theros Bestiary TBVXIX*  

<blockquote><small>“Let the humans have their pantheon. We need no gods to thrive. Even a mortal such as I can capture a part of the sun’s power.”</small></blockquote>

![Oreskos Sun Guide](Compendium/bestiary/humanoid/img/oreskos-sun-guide.webp#right|850)  

```statblock
"name": "Oreskos Sun Guide (TBVXIX)"
"size": "Medium"
"type": "humanoid"
"subtype": "leonin"
"alignment": "Any alignment"
"ac": !!int "15"
"hp": !!int "42"
"hit_dice": "7d8 + 14"
"modifier": !!int "3"
"stats":
  - !!int "11"
  - !!int "17"
  - !!int "15"
  - !!int "10"
  - !!int "14"
  - !!int "10"
"speed": "45 ft."
"skillsaves":
  - "name": "[Survival](Compendium/rules/skills.md#Survival)"
    "desc": "+4"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Common, Leonin"
"cr": "2"
"traits":
  - "desc": "As a bonus action, the sun guide can let out an especially menacing roar. Creatures it chooses within 10 feet of itself that can hear it must succeed on a DC 12 Wisdom saving throw or become frightened of it until the end of its next turn."
    "name": "Daunting Roar (Recharges after a Short or Long Rest)"
  - "desc": "At the beginning of the sun guide's turn, if the sun cast light on it as it was bowing at any point since the sun guide's last turn, it regains 11 (2d10) hit points."
    "name": "Inspired"
  - "desc": "While the sun guide isn't wearing armor, its armor class includes its Wisdom modifier."
    "name": "Unarmored Defense"
"actions":
  - "desc": "The sun guide makes two attacks with its Sun Bolt. It can then use its Radiant Swathe, if available."
    "name": "Multiattack"
  - "desc": "_Ranged Spell Attack:_ +2 to hit, range 30 ft., one target. _Hit:_ 4 (1d4 + 2) radiant damage."
    "name": "Sun Bolt"
  - "desc": "The sun guide swishes its hands through the air, creating a streak of white-hot light. Each creature in a 15-foot cone originating from the sun guide must succeed on a DC 13 Dexterity saving throw or take 14 (4d6) radiant damage."
    "name": "Radiant Swathe (Recharge 5-6)"
  - "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4 + 0) slashing damage."
    "name": "Claws"
  - "desc": "The sun guide bows down to a sun it can see. It remains in this position until a different action is used."
    "name": "Bow"
"source":
  - "TBVXIX"
"image": "Compendium/bestiary/humanoid/token/oreskos-sun-guide-tbvxix.webp"
```
^statblock
---
title: Leonin Iconoclast
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxix
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Leonin Iconoclast"]
---
# Leonin Iconoclast
*Source: Theros Bestiary TBVXIX*  

<blockquote><small>“The stars belong in the night sky. This is our world, and we are our own masters.”</small></blockquote>

![Leonin Iconoclast](Compendium/bestiary/humanoid/img/leonin-iconoclast.webp#right|850)  

```statblock
"name": "Leonin Iconoclast (TBVXIX)"
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
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": "Common, Leonin"
"cr": "2"
"traits":
  - "desc": "As a bonus action, the iconoclast can let out an especially menacing roar. Creatures it chooses within 10 feet of itself that can hear it must succeed on a DC 12 Wisdom saving throw or become [frightened](Compendium/rules/conditions.md#Frightened) of it until the end of its next turn."
    "name": "Daunting Roar (Recharges after a Short or Long Rest)"
  - "desc": "Whenever the iconoclast becomes targeted by a spell, that spell's caster chooses whether the iconoclast may use a bonus action to cast [Dispel Magic](Compendium/spells/dispel-magic-xphb.md), requiring no components or spell slots."
    "name": "Heroic"
  - "desc": "While the iconoclast isn't wearing armor, its armor class includes its Wisdom modifier."
    "name": "Unarmored Defense"
"actions":
  - "desc": "The iconoclast makes two attacks with its claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4 + 0) slashing damage."
    "name": "Claws"
"source":
  - "TBVXIX"
"image": "Compendium/bestiary/humanoid/token/leonin-iconoclast-tbvxix.webp"
```
^statblock
---
title: Vanguard of Brimaz
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxix
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Vanguard of Brimaz"]
---
# Vanguard of Brimaz
*Source: Theros Bestiary TBVXIX*  

<blockquote><small>"The humans and their gods never blessed me. Only the pride deserves my allegiance."</small></blockquote>

![Vanguard of Brimaz](https://img.scryfall.com/cards/art_crop/front/a/d/adb38717-97d5-4763-9e6c-46251df704ed.jpg?1578451703#right)  

```statblock
"name": "Vanguard of Brimaz (TBVXIX)"
"size": "Medium"
"type": "humanoid"
"subtype": "leonin"
"alignment": "Any alignment"
"ac": !!int "10"
"hp": !!int "18"
"hit_dice": "3d8 + 6"
"modifier": !!int "1"
"stats":
  - !!int "14"
  - !!int "12"
  - !!int "14"
  - !!int "10"
  - !!int "13"
  - !!int "11"
"speed": "35 ft."
"skillsaves":
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+4"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+2"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": "Common, Leonin"
"cr": "1"
"traits":
  - "desc": "As a bonus action, the vanguard can let out an especially menacing roar. Creatures it chooses within 10 feet of itself that can hear it must succeed on a DC 12 Wisdom saving throw or become [frightened](Compendium/rules/conditions.md#Frightened) of it until the end of its next turn."
    "name": "Daunting Roar (Recharges after a Short or Long Rest)"
  - "desc": "The vanguard has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against being [charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened), [grappled](Compendium/rules/conditions.md#Grappled), or [restrained](Compendium/rules/conditions.md#Restrained) while it is within 5 feet of at least one ally."
    "name": "Formation Tactics"
  - "desc": "Whenever the vanguard becomes targeted by a spell, that spell's caster chooses whether the vanguard summons a **soldier of Brimaz**. The summoned soldier appears in an unoccupied space that the vanguard can see within 60 feet of itself, and it acts as an ally to its summoner and its allies."
    "name": "Heroic"
  - "desc": "The vanguard can't be surprised."
    "name": "Vigilant"
"actions":
  - "desc": "The vanguard makes two melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) bludgeoning damage."
    "name": "Mace"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."
    "name": "Claws"
"source":
  - "TBVXIX"
"image": "Compendium/bestiary/humanoid/token/vanguard-of-brimaz-tbvxix.webp"
```
^statblock
---
title: Battlefield Thaumaturge
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxvi
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Battlefield Thaumaturge"]
---
# Battlefield Thaumaturge
*Source: Theros Bestiary TBVXVI*  



![Battlefield Thaumaturge](Compendium/bestiary/humanoid/img/battlefield-thaumaturge.webp#right|850)  

```statblock
"name": "Battlefield Thaumaturge (TBVXVI)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "12"
"hp": !!int "45"
"hit_dice": "9d8 + 9"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "15"
  - !!int "12"
  - !!int "18"
  - !!int "13"
  - !!int "12"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "6"
  - "wisdom": !!int "3"
"skillsaves":
  - "name": "[Arcana](Compendium/rules/skills.md#Arcana)"
    "desc": "+6"
  - "name": "[History](Compendium/rules/skills.md#History)"
    "desc": "+6"
"senses": "passive Perception 10"
"languages": "Common, Any four languages"
"cr": "7"
"traits":
  - "desc": "The thaumaturge is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). It has the following wizard spells prepared: • Cantrips (at will): fire bolt, light, mage hand, prestidigitation • 1st level (4 slots): detect magic, mage armor, magic missile, shield • 2nd level (3 slots): misty step, suggestion • 3rd level (3 slots): counterspell, fireball, fly • 4th level (3 slots): greater invisibility, ice storm • 5th level (1 slot): cone of cold"
    "name": "Spellcasting"
  - "desc": "For every creature targeted by a spell cast by a friendly creature within 30 feet of the thaumaturge (including the thaumaturge), there is a 25% chance of the caster regenerating that spell slot immediately."
    "name": "Mana-Generating Staff"
"actions":
  - "desc": "_Melee Weapon Attack:_ +2 to hit, reach 5 ft., one target. _Hit:_ 3 (1d6) bludgeoning damage."
    "name": "Quarterstaff"
"reactions":
  - "desc": "Whenever the thaumaturge is the target of a spell, that spell's caster chooses whether following happens: - Until the beginning of the thaumaturge's next turn, the thaumaturge can't be affected or detected by spells of 6th level or lower unless it wishes to be, and it has advantage on saving throws against all other spells and magical effects."
    "name": "Heroic"
"source":
  - "TBVXVI"
"image": "Compendium/bestiary/humanoid/token/battlefield-thaumaturge-tbvxvi.webp"
```
^statblock
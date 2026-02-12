---
title: Wavecrash Triton
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvii
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Wavecrash Triton"]
---
# Wavecrash Triton
*Source: Theros Bestiary TBVVII*  

Mages spend their lives in the study and practice of magic. Good-aligned mages offer counsel to nobles and others in power.

![Wavecrash Triton](Compendium/bestiary/humanoid/img/wavecrash-triton.webp#right|850)  

```statblock
"name": "Wavecrash Triton (TBVVII)"
"size": "Medium"
"type": "humanoid"
"subtype": "triton"
"alignment": "Neutral"
"ac": !!int "12"
"hp": !!int "45"
"hit_dice": "9d8 + 9"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "14"
  - !!int "12"
  - !!int "17"
  - !!int "12"
  - !!int "12"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "6"
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[Arcana](Compendium/rules/skills.md#Arcana)"
    "desc": "+6"
  - "name": "[History](Compendium/rules/skills.md#History)"
    "desc": "+6"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Common, Primordial, Any two other languages"
"cr": "7"
"traits":
  - "desc": "The triton can breathe air and water."
    "name": "Amphibious"
  - "desc": "The triton wizard's innate spellcasting ability is Charisma (spell save DC 12, +4 to hit with spell attacks). It can innately cast the following spells, requiring no material components: 1/day each: _fog cloud_, _gust of wind_, _wall of water_"
    "name": "Innate Spellcasting"
  - "desc": "The triton is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The triton has the following wizard spells prepared: • Cantrips (at will): fire bolt, light, mage hand, prestidigitation • 1st level (4 slots): detect magic, mage armor, magic missile, shield • 2nd level (3 slots): misty step, suggestion • 3rd level (3 slots): counterspell, fireball, fly • 4th level (3 slots): greater invisibility, ice storm • 5th level (1 slot): cone of cold"
    "name": "Spellcasting"
"actions":
  - "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage."
    "name": "Dagger"
"reactions":
  - "desc": "Whenever the triton becomes targeted by a spell, that spell's caster decides whether the triton may innately cast _tsunami_ as a bonus action."
    "name": "Heroic"
"source":
  - "TBVVII"
"image": "Compendium/bestiary/humanoid/token/wavecrash-triton-tbvvii.webp"
```
^statblock
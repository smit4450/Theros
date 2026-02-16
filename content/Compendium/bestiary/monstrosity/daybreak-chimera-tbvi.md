---
title: Daybreak Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvi
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Daybreak Chimera"]
---
# Daybreak Chimera
*Source: Theros Bestiary TBVI*  

The daybreak chimera has the body and tail of a dragon, the heads of a ram-horned lion, a unicorn, and an eagle, and an eagle's wings. It favors the just.

![Daybreak Chimera](https://media.dndbeyond.com/compendium-images/moot/ds6d2NLXmv1wnY8q/06-12.png#right)  

```statblock
"name": "Daybreak Chimera (TBVI)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "160"
"hit_dice": "16d10 + 80"
"modifier": !!int "0"
"stats":
  - !!int "23"
  - !!int "10"
  - !!int "21"
  - !!int "11"
  - !!int "17"
  - !!int "16"
"speed": "40 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "2"
  - "constitution": !!int "7"
"skillsaves":
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+2"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+5"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": "Understands Celestial but can't speak"
"cr": "9"
"traits":
  - "desc": "The chimera has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on Wisdom (perception) checks that rely on sight."
    "name": "Keen Sight"
  - "desc": "The chimera can’t be surprised, and it has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against being knocked [unconscious](Compendium/rules/conditions.md#Unconscious)."
    "name": "Multiheaded"
"actions":
  - "desc": "The chimera makes five attacks: two with its claw, one with its eagle bite, one with its lion bite, and one with its horn."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d6 + 6) piercing damage."
    "name": "Eagle Bite"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (1d8 + 6) piercing damage."
    "name": "Lion Bite"
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 10 (1d8 + 6) piercing damage."
    "name": "Horn"
"source":
  - "TBVI"
"image": "Compendium/bestiary/monstrosity/token/daybreak-chimera-tbvi.webp"
```
^statblock
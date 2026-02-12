---
title: Coastline Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvi
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Coastline Chimera"]
---
# Coastline Chimera
*Source: Theros Bestiary TBVI*  

<blockquote>Seeing a chimera overhead foretells good fortune, but only because seeing one any closer foretells dismemberment.</blockquote>

The coastline chimera has the body and head of a lion, the wings of an eagle, a second ram head, and a serpent for its tail.

![Coastline Chimera](Compendium/bestiary/monstrosity/img/coastline-chimera.webp#right)  

```statblock
"name": "Coastline Chimera (TBVI)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "12"
"ac_class": "natural armor"
"hp": !!int "24"
"hit_dice": "4d10 + 4"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "15"
  - !!int "13"
  - !!int "6"
  - !!int "14"
  - !!int "6"
"speed": "60 ft., fly 60 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": ""
"cr": "2"
"traits":
  - "desc": "If the chimera moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 5 (2d4) bludgeoning damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
    "name": "Charge"
  - "desc": "The chimera can’t be surprised, and it has advantage on saving throws against being knocked unconscious."
    "name": "Multiheaded"
  - "desc": "If the chimera moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the chimera can make one bite attack against it as a bonus action."
    "name": "Pounce"
"actions":
  - "desc": "The chimera makes three attacks: one with its lion bite, one with its ram attack, and one with its snake bite."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage."
    "name": "Lion Bite"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) bludgeoning damage."
    "name": "Ram"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 5 (1d4 + 3) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one."
    "name": "Snake Bite"
"source":
  - "TBVI"
"image": "Compendium/bestiary/monstrosity/token/coastline-chimera-tbvi.webp"
```
^statblock
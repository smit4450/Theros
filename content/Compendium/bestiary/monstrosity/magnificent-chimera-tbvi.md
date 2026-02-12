---
title: Magnificent Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvi
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Magnificent Chimera"]
---
# Magnificent Chimera
*Source: Theros Bestiary TBVI*  

<blockquote><small>"I see . . . elk? And lion? And . . . teeth! A lot of teeth!" - Teraklos of Meletis</small></blockquote>
This chimera resembles a lion with a dragon's tail and the upper skull and rack of an elk.

It is based on the undead creature featured in MtG as the Loathsome Chimera. Currently, no image is available for the living version.

```statblock
"name": "Magnificent Chimera (TBVI)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "32"
"hit_dice": "4d10 + 12"
"modifier": !!int "2"
"stats":
  - !!int "19"
  - !!int "15"
  - !!int "17"
  - !!int "2"
  - !!int "10"
  - !!int "8"
"speed": "50 ft."
"senses": "passive Perception 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "If the chimera moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
    "name": "Charge"
"actions":
  - "desc": "The chimera makes two attacks: one with its bite and one with its claw."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) bludgeoning damage."
    "name": "Ram"
"source":
  - "TBVI"
"image": "Compendium/bestiary/monstrosity/token/magnificent-chimera-tbvi.webp"
```
^statblock
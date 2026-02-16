---
title: Stormchaser Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvi
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Stormchaser Chimera"]
---
# Stormchaser Chimera
*Source: Theros Bestiary TBVI*  

The stormchaser chimera has the body of a hound, the heads of a bull and an eagle, the wings of an eagle, and the hindquarters of a bull. Its bullhorns channel a powerful electric current.

![Stormchaser Chimera](https://img.scryfall.com/cards/art_crop/front/1/f/1fd9c037-64d0-4d33-b06f-4d51b1c32b1a.jpg?1573515703#right)  

```statblock
"name": "Stormchaser Chimera (TBVI)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "42"
"hit_dice": "7d8 + 14"
"modifier": !!int "1"
"stats":
  - !!int "17"
  - !!int "12"
  - !!int "14"
  - !!int "2"
  - !!int "14"
  - !!int "7"
"speed": "30 ft., fly 60 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"damage_immunities": "lightning"
"senses": "passive Perception 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "If the chimera moves at least 20 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 7 (2d6) piercing damage."
    "name": "Charge"
  - "desc": "The chimera has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on Wisdom (perception) checks that rely on sight."
    "name": "Keen Sight"
  - "desc": "The chimera can’t be surprised, and it has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against being knocked [unconscious](Compendium/rules/conditions.md#Unconscious)."
    "name": "Multiheaded"
"actions":
  - "desc": "The chimera makes two attacks: one with its gore attack and one with its beak."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6+3) piercing damage plus 5 (1d10) lightning damage."
    "name": "Gore"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."
    "name": "Beak"
"source":
  - "TBVI"
"image": "Compendium/bestiary/monstrosity/token/stormchaser-chimera-tbvi.webp"
```
^statblock
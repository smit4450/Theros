---
title: Shimmerwing Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxiii
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Shimmerwing Chimera"]
---
# Shimmerwing Chimera
*Source: Theros Bestiary TBVXXIII*  

<blockquote><small>It swims upon the winds and soars through the waves.</small></blockquote>
The shimmerwing chimera is a nyxborn creature with the body of an eel, the head and wings of an eagle, and the claws of a crab. Its presence has the power to dispel magic.

![Shimmerwing Chimera](https://img.scryfall.com/cards/art_crop/front/f/3/f3b54bea-f2c5-4000-9cbd-04c03a1d2ea2.jpg?1581479499#right)  

```statblock
"name": "Shimmerwing Chimera (TBVXXIII)"
"size": "Large"
"type": "4th-level transmutation monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "24"
"hit_dice": "4d10 + 4"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "17"
  - !!int "13"
  - !!int "2"
  - !!int "14"
  - !!int "7"
"speed": "0 ft., fly 40 ft., swim 40 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The chimera's innate spellcasting ability is Charisma (spell save DC 8, +0 to hit with spell attacks). It can innately cast the following spells, requiring no components: At will: [[dispel-magic-xphb|Dispel Magic]]"
    "name": "Innate Spellcasting"
  - "desc": "The chimera can hold its breath for 15 minutes."
    "name": "Hold Breath"
  - "desc": "The chimera's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "In addition to being a creature, the chimera is a 4th-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The chimera glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "The chimera makes three attacks: one with its claw, one with its bite, and one with its [[dispel-magic-xphb|Dispel Magic]]."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 3) bludgeoning damage, and the target is [[conditions#Grappled|grappled]] (escape DC 11). The chimera has two claws, each of which can grapple only one target."
    "name": "Claw"
"source":
  - "TBVXXIII"
"image": "Compendium/bestiary/miscellaneous/token/shimmerwing-chimera-tbvxxiii.webp"
```
^statblock
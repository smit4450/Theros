---
title: Huge Anvilwrought Raptor
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvii
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Huge Anvilwrought Raptor"]
---
# Huge Anvilwrought Raptor
*Source: Theros Bestiary TBVII*  

<blockquote><i>"I know its lightness, for I have seen it fly. I know its weight, for I have seen it strike." —Brigone, soldier of Meletis</i></blockquote>

<b><big>Anvilwroughts</big></b>
The first anvilwroughts were created by the god of the forge, Purphoros. He gave the secret of breathing life into these metal creatures to his most devoted followers so they could mimic his works and invent new forms at their own forges.

Some anvilwroughts are vigilant guardians at holy shrines, others serve as familiars and messengers, and a few were created to emulate beauty found among the animals of the mortal world. Each exhibits abilities suited to its role, with some behaving like companionable creatures or stoic guardians.

A few extremely rare and valuable anvilwroughts were crafted by the hand of Purphoros himself. A number of these magnificent creations are now heirlooms of monarchs; others are lost to the sands of time or are guarded by ancient monsters.

<b><i>Constructed Nature.</i></b> An anvilwrought doesn’t require air, food, drink, or sleep.

![Huge Anvilwrought Raptor](https://media.dndbeyond.com/compendium-images/moot/ds6d2NLXmv1wnY8q/06-06.png#right)  

```statblock
"name": "Huge Anvilwrought Raptor (TBVII)"
"size": "Huge"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "32"
"hit_dice": "4d12 + 8"
"modifier": !!int "1"
"stats":
  - !!int "20"
  - !!int "13"
  - !!int "14"
  - !!int "3"
  - !!int "14"
  - !!int "1"
"speed": "20 ft., fly 90 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"damage_immunities": "fire, poison"
"condition_immunities": "charmed, exhaustion, paralyzed, petrified, poisoned"
"senses": "darkvision 120 ft., passive Perception 10"
"languages": "Understands the language of its creator but can't speak"
"cr": "5"
"traits":
  - "desc": "The raptor has advantage on Wisdom (Perception) checks that rely on sight."
    "name": "Keen Sight"
  - "desc": "If the raptor moves at least 20 ft. straight toward a target and then hits it with a Beak or Talons attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone."
    "name": "Charge"
"actions":
  - "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 20 (4d8 + 6) piercing damage."
    "name": "Beak"
  - "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 20 (4d8 + 6) slashing damage."
    "name": "Talons"
"source":
  - "TBVII"
"image": "Compendium/bestiary/construct/token/huge-anvilwrought-raptor-tbvii.webp"
```
^statblock
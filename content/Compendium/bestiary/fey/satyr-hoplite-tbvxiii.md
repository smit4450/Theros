---
title: Satyr Hoplite
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxiii
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Satyr Hoplite"]
---
# Satyr Hoplite
*Source: Theros Bestiary TBVXIII*  

<small><blockquote>“Xenagos has become what he once despised: a tyrant and an oppressor.”</blockquote></small>

![Satyr Hoplite](https://img.scryfall.com/cards/art_crop/front/b/8/b8754d66-facb-432e-a6c2-91430a6dec94.jpg?1593096089#right)  

```statblock
"name": "Satyr Hoplite (TBVXIII)"
"size": "Medium"
"type": "fey"
"subtype": "satyr"
"alignment": "Chaotic Good"
"ac": !!int "16"
"ac_class": "half plate"
"hp": !!int "5"
"hit_dice": "1d8 + 1"
"modifier": !!int "1"
"stats":
  - !!int "13"
  - !!int "13"
  - !!int "13"
  - !!int "10"
  - !!int "11"
  - !!int "13"
"speed": "35 ft."
"skillsaves":
  - "name": "[Performance](Compendium/rules/skills.md#Performance)"
    "desc": "+3"
  - "name": "[Persuasion](Compendium/rules/skills.md#Persuasion)"
    "desc": "+3"
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+3"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Sylvan, Common"
"cr": "1"
"traits":
  - "desc": "The hoplite has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against being [charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened), [grappled](Compendium/rules/conditions.md#Grappled), or [restrained](Compendium/rules/conditions.md#Restrained) while it is within 5 feet of at least one ally."
    "name": "Formation Tactics"
  - "desc": "The hoplite has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "Whenever the hoplite makes a long or high jump, it can cover an additional 1d8 feet, even when making a standing jump. This extra distance costs movement as normal."
    "name": "Mirthful Leaps"
"actions":
  - "desc": "The hoplite makes two melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +3 to hit, reach 5 ft., one target. _Hit:_ 3 (1d4 + 1) bludgeoning damage."
    "name": "Ram"
  - "desc": "_Melee Weapon Attack:_ +3 to hit, reach 5 ft., one target. _Hit:_ 4 (1d6 + 1) slashing damage."
    "name": "Scimitar"
"reactions":
  - "desc": "Whenever the oathsworn is the target of a spell, that spell's caster chooses whether following happens: - Until the end of combat, the oathsworn gains a +1 bonus to damage rolls and Strength checks, and it gains 4 (1d8) temporary [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Heroic"
"source":
  - "TBVXIII"
"image": "Compendium/bestiary/fey/token/satyr-hoplite-tbvxiii.webp"
```
^statblock
---
title: Baleful Eidolon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxii
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Baleful Eidolon"]
---
# Baleful Eidolon
*Source: Theros Bestiary TBVXXII*  

A dangerous, menacing soul.

![Baleful Eidolon](https://img.scryfall.com/cards/art_crop/front/8/5/853a89c6-63f9-4b12-8a5b-2c382e22b226.jpg?1562820831#right)  

```statblock
"name": "Baleful Eidolon (TBVXXII)"
"size": "Medium"
"type": "2nd-level necromancy undead"
"alignment": "Any alignment"
"ac": !!int "14"
"hp": !!int "40"
"hit_dice": "8d8 + 8"
"modifier": !!int "2"
"stats":
  - !!int "8"
  - !!int "15"
  - !!int "13"
  - !!int "11"
  - !!int "12"
  - !!int "10"
"speed": "30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"damage_resistances": "necrotic, bludgeoning, piercing, and slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [exhaustion](Compendium/rules/conditions.md#Exhaustion), [frightened](Compendium/rules/conditions.md#Frightened), [grappled](Compendium/rules/conditions.md#Grappled), [paralyzed](Compendium/rules/conditions.md#Paralyzed), [petrified](Compendium/rules/conditions.md#Petrified), [poisoned](Compendium/rules/conditions.md#Poisoned), [restrained](Compendium/rules/conditions.md#Restrained)"
"senses": "passive Perception 10"
"languages": "The languages it knew in life"
"cr": "1"
"traits":
  - "desc": "Attack rolls against the eidolon are made with [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md) unless the eidolon is [incapacitated](Compendium/rules/conditions.md#Incapacitated)."
    "name": "Blurred Form"
  - "desc": "As a bonus action, the eidolon can target one creature it can see within 5 feet of it that has 0 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) and is still alive. The target must succeed on a DC 10 Constitution saving throw against this magic or die. If the target dies, the eidolon regains 10 (3d6) [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Consume Life"
  - "desc": "The eidolon can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object."
    "name": "Incorporeal Movement"
  - "desc": "In addition to being a creature, the eidolon is a level 2 divine necromancy spell with no target. Its weapon attacks are magical, and it glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Spell Nature"
  - "desc": "The eidolon has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against any effect that turns undead."
    "name": "Turn Resistance"
  - "desc": "The eidolon doesn’t require air, food, drink, or sleep."
    "name": "Undead Nature"
"actions":
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d4 + 4) necrotic damage. The eidolon regains life equal to that amount."
    "name": "Life Drain"
"source":
  - "TBVXXII"
"image": "Compendium/bestiary/miscellaneous/token/baleful-eidolon-tbvxxii.webp"
```
^statblock
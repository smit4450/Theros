---
title: Cloaked Siren
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Cloaked Siren"]
---
# Cloaked Siren
*Source: Theros Bestiary TBVVI*  

<blockquote><small>“That is not the voice of the wind singing on the stones.”

—Callaphe the mariner</small></blockquote>

![Cloaked Siren](https://img.scryfall.com/cards/art_crop/front/7/9/79a639aa-91f4-49df-8671-122710073084.jpg?1593095394#right)  

```statblock
"name": "Cloaked Siren (TBVVI)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "12"
"hp": !!int "42"
"hit_dice": "7d8 + 14"
"modifier": !!int "1"
"stats":
  - !!int "16"
  - !!int "13"
  - !!int "14"
  - !!int "7"
  - !!int "10"
  - !!int "13"
"speed": "20 ft., fly 40 ft."
"skillsaves":
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+3"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed)"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "1"
"traits":
  - "desc": "The siren has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on attack rolls against any creature it has surprised."
    "name": "Ambusher"
  - "desc": "The siren has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on Dexterity (Stealth) checks made to hide in rocky terrain."
    "name": "Stone Camouflage"
"actions":
  - "desc": "The siren makes two attacks: one with its claws and one with its club."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) slashing damage."
    "name": "Claws"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage."
    "name": "Club"
  - "desc": "The siren sings a magical melody. Every humanoid and giant within 300 ft. of the siren that can hear the song must succeed on a DC 11 Wisdom saving throw or be [charmed](Compendium/rules/conditions.md#Charmed) until the song ends. The siren must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the siren is [incapacitated](Compendium/rules/conditions.md#Incapacitated). While [charmed](Compendium/rules/conditions.md#Charmed) by the siren, a target is [incapacitated](Compendium/rules/conditions.md#Incapacitated) and ignores the songs of other sirens. If the [charmed](Compendium/rules/conditions.md#Charmed) target is more than 5 ft. away from the siren, the must move on its turn toward the siren by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the siren, a target can repeat the saving throw. A creature can also repeat the saving throw at the end of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this siren's song for the next 24 hours."
    "name": "Luring Song"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/monstrosity/token/cloaked-siren-tbvvi.webp"
```
^statblock
---
title: Shrike Harpy
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Shrike Harpy"]
---
# Shrike Harpy
*Source: Theros Bestiary TBVVI*  

<b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more harpy cultists might be nearby who will pay tribute.
<li>A quest goal might involve securing a harpy egg.
<li>A quest goal might involve protecting something, and being carried off by the harpy would make this goal difficult.

![Shrike Harpy](https://img.scryfall.com/cards/art_crop/front/1/c/1c2b1eeb-6cc9-48a7-a068-afa1011c45f2.jpg?1593092105#right)  

```statblock
"name": "Shrike Harpy (TBVVI)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "10"
"hp": !!int "10"
"hit_dice": "2d8 + 2"
"modifier": !!int "1"
"stats":
  - !!int "12"
  - !!int "13"
  - !!int "12"
  - !!int "6"
  - !!int "11"
  - !!int "14"
"speed": "20 ft., fly 40 ft."
"skillsaves":
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "0"
"traits":
  - "desc": "The harpy has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against being [charmed](Compendium/rules/conditions.md#Charmed) or [frightened](Compendium/rules/conditions.md#Frightened)."
    "name": "Dark Devotion"
  - "desc": "The harpy roosts in a next 100 feet from the ground in a dead cypress tree. Its 5-foot-radius nest is made of human bones held together with dried mud. Roll a two d4's to determine how many eggs are in the clutch: 2: 1 egg 3-7: 2 eggs 8: 3 eggs If the DM decides to have the eggs hatch, use the **harpy chick** stat block."
    "name": "Harpy's Roost"
"actions":
  - "desc": "The harpy makes two melee attacks: one with its bite and one with its claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) slashing damage."
    "name": "Claws"
"reactions":
  - "desc": "Immediately after initiative rolls in which the harpy participates, it demands tribute from a creature it can see. That creature may bow, genuflect, salute, or perform a similar gesture as a bonus action. If tribute is paid: Until the end of combat, the harpy gains a +2 bonus to damage rolls and Strength and Dexterity checks, and 9 (2d8) temporary [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md). If tribute isn't paid: The creature becomes [grappled](Compendium/rules/conditions.md#Grappled) by the harpy (escape DC 11 Strength check). The harpy can carry a Medium or smaller creature with both claws of its feet while flying. A creature that successfully escapes while the harpy is flying falls."
    "name": "Demand Tribute"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/monstrosity/token/shrike-harpy-tbvvi.webp"
```
^statblock
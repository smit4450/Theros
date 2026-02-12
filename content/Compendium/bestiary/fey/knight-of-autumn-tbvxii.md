---
title: Knight of Autumn
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxii
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Knight of Autumn"]
---
# Knight of Autumn
*Source: Theros Bestiary TBVXII*  

These knights ride into battle alongside the mightier Conclave dryads (see GGR). They ride into the battle to defend the Selesnya Conclave astride mounts composed of vines, branches, and leaves.

Adventurers are most likely to run into these knights while they are escorting important Selesnya dignitaries from Vitu-Ghazi to the hall of the Guildpact.

![Knight of Autumn](https://img.scryfall.com/cards/art_crop/front/3/0/3028075c-5fc5-4942-a984-1ffcf7a8933d.jpg?1538880355#right)  

```statblock
"name": "Knight of Autumn (TBVXII)"
"size": "Medium"
"type": "fey"
"alignment": "Lawful Good"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "132"
"hit_dice": "22d8 + 44"
"modifier": !!int "4"
"stats":
  - !!int "15"
  - !!int "19"
  - !!int "14"
  - !!int "19"
  - !!int "20"
  - !!int "21"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "7"
  - "wisdom": !!int "8"
  - "charisma": !!int "8"
"skillsaves":
  - "name": "[Arcana](Compendium/rules/skills.md#Arcana)"
    "desc": "+7"
  - "name": "[Nature](Compendium/rules/skills.md#Nature)"
    "desc": "+7"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+8"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Common, Elvish, Sylvan"
"cr": "5"
"traits":
  - "desc": "If the knight is mounted and moves at least 20 feet straight toward a target and then hits it with a lance attack on the same turn, that target must succeed on a DC 15 Strength saving throw or be knocked prone."
    "name": "Mounted Charge"
  - "desc": "The knight of autumn can communicate with beasts and plants as if they shared a language."
    "name": "Speak with Beasts and Plants"
"actions":
  - "desc": "The knight makes two attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 15 (2d12 + 2) piercing damage."
    "name": "Lance"
  - "desc": "The knight of autumn summons a mount, which appears in an unoccupied space within 60 feet of the knight. The mount remains for 8 hours until it or the knight dies, or until the knight dismisses it as an action. The mount uses the stat block of an elk with these changes: it is a plant instead of a beast, it has an Intelligence of 6, and it understands Sylvan but can’t speak. While within 1 mile of the mount, the knight can communicate with it telepathically."
    "name": "Summon Mount (1/Day)"
"source":
  - "TBVXII"
"image": "Compendium/bestiary/fey/token/knight-of-autumn-tbvxii.webp"
```
^statblock
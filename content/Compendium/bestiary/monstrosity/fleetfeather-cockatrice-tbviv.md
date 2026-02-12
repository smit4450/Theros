---
title: Fleetfeather Cockatrice
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/17
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Fleetfeather Cockatrice"]
---
# Fleetfeather Cockatrice
*Source: Theros Bestiary TBVIV*  

A titanic wyvern-peacock with a poisonous gaze. It needs merely to fix its eyes on a target to putrefy it. The fleetfeather cockatrice is so named for its fleeting speed.

![Fleetfeather Cockatrice](https://img.scryfall.com/cards/art_crop/front/1/1/1139236e-5d71-4fc1-937d-ba1efadee031.jpg?1593096401#right)  

```statblock
"name": "Fleetfeather Cockatrice (TBVIV)"
"size": "Gargantuan"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "390"
"hit_dice": "30d20 + 90"
"modifier": !!int "3"
"stats":
  - !!int "17"
  - !!int "17"
  - !!int "16"
  - !!int "2"
  - !!int "13"
  - !!int "5"
"speed": "50 ft., fly 300 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Acrobatics](Compendium/rules/skills.md#Acrobatics)"
    "desc": "+5"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": ""
"cr": "17"
"traits":
  - "desc": "The cockatrice has advantage on attack rolls against any creature it has surprised."
    "name": "Ambusher"
  - "desc": "The cockatrice doesn't provoke opportunity attacks when it flies out of an enemy's reach."
    "name": "Flyby"
  - "desc": "The cockatrice can't be petrified by a member of its own species."
    "name": "Limited Petrification Immunity"
  - "desc": "If the cockatrice is reduced to 0 hit points, it doesn’t die or fall unconscious. Instead, it sheds its skin, regains 405 (30d20+90) hit points, and moves up to its speed without provoking opportunity attacks."
    "name": "Molt (Mythic Trait; Recharges After a Short or Long Rest)"
"actions":
  - "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one creature. Hit: 30 (6d6 + 3) piercing damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 30 (6d8 + 3) slashing damage."
    "name": "Claws"
  - "desc": "The cockatrice fixes its gaze on one creature within 30 feet of it that the cockatrice can see with both eyes and forces the target to make a DC 13 saving throw. A creature that isn't surprised can use a reaction to Hide and avoid the saving throw. On a failed save, the creature is instantly petrified. A creature that succeeds on the saving throw begins to turn to stone and is restrained. The restrained creature must repeat the saving throw at the end of its next turn, becoming petrified on a failure or ending the effect on a success. The petrification can only be cured by a god."
    "name": "Death-Darting Eyes"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 60 ft., one target. _Hit:_ 18 (6d4 + 3) bludgeoning damage."
    "name": "Tail"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/monstrosity/token/fleetfeather-cockatrice-tbviv.webp"
```
^statblock
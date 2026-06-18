---
title: Ill-Tempered Cyclops
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvix
- monster/cr/16
- monster/size/g
- monster/type/giant
statblock: inline
aliases: ["Ill-Tempered Cyclops"]
---
# Ill-Tempered Cyclops
*Source: Theros Bestiary TBVIX*  

<blockquote><small>A cyclops has two moods: angry and asleep.</small></blockquote>

![Ill-Tempered Cyclops](Homebrew/bestiary/giant/img/ill-tempered-cyclops.webp#right|850)  

```statblock
"name": "Ill-Tempered Cyclops (TBVIX)"
"size": "Gargantuan"
"type": "giant"
"alignment": "Chaotic Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "390"
"hit_dice": "30d20 + 90"
"modifier": !!int "0"
"stats":
  - !!int "17"
  - !!int "11"
  - !!int "17"
  - !!int "8"
  - !!int "6"
  - !!int "10"
"speed": "120 ft."
"senses": "passive Perception 10"
"languages": "Giant"
"cr": "16"
"traits":
  - "desc": "When the cyclops is reduced to 0 [[hit-points-xphb|Hit Points]], it doesn’t die or fall [[conditions#Unconscious|unconscious]]. Instead, the damage creates tears in its skin, revealing its hearts. The cyclops has three hearts in its chest. A heart has an AC of 14 and 135 [[hit-points-xphb|Hit Points]]. It is immune to all conditions. If it is forced to make a saving throw, treat its ability scores as 10 (+0). The cyclops dies when all the hearts are destroyed."
    "name": "Hearts of the Cyclops (Mythic Trait; Recharges after a Short or Long Rest)"
  - "desc": "The cyclops has [[disadvantage-xphb|Disadvantage]] on any attack roll against a target more than 30 feet away."
    "name": "Poor Depth Perception"
  - "desc": "The cyclops can move in and out of a Huge or smaller creature's space. If it would, it uses a bonus action to attack that creature with its unarmed strike. That creature must succeed on a DC 13 Strength saving throw or be knocked [[conditions#Prone|prone]]. If the creature succeeds, the cyclops can't enter that space and must end its turn immediately. If the cyclops stops on top of that creature, that creature becomes [[conditions#Restrained|restrained]] until the cyclops moves off it (escape DC 13)."
    "name": "Trample"
"actions":
  - "desc": "The cyclops makes two greatclub attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 30 (6d8 + 3) bludgeoning damage."
    "name": "Greatclub"
  - "desc": "Ranged Weapon Attack: +5 to hit, range 30/120 ft., one target. Hit: 44 (8d10) bludgeoning damage."
    "name": "Rock"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 30 (6d8 + 3) bludgeoning damage."
    "name": "Unarmed Strike"
"source":
  - "TBVIX"
"image": "Homebrew/bestiary/giant/token/ill-tempered-cyclops-tbvix.webp"
```
^statblock
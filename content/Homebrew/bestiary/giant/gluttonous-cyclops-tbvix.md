---
title: Gluttonous Cyclops
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvix
- monster/cr/23
- monster/size/g
- monster/type/giant
statblock: inline
aliases: ["Gluttonous Cyclops"]
---
# Gluttonous Cyclops
*Source: Theros Bestiary TBVIX*  

<blockquote><small>The cyclops had learned to never eat a shepherd. Instead he gently flung the “pit” aside to grow a new flock.</small></blockquote>

![Gluttonous Cyclops](Homebrew/bestiary/giant/img/gluttonous-cyclops.webp#right)  

```statblock
"name": "Gluttonous Cyclops (TBVIX)"
"size": "Gargantuan"
"type": "giant"
"alignment": "Chaotic Neutral"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "560"
"hit_dice": "40d20 + 160"
"modifier": !!int "0"
"stats":
  - !!int "20"
  - !!int "11"
  - !!int "18"
  - !!int "8"
  - !!int "6"
  - !!int "10"
"speed": "120 ft."
"senses": "passive Perception 10"
"languages": "Giant"
"cr": "23"
"traits":
  - "desc": "The cyclops has [[disadvantage-xphb|Disadvantage]] on any attack roll against a target more than 30 feet away."
    "name": "Poor Depth Perception"
  - "desc": "When the cyclops is reduced to 0 [[hit-points-xphb|Hit Points]], it doesn’t die or fall [[conditions#Unconscious|unconscious]]. Instead, the damage creates tears in its skin, revealing its hearts. The cyclops has three hearts in its chest. A heart has an AC of 14 and 145 [[hit-points-xphb|Hit Points]]. It is immune to all conditions. If it is forced to make a saving throw, treat its ability scores as 10 (+0). The cyclops dies when all the hearts are destroyed."
    "name": "Hearts of the Cyclops (Mythic Trait; Recharges after a Short or Long Rest)"
"actions":
  - "desc": "The cyclops makes two greatclub attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 48 (10d8 + 3) bludgeoning damage."
    "name": "Greatclub"
  - "desc": "Ranged Weapon Attack: +7 to hit, range 30/120 ft., one target. Hit: 55 (10d10) bludgeoning damage."
    "name": "Rock"
"source":
  - "TBVIX"
"image": "Homebrew/bestiary/giant/token/gluttonous-cyclops-tbvix.webp"
```
^statblock
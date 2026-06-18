---
title: Nessian Courser
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxv
- monster/cr/3
- monster/size/m
- monster/type/fey
statblock: inline
aliases: ["Nessian Courser"]
---
# Nessian Courser
*Source: Theros Bestiary TBVXV*  

<blockquote><small>Khestes the Adamant, the Champion’s closest ally among the centaurs, took one stone to his shoulder and another to his flank. He held his stride and his aim, and let fly the arrow that killed the giant Grinthax.

—The Theriad</small></blockquote>

![Nessian Courser](Homebrew/bestiary/fey/img/nessian-courser.webp#right|850)  

```statblock
"name": "Nessian Courser (TBVXV)"
"size": "Medium"
"type": "fey"
"subtype": "centaur"
"alignment": "Chaotic Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "3"
"stats":
  - !!int "17"
  - !!int "16"
  - !!int "16"
  - !!int "10"
  - !!int "13"
  - !!int "10"
"speed": "40 ft."
"saves":
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+5"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+3"
  - "name": "[[skills#Nature|Nature]]"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Common, Sylvan"
"cr": "3"
"traits":
  - "desc": "The courser has [[advantage-xphb|Advantage]] on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "If the courser moves at least 30 feet straight toward a target and then hits it with a melee attack on the same turn, it can immediately follow that attack with a bonus action, making one attack against the target with its hooves."
    "name": "Charge"
  - "desc": "The courser counts as one size larger when determining its carrying capacity and the weight it can push or drag. In addition, any climb that requires hands and feet is especially difficult for it because of its equine legs. When it makes such a climb, each foot of movement costs it 4 extra feet instead of the normal 1 extra foot."
    "name": "Equine Build"
  - "desc": "The courser's attack rolls score a critical hit on a roll of 19 or 20 on the d20."
    "name": "Improved Critical"
"actions":
  - "desc": "The courser makes two attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage."
    "name": "Hooves"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 10 ft., one target. _Hit:_ 8 (1d10 + 3) slashing damage."
    "name": "Glaive"
  - "desc": "_Ranged Weapon Attack:_ +7 to hit, range 150/600 ft., one target. _Hit:_ 7 (1d8 + 3) piercing damage."
    "name": "Longbow"
"source":
  - "TBVXV"
"image": "Homebrew/bestiary/fey/token/nessian-courser-tbvxv.webp"
```
^statblock
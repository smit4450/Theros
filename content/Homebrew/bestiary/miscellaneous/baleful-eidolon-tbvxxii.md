---
title: Baleful Eidolon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxii
- monster/cr/1
- monster/size/m
- monster/type/miscellaneous
statblock: inline
aliases: ["Baleful Eidolon"]
---
# Baleful Eidolon
*Source: Theros Bestiary TBVXXII*  

A dangerous, menacing soul.

![Baleful Eidolon](Homebrew/bestiary/miscellaneous/img/baleful-eidolon.webp#right)  

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
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"damage_resistances": "necrotic, bludgeoning, piercing, and slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]], [[conditions#Frightened|frightened]], [[conditions#Grappled|grappled]], [[conditions#Paralyzed|paralyzed]], [[conditions#Petrified|petrified]], [[conditions#Poisoned|poisoned]], [[conditions#Restrained|restrained]]"
"senses": "passive Perception 10"
"languages": "The languages it knew in life"
"cr": "1"
"traits":
  - "desc": "Attack rolls against the eidolon are made with [[disadvantage-xphb|Disadvantage]] unless the eidolon is [[conditions#Incapacitated|incapacitated]]."
    "name": "Blurred Form"
  - "desc": "As a bonus action, the eidolon can target one creature it can see within 5 feet of it that has 0 [[hit-points-xphb|Hit Points]] and is still alive. The target must succeed on a DC 10 Constitution saving throw against this magic or die. If the target dies, the eidolon regains 10 (3d6) [[hit-points-xphb|Hit Points]]."
    "name": "Consume Life"
  - "desc": "The eidolon can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object."
    "name": "Incorporeal Movement"
  - "desc": "In addition to being a creature, the eidolon is a level 2 divine necromancy spell with no target. Its weapon attacks are magical, and it glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Spell Nature"
  - "desc": "The eidolon has [[advantage-xphb|Advantage]] on saving throws against any effect that turns undead."
    "name": "Turn Resistance"
  - "desc": "The eidolon doesn’t require air, food, drink, or sleep."
    "name": "Undead Nature"
"actions":
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d4 + 4) necrotic damage. The eidolon regains life equal to that amount."
    "name": "Life Drain"
"source":
  - "TBVXXII"
"image": "Homebrew/bestiary/miscellaneous/token/baleful-eidolon-tbvxxii.webp"
```
^statblock
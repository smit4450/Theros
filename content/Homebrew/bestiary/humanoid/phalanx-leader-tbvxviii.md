---
title: Phalanx Leader
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxviii
- monster/cr/3
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Phalanx Leader"]
---
# Phalanx Leader
*Source: Theros Bestiary TBVXVIII*  

<small><blockquote>His soldiers etch his words on the insides of their shields, their inspiration always in sight during battle.</blockquote></small>

![Phalanx Leader](Homebrew/bestiary/humanoid/img/phalanx-leader.webp#right)  

```statblock
"name": "Phalanx Leader (TBVXVIII)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "breastplate, shield"
"hp": !!int "48"
"hit_dice": "8d8 + 16"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "16"
  - !!int "14"
  - !!int "11"
  - !!int "14"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "strength": !!int "5"
  - "dexterity": !!int "5"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "3"
"traits":
  - "desc": "While the phalanx leader is holding a spear, other creatures provoke an opportunity attack from the phalanx leader when they move within 5 feet of it. When the phalanx leader hits a creature with an opportunity attack using its spear, the creature takes an extra 4 (1d8) piercing damage, and the creature’s speed becomes 0 for the rest of the turn."
    "name": "Hold the Line"
"actions":
  - "desc": "The phalanx leader makes three melee attacks or two ranged attacks."
    "name": "Multiattack"
  - "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft., or range 20/60 ft., one target. Hit: 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing damage if used with two hands to make a melee attack."
    "name": "Spear"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 13 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Shield Bash"
"reactions":
  - "desc": "Whenever the phalanx leader becomes targeted by a spell, that spell's caster determines whether the following happens: - The phalanx leader speaks words of inspiration as a bonus action. It and its allies within 30 ft. of it that can hear it are affected. Until the end of combat, each gains a +1 bonus to damage rolls and Strength and Dexterity checks, and each gains 4 (1d8) temporary [[hit-points-xphb|Hit Points]]."
    "name": "Heroic"
"source":
  - "TBVXVIII"
"image": "Homebrew/bestiary/humanoid/token/phalanx-leader-tbvxviii.webp"
```
^statblock
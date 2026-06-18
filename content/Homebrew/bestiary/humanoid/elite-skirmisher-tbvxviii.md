---
title: Elite Skirmisher
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxviii
- monster/cr/2
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Elite Skirmisher"]
---
# Elite Skirmisher
*Source: Theros Bestiary TBVXVIII*  

<blockquote><small>Some adopted the tactics of the leonin to combat the ferocity of the minotaurs.</small></blockquote>

![Elite Skirmisher](Homebrew/bestiary/humanoid/img/elite-skirmisher.webp#right)  

```statblock
"name": "Elite Skirmisher (TBVXVIII)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "17"
"ac_class": "half plate"
"hp": !!int "15"
"hit_dice": "3d8 + 3"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "16"
  - !!int "13"
  - !!int "11"
  - !!int "14"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "strength": !!int "5"
  - "dexterity": !!int "5"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "2"
"actions":
  - "desc": "The skirmisher makes three unarmed strikes."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 5 (1d4 + 3) bludgeoning damage."
    "name": "Unarmed Strike"
"reactions":
  - "desc": "Whenever a spell targets the hoplite, that spell's caster chooses whether the following happens: - The skirmisher lets out an especially menacing roar. Creatures it chooses within 10 feet of itself that can hear it must succeed on a DC 10 Wisdom saving throw or become [[conditions#Frightened|frightened]] of it until the end of your next turn."
    "name": "Heroic"
"source":
  - "TBVXVIII"
"image": "Homebrew/bestiary/humanoid/token/elite-skirmisher-tbvxviii.webp"
```
^statblock
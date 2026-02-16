---
title: Battlewise Hoplite
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxviii
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Battlewise Hoplite"]
---
# Battlewise Hoplite
*Source: Theros Bestiary TBVXVIII*  



![Battlewise Hoplite](Compendium/bestiary/humanoid/img/battlewise-hoplite.webp#right|850)  

```statblock
"name": "Battlewise Hoplite (TBVXVIII)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "breastplate, shield"
"hp": !!int "45"
"hit_dice": "9d8 + 9"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "14"
  - !!int "12"
  - !!int "16"
  - !!int "13"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "4"
  - "intelligence": !!int "5"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+5"
  - "name": "[[skills#History|History]]"
    "desc": "+5"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "3"
"traits":
  - "desc": "The hoplite is a 3rd-level spellcaster. The hoplite's spellcasting ability is Intelligence (spell save DC 13, +5 to hit with spell attacks). The hoplite has the following wizard spells prepared: Cantrips (at will): [[mage-hand-xphb|Mage Hand]], [[minor-illusion-xphb|Minor Illusion]], [[ray-of-frost-xphb|Ray Of Frost]] 1st level (4 slots): [[color-spray-xphb|Color Spray]], [[expeditious-retreat-xphb|Expeditious Retreat]], [[sleep-xphb|Sleep]] 2nd level (2 slots): [[blur-xphb|Blur]], _cloud of daggers_, [[invisibility-xphb|Invisibility]]"
    "name": "Spellcasting"
"actions":
  - "desc": "The hoplite makes three weapon attacks. It can replace one weapon attack with _ray of frost._"
    "name": "Multiattack"
  - "desc": "_Melee or Ranged Weapon Attack_: +4 to hit, reach 5 ft., one target. _Hit_: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack."
    "name": "Spear"
  - "desc": "_Melee Weapon Attack_: +4 to hit, reach 5 ft., one creature. _Hit_: 4 (1d4 + 2) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 12 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Shield Bash"
  - "desc": "_Ranged Spell Attack_: +5 to hit, range 60 ft., one creature. _Hit_: 4 (1d8) cold damage, and the target’s speed is reduced by 10 feet until the start of the hoplite’s next turn."
    "name": "Ray of Frost (Cantrip)"
"reactions":
  - "desc": "Whenever a spell targets the hoplite, that spell's caster chooses whether the following happens: - Until the end of combat, the hoplite gains a +1 bonus to damage rolls and Strength and Dexterity checks, and it gains 4 (1d8) temporary [[hit-points-xphb|Hit Points]]. The hoplite gains a +1 bonus on the next Intelligence check it makes."
    "name": "Heroic"
"source":
  - "TBVXVIII"
"image": "Compendium/bestiary/humanoid/token/battlewise-hoplite-tbvxviii.webp"
```
^statblock
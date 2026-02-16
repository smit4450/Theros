---
title: Labyrinth Champion
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxvi
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Labyrinth Champion"]
---
# Labyrinth Champion
*Source: Theros Bestiary TBVXVI*  

<blockquote><small>“It used to be a lair. Now it’s just a tunnel.”</small></blockquote>

![Labyrinth Champion](Compendium/bestiary/humanoid/img/labyrinth-champion.webp#right|850)  

```statblock
"name": "Labyrinth Champion (TBVXVI)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "20"
"ac_class": "plate, shield"
"hp": !!int "48"
"hit_dice": "8d8 + 16"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "15"
  - !!int "15"
  - !!int "11"
  - !!int "13"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+5"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": "Common, any two languages"
"cr": "4"
"traits":
  - "desc": "The champion has [[advantage-xphb|Advantage]] on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "The champion's attack rolls score a critical hit on a roll of 19 or 20 on the d20."
    "name": "Improved Critical"
"actions":
  - "desc": "The champion can attack twice, instead of once, whenever it takes the Attack action on its turn."
    "name": "Extra Attack"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) piercing damage."
    "name": "Shortsword"
"reactions":
  - "desc": "Whenever the champion becomes targeted by a spell, that spell's caster chooses whether the champion may make a Shortsword attack as a bonus action."
    "name": "Heroic"
"source":
  - "TBVXVI"
"image": "Compendium/bestiary/humanoid/token/labyrinth-champion-tbvxvi.webp"
```
^statblock
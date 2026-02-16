---
title: Cruel Centaur Feeder
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvv
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Cruel Centaur Feeder"]
---
# Cruel Centaur Feeder
*Source: Theros Bestiary TBVV*  



![Cruel Centaur Feeder](https://img.scryfall.com/cards/art_crop/front/a/5/a53624ee-2925-4a56-8706-e278db5d963d.jpg?1593095659#right)  

```statblock
"name": "Cruel Centaur Feeder (TBVV)"
"size": "Medium"
"type": "undead aberration"
"alignment": "Any alignment"
"ac": !!int "10"
"hp": !!int "7"
"hit_dice": "5d1 + 5"
"modifier": !!int "0"
"stats":
  - !!int "18"
  - !!int "10"
  - !!int "13"
  - !!int "10"
  - !!int "11"
  - !!int "10"
"speed": "20 ft."
"skillsaves":
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+2"
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "passive Perception 10"
"languages": "Sylvan, Common"
"cr": "1"
"traits":
  - "desc": "The centaur counts as one size larger when determining its carrying capacity and the weight it can push or drag. In addition, any climb that requires hands and feet is especially difficult for it because of its equine legs. When it makes such a climb, each foot of movement costs it 4 extra feet instead of the normal 1 extra foot."
    "name": "Equine Build"
  - "desc": "The centaur doesn't suffer [[conditions#Exhaustion|exhaustion]] from lack of food, drink, or sleep. It has [[disadvantage-xphb|Disadvantage]] on ability checks, attack rolls, and saving throws."
    "name": "Exhausted and Afraid"
"actions":
  - "desc": "The centaur makes three attacks: one with its hooves and two with its feed attack."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d4 + 4) bludgeoning damage."
    "name": "Hooves"
  - "desc": "_Melee Weapon Attack:_ +6 to hit, reach 5 ft., one target. _Hit:_ 7 (1d6 + 4) piercing damage. The centaur regains that much life."
    "name": "Feed"
"source":
  - "TBVV"
"image": "Compendium/bestiary/undead/token/cruel-centaur-feeder-tbvv.webp"
```
^statblock
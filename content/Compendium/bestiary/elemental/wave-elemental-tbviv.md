---
title: Wave Elemental
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Wave Elemental"]
---
# Wave Elemental
*Source: Theros Bestiary TBVIV*  



![Wave Elemental](https://img.scryfall.com/cards/art_crop/front/f/0/f0e68ed9-d863-4822-b281-e184f3d62faa.jpg?1562636937#right)  

```statblock
"name": "Wave Elemental (TBVIV)"
"size": "Large"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "13"
"hp": !!int "3"
"hit_dice": "1d4 + 1"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "15"
  - !!int "13"
  - !!int "11"
  - !!int "10"
  - !!int "10"
"speed": "swim 60 ft."
"damage_resistances": "fire, bludgeoning, piercing, and slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]], [[conditions#Grappled|grappled]], [[conditions#Paralyzed|paralyzed]], [[conditions#Poisoned|poisoned]], [[conditions#Prone|prone]], [[conditions#Restrained|restrained]], [[conditions#Unconscious|unconscious]]"
"senses": "[[senses#Blindsight|Blindsight]] 30ft., passive Perception 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "If the elemental takes cold damage, it partially freezes; its speed is reduced by 20 feet until the end of its next turn."
    "name": "Freeze"
  - "desc": "The elemental is [[conditions#Invisible|invisible]] while fully immersed in water."
    "name": "Invisible in Water"
  - "desc": "If the elemental moves at least 20 feet straight toward a creature and then hits it with a hooves attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked [[conditions#Prone|prone]]. If the target is [[conditions#Prone|prone]], the elemental can make another attack with its hooves against it as a bonus action."
    "name": "Trampling Charge"
  - "desc": "The elemental dies if it leaves the water to which it is bound or that water is destroyed."
    "name": "Water Bound"
"actions":
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 4 (1d4 + 2) bludgeoning damage."
    "name": "Hooves"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/elemental/token/wave-elemental-tbviv.webp"
```
^statblock
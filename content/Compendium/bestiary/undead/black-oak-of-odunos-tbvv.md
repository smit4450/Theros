---
title: Black Oak of Odunos
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvv
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Black Oak of Odunos"]
---
# Black Oak of Odunos
*Source: Theros Bestiary TBVV*  

<blockquote><small>Phenax promised the newly dead souls they would be spared from Erebos. In this, he did not lie.</small></blockquote>

![Black Oak of Odunos](Compendium/bestiary/undead/img/black-oak-of-odunos.webp#right|850)  

```statblock
"name": "Black Oak of Odunos (TBVV)"
"size": "Huge"
"type": "undead plant"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "63"
"hit_dice": "7d12 + 21"
"modifier": !!int "-2"
"stats":
  - !!int "19"
  - !!int "6"
  - !!int "16"
  - !!int "3"
  - !!int "6"
  - !!int "5"
"speed": "0 ft."
"damage_vulnerabilities": "fire"
"damage_resistances": "bludgeoning, piercing"
"damage_immunities": "necrotic"
"condition_immunities": "[poisoned](Compendium/rules/conditions.md#Poisoned), [restrained](Compendium/rules/conditions.md#Restrained)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": "understands all languages it spoke in life but can't speak"
"cr": "1/2"
"traits":
  - "desc": "While the oak remains motionless, it is indistinguishable from a normal oak. A successful DC 10 Wisdom (Perception) check in sufficient lighting within 60 feet of the oak reveals it appears to be composed of human corpses."
    "name": "False Appearance"
  - "desc": "A creature that touches the oak or hits it with a melee attack while within 5 feet of it takes 5 (1d10) necrotic damage."
    "name": "Necrotic Body"
  - "desc": "The oak can't be surprised."
    "name": "Vigilant"
  - "desc": "If damage reduces the oak to 0 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md), it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the oak drops to 1 hit point instead."
    "name": "Undead Fortitude"
"source":
  - "TBVV"
"image": "Compendium/bestiary/undead/token/black-oak-of-odunos-tbvv.webp"
```
^statblock
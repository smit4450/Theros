---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvv
- monster/cr/1-2
- monster/size/huge
- monster/type/undead
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Black Oak of Odunos"
---
# Black Oak of Odunos
*Source: Theros Bestiary, Vol. V*
![](/Compendium/bestiary/undead/img/black-oak-of-odunos.webp#right)

Phenax promised the newly dead souls they would be spared from Erebos. In this, he did not lie.

```statblock
"name": "Black Oak of Odunos"
"size": "Huge"
"type": "undead"
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
"condition_immunities": "[poisoned](/Compendium/rules/conditions.md#Poisoned), [restrained](/Compendium/rules/conditions.md#Restrained)"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "understands all languages it spoke in life but can't speak"
"cr": "1/2"
"traits":
  - "desc": "While the oak remains motionless, it is indistinguishable from a normal\
      \ oak. A successful DC 10 Wisdom (Perception) check in sufficient lighting within\
      \ 60 feet of the oak reveals it appears to be composed of human corpses."
    "name": "False Appearance"
  - "desc": "A creature that touches the oak or hits it with a melee attack while\
      \ within 5 feet of it takes 5 (1d10) necrotic damage."
    "name": "Necrotic Body"
  - "desc": "The oak can't be surprised."
    "name": "Vigilant"
  - "desc": "If damage reduces the oak to 0 Hit Points, it must make a Constitution\
      \ saving throw with a DC of 5 + the damage taken, unless the damage is radiant\
      \ or from a critical hit. On a success, the oak drops to 1 hit point instead."
    "name": "Undead Fortitude"
"source":
  - "TBVV"
```
^statblock
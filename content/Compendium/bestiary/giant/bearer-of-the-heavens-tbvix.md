---
title: Bearer of the Heavens
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvix
- ttrpg-cli/monster/cr/30
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Bearer of the Heavens"]
---
# Bearer of the Heavens
*Source: Theros Bestiary TBVIX*  

<small><blockquote>To hold the heavens from the earth is no curse, but a titanic responsibility.</blockquote></small>
WARNING: This creature is intended to serve as an NPC, not as a boss. Engaging it could result in planar chaos. Killing it will result in destroying Theros.

![Bearer of the Heavens](Compendium/bestiary/giant/img/bearer-of-the-heavens.webp#right|850)  

```statblock
"name": "Bearer of the Heavens (TBVIX)"
"size": "Gargantuan"
"type": "giant"
"subtype": "titan"
"alignment": "Lawful Good"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "2000"
"hit_dice": "100d20 + 1000"
"modifier": !!int "5"
"stats":
  - !!int "30"
  - !!int "20"
  - !!int "30"
  - !!int "13"
  - !!int "20"
  - !!int "20"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "19"
  - "constitution": !!int "24"
  - "wisdom": !!int "19"
  - "strength": !!int "24"
  - "charisma": !!int "19"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+19"
  - "name": "[[skills#History|History]]"
    "desc": "+15"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+19"
"damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks, force"
"damage_immunities": "fire"
"senses": "passive Perception 10"
"languages": "Giant"
"cr": "30"
"traits":
  - "desc": "If the giant fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (3/Day)"
  - "desc": "The giant takes pride in its duty to suspend Nyx above the earth. If it drops Nyx, Nyx crashes down upon the earth, annihilating everything in the mortal realm. When this happens, Nyx, the underworld, and everything in them cease to exist and the plane of Theros becomes a dead waste."
    "name": "Pillar of Heavens"
  - "desc": "The giant deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "Unless provoked, the giant ignores all creatures and objects."
    "name": "Titanic Nature"
"actions":
  - "desc": "_Melee Weapon Attack:_ +19 to hit, reach 1000 ft., one target. _Hit:_ 2110 (200d20 + 10) bludgeoning damage plus 2100 (200d20) fire damage. Every creature, object, and structure in a 500-foot radius is dealt this damage."
    "name": "Unarmed Strike"
"source":
  - "TBVIX"
"image": "Compendium/bestiary/giant/token/bearer-of-the-heavens-tbvix.webp"
```
^statblock
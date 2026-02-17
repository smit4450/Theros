---
title: Pharagax Giant
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvix
- monster/cr/15
- monster/size/g
- monster/type/giant
statblock: inline
aliases: ["Pharagax Giant"]
---
# Pharagax Giant
*Source: Theros Bestiary TBVIX*  

<b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more Pharagax giant cultists might be nearby who will pay tribute to the giant.
<li>The Pharagax giant could be guarding the Pharagax bridge.
<li>A quest goal might involve destroying a structure.
<li>A quest goal might involve preserving a structure.

![Pharagax Giant](Compendium/bestiary/giant/img/pharagax-giant.webp#right|850)  

```statblock
"name": "Pharagax Giant (TBVIX)"
"size": "Gargantuan"
"type": "giant"
"alignment": "Unaligned"
"ac": !!int "17"
"hp": !!int "390"
"hit_dice": "30d20 + 90"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "15"
  - !!int "17"
  - !!int "10"
  - !!int "12"
  - !!int "9"
"speed": "120 ft."
"saves":
  - "dexterity": !!int "7"
  - "constitution": !!int "8"
  - "wisdom": !!int "6"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+8"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
"damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": "Giant"
"cr": "15"
"traits":
  - "desc": "The giant deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "Unless provoked, the giant ignores all nonflying things that are Huge or smaller and all flying things that are Large or smaller."
    "name": "Titanic Nature"
"actions":
  - "desc": "Ranged Weapon Attack: +8 to hit, range 120/480 ft., one target. Hit: 30 (3d8 + 3) bludgeoning damage. If the target is a creature, it must succeed on a DC 16 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Boulder"
"reactions":
  - "desc": "If a rock or similar object is hurled at the giant, the giant can, with a successful DC 15 Dexterity saving throw, catch the missile and take no bludgeoning damage from it."
    "name": "Rock Catching"
  - "desc": "Immediately after initiative rolls in which the giant participates, it demands tribute from a creature it can see. That creature may bow, genuflect, salute, or perform a similar gesture as a bonus action. If tribute is paid: Until the end of combat, the giant gains a +2 bonus to damage rolls and Strength and Dexterity checks, and 210 (20d20) temporary [[hit-points-xphb|Hit Points]]. If tribute isn't paid: the giant pounds the earth, dealing 28 (10d4+3) damage to every creature, object, and structure on the ground within a 15-foot radius."
    "name": "Demand Tribute"
"source":
  - "TBVIX"
"image": "Compendium/bestiary/giant/token/pharagax-giant-tbvix.webp"
```
^statblock
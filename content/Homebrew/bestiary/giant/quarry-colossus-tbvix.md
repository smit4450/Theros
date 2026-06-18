---
title: Quarry Colossus
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvix
- monster/cr/17
- monster/size/g
- monster/type/giant
statblock: inline
aliases: ["Quarry Colossus"]
---
# Quarry Colossus
*Source: Theros Bestiary TBVIX*  



![Quarry Colossus](Homebrew/bestiary/giant/img/quarry-colossus.webp#right)  

```statblock
"name": "Quarry Colossus (TBVIX)"
"size": "Gargantuan"
"type": "giant"
"alignment": "Lawful Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "960"
"hit_dice": "60d20 + 360"
"modifier": !!int "2"
"stats":
  - !!int "20"
  - !!int "15"
  - !!int "22"
  - !!int "14"
  - !!int "16"
  - !!int "16"
"speed": "120 ft."
"condition_immunities": "[[conditions#Frightened|frightened]]"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception 10"
"languages": "Giant"
"cr": "17"
"traits":
  - "desc": "The giant deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "Unless provoked, the giant ignores all nonflying things that are Huge or smaller and all flying things that are Large or smaller."
    "name": "Titanic Nature"
"actions":
  - "desc": "The colossus pounds a hole in the earth, which swallows all creatures, objects, and structure in a 10-foot radius. Each creature in that area must succeed on a DC 15 Dexterity saving throw or fall 1d6 × 10 feet into the sinkhole, take 10 (3d6) bludgeoning damage, and be knocked [[conditions#Prone|prone]] and buried. Buried creatures are [[conditions#Restrained|restrained]] and unable to breathe or stand up. A creature can take an action to make a DC 10 Strength check, ending the buried state on a success."
    "name": "Bury (Recharge 6)"
  - "desc": "Ranged Weapon Attack: +7 to hit, range 60/240 ft., one target. Hit: 30 (10d4 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 15 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Rock"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 10 ft., one target. _Hit:_ 30 (10d4 + 5) bludgeoning damage."
    "name": "Unarmed Strike"
"source":
  - "TBVIX"
"image": "Homebrew/bestiary/giant/token/quarry-colossus-tbvix.webp"
```
^statblock
---
title: Squelching Leeches
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxvii
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Squelching Leeches"]
---
# Squelching Leeches
*Source: Theros Bestiary TBVXVII*  

<blockquote><small>Leeches are sacred to followers of Pharika for drawing poison from a wound, but feared by everyone else for drawing blood from the flesh.</small></blockquote>

![Squelching Leeches](Compendium/bestiary/miscellaneous/img/squelching-leeches.webp#right|850)  

```statblock
"name": "Squelching Leeches (TBVXVII)"
"size": "Medium"
"type": "swarm of tiny beasts"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "15"
"hit_dice": "5d8 + -5"
"modifier": !!int "0"
"stats":
  - !!int "10"
  - !!int "10"
  - !!int "8"
  - !!int "1"
  - !!int "9"
  - !!int "3"
"speed": "5 ft., climb 5 ft., swim 20 ft."
"skillsaves":
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+2"
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[[conditions#Blinded|blinded]], [[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]], [[conditions#Grappled|grappled]], [[conditions#Paralyzed|paralyzed]], [[conditions#Petrified|petrified]], [[conditions#Prone|prone]], [[conditions#Restrained|restrained]], [[conditions#Stunned|stunned]]"
"senses": "[[senses#Blindsight|Blindsight]] 30 ft. (blind beyond this radius), passive Perception 10"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The leeches can breathe air and water."
    "name": "Amphibious"
  - "desc": "For every handful of salt thrown on the swarm, it takes 3 (1d6) acid damage."
    "name": "Salt Susceptibility"
  - "desc": "The swarm has [[advantage-xphb|Advantage]] on Dexterity (Stealth) checks made to hide in swampy terrain."
    "name": "Swamp Camouflage"
  - "desc": "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny leech. The swarm can't regain [[hit-points-xphb|Hit Points]] or gain temporary [[hit-points-xphb|Hit Points]]."
    "name": "Swarm"
"actions":
  - "desc": "Melee Weapon Attack: +2 to hit, reach 0 ft., one creature in the swarm's space. Hit: 10 (4d4) piercing damage, or 5 (2d4) piercing damage if the swarm has half of its [[hit-points-xphb|Hit Points]] or fewer, and the swarm attaches to the target. While attached, the swarm doesn't attack. Instead, at the start of each of the swarm's turns, the target loses 10 (4d4) [[hit-points-xphb|Hit Points]] due to blood loss, or 5 (2d4) if the swarm has half its [[hit-points-xphb|Hit Points]] or fewer. The swarm can detach itself by spending 5 feet of its movement. It does so after it drains 20 [[hit-points-xphb|Hit Points]] of blood from the target or the target dies."
    "name": "Bites"
"source":
  - "TBVXVII"
"image": "Compendium/bestiary/miscellaneous/token/squelching-leeches-tbvxvii.webp"
```
^statblock
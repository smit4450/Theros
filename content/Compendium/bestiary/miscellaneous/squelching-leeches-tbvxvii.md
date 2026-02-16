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
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+2"
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[blinded](Compendium/rules/conditions.md#Blinded), [charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened), [grappled](Compendium/rules/conditions.md#Grappled), [paralyzed](Compendium/rules/conditions.md#Paralyzed), [petrified](Compendium/rules/conditions.md#Petrified), [prone](Compendium/rules/conditions.md#Prone), [restrained](Compendium/rules/conditions.md#Restrained), [stunned](Compendium/rules/conditions.md#Stunned)"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 30 ft. (blind beyond this radius), passive Perception 10"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The leeches can breathe air and water."
    "name": "Amphibious"
  - "desc": "For every handful of salt thrown on the swarm, it takes 3 (1d6) acid damage."
    "name": "Salt Susceptibility"
  - "desc": "The swarm has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on Dexterity (Stealth) checks made to hide in swampy terrain."
    "name": "Swamp Camouflage"
  - "desc": "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny leech. The swarm can't regain [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) or gain temporary [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Swarm"
"actions":
  - "desc": "Melee Weapon Attack: +2 to hit, reach 0 ft., one creature in the swarm's space. Hit: 10 (4d4) piercing damage, or 5 (2d4) piercing damage if the swarm has half of its [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) or fewer, and the swarm attaches to the target. While attached, the swarm doesn't attack. Instead, at the start of each of the swarm's turns, the target loses 10 (4d4) [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) due to blood loss, or 5 (2d4) if the swarm has half its [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) or fewer. The swarm can detach itself by spending 5 feet of its movement. It does so after it drains 20 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) of blood from the target or the target dies."
    "name": "Bites"
"source":
  - "TBVXVII"
"image": "Compendium/bestiary/miscellaneous/token/squelching-leeches-tbvxvii.webp"
```
^statblock
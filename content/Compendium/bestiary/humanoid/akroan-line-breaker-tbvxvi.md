---
title: Akroan Line Breaker
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxvi
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Akroan Line Breaker"]
---
# Akroan Line Breaker
*Source: Theros Bestiary TBVXVI*  

<small><blockquote>The enemies’ shields are the first to shatter, and their battle line is never far behind.</blockquote></small>

![Akroan Line Breaker](Compendium/bestiary/humanoid/img/akroan-line-breaker.webp#right|850)  

```statblock
"name": "Akroan Line Breaker (TBVXVI)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "20"
"ac_class": "plate, shield"
"hp": !!int "40"
"hit_dice": "8d8 + 8"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "15"
  - !!int "13"
  - !!int "11"
  - !!int "13"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "constitution": !!int "4"
"skillsaves":
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+5"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Survival](Compendium/rules/skills.md#Survival)"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": "Common, any two languages"
"cr": "5"
"traits":
  - "desc": "The warrior has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "The warrior's attack rolls score a critical hit on a roll of 19 or 20 on the d20."
    "name": "Improved Critical"
"actions":
  - "desc": "The warrior makes four attacks with its battleaxe."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +8 to hit, reach 5 ft., one target. _Hit:_ 6 (1d8 + 2) slashing damage."
    "name": "Battleaxe"
"reactions":
  - "desc": "Whenever the warrior is the target of a spell, that spell's caster chooses whether following happens: - Until the end of combat, the warrior gains a +2 bonus to damage rolls and Strength checks, and it gains 9 (2d8) temporary [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md). It chooses one creature that it can see within 30 feet of itself. If the target can see or hear the warrior, the target must succeed on a DC 11 Wisdom saving throw or be [frightened](Compendium/rules/conditions.md#Frightened) of the warrior until the end of the warrior's next turn. If the target succeeds on its saving throw, the warrior can't choose that target again for this reaction for 24 hours."
    "name": "Heroic"
"source":
  - "TBVXVI"
"image": "Compendium/bestiary/humanoid/token/akroan-line-breaker-tbvxvi.webp"
```
^statblock
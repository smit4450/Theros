---
title: Construct Spirit (Clay)
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xphb
- ttrpg-cli/monster/cr/
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Construct Spirit (Clay)"]
---
# Construct Spirit (Clay)
*Source: Player's Handbook (2024) p. 324*  

```statblock
"name": "Construct Spirit (Clay) (XPHB)"
"size": "Medium"
"type": "construct"
"alignment": "Neutral"
"ac_class": "13 + the spell's level"
"modifier": !!int "0"
"stats":
  - !!int "18"
  - !!int "10"
  - !!int "18"
  - !!int "14"
  - !!int "11"
  - !!int "5"
"speed": "30 ft."
"damage_resistances": "poison"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](Compendium/rules/conditions.md#Frightened), [paralyzed](Compendium/rules/conditions.md#Paralyzed),\
  \ [poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Understands the languages you know"
"actions":
  - "desc": "The spirit makes a number of Slam attacks equal to half this spell's\
      \ level (round down)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 1d8 + 4 + the spell's level Bludgeoning damage."
    "name": "Slam"
"reactions":
  - "desc": "Trigger: The spirit takes damage from a creature. _Response:_ The spirit\
      \ makes a Slam attack against that creature if possible, or the spirit moves\
      \ up to half its Speed toward that creature without provoking [Opportunity Attacks](Compendium/rules/actions.md#Opportunity%20Attack)."
    "name": "Berserk Lashing"
"source":
  - "XPHB"
```
^statblock
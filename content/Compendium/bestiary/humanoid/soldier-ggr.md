---
title: Soldier
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/ggr
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
aliases: ["Soldier"]
---
# Soldier
*Source: Guildmasters' Guide to Ravnica p. 226, Mythic Odysseys of Theros*  

Soldiers are found in many of Ravnica's guilds. The soldier stat block represents a typical member of the rank and file, though weaponry and armor can vary.
```statblock
"name": "Soldier (GGR)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "[chain mail](Compendium/items/chain-mail-xphb.md), [shield](Compendium/items/shield-xphb.md)"
"hp": !!int "16"
"hit_dice": "3d8 + 3"
"modifier": !!int "1"
"stats":
  - !!int "13"
  - !!int "12"
  - !!int "12"
  - !!int "10"
  - !!int "11"
  - !!int "11"
"speed": "30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+2"
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+3"
"senses": "passive Perception 12"
"languages": "any one language (usually Common)"
"cr": "1/2"
"traits":
  - "desc": "The soldier has advantage on saving throws against being [charmed](Compendium/rules/conditions.md#Charmed),\
      \ [frightened](Compendium/rules/conditions.md#Frightened), [grappled](Compendium/rules/conditions.md#Grappled),\
      \ or [restrained](Compendium/rules/conditions.md#Restrained) while it is within\
      \ 5 feet of at least one ally."
    "name": "Formation Tactics"
"actions":
  - "desc": "The soldier makes two melee attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 6\
      \ (1d8 + 2) slashing damage, or 7 (1d10 + 2) slashing damage if used with\
      \ two hands."
    "name": "Longsword"
"source":
  - "GGR"
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/soldier-ggr.webp"
```
^statblock
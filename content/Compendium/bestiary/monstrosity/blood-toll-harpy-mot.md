---
title: Blood-Toll Harpy
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/1-8
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Blood-Toll Harpy"]
---
# Blood-Toll Harpy
*Source: Mythic Odysseys of Theros p. 227*  

![](Compendium/bestiary/monstrosity/img/blood-toll-harpy.webp#right|850)  
Murderous gangs of harpies collect in grim places across Theros, preying on any who pass by. Many merchants face regular losses at the harpies' claws, common casualties often referred to as a "blood toll."

Cruel, corpse-eating creatures, harpies endlessly seek their next meal, careless of whether it comes from the living or the dead. With equal zeal, these vicious scavengers set upon travelers or claw open fresh graves, stripping bodies of riches and flesh. Then they carry back any treasures or appealing bones they find to reeking nests situated in cramped caves or rotten trees.
```statblock
"name": "Blood-Toll Harpy (MOT)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "11"
"hp": !!int "9"
"hit_dice": "2d8"
"modifier": !!int "1"
"stats":
  - !!int "12"
  - !!int "13"
  - !!int "10"
  - !!int "6"
  - !!int "11"
  - !!int "13"
"speed": "20 ft., fly 40 ft."
"skillsaves":
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "1/8"
"traits":
  - "desc": "The harpy has advantage on melee attack rolls against any creature that\
      \ doesn't have all its hit points."
    "name": "Blood Frenzy"
  - "desc": "The harpy has advantage on saving throws against being [charmed](Compendium/rules/conditions.md#Charmed)\
      \ or [frightened](Compendium/rules/conditions.md#Frightened)."
    "name": "Dark Devotion"
"actions":
  - "desc": "The harpy makes two melee attacks: one with its bite and one with its\
      \ claws."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 3\
      \ (1d4 + 1) piercing damage."
    "name": "Bite"
  - "desc": "*Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 3\
      \ (1d4 + 1) slashing damage."
    "name": "Claws"
"source":
  - "MOT"
"image": "Compendium/bestiary/monstrosity/token/blood-toll-harpy-mot.webp"
```
^statblock
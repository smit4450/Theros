---
title: Priest of Iroas
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxv
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Priest of Iroas"]
---
# Priest of Iroas
*Source: Theros Bestiary TBVXXV*  

<blockquote><small>“Even my last breath will be a blow struck for Iroas.”</small></blockquote>

![Priest of Iroas](Compendium/bestiary/humanoid/img/priest-of-iroas.webp#right)  

```statblock
"name": "Priest of Iroas (TBVXXV)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "10"
"hp": !!int "35"
"hit_dice": "7d8 + 7"
"modifier": !!int "0"
"stats":
  - !!int "11"
  - !!int "11"
  - !!int "13"
  - !!int "14"
  - !!int "13"
  - !!int "14"
"speed": "30 ft."
"skillsaves":
  - "name": "[Medicine](Compendium/rules/skills.md#Medicine)"
    "desc": "+5"
  - "name": "[Persuasion](Compendium/rules/skills.md#Persuasion)"
    "desc": "+5"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+6"
"senses": "passive Perception 10"
"languages": "Common, any two languages"
"cr": "2"
"traits":
  - "desc": "As a bonus action, the priest can expend a spell slot to cause its melee weapon attacks to magically deal an extra 10 (3d6) radiant damage to a target on a hit. This benefit lasts until the end of the turn. If the priest expends a spell slot of 2nd level or higher, the extra damage increases by 1d6 for each level above 1st."
    "name": "Divine Eminence"
  - "desc": "The priest is a 7th-level spellcaster. The priest's spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). The priest has the following cleric spells prepared: Cantrip (at will): _guidance_, _light_, _sacred flame_, _thaumaturgy_ 1st level (4 slots): _bane_, _cure wounds_, _divine favor_, _guiding bolt_, _sanctuary_, _shield of faith_ 2nd level (3 slots): _lesser restoration_, _magic weapon_, _spiritual weapon_ 3rd level (3 slots): _dispel magic_, _spirit guardians_ 4th level (1 slot): _divination_, _freedom of movement_, _stoneskin_"
    "name": "Spellcasting"
  - "desc": "As a bonus action, the priest can cast _dispel magic_ even if it has no spell slots left. The components for the spell if cast this way are replaced with a deep exhalation that kills the priest."
    "name": "Last Breath"
"actions":
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 3 (1d6) bludgeoning damage."
    "name": "Mace"
"source":
  - "TBVXXV"
"image": "Compendium/bestiary/humanoid/token/priest-of-iroas-tbvxxv.webp"
```
^statblock
---
title: Priest of Iroas
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxv
- monster/cr/2
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Priest of Iroas"]
---
# Priest of Iroas
*Source: Theros Bestiary TBVXXV*  

<blockquote><small>“Even my last breath will be a blow struck for Iroas.”</small></blockquote>

![Priest of Iroas](Homebrew/bestiary/humanoid/img/priest-of-iroas.webp#right|850)  

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
  - "name": "[[skills#Medicine|Medicine]]"
    "desc": "+5"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+5"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+6"
"senses": "passive Perception 10"
"languages": "Common, any two languages"
"cr": "2"
"traits":
  - "desc": "As a bonus action, the priest can expend a spell slot to cause its melee weapon attacks to magically deal an extra 10 (3d6) radiant damage to a target on a hit. This benefit lasts until the end of the turn. If the priest expends a spell slot of 2nd level or higher, the extra damage increases by 1d6 for each level above 1st."
    "name": "Divine Eminence"
  - "desc": "The priest is a 7th-level spellcaster. The priest's spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). The priest has the following cleric spells prepared: Cantrip (at will): _guidance_, [[light-xphb|Light]], [[sacred-flame-xphb|Sacred Flame]], [[thaumaturgy-xphb|Thaumaturgy]] 1st level (4 slots): _bane_, [[cure-wounds-xphb|Cure Wounds]], [[divine-favor-xphb|Divine Favor]], [[guiding-bolt-xphb|Guiding Bolt]], [[sanctuary-xphb|Sanctuary]], [[shield-of-faith-xphb|Shield Of Faith]] 2nd level (3 slots): [[lesser-restoration-xphb|Lesser Restoration]], [[magic-weapon-xphb|Magic Weapon]], [[spiritual-weapon-xphb|Spiritual Weapon]] 3rd level (3 slots): [[dispel-magic-xphb|Dispel Magic]], [[spirit-guardians-xphb|Spirit Guardians]] 4th level (1 slot): [[divination-xphb|Divination]], [[freedom-of-movement-xphb|Freedom Of Movement]], [[stoneskin-xphb|Stoneskin]]"
    "name": "Spellcasting"
  - "desc": "As a bonus action, the priest can cast [[dispel-magic-xphb|Dispel Magic]] even if it has no spell slots left. The components for the spell if cast this way are replaced with a deep exhalation that kills the priest."
    "name": "Last Breath"
"actions":
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 3 (1d6) bludgeoning damage."
    "name": "Mace"
"source":
  - "TBVXXV"
"image": "Homebrew/bestiary/humanoid/token/priest-of-iroas-tbvxxv.webp"
```
^statblock
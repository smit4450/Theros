---
title: Tethmos High Priest
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxix
- monster/cr/3
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Tethmos High Priest"]
---
# Tethmos High Priest
*Source: Theros Bestiary TBVXIX*  

<small><blockquote>“Death is tyranny. Like all tyranny, it must be opposed.”</blockquote></small>

![Tethmos High Priest](Homebrew/bestiary/humanoid/img/tethmos-high-priest.webp#right)  

```statblock
"name": "Tethmos High Priest (TBVXIX)"
"size": "Medium"
"type": "humanoid"
"subtype": "leonin"
"alignment": "Lawful Evil"
"ac": !!int "11"
"ac_class": "padded"
"hp": !!int "126"
"hit_dice": "18d8 + 54"
"modifier": !!int "0"
"stats":
  - !!int "15"
  - !!int "10"
  - !!int "16"
  - !!int "11"
  - !!int "15"
  - !!int "13"
"speed": "35 ft."
"saves":
  - "constitution": !!int "5"
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+3"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+2"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": "Common, Leonin, Any one language"
"cr": "3"
"traits":
  - "desc": "As a bonus action, the priest can let out an especially menacing roar. Creatures of it chooses within 10 feet of itself that can hear it must succeed on a DC 13 Wisdom saving throw or become [[conditions#Frightened|frightened]] of it until the end of the priest's next turn."
    "name": "Daunting Roar (Recharges after a Short or Long Rest)"
  - "desc": "Whenever the priest becomes targeted by a spell, that spell's caster chooses whether the priest may use a bonus action to cast [[raise-dead-xphb|Raise Dead]] targeting a leonin, requiring no components or spell slots."
    "name": "Heroic"
  - "desc": "The priest is a 9th-level spellcaster. The priest's spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). The priest has the following cleric spells prepared: Cantrip (at will): [[light-xphb|Light]], [[mending-xphb|Mending]], [[sacred-flame-xphb|Sacred Flame]], [[spare-the-dying-xphb|Spare The Dying]] 1st level (4 slots): [[divine-favor-xphb|Divine Favor]], [[guiding-bolt-xphb|Guiding Bolt]], [[healing-word-xphb|Healing Word]], [[shield-of-faith-xphb|Shield Of Faith]] 2nd level (3 slots): [[lesser-restoration-xphb|Lesser Restoration]], [[magic-weapon-xphb|Magic Weapon]], [[prayer-of-healing-xphb|Prayer Of Healing]], [[silence-xphb|Silence]], [[spiritual-weapon-xphb|Spiritual Weapon]] 3rd level (3 slots): [[beacon-of-hope-xphb|Beacon Of Hope]], _crusader's mantle_, [[dispel-magic-xphb|Dispel Magic]], [[revivify-xphb|Revivify]], [[spirit-guardians-xphb|Spirit Guardians]], _wall of water_ 4th level (3 slots): [[banishment-xphb|Banishment]], [[freedom-of-movement-xphb|Freedom Of Movement]], [[guardian-of-faith-xphb|Guardian Of Faith]], [[stoneskin-xphb|Stoneskin]] 5th level (1 slots): [[flame-strike-xphb|Flame Strike]], [[mass-cure-wounds-xphb|Mass Cure Wounds]], [[hold-monster-xphb|Hold Monster]]"
    "name": "Spellcasting"
"actions":
  - "desc": "The priest makes two melee attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."
    "name": "Claws"
  - "desc": "_Melee Weapon Attack:_ +6 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) bludgeoning damage."
    "name": "Quarterstaff"
"reactions":
  - "desc": "The priest grants a +10 bonus to an attack roll made by itself or another creature within 30 feet of it. The priest can make this choice after the roll is made but before it hits or misses."
    "name": "Guided Strike (1/Rest)"
"source":
  - "TBVXIX"
"image": "Homebrew/bestiary/humanoid/token/tethmos-high-priest-tbvxix.webp"
```
^statblock
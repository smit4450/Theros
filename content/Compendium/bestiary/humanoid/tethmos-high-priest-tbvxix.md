---
title: Tethmos High Priest
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxix
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Tethmos High Priest"]
---
# Tethmos High Priest
*Source: Theros Bestiary TBVXIX*  

<small><blockquote>“Death is tyranny. Like all tyranny, it must be opposed.”</blockquote></small>

![Tethmos High Priest](https://img.scryfall.com/cards/art_crop/front/d/9/d901b9d7-6af9-40ce-afb7-d3c9f9143c18.jpg?1593095373#right)  

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
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+3"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+2"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": "Common, Leonin, Any one language"
"cr": "3"
"traits":
  - "desc": "As a bonus action, the priest can let out an especially menacing roar. Creatures of it chooses within 10 feet of itself that can hear it must succeed on a DC 13 Wisdom saving throw or become [frightened](Compendium/rules/conditions.md#Frightened) of it until the end of the priest's next turn."
    "name": "Daunting Roar (Recharges after a Short or Long Rest)"
  - "desc": "Whenever the priest becomes targeted by a spell, that spell's caster chooses whether the priest may use a bonus action to cast [Raise Dead](Compendium/spells/raise-dead-xphb.md) targeting a leonin, requiring no components or spell slots."
    "name": "Heroic"
  - "desc": "The priest is a 9th-level spellcaster. The priest's spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). The priest has the following cleric spells prepared: Cantrip (at will): [Light](Compendium/spells/light-xphb.md), [Mending](Compendium/spells/mending-xphb.md), [Sacred Flame](Compendium/spells/sacred-flame-xphb.md), [Spare The Dying](Compendium/spells/spare-the-dying-xphb.md) 1st level (4 slots): [Divine Favor](Compendium/spells/divine-favor-xphb.md), [Guiding Bolt](Compendium/spells/guiding-bolt-xphb.md), [Healing Word](Compendium/spells/healing-word-xphb.md), [Shield Of Faith](Compendium/spells/shield-of-faith-xphb.md) 2nd level (3 slots): [Lesser Restoration](Compendium/spells/lesser-restoration-xphb.md), [Magic Weapon](Compendium/spells/magic-weapon-xphb.md), [Prayer Of Healing](Compendium/spells/prayer-of-healing-xphb.md), [Silence](Compendium/spells/silence-xphb.md), [Spiritual Weapon](Compendium/spells/spiritual-weapon-xphb.md) 3rd level (3 slots): [Beacon Of Hope](Compendium/spells/beacon-of-hope-xphb.md), _crusader's mantle_, [Dispel Magic](Compendium/spells/dispel-magic-xphb.md), [Revivify](Compendium/spells/revivify-xphb.md), [Spirit Guardians](Compendium/spells/spirit-guardians-xphb.md), _wall of water_ 4th level (3 slots): [Banishment](Compendium/spells/banishment-xphb.md), [Freedom Of Movement](Compendium/spells/freedom-of-movement-xphb.md), [Guardian Of Faith](Compendium/spells/guardian-of-faith-xphb.md), [Stoneskin](Compendium/spells/stoneskin-xphb.md) 5th level (1 slots): [Flame Strike](Compendium/spells/flame-strike-xphb.md), [Mass Cure Wounds](Compendium/spells/mass-cure-wounds-xphb.md), [Hold Monster](Compendium/spells/hold-monster-xphb.md)"
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
"image": "Compendium/bestiary/humanoid/token/tethmos-high-priest-tbvxix.webp"
```
^statblock
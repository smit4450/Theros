---
title: Setessan Battle Priest
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxvi
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Setessan Battle Priest"]
---
# Setessan Battle Priest
*Source: Theros Bestiary TBVXVI*  

<small><blockquote>"Your god teaches you only how to kill. Karametra teaches me to defend what I hold dear. That is why I will prevail."</blockquote></small>

![Setessan Battle Priest](https://img.scryfall.com/cards/art_crop/front/9/c/9c9cfa33-dcec-4b34-9218-c08ad932d27b.jpg?1562822261#right)  

```statblock
"name": "Setessan Battle Priest (TBVXVI)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Lawful Evil"
"ac": !!int "18"
"ac_class": "plate"
"hp": !!int "108"
"hit_dice": "18d8 + 36"
"modifier": !!int "0"
"stats":
  - !!int "17"
  - !!int "11"
  - !!int "15"
  - !!int "12"
  - !!int "18"
  - !!int "14"
"speed": "30 ft."
"saves":
  - "constitution": !!int "6"
  - "wisdom": !!int "8"
"skillsaves":
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+6"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": "Common, Any one language"
"cr": "10"
"traits":
  - "desc": "The war priest is a 9th-level spellcaster. It's spellcasting ability is Wisdom (spell save DC 15, +7 to hit with spell attacks). It has the following cleric spells prepared: Cantrip (at will): [Light](Compendium/spells/light-xphb.md), [Mending](Compendium/spells/mending-xphb.md), [Sacred Flame](Compendium/spells/sacred-flame-xphb.md), [Spare The Dying](Compendium/spells/spare-the-dying-xphb.md) 1st level (4 slots): [Divine Favor](Compendium/spells/divine-favor-xphb.md), [Guiding Bolt](Compendium/spells/guiding-bolt-xphb.md), [Healing Word](Compendium/spells/healing-word-xphb.md), [Shield Of Faith](Compendium/spells/shield-of-faith-xphb.md) 2nd level (3 slots): [Lesser Restoration](Compendium/spells/lesser-restoration-xphb.md), [Magic Weapon](Compendium/spells/magic-weapon-xphb.md), [Prayer Of Healing](Compendium/spells/prayer-of-healing-xphb.md), [Silence](Compendium/spells/silence-xphb.md), [Spiritual Weapon](Compendium/spells/spiritual-weapon-xphb.md) 3rd level (3 slots): [Beacon Of Hope](Compendium/spells/beacon-of-hope-xphb.md), _crusader's mantle_, [Dispel Magic](Compendium/spells/dispel-magic-xphb.md), [Revivify](Compendium/spells/revivify-xphb.md), [Spirit Guardians](Compendium/spells/spirit-guardians-xphb.md), _wall of water_ 4th level (3 slots): [Banishment](Compendium/spells/banishment-xphb.md), [Freedom Of Movement](Compendium/spells/freedom-of-movement-xphb.md), [Guardian Of Faith](Compendium/spells/guardian-of-faith-xphb.md), [Stoneskin](Compendium/spells/stoneskin-xphb.md) 5th level (1 slots): [Flame Strike](Compendium/spells/flame-strike-xphb.md), [Mass Cure Wounds](Compendium/spells/mass-cure-wounds-xphb.md), [Hold Monster](Compendium/spells/hold-monster-xphb.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "The war priest makes two melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 5 ft., one creature. _Hit:_ 10 (2d6 + 3) bludgeoning damage."
    "name": "Maul"
"reactions":
  - "desc": "The priest grants a +10 bonus to an attack roll made by itself or another creature within 30 feet of it. The priest can make this choice after the roll is made but before it hits or misses."
    "name": "Guided Strike (1/Rest)"
  - "desc": "Whenever a spell targets the priest, that spell's caster chooses whether the priest regains 16 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Heroic"
"source":
  - "TBVXVI"
"image": "Compendium/bestiary/humanoid/token/setessan-battle-priest-tbvxvi.webp"
```
^statblock
---
title: War Priest
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
aliases: ["War Priest"]
---
# War Priest
*Source: Volo's Guide to Monsters p. 218, Mythic Odysseys of Theros*  

War priests worship deities of war and combat. They plan tactics, lead soldiers into battle, confront enemy spellcasters, and tend to casualties. A war priest might command an army or serve as a warlord's right hand on the battlefield.
```statblock
"name": "War Priest (VGM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "[plate armor](Compendium/items/plate-armor-xphb.md)"
"hp": !!int "117"
"hit_dice": "18d8 + 36"
"modifier": !!int "0"
"stats":
  - !!int "16"
  - !!int "10"
  - !!int "14"
  - !!int "11"
  - !!int "17"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "constitution": !!int "6"
  - "wisdom": !!int "7"
"skillsaves":
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+5"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+4"
"senses": "passive Perception 13"
"languages": "any two languages"
"cr": "9"
"traits":
  - "desc": "The priest is a 9th-level spellcaster. Its spellcasting ability is Wisdom\
      \ (spell save DC 15, +7 to hit with spell attacks). It has the following cleric\
      \ spells prepared:\n\n**Cantrips (at will):** [light](Compendium/spells/light-xphb.md),\
      \ [mending](Compendium/spells/mending-xphb.md), [sacred flame](Compendium/spells/sacred-flame-xphb.md),\
      \ [spare the dying](Compendium/spells/spare-the-dying-xphb.md)\n\n**1st level\
      \ (4 slots):** [divine favor](Compendium/spells/divine-favor-xphb.md), [guiding\
      \ bolt](Compendium/spells/guiding-bolt-xphb.md), [healing word](Compendium/spells/healing-word-xphb.md),\
      \ [shield of faith](Compendium/spells/shield-of-faith-xphb.md)\n\n**2nd level\
      \ (3 slots):** [lesser restoration](Compendium/spells/lesser-restoration-xphb.md),\
      \ [magic weapon](Compendium/spells/magic-weapon-xphb.md), [prayer of healing](Compendium/spells/prayer-of-healing-xphb.md),\
      \ [silence](Compendium/spells/silence-xphb.md), [spiritual weapon](Compendium/spells/spiritual-weapon-xphb.md)\n\
      \n**3rd level (3 slots):** [beacon of hope](Compendium/spells/beacon-of-hope-xphb.md),\
      \ [crusader's mantle](Compendium/spells/crusaders-mantle-xphb.md), [dispel magic](Compendium/spells/dispel-magic-xphb.md),\
      \ [revivify](Compendium/spells/revivify-xphb.md), [spirit guardians](Compendium/spells/spirit-guardians-xphb.md),\
      \ [water walk](Compendium/spells/water-walk-xphb.md)\n\n**4th level (3 slots):**\
      \ [banishment](Compendium/spells/banishment-xphb.md), [freedom of movement](Compendium/spells/freedom-of-movement-xphb.md),\
      \ [guardian of faith](Compendium/spells/guardian-of-faith-xphb.md), [stoneskin](Compendium/spells/stoneskin-xphb.md)\n\
      \n**5th level (1 slots):** [flame strike](Compendium/spells/flame-strike-xphb.md),\
      \ [mass cure wounds](Compendium/spells/mass-cure-wounds-xphb.md), [hold monster](Compendium/spells/hold-monster-xphb.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "The priest makes two melee attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 10\
      \ (2d6 + 3) bludgeoning damage."
    "name": "Maul"
"reactions":
  - "desc": "The priest grants a +10 bonus to an attack roll made by itself or another\
      \ creature within 30 feet of it. The priest can make this choice after the roll\
      \ is made but before it hits or misses."
    "name": "Guided Strike (Recharges after a Short or Long Rest)"
"source":
  - "VGM"
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/war-priest-vgm.webp"
```
^statblock
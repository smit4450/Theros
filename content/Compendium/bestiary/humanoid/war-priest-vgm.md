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
"ac_class": "[[plate-armor-xphb|plate armor]]"
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
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+5"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+4"
"senses": "passive Perception 13"
"languages": "any two languages"
"cr": "9"
"traits":
  - "desc": "The priest is a 9th-level spellcaster. Its spellcasting ability is Wisdom\
      \ (spell save DC 15, +7 to hit with spell attacks). It has the following cleric\
      \ spells prepared:\n\n**Cantrips (at will):** [[light-xphb|light]],\
      \ [[mending-xphb|mending]], [[sacred-flame-xphb|sacred flame]],\
      \ [[spare-the-dying-xphb|spare the dying]]\n\n**1st level\
      \ (4 slots):** [[divine-favor-xphb|divine favor]], [[guiding-bolt-xphb|guiding\
      \ bolt]], [[healing-word-xphb|healing word]],\
      \ [[shield-of-faith-xphb|shield of faith]]\n\n**2nd level\
      \ (3 slots):** [[lesser-restoration-xphb|lesser restoration]],\
      \ [[magic-weapon-xphb|magic weapon]], [[prayer-of-healing-xphb|prayer of healing]],\
      \ [[silence-xphb|silence]], [[spiritual-weapon-xphb|spiritual weapon]]\n\
      \n**3rd level (3 slots):** [[beacon-of-hope-xphb|beacon of hope]],\
      \ [[crusaders-mantle-xphb|crusader's mantle]], [[dispel-magic-xphb|dispel magic]],\
      \ [[revivify-xphb|revivify]], [[spirit-guardians-xphb|spirit guardians]],\
      \ [[water-walk-xphb|water walk]]\n\n**4th level (3 slots):**\
      \ [[banishment-xphb|banishment]], [[freedom-of-movement-xphb|freedom of movement]],\
      \ [[guardian-of-faith-xphb|guardian of faith]], [[stoneskin-xphb|stoneskin]]\n\
      \n**5th level (1 slots):** [[flame-strike-xphb|flame strike]],\
      \ [[mass-cure-wounds-xphb|mass cure wounds]], [[hold-monster-xphb|hold monster]]"
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
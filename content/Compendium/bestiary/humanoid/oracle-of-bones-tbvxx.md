---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxx
- monster/cr/1
- monster/size/medium
- monster/type/humanoid/minotaur
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Oracle of Bones"
---
# Oracle of Bones
*Source: Theros Bestiary, Vol. XX*
![](/Compendium/bestiary/humanoid/img/oracle-of-bones.webp#center)

```statblock
"name": "Oracle of Bones"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "blessings of the gods"
"hp": !!int "5"
"hit_dice": "1d8 + 1"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "14"
  - !!int "13"
  - !!int "13"
  - !!int "16"
  - !!int "15"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "5"
  - "charisma": !!int "4"
"skillsaves":
  - "name": "[Insight](/Compendium/rules/skills.md#Insight)"
    "desc": "+5"
  - "name": "[Persuasion](/Compendium/rules/skills.md#Persuasion)"
    "desc": "+4"
  - "name": "[Religion](/Compendium/rules/skills.md#Religion)"
    "desc": "+5"
  - "name": "[Intimidation](/Compendium/rules/skills.md#Intimidation)"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": "Celestial, Common, Minotaur"
"cr": "1"
"traits":
  - "desc": "The oracle has Advantage on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "While the oracle is wearing no armor and wielding no shield, its AC includes\
      \ its Wisdom modifier. In addition, a creature that hits the oracle with a melee\
      \ attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Just the oracle seeks insights from interpreting the divine, so too do\
      \ the gods occasionally seek to manipulate the world through the oracle. Sometimes\
      \ the gods might speak directly, be it with dramatic manifestations or direct\
      \ possession of the oracle. Although the gods' words might be steeped in metaphors,\
      \ should they wish to make their intentions clear, they often find dramatic\
      \ ways to make their thoughts known."
    "name": "Divine Influence"
  - "desc": "Immediately after the oracle uses the Dash action on its turn and moves\
      \ at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "The oracle possesses unparalleled experience in divining godly whims\
      \ from cryptic visions and mundane forces"
    "name": "Interpreter of Signs"
  - "desc": "The oracle of bones is a 9th-level spellcaster. The oracle of bones's\
      \ spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks).\
      \ The oracle of bones has the following cleric spells prepared: Cantrip (at\
      \ will): _guidance_, Sacred Flame, Spare The Dying 2nd level (3 slots): Augury\
      \ 4th level (3 slots): Divination 5th level (1 slots): _commune_"
    "name": "Spellcasting"
"actions":
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6\
      \ + 3) piercing damage, and the oracle can use a bonus action to attempt to\
      \ shove that target with its horns. The target must be within 5 feet of the\
      \ oracle and no more than one size larger than it. Unless the target succeeds\
      \ on a DC 13 Strength saving throw, the oracle pushes it up to 10 feet away\
      \ from the oracle."
    "name": "Horns"
"reactions":
  - "desc": "When the oracle or a creature it can see makes an attack roll, a saving\
      \ throw, or an ability check, the oracle can cause the roll to be made with\
      \ Advantage or Disadvantage."
    "name": "Divine Insight (3/Day)"
  - "desc": "Immediately after initiative rolls in which the oracle participates,\
      \ it demands tribute from a creature it can see. That creature may bow, genuflect,\
      \ salute, or perform a similar gesture as a bonus action. If tribute is paid:\
      \ Until the end of combat, the oracle gains a +2 bonus to damage rolls and Strength\
      \ and Dexterity checks, and 9 (2d8) temporary Hit Points. If tribute isn't paid:\
      \ The oracle casts a Sacred Flame on that creature."
    "name": "Demand Tribute"
"source":
  - "TBVXX"
```
^statblock
---
title: War Oracle
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxx
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["War Oracle"]
---
# War Oracle
*Source: Theros Bestiary TBVXX*  

<blockquote><small>"When you are felled by my mace, you shall know it was divine fate."</small></blockquote>

![War Oracle](https://c1.scryfall.com/file/scryfall-cards/art_crop/front/3/d/3d8827bf-11c3-4f78-b7aa-ae953442c709.jpg?1562015872#right)  

```statblock
"name": "War Oracle (TBVXX)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Lawful Evil"
"ac": !!int "21"
"ac_class": "blessings of the gods, plate"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "15"
  - !!int "16"
  - !!int "14"
  - !!int "17"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "6"
  - "charisma": !!int "6"
  - "constitution": !!int "6"
"skillsaves":
  - "name": "[Insight](Compendium/rules/skills.md#Insight)"
    "desc": "+6"
  - "name": "[Persuasion](Compendium/rules/skills.md#Persuasion)"
    "desc": "+6"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+7"
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+6"
"senses": "passive Perception 10"
"languages": "Celestial, Common, any one language"
"cr": "5"
"traits":
  - "desc": "While the oracle is wearing no armor and wielding no shield, its AC includes its Wisdom modifier. In addition, a creature that hits the oracle with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Just as oracle seeks insights from interpreting the divine, so too do gods occasionally seek to manipulate the world through the oracle. Sometimes a god might speak directly, be it with dramatic manifestations or direct possession of the oracle. Although a deity’s words might be steeped in metaphors, should a god wish to make their intentions clear, they often find dramatic ways to make their thoughts known."
    "name": "Divine Influence"
  - "desc": "The oracle's innate spellcasting ability is Wisdom (spell save DC 15, +7 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: _guidance_, _light_, _thaumaturgy_ 3/day: _bless_, _guiding bolt_, _healing word_, _hold person_ 1/day: _augury_, _scrying_"
    "name": "Innate Spellcasting"
  - "desc": "Oracles possess unparalleled experience in divining godly whims from cryptic visions and mundane forces. Those who receive divine omens (such as those presented in chapter 4) might seek out an oracle to gain a clearer vision of the god’s intentions. Finding an oracle, though, or one experienced in interpreting certain types of visions, might prove to be an adventure in its own right."
    "name": "Interpreter of Signs"
  - "desc": "The oracle's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The oracle is a 9th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 15, +7 to hit with spell attacks). It has the following cleric spells prepared: Cantrip (at will): _mending_, _sacred flame_, _spare the dying_ 1st level (4 slots): _divine favor_, _shield of faith_ 2nd level (3 slots): _lesser restoration_, _magic weapon_, _prayer of healing_, _silence_, _spiritual weapon_ 3rd level (3 slots): _beacon of hope_, _crusader's mantle_, _dispel magic_, _revivify_, _spirit guardians_, _wall of water_ 4th level (3 slots): _banishment_, _freedom of movement_, _guardian of faith_, _stoneskin_ 5th level (1 slots): _flame strike_, _mass cure wounds_, _hold monster_"
    "name": "Spellcasting"
"actions":
  - "desc": "The oracle makes two melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +8 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6 + 3) force damage, and it regains that many hit points."
    "name": "Eldritch Mace"
"reactions":
  - "desc": "When the oracle or a creature it can see makes an attack roll, a saving throw, or an ability check, the oracle can cause the roll to be made with advantage or disadvantage."
    "name": "Divine Insight (3/Day)"
  - "desc": "The oracle grants a +10 bonus to an attack roll made by itself or another creature within 30 feet of it. The oracle can make this choice after the roll is made but before it hits or misses."
    "name": "Guided Strike (1/Rest)"
"source":
  - "TBVXX"
"image": "Compendium/bestiary/humanoid/token/war-oracle-tbvxx.webp"
```
^statblock
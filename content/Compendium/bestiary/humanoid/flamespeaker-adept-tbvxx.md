---
title: Flamespeaker Adept
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxx
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Flamespeaker Adept"]
---
# Flamespeaker Adept
*Source: Theros Bestiary TBVXX*  

<blockquote><small>“I see your future, mantled in ash.”</small></blockquote>

![Flamespeaker Adept](Compendium/bestiary/humanoid/img/flamespeaker-adept.webp#right)  

```statblock
"name": "Flamespeaker Adept (TBVXX)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "blessings of the gods"
"hp": !!int "56"
"hit_dice": "8d8 + 24"
"modifier": !!int "2"
"stats":
  - !!int "11"
  - !!int "15"
  - !!int "16"
  - !!int "14"
  - !!int "15"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "4"
  - "charisma": !!int "5"
"skillsaves":
  - "name": "[Insight](Compendium/rules/skills.md#Insight)"
    "desc": "+4"
  - "name": "[Persuasion](Compendium/rules/skills.md#Persuasion)"
    "desc": "+5"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+5"
"damage_immunities": "fire"
"senses": "passive Perception 10"
"languages": "Celestial, Common, any one language"
"cr": "4"
"traits":
  - "desc": "While the oracle is wearing no armor and wielding no shield, its AC includes its Wisdom modifier. In addition, a creature that hits the oracle with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Just as oracles seek insights from interpreting the divine, so too do gods occasionally seek to manipulate the world through oracles. Sometimes a god might speak directly, be it with dramatic manifestations or direct possession of their servant. Although a deity’s words might be steeped in metaphors, should a god wish to make their intentions clear, they often find dramatic ways to make their thoughts known."
    "name": "Divine Influence"
  - "desc": "The flamespeaker must use a fiery ritual to for each of its spells and spell attacks, which deals 9 (2d8) magical fire damage to all creatures within 5 feet of it."
    "name": "Fiery Magic"
  - "desc": "The oracle's innate spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no material components (but an additional component is required; see Fiery Magic above): At will: _guidance_, _light_, _thaumaturgy_ 3/day: _bless_, _guiding bolt_, _healing word_, _hold person_ 1/day: _augury_, _scrying_"
    "name": "Innate Spellcasting"
  - "desc": "Oracles possess unparalleled experience in divining godly whims from cryptic visions and mundane forces. Those who receive divine omens might seek out an oracle to gain a clearer vision of the god’s intentions. Finding an oracle, though, or one experienced in interpreting certain types of visions, might prove to be an adventure in its own right."
    "name": "Interpreter of Signs"
"actions":
  - "desc": "Melee Spell Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) force damage. (See Fiery Magic above.)"
    "name": "Eldritch Touch"
"reactions":
  - "desc": "When the oracle or a creature it can see makes an attack roll, a saving throw, or an ability check, the oracle can cause the roll to be made with advantage or disadvantage."
    "name": "Divine Insight (3/Day)"
"source":
  - "TBVXX"
"image": "Compendium/bestiary/humanoid/token/flamespeaker-adept-tbvxx.webp"
```
^statblock
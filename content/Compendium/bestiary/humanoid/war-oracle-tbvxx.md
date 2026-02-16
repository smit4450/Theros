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
  - "desc": "The oracle's innate spellcasting ability is Wisdom (spell save DC 15, +7 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: _guidance_, [Light](Compendium/spells/light-xphb.md), [Thaumaturgy](Compendium/spells/thaumaturgy-xphb.md) 3/day: [Bless](Compendium/spells/bless-xphb.md), [Guiding Bolt](Compendium/spells/guiding-bolt-xphb.md), [Healing Word](Compendium/spells/healing-word-xphb.md), [Hold Person](Compendium/spells/hold-person-xphb.md) 1/day: [Augury](Compendium/spells/augury-xphb.md), [Scrying](Compendium/spells/scrying-xphb.md)"
    "name": "Innate Spellcasting"
  - "desc": "Oracles possess unparalleled experience in divining godly whims from cryptic visions and mundane forces. Those who receive divine omens (such as those presented in chapter 4) might seek out an oracle to gain a clearer vision of the god’s intentions. Finding an oracle, though, or one experienced in interpreting certain types of visions, might prove to be an adventure in its own right."
    "name": "Interpreter of Signs"
  - "desc": "The oracle's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The oracle is a 9th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 15, +7 to hit with spell attacks). It has the following cleric spells prepared: Cantrip (at will): [Mending](Compendium/spells/mending-xphb.md), [Sacred Flame](Compendium/spells/sacred-flame-xphb.md), [Spare The Dying](Compendium/spells/spare-the-dying-xphb.md) 1st level (4 slots): [Divine Favor](Compendium/spells/divine-favor-xphb.md), [Shield Of Faith](Compendium/spells/shield-of-faith-xphb.md) 2nd level (3 slots): [Lesser Restoration](Compendium/spells/lesser-restoration-xphb.md), [Magic Weapon](Compendium/spells/magic-weapon-xphb.md), [Prayer Of Healing](Compendium/spells/prayer-of-healing-xphb.md), [Silence](Compendium/spells/silence-xphb.md), [Spiritual Weapon](Compendium/spells/spiritual-weapon-xphb.md) 3rd level (3 slots): [Beacon Of Hope](Compendium/spells/beacon-of-hope-xphb.md), _crusader's mantle_, [Dispel Magic](Compendium/spells/dispel-magic-xphb.md), [Revivify](Compendium/spells/revivify-xphb.md), [Spirit Guardians](Compendium/spells/spirit-guardians-xphb.md), _wall of water_ 4th level (3 slots): [Banishment](Compendium/spells/banishment-xphb.md), [Freedom Of Movement](Compendium/spells/freedom-of-movement-xphb.md), [Guardian Of Faith](Compendium/spells/guardian-of-faith-xphb.md), [Stoneskin](Compendium/spells/stoneskin-xphb.md) 5th level (1 slots): [Flame Strike](Compendium/spells/flame-strike-xphb.md), [Mass Cure Wounds](Compendium/spells/mass-cure-wounds-xphb.md), [Hold Monster](Compendium/spells/hold-monster-xphb.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "The oracle makes two melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +8 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6 + 3) force damage, and it regains that many [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Eldritch Mace"
"reactions":
  - "desc": "When the oracle or a creature it can see makes an attack roll, a saving throw, or an ability check, the oracle can cause the roll to be made with [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) or [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md)."
    "name": "Divine Insight (3/Day)"
  - "desc": "The oracle grants a +10 bonus to an attack roll made by itself or another creature within 30 feet of it. The oracle can make this choice after the roll is made but before it hits or misses."
    "name": "Guided Strike (1/Rest)"
"source":
  - "TBVXX"
"image": "Compendium/bestiary/humanoid/token/war-oracle-tbvxx.webp"
```
^statblock
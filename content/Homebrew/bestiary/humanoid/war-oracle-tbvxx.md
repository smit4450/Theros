---
title: War Oracle
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxx
- monster/cr/5
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["War Oracle"]
---
# War Oracle
*Source: Theros Bestiary TBVXX*  

<blockquote><small>"When you are felled by my mace, you shall know it was divine fate."</small></blockquote>

![War Oracle](Homebrew/bestiary/humanoid/img/war-oracle.webp#right)  

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
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+6"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+6"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+7"
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+6"
"senses": "passive Perception 10"
"languages": "Celestial, Common, any one language"
"cr": "5"
"traits":
  - "desc": "While the oracle is wearing no armor and wielding no shield, its AC includes its Wisdom modifier. In addition, a creature that hits the oracle with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Just as oracle seeks insights from interpreting the divine, so too do gods occasionally seek to manipulate the world through the oracle. Sometimes a god might speak directly, be it with dramatic manifestations or direct possession of the oracle. Although a deity’s words might be steeped in metaphors, should a god wish to make their intentions clear, they often find dramatic ways to make their thoughts known."
    "name": "Divine Influence"
  - "desc": "The oracle's innate spellcasting ability is Wisdom (spell save DC 15, +7 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: _guidance_, [[light-xphb|Light]], [[thaumaturgy-xphb|Thaumaturgy]] 3/day: [[bless-xphb|Bless]], [[guiding-bolt-xphb|Guiding Bolt]], [[healing-word-xphb|Healing Word]], [[hold-person-xphb|Hold Person]] 1/day: [[augury-xphb|Augury]], [[scrying-xphb|Scrying]]"
    "name": "Innate Spellcasting"
  - "desc": "Oracles possess unparalleled experience in divining godly whims from cryptic visions and mundane forces. Those who receive divine omens (such as those presented in chapter 4) might seek out an oracle to gain a clearer vision of the god’s intentions. Finding an oracle, though, or one experienced in interpreting certain types of visions, might prove to be an adventure in its own right."
    "name": "Interpreter of Signs"
  - "desc": "The oracle's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The oracle is a 9th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 15, +7 to hit with spell attacks). It has the following cleric spells prepared: Cantrip (at will): [[mending-xphb|Mending]], [[sacred-flame-xphb|Sacred Flame]], [[spare-the-dying-xphb|Spare The Dying]] 1st level (4 slots): [[divine-favor-xphb|Divine Favor]], [[shield-of-faith-xphb|Shield Of Faith]] 2nd level (3 slots): [[lesser-restoration-xphb|Lesser Restoration]], [[magic-weapon-xphb|Magic Weapon]], [[prayer-of-healing-xphb|Prayer Of Healing]], [[silence-xphb|Silence]], [[spiritual-weapon-xphb|Spiritual Weapon]] 3rd level (3 slots): [[beacon-of-hope-xphb|Beacon Of Hope]], _crusader's mantle_, [[dispel-magic-xphb|Dispel Magic]], [[revivify-xphb|Revivify]], [[spirit-guardians-xphb|Spirit Guardians]], _wall of water_ 4th level (3 slots): [[banishment-xphb|Banishment]], [[freedom-of-movement-xphb|Freedom Of Movement]], [[guardian-of-faith-xphb|Guardian Of Faith]], [[stoneskin-xphb|Stoneskin]] 5th level (1 slots): [[flame-strike-xphb|Flame Strike]], [[mass-cure-wounds-xphb|Mass Cure Wounds]], [[hold-monster-xphb|Hold Monster]]"
    "name": "Spellcasting"
"actions":
  - "desc": "The oracle makes two melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +8 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6 + 3) force damage, and it regains that many [[hit-points-xphb|Hit Points]]."
    "name": "Eldritch Mace"
"reactions":
  - "desc": "When the oracle or a creature it can see makes an attack roll, a saving throw, or an ability check, the oracle can cause the roll to be made with [[advantage-xphb|Advantage]] or [[disadvantage-xphb|Disadvantage]]."
    "name": "Divine Insight (3/Day)"
  - "desc": "The oracle grants a +10 bonus to an attack roll made by itself or another creature within 30 feet of it. The oracle can make this choice after the roll is made but before it hits or misses."
    "name": "Guided Strike (1/Rest)"
"source":
  - "TBVXX"
"image": "Homebrew/bestiary/humanoid/token/war-oracle-tbvxx.webp"
```
^statblock
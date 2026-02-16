---
title: Pain Seer
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxx
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Pain Seer"]
---
# Pain Seer
*Source: Theros Bestiary TBVXX*  

<blockquote><small>Every twitching nerve and pulsing vein carries a message, discernible with the right tools.</small></blockquote>

![Pain Seer](https://img.scryfall.com/cards/art_crop/front/8/c/8ce8891f-b44c-4be4-878e-9fc45a9dc9cb.jpg?1593092076#right)  

```statblock
"name": "Pain Seer (TBVXX)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "blessings of the gods"
"hp": !!int "12"
"hit_dice": "2d8 + 4"
"modifier": !!int "2"
"stats":
  - !!int "14"
  - !!int "15"
  - !!int "15"
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
"damage_immunities": "force damage dealt by the gods when inflicting pain on itself"
"senses": "passive Perception 10"
"languages": "Celestial, Common, any one language"
"cr": "1"
"traits":
  - "desc": "While the oracle is wearing no armor and wielding no shield, its AC includes its Wisdom modifier. In addition, a creature that hits the oracle with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Just as oracles seek insights from interpreting the divine, so too do gods occasionally seek to manipulate the world through oracles. Sometimes a god might speak directly, be it with dramatic manifestations or direct possession of their servant. Although a deity’s words might be steeped in metaphors, should a god wish to make their intentions clear, they often find dramatic ways to make their thoughts known."
    "name": "Divine Influence"
  - "desc": "If damage was dealt to any creature since the seer's last turn, it may cast a spell it has prepared as its action."
    "name": "Inspired"
  - "desc": "Oracles possess unparalleled experience in divining godly whims from cryptic visions and mundane forces. Those who receive divine omens might seek out an oracle to gain a clearer vision of the god’s intentions. Finding an oracle, though, or one experienced in interpreting certain types of visions, might prove to be an adventure in its own right."
    "name": "Interpreter of Signs"
  - "desc": "The pain seer's innate spellcasting ability is Charisma (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no material components: 3/day: _commune_, [Divination](Compendium/spells/divination-xphb.md), [Scrying](Compendium/spells/scrying-xphb.md) 1/day: [Finger Of Death](Compendium/spells/finger-of-death-xphb.md), _symbol (pain)_"
    "name": "Innate Spellcasting"
  - "desc": "The pain seer can't cast spells except with its Inspired trait."
    "name": "Painful Magic"
"actions":
  - "desc": "_Melee or Ranged Weapon Attack:_ +4 to hit, reach 5 ft. or range 20/60 ft., one target. _Hit:_ 4 (1d4 + 2) piercing damage in melee, or 4 (1d4 + 2) piercing damage at range."
    "name": "Kauterion"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 4 (1d4 + 2) piercing damage and 4 (1d4 + 2) slashing damage."
    "name": "Agkistron"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 4 (1d4 + 2) piercing damage, or 4 (1d4 + 2) slashing damage if used with extreme precision to pry an exposed bone outward on a nonmoving target."
    "name": "Mochliskos"
"reactions":
  - "desc": "When the oracle or a creature it can see makes an attack roll, a saving throw, or an ability check, the oracle can cause the roll to be made with [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) or [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md)."
    "name": "Divine Insight (3/Day)"
"source":
  - "TBVXX"
"image": "Compendium/bestiary/humanoid/token/pain-seer-tbvxx.webp"
```
^statblock
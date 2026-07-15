---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxx
- monster/cr/5
- monster/size/medium
- monster/type/humanoid/human
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Prophetic Flamespeaker"
---
# Prophetic Flamespeaker
*Source: Theros Bestiary, Vol. XX*
![](/Compendium/bestiary/humanoid/img/prophetic-flamespeaker.webp#right)

Fire to destroy. Fire to create.

```statblock
"name": "Prophetic Flamespeaker"
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
  - !!int "13"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "3"
  - "charisma": !!int "5"
"skillsaves":
  - "name": "[Insight](/Compendium/rules/skills.md#Insight)"
    "desc": "+3"
  - "name": "[Persuasion](/Compendium/rules/skills.md#Persuasion)"
    "desc": "+5"
  - "name": "[Religion](/Compendium/rules/skills.md#Religion)"
    "desc": "+5"
"damage_immunities": "fire"
"senses": "passive Perception 10"
"languages": "Celestial, Common, any one language"
"cr": "5"
"traits":
  - "desc": "While the flamespeaker is wearing no armor and wielding no shield, its\
      \ AC includes its Wisdom modifier. In addition, a creature that hits the flamespeaker\
      \ with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Every time the flamespeaker deals damage, the fiery sparks create an\
      \ **anvilwrought golem** in an unoccupied space within 5 feet of the target.\
      \ The anvilwroughts are friendly to the flamespeaker."
    "name": "Creation"
  - "desc": "Just as oracles seek insights from interpreting the divine, so too does\
      \ Purphoros occasionally seek to manipulate the world through the flamespeaker.\
      \ Sometimes Purphoros might speak directly, be it with dramatic manifestations\
      \ or direct possession of his servant. Although Purphoros’s words might be steeped\
      \ in metaphors, should he wish to make his intentions clear, he often finds\
      \ dramatic ways to make his thoughts known."
    "name": "Divine Influence"
  - "desc": "The flamespeaker must use a fiery ritual to for each of its spells and\
      \ spell attacks, which deals 9 (2d8) magical fire damage to all creatures within\
      \ 5 feet of it."
    "name": "Fiery Magic"
  - "desc": "The flamespeaker's innate spellcasting ability is Wisdom (spell save\
      \ DC 12, +4 to hit with spell attacks). It can innately cast the following spells,\
      \ requiring no material components (but an additional component is required;\
      \ see Fiery Magic above): At will: _guidance_, Light, Thaumaturgy 3/day: Bless,\
      \ Guiding Bolt, Healing Word, Hold Person 1/day: Augury, Scrying"
    "name": "Innate Spellcasting"
  - "desc": "The flamespeaker possesses unparalleled experience in divining godly\
      \ whims from cryptic visions and mundane forces."
    "name": "Interpreter of Signs"
  - "desc": "The flamespeaker can move in and out of a Medium or smaller creature's\
      \ space. If it would, it uses a bonus action to attack that creature with its\
      \ eldritch touch. That creature must succeed on a DC 13 Constitution saving\
      \ throw or be knocked prone. If the creature succeeds, the flamespeaker can't\
      \ enter that space and must end its turn immediately. If the flamespeaker stops\
      \ on top of that creature, that creature becomes restrained until the flamespeaker\
      \ moves off it (escape DC 10)."
    "name": "Trample"
"actions":
  - "desc": "The flamespeaker makes two attacks."
    "name": "Multiattack"
  - "desc": "Melee Spell Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d6 +\
      \ 1) force damage. (See Fiery Magic above.)"
    "name": "Eldritch Touch"
"reactions":
  - "desc": "When the flamespeaker or a creature it can see makes an attack roll,\
      \ a saving throw, or an ability check, the flamespeaker can cause the roll to\
      \ be made with Advantage or Disadvantage."
    "name": "Divine Insight (3/Day)"
"source":
  - "TBVXX"
```
^statblock
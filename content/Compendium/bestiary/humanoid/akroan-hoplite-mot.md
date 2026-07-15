---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/mot
- monster/cr/3
- monster/size/medium
- monster/type/humanoid
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Akroan Hoplite"
---
# Akroan Hoplite
*Source: Mythic Odysseys of Theros p. 228*
![](/Compendium/bestiary/humanoid/img/hoplite.webp#right)

Akroan hoplites, also called stratians, number among the fiercest soldiers on Theros. They train relentlessly and possess unflinching resolve. In the annals of Akros, tales abound of squads of stratians that defended a key location against a much larger force or crept behind enemy lines and wreaked havoc in the opposing army.

Hoplites are highly trained warriors, versed not only in strategy and tactics but in the glorification of the warrior's spirit, the basis of an ethos that forges an unbreakable bond between members of a military unit. In combat, hoplites typically work in groups and use coordinated tactics to win victories.

The three Hoplite Unit Names tables present the sorts of titles used by hoplite contingents hailing from Theros's great poleis. Consider using these names for military forces characters encounter during their adventures or that they were once a part of.

**Akroan Hoplite Unit Names**

| D8 | Name |
|----|------|
| 1 | Spears of Iroas |
| 2 | Iron Fangs |
| 3 | Arrows of Anax |
| 4 | The Unbroken |
| 5 | Anvil of Purphoros |
| 6 | Skewering Squad |
| 7 | Shield of Akros |
| 8 | Cymede's Heart |
^akroan-hoplite-unit-names

**Meletian Hoplite Unit Names**

| D8 | Name |
|----|------|
| 1 | Kraken's Claw |
| 2 | Hands of Justice |
| 3 | Thassa's Spear |
| 4 | Ephara's Shield |
| 5 | Kindred of the Deep |
| 6 | Riders of Heliod |
| 7 | Keepers of Pyrgnos |
| 8 | The Skysworn |
^meletian-hoplite-unit-names

**Setessan Hoplite Unit Names**

| dice: d8 | Name |
|----------|------|
| 1 | Nylea's Arrows |
| 2 | The Watchers |
| 3 | Fangs of Ophis |
| 4 | The Swiftswords |
| 5 | Karametra's Wolves |
| 6 | Defenders of the Grove |
| 7 | Bronze Blades |
| 8 | The Jackals |
^setessan-hoplite-unit-names

```statblock
"name": "Akroan Hoplite"
"size": "Medium"
"type": "humanoid"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "breastplate, shield"
"hp": !!int "52"
"hit_dice": "8d8 + 16"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "16"
  - !!int "14"
  - !!int "11"
  - !!int "14"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "strength": !!int "5"
  - "dexterity": !!int "5"
"gear":
  - "spear"
"senses": "passive Perception 12"
"languages": "Common"
"cr": "3"
"traits":
  - "desc": "While the hoplite is holding a spear, other creatures provoke an opportunity\
      \ attack from the hoplite when they move within 5 feet of it. When the hoplite\
      \ hits a creature with an opportunity attack using its spear, the creature takes\
      \ an extra 4 (1d8) piercing damage, and the creature's speed becomes 0 for the\
      \ rest of the turn."
    "name": "Hold the Line"
"actions":
  - "desc": "The hoplite makes three melee attacks or two ranged attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Weapon Attack:* +5 to hit, reach 5 ft., or range 20/60\
      \ ft., one target. *Hit:* 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing\
      \ damage if used with two hands to make a melee attack."
    "name": "Spear"
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one creature. *Hit:* 5\
      \ (1d4 + 3) bludgeoning damage. If the target is a Medium or smaller creature,\
      \ it must succeed on a DC 13 Strength saving throw or be knocked [prone](/Compendium/rules/conditions.md#Prone)."
    "name": "Shield Bash"
"source":
  - "MOT"
"image": "/Compendium/bestiary/humanoid/token/akroan-hoplite-mot.webp"
```
^statblock
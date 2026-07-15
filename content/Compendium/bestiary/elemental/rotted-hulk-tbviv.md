---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbviv
- monster/cr/15
- monster/size/gargantuan
- monster/type/elemental
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Rotted Hulk"
---
# Rotted Hulk
*Source: Theros Bestiary, Vol. IV*
![](/Compendium/bestiary/elemental/img/rotted-hulk.webp#right)

The hulk rose from the sea and loomed over the Champion. Pinned beneath the twisting, rotted planks of wood was the body of Kaliaros, the helmsman of her former crew, and beside him the captain, Photine.

—The Theriad

```statblock
"name": "Rotted Hulk"
"size": "Gargantuan"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "12"
"ac_class": "natural armor"
"hp": !!int "750"
"hit_dice": "50d20 + 250"
"modifier": !!int "-1"
"stats":
  - !!int "15"
  - !!int "8"
  - !!int "20"
  - !!int "5"
  - !!int "11"
  - !!int "5"
"speed": "10 ft., swim 10 ft."
"damage_vulnerabilities": "fire"
"damage_resistances": "cold, bludgeoning, piercing, slashing, necrotic"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [paralyzed](/Compendium/rules/conditions.md#Paralyzed), [poisoned](/Compendium/rules/conditions.md#Poisoned),\
  \ [unconscious](/Compendium/rules/conditions.md#Unconscious)"
"senses": "[darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "15"
"traits":
  - "desc": "Any humanoid that starts its turn within 30 feet of the hulk and can\
      \ see the hulk must make a DC 10 Wisdom saving throw. On a failed save, the\
      \ creature is frightened for 1 minute. A creature can repeat the saving throw\
      \ at the end of each of its turns, with Disadvantage if the hulk is within line\
      \ of sight, ending the effect on itself on a success. If a creature's saving\
      \ throw is successful or the effect ends for it, the creature is immune to the\
      \ hulk's Horrific Appearance for the next 24 hours. Unless the target is surprised,\
      \ the target can avert its eyes and avoid making the initial saving throw. Until\
      \ the start of its next turn, a creature that averts its eyes has Disadvantage\
      \ on attack rolls against the hulk."
    "name": "Horrific Appearance"
"actions":
  - "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 24 (4d8+6)\
      \ bludgeoning damage."
    "name": "Slam"
"source":
  - "TBVIV"
```
^statblock
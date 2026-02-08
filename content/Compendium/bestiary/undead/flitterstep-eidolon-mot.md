---
title: Flitterstep Eidolon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Flitterstep Eidolon"]
---
# Flitterstep Eidolon
*Source: Mythic Odysseys of Theros p. 222*  

When a mortal soul traumatically sacrifices its identity in order to escape the Underworld as a Returned, its identity manifests as a spirit-like eidolon. While eidolons possess many of the skills and details related to their past lives, they're disconnected from those experiences, choosing to wander the world or brood in haunts they're drawn to in death. They care nothing for morbid reunions with their lost bodies or Returned remnants.

Of the various types of eidolons, flitterstep eidolons are the most common and wander without purpose.
```statblock
"name": "Flitterstep Eidolon (MOT)"
"size": "Medium"
"type": "undead"
"alignment": "Any alignment"
"ac": !!int "14"
"hp": !!int "44"
"hit_dice": "8d8 + 8"
"modifier": !!int "4"
"stats":
  - !!int "8"
  - !!int "18"
  - !!int "13"
  - !!int "11"
  - !!int "12"
  - !!int "10"
"speed": "40 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+8"
"damage_resistances": "necrotic; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](Compendium/rules/conditions.md#Frightened), [grappled](Compendium/rules/conditions.md#Grappled),\
  \ [paralyzed](Compendium/rules/conditions.md#Paralyzed), [petrified](Compendium/rules/conditions.md#Petrified),\
  \ [poisoned](Compendium/rules/conditions.md#Poisoned), [restrained](Compendium/rules/conditions.md#Restrained)"
"senses": "passive Perception 13"
"languages": "the languages it knew in life"
"cr": "3"
"traits":
  - "desc": "Attack rolls against the eidolon are made with disadvantage unless the\
      \ eidolon is [incapacitated](Compendium/rules/conditions.md#Incapacitated)."
    "name": "Blurred Form"
  - "desc": "If the eidolon is subjected to an effect that allows it to make a Dexterity\
      \ saving throw to take only half damage, the eidolon instead takes no damage\
      \ if it succeeds on the saving throw, and only half damage if it fails. It can't\
      \ use this trait if it's [incapacitated](Compendium/rules/conditions.md#Incapacitated)."
    "name": "Evasion"
  - "desc": "The eidolon can move through other creatures and objects as if they were\
      \ difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside\
      \ an object."
    "name": "Incorporeal Movement"
  - "desc": "The eidolon has advantage on saving throws against any effect that turns\
      \ undead."
    "name": "Turn Resistance"
"actions":
  - "desc": "The eidolon makes two melee attacks. Immediately before or after one\
      \ of its attacks, it can use Flitterstep if it is available."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 6\
      \ (1d4 + 4) piercing damage plus 3 (1d6) psychic damage."
    "name": "Flickering Dagger"
  - "desc": "The eidolon magically teleports to an unoccupied space it can see within\
      \ 30 feet of it. If it makes an attack immediately after teleporting, it has\
      \ advantage on the attack roll."
    "name": "Flitterstep (Recharge 5-6)"
"source":
  - "MOT"
"image": "Compendium/bestiary/undead/token/flitterstep-eidolon-mot.webp"
```
^statblock
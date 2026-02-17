---
title: Ghostblade Eidolon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/mot
- monster/cr/5
- monster/size/medium
- monster/type/undead
statblock: inline
aliases: ["Ghostblade Eidolon"]
---
# Ghostblade Eidolon
*Source: Mythic Odysseys of Theros p. 222*  

![](Compendium/bestiary/undead/img/ghostblade-eidolon.webp#right|850)  
When a mortal soul traumatically sacrifices its identity in order to escape the Underworld as a Returned, its identity manifests as a spirit-like eidolon. While eidolons possess many of the skills and details related to their past lives, they're disconnected from those experiences, choosing to wander the world or brood in haunts they're drawn to in death. They care nothing for morbid reunions with their lost bodies or Returned remnants.

Of the various types of eidolons, ghostblade eidolons typically arise from fallen warriors and believe they're endlessly embroiled in great battles.
```statblock
"name": "Ghostblade Eidolon (MOT)"
"size": "Medium"
"type": "undead"
"alignment": "Any alignment"
"ac": !!int "12"
"hp": !!int "55"
"hit_dice": "10d8 + 10"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "15"
  - !!int "12"
  - !!int "13"
  - !!int "12"
  - !!int "14"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+5"
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+6"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
"damage_resistances": "necrotic; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Frightened|frightened]], [[conditions#Grappled|grappled]],\
  \ [[conditions#Paralyzed|paralyzed]], [[conditions#Petrified|petrified]],\
  \ [[conditions#Poisoned|poisoned]], [[conditions#Restrained|restrained]]"
"senses": "passive Perception 14"
"languages": "the languages it knew in life"
"cr": "5"
"traits":
  - "desc": "Attack rolls against the eidolon are made with disadvantage unless the\
      \ eidolon is [[conditions#Incapacitated|incapacitated]]."
    "name": "Blurred Form"
  - "desc": "The eidolon can move through other creatures and objects as if they were\
      \ difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside\
      \ an object."
    "name": "Incorporeal Movement"
  - "desc": "The eidolon has advantage on saving throws against any effect that turns\
      \ undead."
    "name": "Turn Resistance"
"actions":
  - "desc": "The eidolon makes two ghostblade attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 8\
      \ (1d8 + 3) slashing damage plus 11 (2d10) force damage."
    "name": "Ghostblade"
"source":
  - "MOT"
"image": "Compendium/bestiary/undead/token/ghostblade-eidolon-mot.webp"
```
^statblock
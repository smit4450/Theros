---
title: Returned Palamnite
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Returned Palamnite"]
---
# Returned Palamnite
*Source: Mythic Odysseys of Theros p. 241*  

![](Compendium/bestiary/undead/img/returned.webp#right|850)  
Even death and the loss of their identities can't erase the rage that inspires Returned palamnites. These Returned led violent lives, existences filled with such pain and hatred that violence now suffuses their deathless bodies. Such makes them exceptionally dangerous to the living, as these aimless killers know only suffering and seek to spread it whenever the opportunity arises. While palamnites might wander the world as dangerous, lone murderers, many gravitate to Odunos, where they serve the vicious will of Tymaret the Murder King (see chapter 3).

Returned have escaped the Underworld and dwell among the living once more, but their second lives are rarely what they expected—not that they remember what it was they expected. As a result of having followed the Path of Phenax (see chapter 4), the Returned lose their identities, which manifest as separate beings known as eidolons. The experience of escaping the Underworld also causes them to lose their faces, which become expressionless surfaces with empty eye sockets and gaping mouths. These blank surfaces they cover with distinctive golden masks.

Returned reenter the world blank and undead. No longer possessing the ability to form long-term memories, they generally can't build meaningful relationships or establish new lives. Instead, most experience fleeting emotions and follow hollow routines, their existences reduced to shadow plays without weight or substance.
```statblock
"name": "Returned Palamnite (MOT)"
"size": "Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "65"
"hit_dice": "10d8 + 20"
"modifier": !!int "3"
"stats":
  - !!int "10"
  - !!int "17"
  - !!int "14"
  - !!int "13"
  - !!int "12"
  - !!int "15"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+5"
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+2"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "passive Perception 11"
"languages": "the languages it knew in life"
"cr": "4"
"traits":
  - "desc": "If another creature deals damage to the Returned, the Returned makes\
      \ attack rolls with advantage until the end of its next turn."
    "name": "Fleeting Anger"
  - "desc": "The Returned has advantage on saving throws against any effect that turns\
      \ undead."
    "name": "Turn Resistance"
  - "desc": "The Returned is immune to any effect that would sense its emotions or\
      \ read its thoughts. Wisdom ([[skills#Insight|Insight]])\
      \ checks to ascertain the Returned's intentions or sincerity are made with disadvantage."
    "name": "Unreadable Face"
"actions":
  - "desc": "The Returned makes two shortsword attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 6\
      \ (1d6 + 3) piercing damage plus 10 (3d6) poison damage."
    "name": "Shortsword"
"source":
  - "MOT"
"image": "Compendium/bestiary/undead/token/returned-palamnite-mot.webp"
```
^statblock
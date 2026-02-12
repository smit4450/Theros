---
title: Returned Phalanx
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxii
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Returned Phalanx"]
---
# Returned Phalanx
*Source: Theros Bestiary TBVXXII*  

<blockquote><small>They lived in different nations and fought in different eras, but as the Returned, they link arms as one.</small></blockquote>

Five Returned hoplites have taken the phalanx formation to a whole new level.

![Returned Phalanx](Compendium/bestiary/undead/img/returned-phalanx.webp#right|850)  

```statblock
"name": "Returned Phalanx (TBVXXII)"
"size": "Large"
"type": "undead"
"subtype": "returned, human"
"alignment": "Any alignment"
"ac": !!int "12"
"hp": !!int "140"
"hit_dice": "20d10 + 40"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "16"
  - !!int "14"
  - !!int "11"
  - !!int "14"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "strength": !!int "5"
  - "dexterity": !!int "5"
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "poisoned"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "8"
"traits":
  - "desc": "While the phalanx is holding a a spear, javelin, or pike, other creatures provoke an opportunity attack from the phalanx when they move within 5 feet of it. When the phalanx hits a creature with an opportunity attack using its spear, javelin, or pike, the creature takes an extra 4 (1d8) piercing damage, and the creature’s speed becomes 0 for the rest of the turn."
    "name": "Hold the Line"
  - "desc": "The returned phalanx has advantage on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious."
    "name": "Multiple Heads"
  - "desc": "The phalanx needs water and air but not food or sleep. It thinks and speaks and even feels emotions based on its new experiences, but given its circumstances, those emotions tend to be muted."
    "name": "Returned Nature"
  - "desc": "The phalanx has advantage on saving throws against any effect that turns undead."
    "name": "Turn Resistance"
  - "desc": "The phalanx is immune to any effect that would sense its emotions or read its thoughts. Wisdom (Insight) checks to ascertain the merchant's intentions or sincerity are made with disadvantage."
    "name": "Unreadable Faces"
"actions":
  - "desc": "The phalanx makes ten melee attacks: one with its glaive, one with its halberd, one with its javelin, one with its maul, one with its morningstar, one with its pike, one with its rapier, one with its scimitar, one with its shortsword, and one with its spear."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 10 ft., one target. _Hit:_ 8 (1d10 + 3) slashing damage."
    "name": "Glaive"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 10 ft., one target. _Hit:_ 8 (1d10 + 3) slashing damage."
    "name": "Halberd"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6 + 3) piercing damage."
    "name": "Javelin"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 10 (2d6 + 3) bludgeoning damage."
    "name": "Maul"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 7 (1d8 + 3) piercing damage."
    "name": "Morningstar"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 10 ft., one target. _Hit:_ 8 (1d10 + 3) piercing damage."
    "name": "Pike"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 7 (1d8 + 3) piercing damage."
    "name": "Rapier"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6 + 3) slashing damage."
    "name": "Scimitar"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6 + 3) piercing damage."
    "name": "Shortsword"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6 + 3) piercing damage."
    "name": "Spear"
"source":
  - "TBVXXII"
"image": "Compendium/bestiary/undead/token/returned-phalanx-tbvxxii.webp"
```
^statblock
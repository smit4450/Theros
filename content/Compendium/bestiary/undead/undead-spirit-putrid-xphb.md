---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xphb
- monster/cr/
- monster/size/medium
- monster/type/undead
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Undead Spirit (Putrid)"
---
# Undead Spirit (Putrid)
*Source: Player's Handbook (2024) p. 328*

```statblock
"name": "Undead Spirit (Putrid)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral"
"ac_class": "11 + the spell's level"
"modifier": !!int "3"
"stats":
  - !!int "12"
  - !!int "16"
  - !!int "15"
  - !!int "4"
  - !!int "10"
  - !!int "9"
"speed": "30 ft."
"damage_immunities": "necrotic, poison"
"condition_immunities": "[exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](/Compendium/rules/conditions.md#Frightened), [paralyzed](/Compendium/rules/conditions.md#Paralyzed),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "understands the languages you know"
"traits":
  - "desc": "*Constitution Saving Throw:* DC equals your spell save DC, any creature\
      \ (other than you) that starts its turn within a 5-foot Emanation originating\
      \ from the spirit. *Failure:* The creature has the [Poisoned](/Compendium/rules/conditions.md#Poisoned)\
      \ condition until the start of its next turn."
    "name": "Festering Aura"
"actions":
  - "desc": "The spirit makes a number of attacks equal to half this spell's level\
      \ (round down)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 1d6 + 3 + the spell's level Slashing damage. If the target has\
      \ the [Poisoned](/Compendium/rules/conditions.md#Poisoned) condition, it has\
      \ the [Paralyzed](/Compendium/rules/conditions.md#Paralyzed) condition until\
      \ the end of its next turn."
    "name": "Rotting Claw"
"source":
  - "XPHB"
```
^statblock
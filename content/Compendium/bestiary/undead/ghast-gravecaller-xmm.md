---
title: Ghast Gravecaller
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Ghast Gravecaller"]
---
# Ghast Gravecaller
*Source: Monster Manual (2024) p. 130*  

![](Compendium/bestiary/undead/img/ghasts.webp#right)  
Ghast gravecallers wield fell magic and converse with corpses. They might pose as liches or vampires.

## Ghasts

*Tyrants among Corpses*

- **Habitat.** Swamp, Underdark, Urban  
- **Treasure.** Any  

Ghasts are reeking, undying corpses closely related to ghouls. They hunger for the vices they enjoyed in life as much as they do for rotting flesh.
## Statblock

```statblock
"name": "Ghast Gravecaller (XMM)"
"size": "Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "16"
"hp": !!int "97"
"hit_dice": "15d8 + 30"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "17"
  - !!int "14"
  - !!int "18"
  - !!int "14"
  - !!int "8"
"speed": "30 ft."
"saves":
  - "constitution": !!int "5"
  - "wisdom": !!int "5"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 120 ft., passive Perception\
  \ 12"
"languages": "Abyssal, Common"
"cr": "6"
"traits":
  - "desc": "*Constitution Saving Throw:* DC 13, any creature that starts its turn\
      \ in a 5-foot [Emanation](Compendium/rules/variant-rules/emanation-area-of-effect-xphb.md)\
      \ originating from the ghast. *Failure:* The target has the [Poisoned](Compendium/rules/conditions.md#Poisoned)\
      \ condition until the start of its next turn. *Success:* The target is immune\
      \ to this ghast's Stench for 24 hours."
    "name": "Stench"
"actions":
  - "desc": "The ghast makes two Horrific Necrosis attacks. It can replace one attack\
      \ with a Claw attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 13 (3d6 + 3) Slashing\
      \ damage. If the target isn't an Undead, it has the [Paralyzed](Compendium/rules/conditions.md#Paralyzed)\
      \ condition until the end of its next turn."
    "name": "Claw"
  - "desc": "*Melee  or Ranged Attack Roll:* +7, reach 5 ft. or range 120 ft. *Hit:*\
      \ 15 (2d10 + 4) Necrotic damage, and the target has the [Frightened](Compendium/rules/conditions.md#Frightened)\
      \ condition until the end of its next turn."
    "name": "Horrific Necrosis"
  - "desc": "The ghast casts one of the following spells, requiring no Material components\
      \ and using Intelligence as the spellcasting ability:\n\n**At will:** [Speak\
      \ with Dead](Compendium/spells/speak-with-dead-xphb.md), [Thaumaturgy](Compendium/spells/thaumaturgy-xphb.md)"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/undead/token/ghast-gravecaller-xmm.webp"
```
^statblock
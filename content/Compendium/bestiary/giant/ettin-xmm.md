---
title: Ettin
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Ettin"]
---
# Ettin
*Source: Monster Manual (2024) p. 116. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/giant/img/ettin.webp#right)  
## Ettin

*Quarrelsome Two-Headed Giant*

- **Habitat.** Hill, Mountain, Underdark  
- **Treasure.** Individual  

Ettins are physically powerful Giants with two heads. While many ettins have features similar to hill giants, others have more bestial or unusual traits, such as tusks, short horns, or a single eye on each head.

Ettins frequently ally with other Giants or groups that value their strength, such as hill giants, bandits, or ogres. Some ettins possess mystical ties to the lands they inhabit, and they might know or guard secrets valued by druids or Fey.

Each ettin head has a distinct personality. While this makes some ettins quarrelsome with themselves and others, many function as a team. An ettin head might have its own name, or both heads might refer to themselves as a single being—either with one name or a portmanteau of two.

Roll on or choose a result from the Ettin Interactions table to inspire how an ettin's heads are interacting when the creature is encountered.

**Ettin Interactions**

| dice: 1d8 | The Ettin's Heads Are... |
|-----------|--------------------------|
| 1 | Amping up one another in preparation for a conflict or challenge. |
| 2 | Arguing over plans for battle, dinner, or how to spend the day. |
| 3 | Criticizing one another as they perform separate tasks. |
| 4 | Engaged in a staring contest. |
| 5 | Making polite small talk as if they were meeting for the first time. |
| 6 | Performatively ignoring one another. |
| 7 | Talking over an increasingly convoluted plot. |
| 8 | Trying to keep one another awake. |
^ettin-interactions

> [!quote] A quote from Bertrand, Inquisitor of the Mind Fire  
> 
> Twice the malice, aggressiveness, and appetite—the ettin demonstrates that two heads aren't necessarily better than one.

```statblock
"name": "Ettin (XMM)"
"size": "Large"
"type": "giant"
"alignment": "Chaotic Evil"
"ac": !!int "12"
"hp": !!int "85"
"hit_dice": "10d10 + 30"
"modifier": !!int "-1"
"stats":
  - !!int "21"
  - !!int "8"
  - !!int "17"
  - !!int "6"
  - !!int "10"
  - !!int "8"
"speed": "40 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"condition_immunities": "[blinded](Compendium/rules/conditions.md#Blinded), [charmed](Compendium/rules/conditions.md#Charmed),\
  \ [deafened](Compendium/rules/conditions.md#Deafened), [frightened](Compendium/rules/conditions.md#Frightened),\
  \ [stunned](Compendium/rules/conditions.md#Stunned), [unconscious](Compendium/rules/conditions.md#Unconscious)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 14"
"languages": "Giant"
"cr": "4"
"actions":
  - "desc": "The ettin makes one Battleaxe attack and one Morningstar attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 14 (2d8 + 5) Slashing\
      \ damage. If the target is a Large or smaller creature, it has the [Prone](Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Battleaxe"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 14 (2d8 + 5) Piercing\
      \ damage, and the target has [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md)\
      \ on the next attack roll it makes before the end of its next turn."
    "name": "Morningstar"
"source":
  - "XMM"
"image": "Compendium/bestiary/giant/token/ettin-xmm.webp"
```
^statblock
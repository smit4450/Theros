---
title: Gray Ooze
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/ooze
statblock: inline
aliases: ["Gray Ooze"]
---
# Gray Ooze
*Source: Monster Manual (2024) p. 151. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/ooze/img/gray-oozes.webp#right|850)  
Gray oozes appear in areas affected by unpredictable magic. Magic-users who fail in their attempts to bind elemental spirits to the bodies of Constructs might also accidentally create gray oozes.

## Gray Oozes

*Hungry Slimes and Magical Failures*

- **Habitat.** Underdark  
- **Treasure.** None  

Gray oozes are predatory, corrosive slimes that blend in with stony surroundings.
## Statblock

```statblock
"name": "Gray Ooze (XMM)"
"size": "Medium"
"type": "ooze"
"alignment": "Unaligned"
"ac": !!int "9"
"hp": !!int "22"
"hit_dice": "3d8 + 9"
"modifier": !!int "-2"
"stats":
  - !!int "12"
  - !!int "6"
  - !!int "16"
  - !!int "1"
  - !!int "6"
  - !!int "2"
"speed": "10 ft., climb 10 ft."
"skillsaves":
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+2"
"damage_resistances": "acid, cold, fire"
"condition_immunities": "[blinded](Compendium/rules/conditions.md#Blinded), [charmed](Compendium/rules/conditions.md#Charmed),\
  \ [deafened](Compendium/rules/conditions.md#Deafened), [exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](Compendium/rules/conditions.md#Frightened), [grappled](Compendium/rules/conditions.md#Grappled),\
  \ [prone](Compendium/rules/conditions.md#Prone), [restrained](Compendium/rules/conditions.md#Restrained)"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 60 ft., passive Perception\
  \ 8"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "The ooze can move through a space as narrow as 1 inch without expending\
      \ extra movement to do so."
    "name": "Amorphous"
  - "desc": "Nonmagical ammunition is destroyed immediately after hitting the ooze\
      \ and dealing any damage. Any nonmagical weapon takes a cumulative -1 penalty\
      \ to attack rolls immediately after dealing damage to the ooze and coming into\
      \ contact with it. The weapon is destroyed if the penalty reaches -5. The penalty\
      \ can be removed by casting the [Mending](Compendium/spells/mending-xphb.md)\
      \ spell on the weapon.\n\nThe ooze can eat through 2-inch-thick, nonmagical\
      \ metal or wood in 1 round."
    "name": "Corrosive Form"
"actions":
  - "desc": "*Melee Attack Roll:* +3, reach 5 ft. *Hit:* 10 (2d8 + 1) Acid damage.\
      \ Nonmagical armor worn by the target takes a -1 penalty to the AC it offers.\
      \ The armor is destroyed if the penalty reduces its AC to 10. The penalty can\
      \ be removed by casting the [Mending](Compendium/spells/mending-xphb.md) spell\
      \ on the armor."
    "name": "Pseudopod"
"source":
  - "XMM"
"image": "Compendium/bestiary/ooze/token/gray-ooze-xmm.webp"
```
^statblock
---
title: Annis Hag (Coven; Prophecy)
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Annis Hag (Coven; Prophecy)"]
---
# Annis Hag (Coven; Prophecy)
*Source: Volo's Guide to Monsters p. 159, Mythic Odysseys of Theros*  

```statblock
"name": "Annis Hag (Coven; Prophecy) (VGM)"
"size": "Large"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "75"
"hit_dice": "10d10 + 20"
"modifier": !!int "1"
"stats":
  - !!int "21"
  - !!int "12"
  - !!int "14"
  - !!int "13"
  - !!int "14"
  - !!int "15"
"speed": "40 ft."
"saves":
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[Deception](Compendium/rules/skills.md#Deception)"
    "desc": "+5"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+5"
"damage_resistances": "cold; bludgeoning, piercing, slashing from nonmagical attacks"
"senses": "[darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 15"
"languages": "Common, Giant, Sylvan"
"cr": "8"
"traits":
  - "desc": "While all three members of a hag coven are within 30 feet of one another,\
      \ they can each cast the following spells from the wizard's spell list but must\
      \ share the spell slots among themselves:\n\n**1st level (4 slots):** [bane](Compendium/spells/bane-xphb.md),\
      \ [bless](Compendium/spells/bless-xphb.md)\n\n**2nd level (3 slots):** [augury](Compendium/spells/augury-xphb.md),\
      \ [detect thoughts](Compendium/spells/detect-thoughts-xphb.md)\n\n**3rd level\
      \ (3 slots):** [clairvoyance](Compendium/spells/clairvoyance-xphb.md), [dispel\
      \ magic](Compendium/spells/dispel-magic-xphb.md), [nondetection](Compendium/spells/nondetection-xphb.md)\n\
      \n**4th level (3 slots):** [arcane eye](Compendium/spells/arcane-eye-xphb.md),\
      \ [locate creature](Compendium/spells/locate-creature-xphb.md)\n\n**5th level\
      \ (2 slots):** [geas](Compendium/spells/geas-xphb.md), [legend lore](Compendium/spells/legend-lore-xphb.md)\n\
      \n**6th level (1 slots):** [true seeing](Compendium/spells/true-seeing-xphb.md)\n\
      \nFor casting these spells, each hag is a 12th-level spellcaster that uses Intelligence\
      \ as her spellcasting ability. The spell save DC 13, and the spell attack bonus\
      \ is +5."
    "name": "Shared Spellcasting (Coven Only)"
  - "desc": "The hag's innate spellcasting ability is Charisma (spell save DC 13).\
      \ She can innately cast the following spells:\n\n**3/day each:** [disguise self](Compendium/spells/disguise-self-xphb.md)\
      \ (including the form of a Medium humanoid), [fog cloud](Compendium/spells/fog-cloud-xphb.md)"
    "name": "Innate Spellcasting"
"actions":
  - "desc": "The annis makes three attacks: one with her bite and two with her claws."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 15\
      \ (3d6 + 5) piercing damage."
    "name": "Bite"
  - "desc": "*Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 15\
      \ (3d6 + 5) slashing damage."
    "name": "Claw"
  - "desc": "*Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 36\
      \ (9d6 + 5) bludgeoning damage, and the target is [grappled](Compendium/rules/conditions.md#Grappled)\
      \ (escape DC 15) if it is a Large or smaller creature. Until the grapple ends,\
      \ the target takes 36 (9d6 + 5) bludgeoning damage at the start of each of\
      \ the hag's turns. The hag can't make attacks while grappling a creature in\
      \ this way."
    "name": "Crushing Hug"
"source":
  - "VGM"
  - "MOT"
```
^statblock
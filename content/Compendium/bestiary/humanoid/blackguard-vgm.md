---
title: Blackguard
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
aliases: ["Blackguard"]
---
# Blackguard
*Source: Volo's Guide to Monsters p. 211, Mythic Odysseys of Theros*  

Blackguards are paladins who broke their sacred oaths and now indulge their own dark ambitions. They consort with fiends and undead, and they reject all goodly things from their former lives.
```statblock
"name": "Blackguard (VGM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any Non-Good alignment"
"ac": !!int "18"
"ac_class": "[plate armor](Compendium/items/plate-armor-xphb.md)"
"hp": !!int "153"
"hit_dice": "18d8 + 72"
"modifier": !!int "0"
"stats":
  - !!int "18"
  - !!int "11"
  - !!int "18"
  - !!int "11"
  - !!int "14"
  - !!int "15"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "5"
  - "charisma": !!int "5"
"skillsaves":
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+7"
  - "name": "[Deception](Compendium/rules/skills.md#Deception)"
    "desc": "+5"
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+5"
"senses": "passive Perception 12"
"languages": "any one language (usually Common)"
"cr": "8"
"traits":
  - "desc": "The blackguard is a 10th-level spellcaster. Its spellcasting ability\
      \ is Charisma (spell save DC 13, +5 to hit with spell attacks). It has the\
      \ following paladin spells prepared:\n\n**1st level (4 slots):** [command](Compendium/spells/command-xphb.md),\
      \ [protection from evil and good](Compendium/spells/protection-from-evil-and-good-xphb.md),\
      \ [thunderous smite](Compendium/spells/thunderous-smite-xphb.md)\n\n**2nd level\
      \ (3 slots):** [branding smite](Compendium/spells/shining-smite-xphb.md), [find\
      \ steed](Compendium/spells/find-steed-xphb.md)\n\n**3rd level (2 slots):** [blinding\
      \ smite](Compendium/spells/blinding-smite-xphb.md), [dispel magic](Compendium/spells/dispel-magic-xphb.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "The blackguard makes three attacks with its glaive or its shortbow."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 10 ft., one target. *Hit:*\
      \ 9 (1d10 + 4) slashing damage."
    "name": "Glaive"
  - "desc": "*Ranged Weapon Attack:* +3 to hit, range 80/320 ft., one target. *Hit:*\
      \ 5 (1d6 + 2) piercing damage."
    "name": "Shortbow"
  - "desc": "The blackguard exudes magical menace. Each enemy within 30 feet of the\
      \ blackguard must succeed on a DC 13 Wisdom saving throw or be [frightened](Compendium/rules/conditions.md#Frightened)\
      \ for 1 minute. If a [frightened](Compendium/rules/conditions.md#Frightened)\
      \ target ends its turn more than 30 feet away from the blackguard, the target\
      \ can repeat the saving throw, ending the effect on itself on a success."
    "name": "Dreadful Aspect (Recharges after a Short or Long Rest)"
"source":
  - "VGM"
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/blackguard-vgm.webp"
```
^statblock
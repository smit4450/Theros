---
title: Unicorn
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/feywild
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Unicorn"]
---
# Unicorn
*Source: Monster Manual (2024), FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/books/monster-manual-2025/img/unicorn.webp#right)  
## Unicorn

*Majestic and Magical Forest Master*

- **Habitat.** Forest, Planar (Feywild)  
- **Treasure.** Any  

Unicorns are majestic defenders of forests. They are revered by many Fey and other forest dwellers, and they do whatever they can to ensure the peace and health of those who shelter in their wooded realms.

### Unicorn Lairs

Unicorns dwell in unspoiled forests, particularly where benevolent Fey creatures live.
```statblock
"name": "Unicorn (XMM)"
"size": "Large"
"type": "celestial"
"alignment": "Lawful Good"
"ac": !!int "12"
"hp": !!int "97"
"hit_dice": "13d10 + 26"
"modifier": !!int "8"
"stats":
  - !!int "18"
  - !!int "14"
  - !!int "15"
  - !!int "11"
  - !!int "17"
  - !!int "16"
"speed": "50 ft."
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Paralyzed|paralyzed]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 13"
"languages": "Celestial, Elvish, Sylvan; telepathy 120 ft."
"cr": "5"
"traits":
  - "desc": "If the unicorn fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (3/Day)"
  - "desc": "The unicorn has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The unicorn makes one Hooves attack and one Radiant Horn attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 11 (2d6 + 4) Bludgeoning\
      \ damage."
    "name": "Hooves"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 9 (1d10 + 4) Radiant\
      \ damage."
    "name": "Radiant Horn"
  - "desc": "The unicorn casts one of the following spells, requiring no spell components\
      \ and using Charisma as the spellcasting ability (spell save DC 14):\n\n**At\
      \ will:** [[detect-evil-and-good-xphb|Detect Evil and Good]],\
      \ [[druidcraft-xphb|Druidcraft]]\n\n**1/day each:** [[calm-emotions-xphb|Calm\
      \ Emotions]], [[dispel-evil-and-good-xphb|Dispel Evil and Good]],\
      \ [[entangle-xphb|Entangle]], [[pass-without-trace-xphb|Pass without Trace]],\
      \ [[word-of-recall-xphb|Word of Recall]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The unicorn touches another creature with its horn and casts [[cure-wounds-xphb|Cure Wounds]]\
      \ or [[lesser-restoration-xphb|Lesser Restoration]] on that\
      \ creature, using the same spellcasting ability as Spellcasting.\n"
    "name": "Unicorn's Blessing (3/Day)"
"regional_effects":
  - "desc": "The region containing a unicorn's lair is changed by its presence, creating\
      \ the following effects:\n\n- **Obscuring Foliage.** The unicorn and its allies\
      \ have [[advantage-xphb|Advantage]] on Dexterity\
      \ ([[skills#Stealth|Stealth]]) checks while within 1 mile\
      \ of the lair.  \n- **Positive Energy.** Whenever a creature within 1 mile of\
      \ the lair regains [[hit-points-xphb|Hit Points]]\
      \ from a spell, it regains the maximum number of [[hit-points-xphb|Hit Points]]\
      \ possible. Additionally, the effects of curses are suppressed within 1 mile\
      \ of the lair.  \n\nIf the unicorn dies or moves its lair elsewhere, these effects\
      \ end immediately."
    "name": ""
"legendary_description": "Legendary Action Uses: 3. Immediately after another creature's\
  \ turn, the unicorn can expend a use to take one of the following actions. The unicorn\
  \ regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "The unicorn moves up to half its [[speed-xphb|Speed]]\
      \ without provoking [[actions#Opportunity%20Attack|Opportunity Attacks]],\
      \ and it makes one Radiant Horn attack."
    "name": "Charging Horn"
  - "desc": "The unicorn targets itself or one creature it can see within 60 feet\
      \ of itself. The target gains 10 (3d6) [[temporary-hit-points-xphb|Temporary Hit Points]],\
      \ and its AC increases by 2 until the end of the unicorn's next turn. The unicorn\
      \ can't take this action again until the start of its next turn."
    "name": "Shimmering Shield"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/celestial/token/unicorn-xmm.webp"
```
^statblock
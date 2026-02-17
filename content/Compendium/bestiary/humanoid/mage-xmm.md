---
title: Mage
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid/wizard
statblock: inline
aliases: ["Mage"]
---
# Mage
*Source: Monster Manual (2024) p. 199, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/humanoid/img/mages.webp#right|850)  
Mages are accomplished spellcasters whose lives have been shaped by magic. They can use their powers to defend or dominate other creatures, or they could focus on magical research and unlocking mystical secrets.

## Mages

*Magical Scholars and Spellcasters*

- **Habitat.** Any  
- **Treasure.** [[random-magic-items-arcana|Arcana]], Individual  

Mages are magical wonder-workers, ranging from spellcasting overlords to reclusive witches. They study mystical secrets and possess insight into monsters, legends, omens, and other lore. Mages often gather allies or hire assistants to aid them in their research or to attain magical might.

Roll on or choose a result from the Mage Roles table to inspire different sorts of mages.

**Mage Roles**

| dice: 1d10 | The Mage Is... |
|------------|----------------|
| 1 | An astronomer who draws magic from stars. |
| 2 | An author who writes about the occult. |
| 3 | A magical engineer who creates wonders. |
| 4 | An oracle who interprets omens. |
| 5 | A prodigy with a remarkable magical heritage. |
| 6 | A psion whose powers manifest as spells. |
| 7 | A scholar investigating ancient lore. |
| 8 | A soothsayer who advises rulers. |
| 9 | A war mage who aids soldiers in battle. |
| 10 | A witch who shares secret wisdom. |
^mage-roles

> [!quote] A quote from Nathor, Thayan Refugee  
> 
> Have you gazed on the Runes of Chaos, held the Death Moon Orb in your trembling hands, entered the Devouring Portal and walked the Paths of the Doomed, or sat at the left hand of Szass Tam during the Ritual of Twin Burnings? No? Then speak not to me of wizards. Speak not to me of Thay.

## Statblock

```statblock
"name": "Mage (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"subtype": "wizard"
"alignment": "Neutral"
"ac": !!int "15"
"hp": !!int "81"
"hit_dice": "18d8"
"modifier": !!int "2"
"stats":
  - !!int "9"
  - !!int "14"
  - !!int "11"
  - !!int "17"
  - !!int "12"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "6"
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+6"
  - "name": "[[skills#History|History]]"
    "desc": "+6"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
"senses": "passive Perception 14"
"languages": "Common and any three languages"
"cr": "6"
"actions":
  - "desc": "The mage makes three Arcane Burst attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +6, reach 5 ft. or range 120 ft. *Hit:*\
      \ 16 (3d8 + 3) Force damage."
    "name": "Arcane Burst"
  - "desc": "The mage casts one of the following spells, using Intelligence as the\
      \ spellcasting ability (spell save DC 14):\n\n**At will:** [[detect-magic-xphb|Detect Magic]],\
      \ [[light-xphb|Light]], [[mage-armor-xphb|Mage Armor]]\
      \ (included in AC), [[mage-hand-xphb|Mage Hand]], [[prestidigitation-xphb|Prestidigitation]]\n\
      \n**2/day each:** [[fireball-xphb|Fireball]] (level 4 version),\
      \ [[invisibility-xphb|Invisibility]]\n\n**1/day each:**\
      \ [[cone-of-cold-xphb|Cone of Cold]], [[fly-xphb|Fly]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The mage casts [[misty-step-xphb|Misty Step]], using\
      \ the same spellcasting ability as Spellcasting.\n"
    "name": "Misty Step (3/Day)"
"reactions":
  - "desc": "The mage casts [[counterspell-xphb|Counterspell]]\
      \ or [[shield-spell-xphb|Shield]] in response to the spell's trigger,\
      \ using the same spellcasting ability as Spellcasting.\n"
    "name": "Protective Magic (3/Day)"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/humanoid/token/mage-xmm.webp"
```
^statblock
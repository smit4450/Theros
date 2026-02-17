---
title: Archmage
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid/wizard
statblock: inline
aliases: ["Archmage"]
---
# Archmage
*Source: Monster Manual (2024) p. 199. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/humanoid/img/mages.webp#right|850)  
Archmages have mastered incredible magical power. While some use their magic to protect the world, others become tyrants or pursue forbidden secrets. Many archmages retain magical servants and collect magic items and occult lore.

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
"name": "Archmage (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"subtype": "wizard"
"alignment": "Neutral"
"ac": !!int "17"
"hp": !!int "170"
"hit_dice": "31d8 + 31"
"modifier": !!int "6"
"stats":
  - !!int "10"
  - !!int "14"
  - !!int "12"
  - !!int "20"
  - !!int "15"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "9"
  - "wisdom": !!int "6"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+13"
  - "name": "[[skills#History|History]]"
    "desc": "+9"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
"damage_immunities": "psychic"
"condition_immunities": "[[conditions#Charmed|charmed]] (with Mind\
  \ Blank)"
"senses": "passive Perception 16"
"languages": "Common plus five other languages"
"cr": "12"
"traits":
  - "desc": "The archmage has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The archmage makes four Arcane Burst attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +9, reach 5 ft. or range 150 ft. *Hit:*\
      \ 27 (4d10 + 5) Force damage."
    "name": "Arcane Burst"
  - "desc": "The archmage casts one of the following spells, using Intelligence as\
      \ the spellcasting ability (spell save DC 17):\n\n**At will:** [[detect-magic-xphb|Detect Magic]],\
      \ [[detect-thoughts-xphb|Detect Thoughts]], [[disguise-self-xphb|Disguise Self]],\
      \ [[invisibility-xphb|Invisibility]], [[light-xphb|Light]],\
      \ [[mage-armor-xphb|Mage Armor]] (included in AC), [[mage-hand-xphb|Mage\
      \ Hand]], [[prestidigitation-xphb|Prestidigitation]]\n\
      \n**2/day each:** [[fly-xphb|Fly]], [[lightning-bolt-xphb|Lightning Bolt]]\
      \ (level 7 version)\n\n**1/day each:** [[cone-of-cold-xphb|Cone of Cold]]\
      \ (level 9 version), [[mind-blank-xphb|Mind Blank]] (cast\
      \ before combat), [[scrying-xphb|Scrying]], [[teleport-xphb|Teleport]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The mage casts [[misty-step-xphb|Misty Step]], using\
      \ the same spellcasting ability as Spellcasting.\n"
    "name": "Misty Step (3/Day)"
"reactions":
  - "desc": "The archmage casts [[counterspell-xphb|Counterspell]]\
      \ or [[shield-spell-xphb|Shield]] in response to the spell's trigger,\
      \ using the same spellcasting ability as Spellcasting.\n"
    "name": "Protective Magic (3/Day)"
"source":
  - "XMM"
"image": "Compendium/bestiary/humanoid/token/archmage-xmm.webp"
```
^statblock
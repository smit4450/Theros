---
title: Death Knight Aspirant
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Death Knight Aspirant"]
---
# Death Knight Aspirant
*Source: Monster Manual (2024) p. 93*  

![](Compendium/bestiary/undead/img/death-knights.webp#right|850)  
When the leader of a villainous order rises as a death knight, their wicked devotees might join them in their cursed existence as death knight aspirants. These followers bear a measure of their leader's power and serve as they did in life, obediently following the death knight's decrees and heralding its terrible will.

## Death Knights

*Haunted Commanders of Unliving Legions*

- **Habitat.** Any  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Champions of evil, death knights are armor-clad, skeletal warlords. Combining devastating martial prowess and blasphemous magic, these undying tyrants lead unholy legions against the living or brood in cursed citadels. Every death knight is haunted by a legacy of tragedy and dishonor that drives it to commit greater evils.
## Statblock

```statblock
"name": "Death Knight Aspirant (XMM)"
"size": "Small or Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "20"
"hp": !!int "178"
"hit_dice": "21d8 + 84"
"modifier": !!int "4"
"stats":
  - !!int "20"
  - !!int "10"
  - !!int "18"
  - !!int "10"
  - !!int "12"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "4"
  - "wisdom": !!int "5"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Frightened|frightened]], [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception\
  \ 11"
"languages": "Abyssal, Common"
"cr": "11"
"traits":
  - "desc": "The aspirant has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "Undead creatures of the aspirant's choice (excluding itself) in a 60-foot\
      \ [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from it have [[advantage-xphb|Advantage]]\
      \ on attack rolls and saving throws. It can't use this trait if it has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition."
    "name": "Marshal Undead"
"actions":
  - "desc": "The aspirant makes three Dread Blade attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +9, reach 5 ft. *Hit:* 14 (2d8 + 5) Slashing\
      \ damage plus 10 (3d6) Necrotic damage."
    "name": "Dread Blade"
  - "desc": "*Dexterity Saving Throw:* DC 15, each creature in a 20-foot-radius [[sphere-area-of-effect-xphb|Sphere]]\
      \ centered on a point the aspirant can see within 120 feet of itself. *Failure:*\
      \ 21 (6d6) Fire damage plus 21 (6d6) Necrotic damage. *Success:* Half damage."
    "name": "Hellfire Orb (Recharge 5-6)"
  - "desc": "The aspirant casts one of the following spells, using Charisma as the\
      \ spellcasting ability (spell save DC 15):\n\n**At will:** [[phantom-steed-xphb|Phantom Steed]]\n\
      \n**1/day each:** [[destructive-wave-xphb|Destructive Wave]]\
      \ (Necrotic), [[dispel-magic-xphb|Dispel Magic]]"
    "name": "Spellcasting"
"reactions":
  - "desc": "Trigger: The aspirant is hit by a melee attack roll while holding a weapon.\
      \ _Response:_ The aspirant adds 4 to its AC against that attack, possibly causing\
      \ it to miss."
    "name": "Parry"
"source":
  - "XMM"
"image": "Compendium/bestiary/undead/token/death-knight-aspirant-xmm.webp"
```
^statblock
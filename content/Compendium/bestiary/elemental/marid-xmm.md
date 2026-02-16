---
title: Marid
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/environment/water
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/elemental/genie
statblock: inline
aliases: ["Marid"]
---
# Marid
*Source: Monster Manual (2024) p. 203*  

![](Compendium/books/monster-manual-2025/img/marid.webp#right)  
## Marid

*Genie of the Water*

- **Habitat.** Coastal, Planar (Elemental Plane of Water), Underwater  
- **Treasure.** [[random-magic-items-relics|Relics]]  

Marids surge with the power of the seas, using it to manipulate the waves or create water. These genies typically dwell in or near bodies of water. While gentle marids make homes amid springs, oases, and serene pools, tempestuous marids inhabit sea stacks, whirlpools, and treacherous coasts. Marids vary in appearance, their bodies reflecting the colors of the waves while distinctive fins and scales accent their features. Marids lend their powers and knowledge of the seas to those who defend the marids' watery realms or who offer them pleasing gifts. Marids appreciate rare aquatic treasures, such as colorful pearls, shell instruments, or delicacies from distant seas.

Marids hail from the Elemental Plane of Water, where they live in wondrous homes drifting amid the endless ocean. Among these is the Citadel of Ten Thousand Pearls—a coral sphere studded with dozens of domed theaters and libraries—and the air-filled, cosmopolitan City of Glass.
```statblock
"name": "Marid (XMM)"
"size": "Large"
"type": "elemental"
"subtype": "genie"
"alignment": "Chaotic Neutral"
"ac": !!int "17"
"hp": !!int "229"
"hit_dice": "17d10 + 136"
"modifier": !!int "5"
"stats":
  - !!int "22"
  - !!int "12"
  - !!int "26"
  - !!int "18"
  - !!int "17"
  - !!int "18"
"speed": "30 ft., fly 60 ft., swim 90 ft."
"saves":
  - "dexterity": !!int "5"
  - "charisma": !!int "8"
"damage_resistances": "acid, cold, lightning"
"senses": "[[senses#Blindsight|Blindsight]] 30 ft., [[senses#Darkvision|Darkvision]]\
  \ 120 ft., passive Perception 13"
"languages": "Primordial (Aquan)"
"cr": "11"
"traits":
  - "desc": "The marid can breathe air and water."
    "name": "Amphibious"
  - "desc": "If the marid dies outside the Elemental Plane of Water, its body dissolves\
      \ into brine, and it gains a new body in 1d4 days, reviving with all its [[hit-points-xphb|Hit\
      \ Points]] somewhere on the\
      \ Plane of Water."
    "name": "Elemental Restoration"
  - "desc": "The marid has a 30 percent chance of knowing the [[wish-xphb|Wish]]\
      \ spell. If the marid knows it, the marid can cast it only on behalf of a non-genie\
      \ creature who communicates a wish in a way the marid can understand. If the\
      \ marid casts the spell for the creature, the marid suffers none of the spell's\
      \ stress. Once the marid has cast it three times, the marid can't do so again\
      \ for 365 days."
    "name": "Wishes"
"actions":
  - "desc": "The marid makes three Aquatic Lash attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +10, reach 15 ft. *Hit:* 15 (2d8 + 6) Slashing\
      \ damage plus 9 (2d8) Cold damage."
    "name": "Aquatic Lash"
  - "desc": "*Dexterity Saving Throw:* DC 18, each creature in a 60-foot-long, 10-foot-wide\
      \ [[line-area-of-effect-xphb|Line]]. *Failure:*\
      \ 31 (9d6) Cold damage. If the target is a Huge or smaller creature, it is\
      \ pushed up to 20 feet straight away from the marid and has the [[conditions#Prone|Prone]]\
      \ condition. *Success:* Half damage only."
    "name": "Water Jet"
  - "desc": "The marid casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 16):\n\n**At\
      \ will:** [[create-or-destroy-water-xphb|Create or Destroy Water]],\
      \ [[detect-evil-and-good-xphb|Detect Evil and Good]], [[detect-magic-xphb|Detect\
      \ Magic]], [[purify-food-and-drink-xphb|Purify Food and Drink]]\n\
      \n**1/day each:** [[control-water-xphb|Control Water]],\
      \ [[gaseous-form-xphb|Gaseous Form]], [[invisibility-xphb|Invisibility]],\
      \ [[plane-shift-xphb|Plane Shift]], [[tongues-xphb|Tongues]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The marid casts [[fog-cloud-xphb|Fog Cloud]], using\
      \ the same spellcasting ability as Spellcasting.\n"
    "name": "Misty Veil (Recharge 5-6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/marid-xmm.webp"
```
^statblock
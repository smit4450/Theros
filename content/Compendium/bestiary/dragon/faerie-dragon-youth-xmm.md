---
title: Faerie Dragon Youth
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1
- monster/environment/forest
- monster/size/tiny
- monster/type/dragon
statblock: inline
aliases: ["Faerie Dragon Youth"]
---
# Faerie Dragon Youth
*Source: Monster Manual (2024) p. 117*  

![](Compendium/bestiary/dragon/img/faerie-dragons.webp#right|850)  
Faerie dragon youths are quick to use their euphoria-inducing breath on rude or uptight folk.

## Faerie Dragons

*Whimsical Draconic Tricksters*

- **Habitat.** Forest  
- **Treasure.** [[random-magic-items-implements|Implements]]  

Faerie dragons are cat-size pranksters with draconic features, butterfly-like wings, and scales of warm hues as youths and cool hues as adults.
## Statblock

```statblock
"name": "Faerie Dragon Youth (XMM)"
"size": "Tiny"
"type": "dragon"
"alignment": "Chaotic Good"
"ac": !!int "13"
"hp": !!int "21"
"hit_dice": "6d4 + 6"
"modifier": !!int "3"
"stats":
  - !!int "3"
  - !!int "16"
  - !!int "12"
  - !!int "12"
  - !!int "12"
  - !!int "14"
"speed": "10 ft., fly 60 ft."
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+3"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 13"
"languages": "Draconic, Sylvan; telepathy 60 ft. (faerie dragons only)"
"cr": "1"
"traits":
  - "desc": "The dragon has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 5 (1d4 + 3) Piercing\
      \ damage plus 2 (1d4) Psychic damage."
    "name": "Bite"
  - "desc": "*Wisdom Saving Throw:* DC 12, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* The target has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition until the end of its next turn and uses all its movement on its\
      \ turn to move in a random direction."
    "name": "Euphoria Breath (Recharge 5-6)"
  - "desc": "The dragon casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 12):\n\n**At\
      \ will:** [[dancing-lights-xphb|Dancing Lights]], [[mage-hand-xphb|Mage\
      \ Hand]], [[minor-illusion-xphb|Minor Illusion]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The dragon casts [[greater-invisibility-xphb|Greater Invisibility]]\
      \ on itself, requiring no spell components and using the same spellcasting ability\
      \ as Spellcasting.\n"
    "name": "Superior Invisibility"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/faerie-dragon-youth-xmm.webp"
```
^statblock
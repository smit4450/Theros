---
title: Faerie Dragon Adult
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Faerie Dragon Adult"]
---
# Faerie Dragon Adult
*Source: Monster Manual (2024) p. 117*  

![](Compendium/bestiary/dragon/img/faerie-dragons.webp#right|850)  
The pranks of faerie dragon adults tend to lead others to people in need or wrongs to be righted.

## Faerie Dragons

*Whimsical Draconic Tricksters*

- **Habitat.** Forest  
- **Treasure.** [[random-magic-items-implements|Implements]]  

Faerie dragons are cat-size pranksters with draconic features, butterfly-like wings, and scales of warm hues as youths and cool hues as adults.
## Statblock

```statblock
"name": "Faerie Dragon Adult (XMM)"
"size": "Tiny"
"type": "dragon"
"alignment": "Chaotic Good"
"ac": !!int "15"
"hp": !!int "35"
"hit_dice": "10d4 + 10"
"modifier": !!int "5"
"stats":
  - !!int "3"
  - !!int "20"
  - !!int "13"
  - !!int "12"
  - !!int "12"
  - !!int "14"
"speed": "10 ft., fly 60 ft."
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+4"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+7"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 13"
"languages": "Draconic, Sylvan; telepathy 60 ft. (faerie dragons only)"
"cr": "2"
"traits":
  - "desc": "The dragon has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 7 (1d4 + 5) Piercing\
      \ damage plus 3 (1d6) Psychic damage."
    "name": "Bite"
  - "desc": "*Wisdom Saving Throw:* DC 13, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* The target has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition and repeats the save at the end of each of its turns, ending the\
      \ effect on itself on a success. After 1 minute, it succeeds automatically.\
      \ While [[conditions#Incapacitated|Incapacitated]], the target\
      \ uses all its movement on each of its turns to move in a random direction."
    "name": "Euphoria Breath (Recharge 5-6)"
  - "desc": "The dragon casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 13):\n\n**At\
      \ will:** [[dancing-lights-xphb|Dancing Lights]], [[mage-hand-xphb|Mage\
      \ Hand]], [[minor-illusion-xphb|Minor Illusion]]\n\
      \n**1/day each:** [[hallucinatory-terrain-xphb|Hallucinatory Terrain]],\
      \ [[polymorph-xphb|Polymorph]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The dragon casts [[greater-invisibility-xphb|Greater Invisibility]]\
      \ on itself, requiring no spell components and using the same spellcasting ability\
      \ as Spellcasting.\n"
    "name": "Superior Invisibility"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/faerie-dragon-adult-xmm.webp"
```
^statblock
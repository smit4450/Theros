---
title: Thri-kreen Psion
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/8
- monster/environment/desert
- monster/environment/grassland
- monster/size/medium
- monster/type/monstrosity
statblock: inline
aliases: ["Thri-kreen Psion"]
---
# Thri-kreen Psion
*Source: Monster Manual (2024) p. 306*  

![](Compendium/bestiary/monstrosity/img/thri-kreen.webp#right|850)  
Thri-kreen psions harness their psychic powers to avoid danger and manipulate objects from afar.

## Thri-kreen

*Mantid Psychics and Scavengers*

- **Habitat.** Desert, Grassland  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Thri-kreen are mantis-like wanderers who harness their innate camouflage and psychic abilities to survive. Different groups of thri-kreen have distinct carapaces, from the rocky shades of desert dwellers to the vibrant hues of those living in verdant lands. While their language has a distinctly insectile quality, thri-kreen often use telepathy to communicate, and groups can rapidly share a wealth of detailed information without making a sound.

> [!quote] A quote from Ka'Cha, Thri-kreen Knowledge Hunter  
> 
> I would tell you now the tale of the first Ka'Cha, the first thri-kreen who knew and taught the truth: that the clutch is all.

## Statblock

```statblock
"name": "Thri-kreen Psion (XMM)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Neutral"
"ac": !!int "16"
"hp": !!int "149"
"hit_dice": "23d8 + 46"
"modifier": !!int "5"
"stats":
  - !!int "18"
  - !!int "15"
  - !!int "14"
  - !!int "19"
  - !!int "12"
  - !!int "11"
"speed": "40 ft., fly 20 ft. (hover)"
"saves":
  - "strength": !!int "7"
  - "dexterity": !!int "5"
  - "constitution": !!int "5"
  - "intelligence": !!int "7"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+8"
"damage_resistances": "psychic"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 14"
"languages": "Thri-kreen; telepathy 120 ft."
"cr": "8"
"actions":
  - "desc": "The thri-kreen makes three Psionic Lance attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +7, reach 10 ft. or range 120 ft. *Hit:*\
      \ 18 (4d6 + 4) Psychic damage."
    "name": "Psionic Lance"
  - "desc": "The thri-kreen casts one of the following spells, requiring no spell\
      \ components and using Intelligence as the spellcasting ability (spell save\
      \ DC 15):\n\n**At will:** [[mage-hand-xphb|Mage Hand]] (the\
      \ hand is Invisible)\n\n**1/day each:** [[detect-thoughts-xphb|Detect Thoughts]],\
      \ [[sending-xphb|Sending]], [[synaptic-static-xphb|Synaptic Static]]"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/monstrosity/token/thri-kreen-psion-xmm.webp"
```
^statblock
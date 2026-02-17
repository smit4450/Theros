---
title: Violet Fungus
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1-4
- monster/environment/underdark
- monster/size/medium
- monster/type/plant
statblock: inline
aliases: ["Violet Fungus"]
---
# Violet Fungus
*Source: Monster Manual (2024) p. 126. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/plant/img/fungi.webp#right|850)  
Slow but mobile, violet fungi rot any flesh they touch with their lashing tendrils.

## Fungi

*Deadly Spores and Predatory Polyps*

- **Habitat.** Underdark  
- **Treasure.** None  

The dank, sunless Underdark is a fertile breeding ground for weird and dangerous fungi.
## Statblock

```statblock
"name": "Violet Fungus (XMM)"
"size": "Medium"
"type": "plant"
"alignment": "Unaligned"
"ac": !!int "5"
"hp": !!int "18"
"hit_dice": "4d8"
"modifier": !!int "-5"
"stats":
  - !!int "3"
  - !!int "1"
  - !!int "10"
  - !!int "1"
  - !!int "3"
  - !!int "1"
"speed": "5 ft."
"condition_immunities": "[[conditions#Blinded|blinded]], [[conditions#Charmed|charmed]],\
  \ [[conditions#Deafened|deafened]], [[conditions#Frightened|frightened]]"
"senses": "[[senses#Blindsight|Blindsight]] 30 ft., passive Perception\
  \ 6"
"languages": ""
"cr": "1/4"
"actions":
  - "desc": "The fungus makes two Rotting Touch attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +2, reach 10 ft. *Hit:* 4 (1d8) Necrotic damage."
    "name": "Rotting Touch"
"source":
  - "XMM"
"image": "Compendium/bestiary/plant/token/violet-fungus-xmm.webp"
```
^statblock
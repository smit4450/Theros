---
title: Lizardfolk Geomancer
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/forest
- monster/environment/swamp
- monster/size/medium
- monster/type/elemental
statblock: inline
aliases: ["Lizardfolk Geomancer"]
---
# Lizardfolk Geomancer
*Source: Monster Manual (2024) p. 197*  

![](Compendium/bestiary/elemental/img/lizardfolk.webp#right|850)  
Lizardfolk geomancers draw magic from the natural world, using it to protect their people and territories.

## Lizardfolk

*Reptilian Defenders of the Land*

- **Habitat.** Forest, Swamp  
- **Treasure.** Individual  

Lizardfolk dwell in wildernesses suffused with primal magic. While many lizardfolk are Humanoids with varied skills, some forge powerful bonds with the Elemental Plane of Earth, granting them magical connections to the cycle of growth and rebirth.
## Statblock

```statblock
"name": "Lizardfolk Geomancer (XMM)"
"size": "Medium"
"type": "elemental"
"alignment": "Neutral"
"ac": !!int "13"
"hp": !!int "33"
"hit_dice": "6d8 + 6"
"modifier": !!int "0"
"stats":
  - !!int "15"
  - !!int "10"
  - !!int "13"
  - !!int "10"
  - !!int "15"
  - !!int "8"
"speed": "30 ft., burrow 20 ft., swim 30 ft."
"skillsaves":
  - "name": "[[skills#Nature|Nature]]"
    "desc": "+2"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
"senses": "passive Perception 14"
"languages": "Draconic, Primordial (Terran)"
"cr": "2"
"actions":
  - "desc": "The lizardfolk makes two Earth Burst attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +4, reach 5 ft. or range 60 ft. *Hit:*\
      \ 9 (2d6 + 2) Bludgeoning damage."
    "name": "Earth Burst"
  - "desc": "*Constitution Saving Throw:* DC 12, each creature in a 20-foot-radius,\
      \ 40-foot-high [[cylinder-area-of-effect-xphb|Cylinder]]\
      \ centered on a point the lizardfolk can see within 60 feet. *Failure:* 15 (6d4)\
      \ Bludgeoning damage, and the target has the [[conditions#Prone|Prone]]\
      \ condition. *Success:* Half damage only."
    "name": "Hail of Stone (Recharge 5-6)"
  - "desc": "The lizardfolk casts one of the following spells, requiring no Material\
      \ components and using Wisdom as the spellcasting ability (spell save DC 12):\n\
      \n**At will:** [[elementalism-xphb|Elementalism]]\n\n**1/day\
      \ each:** [[meld-into-stone-xphb|Meld into Stone]], [[speak-with-plants-xphb|Speak\
      \ with Plants]], [[spike-growth-xphb|Spike Growth]]"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/lizardfolk-geomancer-xmm.webp"
```
^statblock
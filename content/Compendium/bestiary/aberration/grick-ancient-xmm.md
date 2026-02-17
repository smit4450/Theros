---
title: Grick Ancient
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/7
- monster/environment/forest
- monster/environment/underdark
- monster/size/large
- monster/type/aberration
statblock: inline
aliases: ["Grick Ancient"]
---
# Grick Ancient
*Source: Monster Manual (2024) p. 158*  

![](Compendium/bestiary/aberration/img/gricks.webp#right|850)  
Gricks can live for centuries, with the eldest growing to monstrous sizes. Grick ancients actively hunt more than they wait in ambush, and they have no qualms about devouring smaller gricks.

## Gricks

*Worms That Hunt the Dark and Decaying*

- **Habitat.** Forest, Underdark  
- **Treasure.** Any  

Gricks are wormlike predators that burst from hiding—flailing and snapping—to consume whatever prey passes near. They hide in cavernous crags or amid deadfalls, the scattered bones and possessions of past meals the only evidence of their threat.

Gricks' origins are unclear, but some suggest these creatures arise from natural worms or similar invertebrates mutated by magical phenomena. Many cite the presence of gricks in a region as evidence of portals to other planes of existence, legendary magic items, or powerful supernatural beings.
## Statblock

```statblock
"name": "Grick Ancient (XMM)"
"size": "Large"
"type": "aberration"
"alignment": "Unaligned"
"ac": !!int "18"
"hp": !!int "135"
"hit_dice": "18d10 + 36"
"modifier": !!int "3"
"stats":
  - !!int "18"
  - !!int "16"
  - !!int "15"
  - !!int "4"
  - !!int "14"
  - !!int "9"
"speed": "30 ft., climb 30 ft."
"skillsaves":
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+6"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "7"
"actions":
  - "desc": "The grick makes one Beak attack, one Slam attack, and one Tentacles attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 22 (4d8 + 4) Piercing\
      \ damage."
    "name": "Beak"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 7 (1d6 + 4) Bludgeoning\
      \ damage. If the target is a Large or smaller creature, it has the [[conditions#Prone|Prone]]\
      \ condition."
    "name": "Slam"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 15 (2d10 + 4) Slashing\
      \ damage. If the target is a Large or smaller creature, it has the [[conditions#Grappled|Grappled]]\
      \ condition (escape DC 14) from all four tentacles."
    "name": "Tentacles"
"source":
  - "XMM"
"image": "Compendium/bestiary/aberration/token/grick-ancient-xmm.webp"
```
^statblock
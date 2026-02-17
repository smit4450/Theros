---
title: Satyr
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1-2
- monster/environment/feywild
- monster/environment/forest
- monster/environment/planar
- monster/size/medium
- monster/type/fey
statblock: inline
aliases: ["Satyr"]
---
# Satyr
*Source: Monster Manual (2024) p. 268, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/fey/img/satyrs.webp#right|850)  
Satyrs enjoy demonstrating their physicality through contests, evicting party poopers, and defending Fey realms.

## Satyrs

*Horned and Hoofed Revelers*

- **Habitat.** Forest, Planar (Feywild)  
- **Treasure.** [[random-magic-items-implements|Implements]]  

Satyrs embody the untamed joys of the wilderness. They indulge in sprees of merrymaking—eating, drinking, performing, fighting, and frolicking.
## Statblock

```statblock
"name": "Satyr (XMM)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "13"
"hp": !!int "31"
"hit_dice": "7d8"
"modifier": !!int "3"
"stats":
  - !!int "12"
  - !!int "16"
  - !!int "11"
  - !!int "12"
  - !!int "10"
  - !!int "14"
"speed": "40 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+2"
  - "name": "[[skills#Performance|Performance]]"
    "desc": "+6"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"senses": "passive Perception 12"
"languages": "Common, Elvish, Sylvan"
"cr": "1/2"
"traits":
  - "desc": "The satyr has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 5 (1d4 + 3) Bludgeoning\
      \ damage. If the target is a Medium or smaller creature, the satyr pushes the\
      \ target up to 10 feet straight away from itself."
    "name": "Hooves"
  - "desc": "*Wisdom Saving Throw:* DC 12, one creature the satyr can see within 90\
      \ feet. *Failure:* 5 (1d6 + 2) Psychic damage."
    "name": "Mockery"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/fey/token/satyr-xmm.webp"
```
^statblock
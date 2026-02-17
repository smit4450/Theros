---
title: Berserker
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/any
- monster/size/small-or-medium
- monster/type/humanoid
statblock: inline
aliases: ["Berserker"]
---
# Berserker
*Source: Monster Manual (2024) p. 37, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/humanoid/img/berserkers.webp#right|850)  
Berserkers might fight for personal glory or form motivated forces or howling hordes.

## Berserkers

*Raging Invaders and Impassioned Warriors*

- **Habitat.** Any  
- **Treasure.** [[random-magic-items-armaments|Armaments]], Individual  

Gripped by the adrenaline of battle, berserkers are reckless invaders, pit fighters, and other ferocious warriors.
## Statblock

```statblock
"name": "Berserker (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "13"
"hp": !!int "67"
"hit_dice": "9d8 + 27"
"modifier": !!int "1"
"stats":
  - !!int "16"
  - !!int "12"
  - !!int "17"
  - !!int "9"
  - !!int "11"
  - !!int "9"
"speed": "30 ft."
"senses": "passive Perception 10"
"languages": "Common"
"cr": "2"
"traits":
  - "desc": "While [[conditions#Bloodied|Bloodied]], the berserker\
      \ has [[advantage-xphb|Advantage]] on attack\
      \ rolls and saving throws."
    "name": "Bloodied Frenzy"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 9 (1d12 + 3) Slashing\
      \ damage."
    "name": "Greataxe"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/humanoid/token/berserker-xmm.webp"
```
^statblock
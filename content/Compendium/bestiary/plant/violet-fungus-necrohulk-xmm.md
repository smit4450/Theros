---
title: Violet Fungus Necrohulk
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/7
- monster/environment/underdark
- monster/size/large
- monster/type/plant
statblock: inline
aliases: ["Violet Fungus Necrohulk"]
---
# Violet Fungus Necrohulk
*Source: Monster Manual (2024) p. 126*  

![](Compendium/bestiary/plant/img/violet-fungus-necrohulk.webp#right|850)  
A violet fungus necrohulk forms when a violet fungus colony infests and animates an ample heap of decay. This necrohulk attacks prey and spreads fungal spores for the colony.

## Fungi

*Deadly Spores and Predatory Polyps*

- **Habitat.** Underdark  
- **Treasure.** None  

The dank, sunless Underdark is a fertile breeding ground for weird and dangerous fungi.
![](Compendium/bestiary/plant/img/fungi.webp#center)  
## Statblock

```statblock
"name": "Violet Fungus Necrohulk (XMM)"
"size": "Large"
"type": "plant"
"alignment": "Neutral Evil"
"ac": !!int "17"
"hp": !!int "123"
"hit_dice": "13d10 + 52"
"modifier": !!int "4"
"stats":
  - !!int "19"
  - !!int "12"
  - !!int "18"
  - !!int "7"
  - !!int "14"
  - !!int "10"
"speed": "40 ft."
"damage_immunities": "necrotic, poison"
"condition_immunities": "[[conditions#Blinded|blinded]], [[conditions#Charmed|charmed]],\
  \ [[conditions#Deafened|deafened]], [[conditions#Frightened|frightened]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Blindsight|Blindsight]] 60 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "7"
"actions":
  - "desc": "The necrohulk makes two Rotting Slam attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 9 (1d10 + 4) Bludgeoning\
      \ damage plus 7 (2d6) Necrotic damage."
    "name": "Rotting Slam"
  - "desc": "*Constitution Saving Throw:* DC 15, each creature in a 20-foot-radius\
      \ [[sphere-area-of-effect-xphb|Sphere]] centered\
      \ on a point the necrohulk can see within 60 feet. *Failure:* 28 (8d6) Necrotic\
      \ damage, and the target has the [[conditions#Poisoned|Poisoned]]\
      \ condition until the start of the necrohulk's next turn. While [[conditions#Poisoned|Poisoned]],\
      \ the target can't regain [[hit-points-xphb|Hit Points]].\
      \ *Success:* Half damage only."
    "name": "Spore Bomb (Recharge 5-6)"
"bonus_actions":
  - "desc": "*Strength Saving Throw:* DC 15, one Medium or Small creature the necrohulk\
      \ can see within 5 feet. *Failure:* The target is pulled into the necrohulk's\
      \ space and becomes grafted to its body. The necrohulk can have only one target\
      \ grafted at a time.\n\nWhile grafted, the target has the [[conditions#Restrained|Restrained]]\
      \ condition and [[disadvantage-xphb|Disadvantage]]\
      \ on Constitution saving throws. When the necrohulk moves, the grafted target\
      \ moves with it. If the target dies while grafted, its body is destroyed, and\
      \ the necrohulk regains 10 [[hit-points-xphb|Hit Points]].\n\
      \nThe grafted target or a creature within 5 feet of the necrohulk can take an\
      \ action to make a DC 15 Strength ([[skills#Athletics|Athletics]])\
      \ check. On a successful check, the target is no longer grafted and moves to\
      \ an unoccupied space within 5 feet of the necrohulk."
    "name": "Absorb Body"
"source":
  - "XMM"
"image": "Compendium/bestiary/plant/token/violet-fungus-necrohulk-xmm.webp"
```
^statblock
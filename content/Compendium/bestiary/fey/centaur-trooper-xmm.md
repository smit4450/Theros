---
title: Centaur Trooper
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/feywild
- monster/environment/forest
- monster/environment/grassland
- monster/environment/planar
- monster/size/large
- monster/type/fey
statblock: inline
aliases: ["Centaur Trooper"]
---
# Centaur Trooper
*Source: Monster Manual (2024) p. 67, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/fey/img/centaurs.webp#right|850)  
Centaur troopers are knight-like guardians. Many are suspicious of non-Fey creatures.

## Centaurs

*Defenders of the Feywild*

- **Habitat.** Forest, Grassland, Planar (Feywild)  
- **Treasure.** [[random-magic-items-armaments|Armaments]], Individual  

Centaurs are defenders of forests, plains, and sites of primeval power. With upper bodies like humans' and the lower bodies of horses, centaurs charge into battle against those who would harm their allies.
## Statblock

```statblock
"name": "Centaur Trooper (XMM)"
"size": "Large"
"type": "fey"
"alignment": "Neutral Good"
"ac": !!int "16"
"hp": !!int "45"
"hit_dice": "6d10 + 12"
"modifier": !!int "2"
"stats":
  - !!int "18"
  - !!int "14"
  - !!int "14"
  - !!int "9"
  - !!int "13"
  - !!int "11"
"speed": "50 ft."
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+6"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"senses": "passive Perception 13"
"languages": "Elvish, Sylvan"
"cr": "2"
"actions":
  - "desc": "The centaur makes two attacks, using Pike or Longbow in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6, reach 10 ft. *Hit:* 9 (1d10 + 4) Piercing\
      \ damage."
    "name": "Pike"
  - "desc": "*Ranged Attack Roll:* +4, range 150/600 ft. *Hit:* 6 (1d8 + 2) Piercing\
      \ damage."
    "name": "Longbow"
"bonus_actions":
  - "desc": "The centaur moves up to its [[speed-xphb|Speed]]\
      \ without provoking [[actions#Opportunity%20Attack|Opportunity Attacks]]\
      \ and can move through the spaces of Medium or smaller creatures. Each creature\
      \ whose space the centaur enters is targeted once by the following effect. *Strength\
      \ Saving Throw:* DC 14. *Failure:* 7 (1d6 + 4) Bludgeoning damage, and the\
      \ target has the [[conditions#Prone|Prone]] condition."
    "name": "Trampling Charge (Recharge 5-6)"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/fey/token/centaur-trooper-xmm.webp"
```
^statblock
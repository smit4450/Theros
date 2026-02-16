---
title: Centaur Warden
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/feywild
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Centaur Warden"]
---
# Centaur Warden
*Source: Monster Manual (2024) p. 67, FRHoF*  

![](Compendium/bestiary/fey/img/centaurs.webp#right|850)  
Centaur wardens often lead groups of centaur troopers and act as intermediaries between Fey creatures and trespassers into their territories.

## Centaurs

*Defenders of the Feywild*

- **Habitat.** Forest, Grassland, Planar (Feywild)  
- **Treasure.** [[random-magic-items-armaments|Armaments]], Individual  

Centaurs are defenders of forests, plains, and sites of primeval power. With upper bodies like humans' and the lower bodies of horses, centaurs charge into battle against those who would harm their allies.
## Statblock

```statblock
"name": "Centaur Warden (XMM)"
"size": "Large"
"type": "fey"
"alignment": "Neutral Good"
"ac": !!int "16"
"hp": !!int "105"
"hit_dice": "14d10 + 28"
"modifier": !!int "2"
"stats":
  - !!int "18"
  - !!int "14"
  - !!int "14"
  - !!int "9"
  - !!int "18"
  - !!int "11"
"speed": "50 ft."
"saves":
  - "constitution": !!int "5"
  - "wisdom": !!int "7"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+7"
  - "name": "[[skills#Nature|Nature]]"
    "desc": "+5"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+7"
"senses": "passive Perception 17"
"languages": "Druidic, Elvish, Sylvan"
"cr": "7"
"actions":
  - "desc": "The centaur makes two attacks, using Forest Staff or Sun Ray in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 13 (2d8 + 4) Bludgeoning\
      \ damage plus 14 (4d6) Poison damage."
    "name": "Forest Staff"
  - "desc": "*Ranged Attack Roll:* +7, range 90 ft. *Hit:* 14 (3d6 + 4) Radiant\
      \ damage, and the target has the [[conditions#Blinded|Blinded]]\
      \ condition until the start of the centaur's next turn."
    "name": "Sun Ray"
  - "desc": "The centaur casts one of the following spells, using Wisdom as the spellcasting\
      \ ability (spell save DC 15):\n\n**At will:** [[druidcraft-xphb|Druidcraft]],\
      \ [[speak-with-animals-xphb|Speak with Animals]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The centaur moves up to its [[speed-xphb|Speed]]\
      \ without provoking [[actions#Opportunity%20Attack|Opportunity Attacks]].\
      \ Each creature within 5 feet of the centaur as it moves is targeted once by\
      \ the following effect. *Strength Saving Throw:* DC 15. *Failure:* 11 (2d6\
      \ + 4) Bludgeoning damage, and the target has the [[conditions#Restrained|Restrained]]\
      \ condition until the end of its next turn."
    "name": "Entangling Trail (Recharge 5-6)"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/fey/token/centaur-warden-xmm.webp"
```
^statblock
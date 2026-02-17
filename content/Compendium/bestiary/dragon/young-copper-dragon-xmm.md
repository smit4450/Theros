---
title: Young Copper Dragon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/7
- monster/environment/hill
- monster/size/large
- monster/type/dragon/metallic
statblock: inline
aliases: ["Young Copper Dragon"]
---
# Young Copper Dragon
*Source: Monster Manual (2024) p. 78. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/dragon/img/copper-dragon.webp#right|850)  
Young copper dragons forge strong connections with a community or group of friends while flitting from one artistic fixation to the next.

## Copper Dragons

*Dragons of Curiosity and Community*

- **Habitat.** Hill  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Relentlessly friendly and curious, most copper dragons view the world as a place of endless wonder and possibility. These gregarious dragons are fonts of patience, hospitality, and humor, and they seek to improve the lives—or, at least, the mood—of those they interact with. If forced to fight to defend themselves or their friends, these dragons favor using their slowing breath and physical attacks to subdue antagonists. Only in cases of extreme peril or emotion do they use their deadly acid breath.

Copper dragons typically live in caverns amid picturesque hills and rock formations—particularly those that are prominent landmarks. These dragons collect gifts, though they have little interest in treasure without meaning, no matter how valuable it is. To them, thoughtfully given presents and the feelings or memories they symbolize are more important than masterpieces or magical relics.

### Copper Dragon Lairs

Copper dragons typically inhabit multi-chamber caves and renovated ruins.
## Statblock

```statblock
"name": "Young Copper Dragon (XMM)"
"size": "Large"
"type": "dragon"
"subtype": "metallic"
"alignment": "Chaotic Good"
"ac": !!int "17"
"hp": !!int "119"
"hit_dice": "14d10 + 42"
"modifier": !!int "4"
"stats":
  - !!int "19"
  - !!int "12"
  - !!int "17"
  - !!int "16"
  - !!int "13"
  - !!int "15"
"speed": "40 ft., climb 40 ft., fly 80 ft."
"saves":
  - "dexterity": !!int "4"
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+5"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+7"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
"damage_immunities": "acid"
"senses": "[[senses#Blindsight|Blindsight]] 30 ft., [[senses#Darkvision|Darkvision]]\
  \ 120 ft., passive Perception 17"
"languages": "Common, Draconic"
"cr": "7"
"actions":
  - "desc": "The dragon makes three Rend attacks. It can replace one attack with a\
      \ use of Slowing Breath."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 15 (2d10 + 4) Slashing\
      \ damage."
    "name": "Rend"
  - "desc": "*Dexterity Saving Throw:* DC 14, each creature in a 40-foot-long, 5-foot-wide\
      \ [[line-area-of-effect-xphb|Line]]. *Failure:*\
      \ 40 (9d8) Acid damage. *Success:* Half damage."
    "name": "Acid Breath (Recharge 5-6)"
  - "desc": "*Constitution Saving Throw:* DC 14, each creature in a 30-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* The target can't take Reactions; its [[speed-xphb|Speed]]\
      \ is halved; and it can take either an action or a [[bonus-action-xphb|Bonus Action]]\
      \ on its turn, not both. This effect lasts until the end of its next turn."
    "name": "Slowing Breath"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/young-copper-dragon-xmm.webp"
```
^statblock
---
title: Winged Kobold
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1-4
- monster/environment/arctic
- monster/environment/coastal
- monster/environment/desert
- monster/environment/forest
- monster/environment/hill
- monster/environment/mountain
- monster/environment/swamp
- monster/environment/underdark
- monster/environment/urban
- monster/size/small
- monster/type/dragon
statblock: inline
aliases: ["Winged Kobold"]
---
# Winged Kobold
*Source: Monster Manual (2024) p. 185*  

![](Compendium/bestiary/dragon/img/kobolds.webp#right|850)  
Some kobolds are born with wings. Called urds by others of their kind, these kobolds are thought to be blessed by a dragon or Tiamat, the Dragon Queen. Despite their favored status, winged kobolds are as cowardly as their brethren and use their flight mostly to keep out of reach of their foes.

## Kobolds

*Tricksters and Servants to Chromatic Dragons*

- **Habitat.** Arctic, Coastal, Desert, Forest, Hill, Mountain, Swamp, Underdark, Urban  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Cowardly cousins to chromatic dragons, kobolds serve draconic overlords as warriors and servants. These scrappy menaces mimic the behaviors of their dragon masters. Though their small stature and recklessness make kobolds poor imitators of dragons, what they lack in ferocity they make up for in zeal and ingenuity. They are especially adept at creating traps and setting ambushes.

Kobolds' scales resemble those of chromatic dragons that live near their warrens. Rarely, kobolds possess features evocative of metallic dragons or other dragon-like creatures.
## Statblock

```statblock
"name": "Winged Kobold (XMM)"
"size": "Small"
"type": "dragon"
"alignment": "Neutral"
"ac": !!int "15"
"hp": !!int "10"
"hit_dice": "4d6 - 4"
"modifier": !!int "3"
"stats":
  - !!int "7"
  - !!int "16"
  - !!int "9"
  - !!int "8"
  - !!int "7"
  - !!int "8"
"speed": "30 ft., fly 30 ft."
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 8"
"languages": "Common, Draconic"
"cr": "1/4"
"traits":
  - "desc": "The kobold has [[advantage-xphb|Advantage]]\
      \ on an attack roll against a creature if at least one of the kobold's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [[conditions#Incapacitated|Incapacitated]]\
      \ condition."
    "name": "Pack Tactics"
  - "desc": "While in sunlight, the kobold has [[disadvantage-xphb|Disadvantage]]\
      \ on ability checks and attack rolls."
    "name": "Sunlight Sensitivity"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 6 (1d6 + 3) Piercing\
      \ damage."
    "name": "Dragon-Tooth Blade"
  - "desc": "*Ranged Attack Roll:* +5, range 30 ft. *Hit:* 6 (1d6 + 3) damage\
      \ of a type chosen by the kobold: Acid, Cold, Fire, Lightning, or Poison."
    "name": "Chromatic Spittle"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/winged-kobold-xmm.webp"
```
^statblock
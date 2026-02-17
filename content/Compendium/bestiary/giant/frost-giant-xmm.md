---
title: Frost Giant
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/8
- monster/environment/arctic
- monster/environment/mountain
- monster/size/huge
- monster/type/giant
statblock: inline
aliases: ["Frost Giant"]
---
# Frost Giant
*Source: Monster Manual (2024) p. 124. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/giant/img/frost-giant.webp#right|850)  
## Frost Giant

*Giant of the Ice and Snow*

- **Habitat.** Arctic, Mountain  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

From glacial mountain heights and vast tundras rise the homes of frost giants. These giants have skin and hair of icy hues. Their natural immunity to cold allows them to flourish in places inhospitable to most other creatures. They use this resilience to aid them when hunting and in combat, bolstering their allies with chilling war cries.

Frost giants often travel far to find food and goods. This leads many to become raiders and earn violent reputations. Others live more peaceably by hunting titanic game or creating sanctuaries from the cold (frequently featuring hot springs or snowy contests). Frost giants sometimes forge partnerships with icy Fey or fire giants dwelling underground, serving as guardians to their realms in exchange for treasure, weapons, and crafts.

> [!quote] A quote from Jarl Grugnur, Frost Giant  
> 
> The small folk have barely anything worth looting, so they shouldn't much mind when we take it from them.

```statblock
"name": "Frost Giant (XMM)"
"size": "Huge"
"type": "giant"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "149"
"hit_dice": "13d12 + 65"
"modifier": !!int "2"
"stats":
  - !!int "23"
  - !!int "9"
  - !!int "21"
  - !!int "9"
  - !!int "10"
  - !!int "12"
"speed": "40 ft."
"saves":
  - "constitution": !!int "8"
  - "wisdom": !!int "3"
  - "charisma": !!int "4"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+9"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"damage_immunities": "cold"
"senses": "passive Perception 13"
"languages": "Giant"
"cr": "8"
"actions":
  - "desc": "The giant makes two attacks, using Frost Axe or Great Bow in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +9, reach 10 ft. *Hit:* 19 (2d12 + 6) Slashing\
      \ damage plus 9 (2d8) Cold damage."
    "name": "Frost Axe"
  - "desc": "*Ranged Attack Roll:* +9, range 150/600 ft. *Hit:* 17 (2d10 + 6)\
      \ Piercing damage plus 7 (2d6) Cold damage, and the target's [[speed-xphb|Speed]]\
      \ decreases by 10 feet until the end of its next turn."
    "name": "Great Bow"
"bonus_actions":
  - "desc": "The giant or one creature of its choice that can see or hear it gains\
      \ 16 (2d10 + 5) [[temporary-hit-points-xphb|Temporary Hit Points]]\
      \ and has [[advantage-xphb|Advantage]] on attack\
      \ rolls until the start of the giant's next turn."
    "name": "War Cry (Recharge 5-6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/giant/token/frost-giant-xmm.webp"
```
^statblock
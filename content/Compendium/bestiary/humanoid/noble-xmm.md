---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-8
- monster/environment/any
- monster/size/small-or-medium
- monster/type/humanoid
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Noble"
---
# Noble
*Source: Monster Manual (2024) p. 227. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/humanoid/img/nobles.webp#right)

A noble's social advantages typically grant the noble access to greater education and training than most common folk, while nobles' experience with business or politics makes many adept negotiators.

## Nobles

*Royals and Rich Folk*

- **Habitat.** Any  
- **Treasure.** Individual  

Nobles encompass a variety of people with social influence. They might be rulers, wealthy merchants, callous bureaucrats, or the idle elite.

## Statblock

```statblock
"name": "Noble"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "15"
"hp": !!int "9"
"hit_dice": "2d8"
"modifier": !!int "1"
"stats":
  - !!int "11"
  - !!int "12"
  - !!int "11"
  - !!int "12"
  - !!int "14"
  - !!int "16"
"speed": "30 ft."
"skillsaves":
  - "name": "[Deception](/Compendium/rules/skills.md#Deception)"
    "desc": "+5"
  - "name": "[Insight](/Compendium/rules/skills.md#Insight)"
    "desc": "+4"
  - "name": "[Persuasion](/Compendium/rules/skills.md#Persuasion)"
    "desc": "+5"
"gear":
  - "[breastplate](/Compendium/items/breastplate-xphb.md)"
  - "[rapier](/Compendium/items/rapier-xphb.md)"
"senses": "passive Perception 12"
"languages": "Common plus two other languages"
"cr": "1/8"
"actions":
  - "desc": "*Melee Attack Roll:* +3, reach 5 ft. *Hit:* 5 (1d8 + 1) Piercing damage."
    "name": "Rapier"
"reactions":
  - "desc": "Trigger: The noble is hit by a melee attack roll while holding a weapon.\
      \ _Response:_ The noble adds 2 to its AC against that attack, possibly causing\
      \ it to miss."
    "name": "Parry"
"source":
  - "XMM"
"image": "/Compendium/bestiary/humanoid/token/noble-xmm.webp"
```
^statblock

## Environment

any
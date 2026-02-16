---
title: Berserker Commander
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Berserker Commander"]
---
# Berserker Commander
*Source: Monster Manual (2024) p. 37*  

![](Compendium/bestiary/humanoid/img/berserkers.webp#right|850)  
Berserker commanders bear the scars of battle and drive their followers to match their deadly zeal. These commanders tap into a primal magic to enhance their might.

## Berserkers

*Raging Invaders and Impassioned Warriors*

- **Habitat.** Any  
- **Treasure.** [[random-magic-items-armaments|Armaments]], Individual  

Gripped by the adrenaline of battle, berserkers are reckless invaders, pit fighters, and other ferocious warriors.
## Statblock

```statblock
"name": "Berserker Commander (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "16"
"hp": !!int "136"
"hit_dice": "16d8 + 64"
"modifier": !!int "5"
"stats":
  - !!int "19"
  - !!int "14"
  - !!int "19"
  - !!int "10"
  - !!int "14"
  - !!int "9"
"speed": "40 ft."
"saves":
  - "strength": !!int "7"
  - "constitution": !!int "7"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+7"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]]"
"senses": "passive Perception 15"
"languages": "Common"
"cr": "8"
"traits":
  - "desc": "While [[conditions#Bloodied|Bloodied]], the berserker\
      \ has [[advantage-xphb|Advantage]] on attack\
      \ rolls and saving throws."
    "name": "Bloodied Frenzy"
"actions":
  - "desc": "The berserker makes three attacks, using Greataxe or Javelin in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 10 (1d12 + 4) Slashing\
      \ damage, plus 10 (3d6) Thunder damage to the target or another creature within\
      \ 5 feet of the target."
    "name": "Greataxe"
  - "desc": "*Melee  or Ranged Attack Roll:* +7, reach 5 ft. or range 30/120 ft.\
      \ *Hit:* 18 (4d6 + 4) Piercing damage, and the target's [[speed-xphb|Speed]]\
      \ decreases by 5 feet until the start of the berserker's next turn."
    "name": "Javelin"
"bonus_actions":
  - "desc": "Each ally within 30 feet of the berserker can take a [[reaction-xphb|Reaction]]\
      \ to move up to half the ally's [[speed-xphb|Speed]]\
      \ without provoking [[actions#Opportunity%20Attack|Opportunity Attacks]].\
      \ The berserker can also move up to half its [[speed-xphb|Speed]]\
      \ without provoking [[actions#Opportunity%20Attack|Opportunity Attacks]]."
    "name": "Frenzied Rush"
"source":
  - "XMM"
"image": "Compendium/bestiary/humanoid/token/berserker-commander-xmm.webp"
```
^statblock
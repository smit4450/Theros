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
- **Treasure.** [Armaments](Compendium/tables/random-magic-items-armaments.md), Individual  

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
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+7"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+5"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened)"
"senses": "passive Perception 15"
"languages": "Common"
"cr": "8"
"traits":
  - "desc": "While [Bloodied](Compendium/rules/conditions.md#Bloodied), the berserker\
      \ has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on attack\
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
      \ *Hit:* 18 (4d6 + 4) Piercing damage, and the target's [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
      \ decreases by 5 feet until the start of the berserker's next turn."
    "name": "Javelin"
"bonus_actions":
  - "desc": "Each ally within 30 feet of the berserker can take a [Reaction](Compendium/rules/variant-rules/reaction-xphb.md)\
      \ to move up to half the ally's [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
      \ without provoking [Opportunity Attacks](Compendium/rules/actions.md#Opportunity%20Attack).\
      \ The berserker can also move up to half its [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
      \ without provoking [Opportunity Attacks](Compendium/rules/actions.md#Opportunity%20Attack)."
    "name": "Frenzied Rush"
"source":
  - "XMM"
"image": "Compendium/bestiary/humanoid/token/berserker-commander-xmm.webp"
```
^statblock
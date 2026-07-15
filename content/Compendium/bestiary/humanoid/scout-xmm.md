---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-2
- monster/environment/any
- monster/size/small-or-medium
- monster/type/humanoid
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Scout"
---
# Scout
*Source: Monster Manual (2024) p. 270. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/humanoid/img/scouts.webp#right)

Scouts are keen archers and acutely aware of their surroundings. They often know several regions particularly well and are familiar with local creatures, landmarks, and perils.

## Scouts

*Watchers and Wanderers*

- **Habitat.** Any  
- **Treasure.** [Implements](/Compendium/tables/random-magic-items-implements.md), Individual  

Scouts are warriors of the wilderness, trained in hunting and tracking. They might be explorers or trappers, or they could perform more martial roles as archers, bounty hunters, or outriders.

## Statblock

```statblock
"name": "Scout"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "13"
"hp": !!int "16"
"hit_dice": "3d8 + 3"
"modifier": !!int "2"
"stats":
  - !!int "11"
  - !!int "14"
  - !!int "12"
  - !!int "11"
  - !!int "13"
  - !!int "11"
"speed": "30 ft."
"skillsaves":
  - "name": "[Nature](/Compendium/rules/skills.md#Nature)"
    "desc": "+4"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+5"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+6"
  - "name": "[Survival](/Compendium/rules/skills.md#Survival)"
    "desc": "+5"
"gear":
  - "[leather armor](/Compendium/items/leather-armor-xphb.md)"
  - "[longbow](/Compendium/items/longbow-xphb.md)"
  - "[shortsword](/Compendium/items/shortsword-xphb.md)"
"senses": "passive Perception 15"
"languages": "Common plus one other language"
"cr": "1/2"
"actions":
  - "desc": "The scout makes two attacks, using Shortsword and Longbow in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 5 (1d6 + 2) Piercing damage."
    "name": "Shortsword"
  - "desc": "*Ranged Attack Roll:* +4, range 150/600 ft. *Hit:* 6 (1d8 + 2) Piercing\
      \ damage."
    "name": "Longbow"
"source":
  - "XMM"
"image": "/Compendium/bestiary/humanoid/token/scout-xmm.webp"
```
^statblock

## Environment

any
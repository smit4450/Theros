---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-8
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
statblock-link: "#^statblock"
aliases:
- "Kobold Warrior"
---
# Kobold Warrior
*Source: Monster Manual (2024) p. 185. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/dragon/img/kobolds.webp#right)

Kobold warriors use hit-and-run tactics to raid their enemies and defend their homes. To avoid danger, they frequently employ haphazard traps.

## Kobolds

*Tricksters and Servants to Chromatic Dragons*

- **Habitat.** Arctic, Coastal, Desert, Forest, Hill, Mountain, Swamp, Underdark, Urban  
- **Treasure.** [Armaments](/Compendium/tables/random-magic-items-armaments.md)  

Cowardly cousins to chromatic dragons, kobolds serve draconic overlords as warriors and servants. These scrappy menaces mimic the behaviors of their dragon masters. Though their small stature and recklessness make kobolds poor imitators of dragons, what they lack in ferocity they make up for in zeal and ingenuity. They are especially adept at creating traps and setting ambushes.

Kobolds' scales resemble those of chromatic dragons that live near their warrens. Rarely, kobolds possess features evocative of metallic dragons or other dragon-like creatures.

## Statblock

```statblock
"name": "Kobold Warrior"
"size": "Small"
"type": "dragon"
"alignment": "Neutral"
"ac": !!int "14"
"hp": !!int "7"
"hit_dice": "3d6 - 3"
"modifier": !!int "2"
"stats":
  - !!int "7"
  - !!int "15"
  - !!int "9"
  - !!int "8"
  - !!int "7"
  - !!int "8"
"speed": "30 ft."
"gear":
  - "three [daggers](/Compendium/items/dagger-xphb.md)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 8"
"languages": "Common, Draconic"
"cr": "1/8"
"traits":
  - "desc": "The kobold has [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on an attack roll against a creature if at least one of the kobold's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [Incapacitated](/Compendium/rules/conditions.md#Incapacitated)\
      \ condition."
    "name": "Pack Tactics"
  - "desc": "While in sunlight, the kobold has [Disadvantage](/Compendium/rules/variant-rules/disadvantage-xphb.md)\
      \ on ability checks and attack rolls."
    "name": "Sunlight Sensitivity"
"actions":
  - "desc": "*Melee  or Ranged Attack Roll:* +4, reach 5 ft. or range 20/60 ft. *Hit:*\
      \ 4 (1d4 + 2) Piercing damage."
    "name": "Dagger"
"source":
  - "XMM"
"image": "/Compendium/bestiary/dragon/token/kobold-warrior-xmm.webp"
```
^statblock

## Environment

arctic, coastal, desert, forest, hill, mountain, swamp, underdark, urban
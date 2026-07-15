---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/6
- monster/environment/coastal
- monster/environment/desert
- monster/environment/grassland
- monster/environment/hill
- monster/environment/mountain
- monster/environment/underdark
- monster/size/huge
- monster/type/giant
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Cyclops Sentry"
---
# Cyclops Sentry
*Source: Monster Manual (2024) p. 88*
![](/Compendium/bestiary/giant/img/cyclopes.webp#right)

Most cyclops sentries serve their divine progenitors and oppose those who would tamper with fate.

## Cyclopes

*Monocular Servants of Destiny*

- **Habitat.** Coastal, Desert, Grassland, Hill, Mountain, Underdark  
- **Treasure.** [Armaments](/Compendium/tables/random-magic-items-armaments.md)  

Cyclopes are gigantic, one-eyed descendants of the gods. Using their mystical vision, cyclopes can witness how future events are likely to occur.

## Statblock

```statblock
"name": "Cyclops Sentry"
"size": "Huge"
"type": "giant"
"alignment": "Chaotic Neutral"
"ac": !!int "14"
"hp": !!int "138"
"hit_dice": "12d12 + 60"
"modifier": !!int "0"
"stats":
  - !!int "22"
  - !!int "11"
  - !!int "20"
  - !!int "8"
  - !!int "6"
  - !!int "10"
"speed": "40 ft."
"senses": "passive Perception 8"
"languages": "Giant"
"cr": "6"
"actions":
  - "desc": "The cyclops makes two attacks, using Stone Club or Rock in any combination."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +9, reach 10 ft. *Hit:* 16 (3d6 + 6) Bludgeoning\
      \ damage. If the target is a Huge or smaller creature, it has the [Prone](/Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Stone Club"
  - "desc": "*Ranged Attack Roll:* +9, range 30/120 ft. *Hit:* 22 (3d10 + 6) Bludgeoning\
      \ damage."
    "name": "Rock"
"reactions":
  - "desc": "Trigger: A creature the cyclops can see makes an attack roll against\
      \ it. _Response:_ The cyclops imposes [Disadvantage](/Compendium/rules/variant-rules/disadvantage-xphb.md)\
      \ on the roll, and the cyclops gains [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on attack rolls against the target until the end of the cyclops's next turn."
    "name": "Limited Foresight (Recharge 6)"
"source":
  - "XMM"
"image": "/Compendium/bestiary/giant/token/cyclops-sentry-xmm.webp"
```
^statblock

## Environment

coastal, desert, grassland, hill, mountain, underdark
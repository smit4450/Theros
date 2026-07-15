---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-2
- monster/environment/underdark
- monster/size/large
- monster/type/plant
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Gas Spore Fungus"
---
# Gas Spore Fungus
*Source: Monster Manual (2024) p. 125*
![](/Compendium/bestiary/plant/img/fungi.webp#right)

Gas spores are floating, orbicular fungi with rhizome growths and protuberances that resemble the stalks and eyes of beholders. If destroyed, a gas spore explodes in a poisonous burst that can infect creatures and slay them in hours. Infected corpses spawn more gas spores that grow to full size in a matter of days.

## Fungi

*Deadly Spores and Predatory Polyps*

- **Habitat.** Underdark  
- **Treasure.** None  

The dank, sunless Underdark is a fertile breeding ground for weird and dangerous fungi.

## Statblock

```statblock
"name": "Gas Spore Fungus"
"size": "Large"
"type": "plant"
"alignment": "Unaligned"
"ac": !!int "8"
"hp": !!int "13"
"hit_dice": "9d10 - 36"
"modifier": !!int "-5"
"stats":
  - !!int "5"
  - !!int "1"
  - !!int "3"
  - !!int "1"
  - !!int "1"
  - !!int "1"
"speed": "5 ft., fly 10 ft. (hover)"
"damage_immunities": "poison"
"condition_immunities": "[blinded](/Compendium/rules/conditions.md#Blinded), [charmed](/Compendium/rules/conditions.md#Charmed),\
  \ [deafened](/Compendium/rules/conditions.md#Deafened), [frightened](/Compendium/rules/conditions.md#Frightened),\
  \ [paralyzed](/Compendium/rules/conditions.md#Paralyzed), [poisoned](/Compendium/rules/conditions.md#Poisoned),\
  \ [prone](/Compendium/rules/conditions.md#Prone)"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 30 ft., passive Perception\
  \ 5"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "The gas spore bursts when it dies. *Constitution Saving Throw:* DC 10,\
      \ each creature in a 20-foot [Emanation](/Compendium/rules/variant-rules/emanation-area-of-effect-xphb.md)\
      \ originating from the gas spore. *Failure:* The target takes 10 (3d6) Poison\
      \ damage and has the [Poisoned](/Compendium/rules/conditions.md#Poisoned) condition\
      \ for 1d12 hours. Unless the [Poisoned](/Compendium/rules/conditions.md#Poisoned)\
      \ condition is removed, the target dies at the end of that time and sprouts\
      \ 2d4 Tiny Gas Spore Fungi (each with 1 [Hit Point](/Compendium/rules/variant-rules/hit-points-xphb.md)).\
      \ After 2d6 days, they become Large and have 13 [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Death Burst"
"actions":
  - "desc": "*Melee Attack Roll:* +0, reach 5 ft. *Hit:* 3 (1d6) Poison damage, and\
      \ the target has the [Poisoned](/Compendium/rules/conditions.md#Poisoned) condition\
      \ until the end of its next turn."
    "name": "Tendril"
"source":
  - "XMM"
"image": "/Compendium/bestiary/plant/token/gas-spore-fungus-xmm.webp"
```
^statblock

## Environment

underdark
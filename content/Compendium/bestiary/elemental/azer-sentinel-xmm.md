---
title: Azer Sentinel
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/fire
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Azer Sentinel"]
---
# Azer Sentinel
*Source: Monster Manual (2024) p. 25. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/elemental/img/azers.webp#right|850)  
Azer sentinels defend their communities' smiths and channel their flames through their weapons.

## Azers

*Fiery Smiths of Living Metal*

- **Habitat.** Mountain, Planar (Elemental Plane of Fire)  
- **Treasure.** [Armaments](Compendium/tables/random-magic-items-armaments.md), Individual  

Azers are living bronze folk who work the primal elements of creation to craft weapons and magical wonders among the multiverse's mightiest infernos.
## Statblock

```statblock
"name": "Azer Sentinel (XMM)"
"size": "Medium"
"type": "elemental"
"alignment": "Lawful Neutral"
"ac": !!int "17"
"hp": !!int "39"
"hit_dice": "6d8 + 12"
"modifier": !!int "1"
"stats":
  - !!int "17"
  - !!int "12"
  - !!int "15"
  - !!int "12"
  - !!int "13"
  - !!int "10"
"speed": "30 ft."
"saves":
  - "constitution": !!int "4"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "passive Perception 11"
"languages": "Primordial (Ignan)"
"cr": "2"
"traits":
  - "desc": "At the end of each of the azer's turns, each creature of the azer's choice\
      \ in a 5-foot [Emanation](Compendium/rules/variant-rules/emanation-area-of-effect-xphb.md)\
      \ originating from the azer takes 5 (1d10) Fire damage unless the azer has\
      \ the [Incapacitated](Compendium/rules/conditions.md#Incapacitated) condition."
    "name": "Fire Aura"
  - "desc": "The azer sheds [Bright Light](Compendium/rules/variant-rules/bright-light-xphb.md)\
      \ in a 10-foot radius and [Dim Light](Compendium/rules/variant-rules/dim-light-xphb.md)\
      \ for an additional 10 feet."
    "name": "Illumination"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 8 (1d10 + 3) Bludgeoning\
      \ damage plus 3 (1d6) Fire damage."
    "name": "Burning Hammer"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/azer-sentinel-xmm.webp"
```
^statblock
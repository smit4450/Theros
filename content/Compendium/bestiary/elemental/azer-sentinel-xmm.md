---
title: Azer Sentinel
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/fire
- monster/environment/mountain
- monster/environment/planar
- monster/size/medium
- monster/type/elemental
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
- **Treasure.** [[random-magic-items-armaments|Armaments]], Individual  

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
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "passive Perception 11"
"languages": "Primordial (Ignan)"
"cr": "2"
"traits":
  - "desc": "At the end of each of the azer's turns, each creature of the azer's choice\
      \ in a 5-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the azer takes 5 (1d10) Fire damage unless the azer has\
      \ the [[conditions#Incapacitated|Incapacitated]] condition."
    "name": "Fire Aura"
  - "desc": "The azer sheds [[bright-light-xphb|Bright Light]]\
      \ in a 10-foot radius and [[dim-light-xphb|Dim Light]]\
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
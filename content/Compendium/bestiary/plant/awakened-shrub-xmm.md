---
title: Awakened Shrub
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Awakened Shrub"]
---
# Awakened Shrub
*Source: Monster Manual (2024) p. 23, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/plant/img/awakened-shrub.webp#right|850)  
Awakened shrubs can be any sort of small plant, from forest bushes to clustered flowers. They often appear near awakened trees or in regions imbued with primal magic. Some have whimsical appearances or foliage resembling rudimentary facial features, while others look like animate topiary creatures.

## Awakened Plants

*Vegetation Given Magical Life*

- **Habitat.** Forest  
- **Treasure.** None  

Magic can invest plants with mobility, sapience, and even a voice. Spells such as [[awaken-xphb|Awaken]] or the influence of other planes of existence might bring mundane vegetation to life, while other remarkable plants might naturally have these features.

> [!quote] A quote from Rivergleam, Pixie  
> 
> Just because we protect the forest doesn't mean it's defenseless.

## Statblock

```statblock
"name": "Awakened Shrub (XMM)"
"size": "Small"
"type": "plant"
"alignment": "Neutral"
"ac": !!int "9"
"hp": !!int "10"
"hit_dice": "3d6"
"modifier": !!int "-1"
"stats":
  - !!int "3"
  - !!int "8"
  - !!int "11"
  - !!int "10"
  - !!int "10"
  - !!int "6"
"speed": "20 ft."
"damage_vulnerabilities": "fire"
"damage_resistances": "piercing"
"senses": "passive Perception 10"
"languages": "Common plus one other language"
"cr": "0"
"actions":
  - "desc": "*Melee Attack Roll:* +1, reach 5 ft. *Hit:* 1 Slashing damage."
    "name": "Rake"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/plant/token/awakened-shrub-xmm.webp"
```
^statblock
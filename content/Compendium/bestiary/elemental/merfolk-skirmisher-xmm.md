---
title: Merfolk Skirmisher
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1-8
- monster/environment/coastal
- monster/environment/underwater
- monster/size/medium
- monster/type/elemental
statblock: inline
aliases: ["Merfolk Skirmisher"]
---
# Merfolk Skirmisher
*Source: Monster Manual (2024) p. 209. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/elemental/img/merfolk.webp#right|850)  
Merfolk skirmishers defend their homes from aquatic monsters and invaders from the surface.

## Merfolk

*Protectors and Explorers of the Seas*

- **Habitat.** Coastal, Underwater  
- **Treasure.** Individual  

Beneath the waves dwell merfolk, mysterious creatures that merge the features of humans and sea creatures. Some are curious about land dwellers, while others view them with suspicion.
## Statblock

```statblock
"name": "Merfolk Skirmisher (XMM)"
"size": "Medium"
"type": "elemental"
"alignment": "Neutral"
"ac": !!int "11"
"hp": !!int "11"
"hit_dice": "2d8 + 2"
"modifier": !!int "1"
"stats":
  - !!int "10"
  - !!int "13"
  - !!int "12"
  - !!int "11"
  - !!int "14"
  - !!int "12"
"speed": "10 ft., swim 40 ft."
"senses": "passive Perception 12"
"languages": "Common, Primordial (Aquan)"
"cr": "1/8"
"traits":
  - "desc": "The merfolk can breathe air and water."
    "name": "Amphibious"
"actions":
  - "desc": "*Melee  or Ranged Attack Roll:* +2, reach 5 ft. or range 20/60 ft.\
      \ *Hit:* 3 (1d6) Piercing damage plus 2 (1d4) Cold damage. If the target\
      \ is a creature, its [[speed-xphb|Speed]] decreases\
      \ by 10 feet until the end of its next turn. *Hit or Miss:* The spear magically\
      \ returns to the merfolk's hand immediately after a ranged attack."
    "name": "Ocean Spear"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/merfolk-skirmisher-xmm.webp"
```
^statblock
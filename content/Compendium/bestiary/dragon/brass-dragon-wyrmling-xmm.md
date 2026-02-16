---
title: Brass Dragon Wyrmling
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/dragon/metallic
statblock: inline
aliases: ["Brass Dragon Wyrmling"]
---
# Brass Dragon Wyrmling
*Source: Monster Manual (2024) p. 54. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/dragon/img/brass-dragon-wyrmling.webp#right|850)  
Brass dragon wyrmlings are relentlessly curious. These dragons eagerly engage approachable creatures and are quick to explore any place that has an interesting story. Once they hear tales of adventure, many are keen to start their own quests.

## Brass Dragons

*Dragons of Lore and Rapport*

- **Habitat.** Desert  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Gregarious and outgoing, brass dragons relish sharing knowledge and stories. Although these metallic dragons favor arid lands, they cheerfully journey considerable distances to visit friendly creatures, pass on what they've learned, and collect news. Though good natured, brass dragons don't shirk from combat when necessary, thwarting foes with magical sleep and searing them with flame.

Brass dragons favor warm climes, particularly steppes and rocky or sandy deserts, and they usually dwell near prominent crossroads or oases that regularly draw visitors. They enjoy adopting Humanoid forms, disguising themselves as traveling merchants, scholars, storytellers, or anyone else invested in others' stories.

Brass dragons collect eclectic objects. While such items might seem like knickknacks, each is part of a story—perhaps a nostalgic memento or evidence of a tale passed into myth. An old friend's hat and the crown of the last ruler of a forgotten dynasty could occupy the same shelf in a brass dragon's hoard.

### Brass Dragon Lairs

Brass dragons usually dwell in secret caves and canyons near well-traveled routes.
## Statblock

```statblock
"name": "Brass Dragon Wyrmling (XMM)"
"size": "Medium"
"type": "dragon"
"subtype": "metallic"
"alignment": "Chaotic Good"
"ac": !!int "15"
"hp": !!int "22"
"hit_dice": "4d8 + 4"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "10"
  - !!int "13"
  - !!int "10"
  - !!int "11"
  - !!int "13"
"speed": "30 ft., burrow 15 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "2"
  - "wisdom": !!int "2"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+2"
"damage_immunities": "fire"
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., [[senses#Darkvision|Darkvision]]\
  \ 60 ft., passive Perception 14"
"languages": "Draconic"
"cr": "1"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 7 (1d10 + 2) Slashing\
      \ damage."
    "name": "Rend"
  - "desc": "*Dexterity Saving Throw:* DC 11, each creature in a 20-foot-long, 5-foot-wide\
      \ [[line-area-of-effect-xphb|Line]]. *Failure:*\
      \ 14 (4d6) Fire damage. *Success:* Half damage."
    "name": "Fire Breath (Recharge 5-6)"
  - "desc": "*Constitution Saving Throw:* DC 11, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* The target has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition until the end of its next turn, at which point it repeats the save.\
      \ *2Nd Failure:* The target has the [[conditions#Unconscious|Unconscious]]\
      \ condition for 1 minute. This effect ends for the target if it takes damage\
      \ or a creature within 5 feet of it takes an action to wake it."
    "name": "Sleep Breath"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/brass-dragon-wyrmling-xmm.webp"
```
^statblock
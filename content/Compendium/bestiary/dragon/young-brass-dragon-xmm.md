---
title: Young Brass Dragon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon/metallic
statblock: inline
aliases: ["Young Brass Dragon"]
---
# Young Brass Dragon
*Source: Monster Manual (2024) p. 54. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/dragon/img/brass-dragon.webp#right|850)  
Young brass dragons travel extensively, often spending a few years in a region before circling back to their lair. Some work closely with other metallic dragons, carrying information between allies.

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
"name": "Young Brass Dragon (XMM)"
"size": "Large"
"type": "dragon"
"subtype": "metallic"
"alignment": "Chaotic Good"
"ac": !!int "17"
"hp": !!int "110"
"hit_dice": "13d10 + 39"
"modifier": !!int "3"
"stats":
  - !!int "19"
  - !!int "10"
  - !!int "17"
  - !!int "12"
  - !!int "11"
  - !!int "15"
"speed": "40 ft., burrow 20 ft., fly 80 ft."
"saves":
  - "dexterity": !!int "3"
  - "wisdom": !!int "3"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+5"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+3"
"damage_immunities": "fire"
"senses": "[[senses#Blindsight|Blindsight]] 30 ft., [[senses#Darkvision|Darkvision]]\
  \ 120 ft., passive Perception 16"
"languages": "Common, Draconic"
"cr": "6"
"actions":
  - "desc": "The dragon makes three Rend attacks. It can replace two attacks with\
      \ a use of Sleep Breath."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 10 ft. *Hit:* 15 (2d10 + 4) Slashing\
      \ damage."
    "name": "Rend"
  - "desc": "*Dexterity Saving Throw:* DC 14, each creature in a 40-foot-long, 5-foot-wide\
      \ [[line-area-of-effect-xphb|Line]]. *Failure:*\
      \ 38 (11d6) Fire damage. *Success:* Half damage."
    "name": "Fire Breath (Recharge 5-6)"
  - "desc": "*Constitution Saving Throw:* DC 14, each creature in a 30-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* The target has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition until the end of its next turn, at which point it repeats the save.\
      \ *2Nd Failure:* The target has the [[conditions#Unconscious|Unconscious]]\
      \ condition for 1 minute. This effect ends for the target if it takes damage\
      \ or a creature within 5 feet of it takes an action to wake it."
    "name": "Sleep Breath"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/young-brass-dragon-xmm.webp"
```
^statblock
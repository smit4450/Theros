---
title: Minotaur Skeleton
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/planar
- monster/environment/shadowfell
- monster/environment/underdark
- monster/environment/urban
- monster/size/large
- monster/type/undead
statblock: inline
aliases: ["Minotaur Skeleton"]
---
# Minotaur Skeleton
*Source: Monster Manual (2024) p. 283. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![Adventurers face an onslau...](Compendium/bestiary/undead/img/skeletons.webp#right|850)  
Minotaur skeletons are the reanimated remains of minotaurs or the skeletons of multiple creatures merged into a minotaur-like shape. These hulking skeletons have greater speed and might than smaller skeletons. They menace the living with their horns and mighty greataxes.

## Skeletons

*Ossified Evil*

- **Habitat.** Planar (Shadowfell), Underdark, Urban  
- **Treasure.** None  

Skeletons rise at the summons of necromancers and foul spirits. Whether they're the remains of the ancient dead or fresh bones bound to morbid ambitions, they commit deathless work for whatever forces reanimated them, often serving as guardians, soldiers, or laborers. In rare cases, skeletons are reanimated but given no particular direction. Roll on or choose a result from the Skeleton Pantomimes table to inspire how undirected skeletons behave.

**Skeleton Pantomimes**

| dice: 1d6 | Left to Its Own Devices, the Skeleton... |
|-----------|------------------------------------------|
| 1 | Delivers meal salvers or ages-old correspondence to the crypt of its dead master. |
| 2 | Endlessly trains in battle with other skeletons, despite being hacked to animate splinters. |
| 3 | Mimics ways it entertained itself in life, such as acting, dancing, or reading. |
| 4 | Performs a familiar task, such as cleaning, cooking, mining, or praying. |
| 5 | Repeats its final moments of life. |
| 6 | Stands guard at the post it protected in life. |
^skeleton-pantomimes
## Statblock

```statblock
"name": "Minotaur Skeleton (XMM)"
"size": "Large"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "12"
"hp": !!int "45"
"hit_dice": "6d10 + 12"
"modifier": !!int "0"
"stats":
  - !!int "18"
  - !!int "11"
  - !!int "15"
  - !!int "6"
  - !!int "8"
  - !!int "5"
"speed": "40 ft."
"damage_vulnerabilities": "bludgeoning"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 9"
"languages": "understands Abyssal but can't speak"
"cr": "2"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 11 (2d6 + 4) Piercing\
      \ damage. If the target is a Large or smaller creature and the skeleton moved\
      \ 20+ feet straight toward it immediately before the hit, the target takes an\
      \ extra 9 (2d8) Piercing damage and has the [[conditions#Prone|Prone]]\
      \ condition."
    "name": "Gore"
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 15 (2d10 + 4) Bludgeoning\
      \ damage."
    "name": "Slam"
"source":
  - "XMM"
"image": "Compendium/bestiary/undead/token/minotaur-skeleton-xmm.webp"
```
^statblock
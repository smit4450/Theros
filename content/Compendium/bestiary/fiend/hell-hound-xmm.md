---
title: Hell Hound
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/3
- monster/environment/lower
- monster/environment/mountain
- monster/environment/planar
- monster/environment/underdark
- monster/size/medium
- monster/type/fiend
statblock: inline
aliases: ["Hell Hound"]
---
# Hell Hound
*Source: Monster Manual (2024) p. 165. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/fiend/img/hell-hound.webp#right|850)  
## Hell Hound

*Unrelenting Warden of the Lower Planes*

- **Habitat.** Mountain, Planar (Lower Planes), Underdark  
- **Treasure.** None  

Spawned from the pits of Acheron, Gehenna, and the Nine Hells, hell hounds enforce the merciless order of those realms and the whims of tyrannical masters. On their home planes of existence, these grim canines ensure that souls don't escape their bleak afterlives. On the Material Plane, hell hounds typically serve cruel masters—such as fire giants and cultists—who appreciate their viciousness, obedience, and fiery characteristics. Hell hounds serve other creatures so long as they're given opportunities to hunt and kill, but they're quick to turn on those who treat them as mere animals.

Hell hounds have greater cunning than normal canines. They're skilled trackers and work together well in packs, often employing tricks and ambushes. Hell hounds enjoy hearing prey scream in their scorching jaws and fiery breath. They often go out of their way to draw out the terror of their victims' final moments.
```statblock
"name": "Hell Hound (XMM)"
"size": "Medium"
"type": "fiend"
"alignment": "Lawful Evil"
"ac": !!int "15"
"hp": !!int "58"
"hit_dice": "9d8 + 18"
"modifier": !!int "1"
"stats":
  - !!int "17"
  - !!int "12"
  - !!int "14"
  - !!int "6"
  - !!int "13"
  - !!int "6"
"speed": "50 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
"damage_immunities": "fire"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 15"
"languages": "understands Infernal but can't speak"
"cr": "3"
"traits":
  - "desc": "The hound has [[advantage-xphb|Advantage]]\
      \ on an attack roll against a creature if at least one of the hound's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [[conditions#Incapacitated|Incapacitated]]\
      \ condition."
    "name": "Pack Tactics"
"actions":
  - "desc": "The hound makes two Bite attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 7 (1d8 + 3) Piercing\
      \ damage plus 3 (1d6) Fire damage."
    "name": "Bite"
  - "desc": "*Dexterity Saving Throw:* DC 12, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 17 (5d6) Fire damage. *Success:* Half damage."
    "name": "Fire Breath (Recharge 5-6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/hell-hound-xmm.webp"
```
^statblock
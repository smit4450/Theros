---
title: Chasme
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/6
- monster/environment/abyss
- monster/environment/planar
- monster/size/large
- monster/type/fiend/demon
statblock: inline
aliases: ["Chasme"]
---
# Chasme
*Source: Monster Manual (2024) p. 69*  

![](Compendium/books/monster-manual-2025/img/chasme.webp#right)  
## Chasme

*Demon of Betrayal and Sycophancy*

- **Habitat.** Planar (Abyss)  
- **Treasure.** [[random-magic-items-relics|Relics]]  

Flying forth from the Abyss, chasmes resemble horse-size flies. They incapacitate foes by producing a mind-numbing droning, then use their proboscises to drain victims of life. In the Abyss, most chasmes obsequiously serve more powerful demons and search for captives to press into demonic hordes.
```statblock
"name": "Chasme (XMM)"
"size": "Large"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"hp": !!int "78"
"hit_dice": "12d10 + 12"
"modifier": !!int "5"
"stats":
  - !!int "15"
  - !!int "15"
  - !!int "12"
  - !!int "11"
  - !!int "14"
  - !!int "10"
"speed": "20 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "5"
  - "wisdom": !!int "5"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., [[senses#Darkvision|Darkvision]]\
  \ 120 ft., passive Perception 15"
"languages": "Abyssal; telepathy 120 ft."
"cr": "6"
"traits":
  - "desc": "If the chasme dies outside the Abyss, its body dissolves into ichor,\
      \ and it gains a new body instantly, reviving with all its [[hit-points-xphb|Hit Points]]\
      \ somewhere in the Abyss."
    "name": "Demonic Restoration"
  - "desc": "The chasme has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "The chasme can climb difficult surfaces, including along ceilings, without\
      \ needing to make an ability check."
    "name": "Spider Climb"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 16 (4d6 + 2) Piercing\
      \ damage plus 21 (6d6) Necrotic damage. If the target is a creature, its [[hit-points-xphb|Hit\
      \ Point]] maximum decreases\
      \ by an amount equal to the Necrotic damage taken."
    "name": "Proboscis"
"bonus_actions":
  - "desc": "*Constitution Saving Throw:* DC 12, each creature in a 30-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the chasme (demons automatically succeed on this save). *Failure:*\
      \ The target has the [[conditions#Unconscious|Unconscious]]\
      \ condition and repeats the save at the end of each of its turns. The target\
      \ succeeds automatically after 10 minutes or if it takes damage or a creature\
      \ within 5 feet of it takes an action to empty a flask of Holy Water on it.\
      \ *Success:* The target is immune to this chasme's Drone for 24 hours."
    "name": "Drone"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/chasme-xmm.webp"
```
^statblock
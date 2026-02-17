---
title: Erinyes
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/12
- monster/environment/nine-hells
- monster/environment/planar
- monster/size/medium
- monster/type/fiend/devil
statblock: inline
aliases: ["Erinyes"]
---
# Erinyes
*Source: Monster Manual (2024) p. 114, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/books/monster-manual-2025/img/erinyes.webp#right)  
## Erinyes

*Devil of Vengeance and Righteous Wrath*

- **Habitat.** Planar (Nine Hells)  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Erinyes, also known as furies, are winged devils clad in fiendish armor. These fallen angels exact a merciless form of divine justice, hunting down oath breakers and dragging the rightfully damned to the Nine Hells in the grip of their magical ropes. Few ever glimpse what lies within these devils' armored exteriors, and erinyes ensure that those who do can never speak of what they've seen.

Erinyes often serve archdevils and guard the order of the Nine Hells against trespassers and escapees. Although they're prone to wrathful outbursts, erinyes cooperate well with other devils. They sometimes hunt in trios with other erinyes, forging infamous reputations for themselves.

When not in the service of a diabolical master, erinyes hunt wicked souls. They pursue quarries relentlessly, across the multiverse and for ages if need be. While they might be summoned to serve evil magic-users, erinyes also listen for oaths and curses sworn in their names. In rare cases, wronged mortals who call out with just rage might be heard by an erinyes who appears to take vengeance on their behalf. Once erinyes are so summoned, they won't leave without claiming the soul of either their quarry or the mortal who summoned them.
```statblock
"name": "Erinyes (XMM)"
"size": "Medium"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "18"
"hp": !!int "178"
"hit_dice": "21d8 + 84"
"modifier": !!int "7"
"stats":
  - !!int "18"
  - !!int "16"
  - !!int "18"
  - !!int "14"
  - !!int "14"
  - !!int "18"
"speed": "30 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "7"
  - "constitution": !!int "8"
  - "charisma": !!int "8"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+8"
"damage_resistances": "cold"
"damage_immunities": "fire, poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception\
  \ 16"
"languages": "Infernal; telepathy 120 ft."
"cr": "12"
"traits":
  - "desc": "If the erinyes dies outside the Nine Hells, its body disappears in sulfurous\
      \ smoke, and it gains a new body instantly, reviving with all its [[hit-points-xphb|Hit Points]]\
      \ somewhere in the Nine Hells."
    "name": "Diabolical Restoration"
  - "desc": "The erinyes has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "The erinyes has a magic rope. While bearing it, the erinyes can use the\
      \ Entangling Rope action. The rope has AC 20, HP 90, and [[immunity-xphb|Immunity]]\
      \ to Poison and Psychic damage. The rope turns to dust if reduced to 0 [[hit-points-xphb|Hit\
      \ Points]], if it is 5+ feet\
      \ away from the erinyes for 1 hour or more, or if the erinyes dies. If the rope\
      \ is damaged or destroyed, the erinyes can fully restore it when finishing a\
      \ [[short-rest-xphb|Short]] or [[long-rest-xphb|Long Rest]]."
    "name": "Magic Rope"
"actions":
  - "desc": "The erinyes makes three Withering Sword attacks and can use Entangling\
      \ Rope."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +8, reach 5 ft. *Hit:* 13 (2d8 + 4) Slashing\
      \ damage plus 11 (2d10) Necrotic damage."
    "name": "Withering Sword"
  - "desc": "*Strength Saving Throw:* DC 16, one creature the erinyes can see within\
      \ 120 feet. *Failure:* 14 (4d6) Force damage, and the target has the [[conditions#Restrained|Restrained]]\
      \ condition until the rope is destroyed, the erinyes uses a [[bonus-action-xphb|Bonus Action]]\
      \ to release the target, or the erinyes uses Entangling Rope again."
    "name": "Entangling Rope (Requires Magic Rope)"
"reactions":
  - "desc": "Trigger: The erinyes is hit by a melee attack roll while holding a weapon.\
      \ _Response:_ The erinyes adds 4 to its AC against that attack, possibly causing\
      \ it to miss."
    "name": "Parry"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/fiend/token/erinyes-xmm.webp"
```
^statblock
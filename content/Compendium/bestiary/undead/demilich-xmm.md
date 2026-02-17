---
title: Demilich
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/18
- monster/environment/any
- monster/size/tiny
- monster/type/undead
statblock: inline
aliases: ["Demilich"]
---
# Demilich
*Source: Monster Manual (2024) p. 96*  

![](Compendium/books/monster-manual-2025/img/demilich.webp#right)  
## Demilich

*What Lies beyond Lichdom*

- **Habitat.** Any  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

A demilich is a skull harboring the remnants of a lich's wicked essence. If the burden of immortality overwhelms a lich, its consciousness turns inward as its body rots away. But if its remains are disturbed, a demilich rises. Demiliches usually appear as skulls adorned with gems or arcane sigils.

### Demilich Lairs

Demiliches jealously guard their deathtrap-laden sanctums. The most notorious of these is the Tomb of Horrors, lair of the infamous Acererak.
```statblock
"name": "Demilich (XMM)"
"size": "Tiny"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "20"
"hp": !!int "180"
"hit_dice": "72d4"
"modifier": !!int "17"
"stats":
  - !!int "1"
  - !!int "20"
  - !!int "10"
  - !!int "20"
  - !!int "17"
  - !!int "20"
"speed": "5 ft., fly 30 ft. (hover)"
"saves":
  - "constitution": !!int "6"
  - "intelligence": !!int "11"
  - "wisdom": !!int "9"
"damage_resistances": "bludgeoning, piercing, slashing"
"damage_immunities": "necrotic, poison, psychic"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Deafened|deafened]],\
  \ [[conditions#Exhaustion|exhaustion]], [[conditions#Frightened|frightened]],\
  \ [[conditions#Paralyzed|paralyzed]], [[conditions#Petrified|petrified]],\
  \ [[conditions#Poisoned|poisoned]], [[conditions#Prone|prone]],\
  \ [[conditions#Stunned|stunned]]"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "18"
"traits":
  - "desc": "If the demilich fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (3/Day, or 4/Day in Lair)"
  - "desc": "If the demilich is destroyed, it reforms and regains all its [[hit-points-xphb|Hit Points]]\
      \ in 1d10 days unless a [[wish-xphb|Wish]] spell is cast\
      \ on its remains."
    "name": "Undead Restoration"
"actions":
  - "desc": "The demilich makes three Necrotic Burst attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +11, reach 5 ft. or range 120 ft. *Hit:*\
      \ 24 (7d6) Necrotic damage."
    "name": "Necrotic Burst"
  - "desc": "*Constitution Saving Throw:* DC 19, each creature in a 30-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the demilich. *Failure:* 70 (20d6) Psychic damage. *Failure\
      \ or Success:* The target has the [[conditions#Frightened|Frightened]]\
      \ condition until the start of the demilich's next turn."
    "name": "Howl (Recharge 5-6)"
"regional_effects":
  - "desc": "The region containing a demilich's lair is twisted by its presence, creating\
      \ the following effects:\n\n- **Enervating Domain.** Whenever a creature other\
      \ than the demilich or one of its allies finishes a [[long-rest-xphb|Long Rest]]\
      \ within 1 mile of the lair, the creature must succeed on a DC 20 Constitution\
      \ saving throw or have its [[hit-points-xphb|Hit Point]]\
      \ maximum reduced by 1d4. This reduction lasts until the creature finishes\
      \ a [[long-rest-xphb|Long Rest]] outside that\
      \ area.  \n- **Travel Ward.** Creatures can't use teleportation or planar travel\
      \ to enter or exit the lair.  \n\nIf the demilich dies or moves its lair elsewhere,\
      \ these effects end immediately."
    "name": ""
"legendary_description": "Legendary Action Uses: 3 (4 in Lair). Immediately after\
  \ another creature's turn, the demilich can expend a use to take one of the following\
  \ actions. The demilich regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "*Constitution Saving Throw:* DC 19, one creature the demilich can see\
      \ within 120 feet. *Failure:* The target's [[hit-points-xphb|Hit Point]]\
      \ maximum decreases by 14 (4d6). *Failure or Success:* The demilich can't\
      \ take this action again until the start of its next turn."
    "name": "Energy Drain"
  - "desc": "The demilich flies up to its [[fly-speed-xphb|Fly Speed]],\
      \ shedding grave dust. Each creature within 5 feet of the demilich as it moves\
      \ is targeted once by the following effect. *Constitution Saving Throw:* DC\
      \ 19. *Failure:* The target has the [[conditions#Blinded|Blinded]]\
      \ condition until the end of the demilich's next turn. *Failure or Success:*\
      \ The demilich can't take this action again until the start of its next turn."
    "name": "Grave-Dust Flight"
  - "desc": "The demilich makes one Necrotic Burst attack."
    "name": "Necrosis"
"source":
  - "XMM"
"image": "Compendium/bestiary/undead/token/demilich-xmm.webp"
```
^statblock
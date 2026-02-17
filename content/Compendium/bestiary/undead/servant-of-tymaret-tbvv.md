---
title: Servant of Tymaret
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvv
- monster/cr/3
- monster/size/m
- monster/type/undead
statblock: inline
aliases: ["Servant of Tymaret"]
---
# Servant of Tymaret
*Source: Theros Bestiary TBVV*  

<blockquote><small>Life is most precious to those who have already lost it.</small></blockquote>

![Servant of Tymaret](Compendium/bestiary/undead/img/servant-of-tymaret.webp#right|850)  

```statblock
"name": "Servant of Tymaret (TBVV)"
"size": "Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "1"
"stats":
  - !!int "12"
  - !!int "13"
  - !!int "16"
  - !!int "13"
  - !!int "12"
  - !!int "15"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+3"
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+3"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+3"
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "passive Perception 10"
"languages": "The languages it knew in life"
"cr": "3"
"traits":
  - "desc": "At the beginning of the servant's turn, if Tymaret saw it bowing to him or his image at any point since the servant's last turn, all hostile creatures within 30 feet of the servant take 9 (2d8) necrotic damage. The servant regains [[hit-points-xphb|Hit Points]] equal to the total damage dealt this way."
    "name": "Inspired"
  - "desc": "The servant regains 8 [[hit-points-xphb|Hit Points]] at the start of its turn. The servant dies only if it starts its turn with 0 [[hit-points-xphb|Hit Points]] and doesn't regenerate."
    "name": "Regeneration"
  - "desc": "If damage reduces the servant to 0 [[hit-points-xphb|Hit Points]], it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the servant drops to 1 hit point instead."
    "name": "Undead Fortitude"
"actions":
  - "desc": "_Melee or Ranged Weapon Attack:_ +3 to hit, reach 5 ft. or range 20/60 ft., one target. _Hit:_ 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."
    "name": "Trident"
  - "desc": "The servant bows down to any manifestation or statue of Tymaret that it can see. It remains in this position until a different action is used."
    "name": "Bow"
"source":
  - "TBVV"
"image": "Compendium/bestiary/undead/token/servant-of-tymaret-tbvv.webp"
```
^statblock
---
title: Ogre Zombie
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
aliases: ["Ogre Zombie"]
---
# Ogre Zombie
*Source: Monster Manual (2024) p. 346. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/undead/img/zombies.webp#right|850)  
Ogre zombies serve as tireless labor and undying weapons of war. These massive zombies possess the size and strength to break through barriers that repel smaller zombies.

## Zombies

*Relentless Reanimated Corpses*

- **Habitat.** Planar (Shadowfell), Underdark, Urban  
- **Treasure.** None  

Zombies are unthinking, reanimated corpses, often gruesomely marred by decay and lethal traumas. They serve whatever supernatural force animates them—typically evil necromancers or fiendish spirits. Zombies are relentless, merciless, and resilient, and their dead flesh can carry on even after suffering grievous wounds. While they can follow simple orders, they rely on primal drives rather than thought. They fulfill commands by working tirelessly or battering through foes, but they are easily stymied by barriers or unexpected circumstances.

Zombies are usually created from Humanoid corpses, but the remains of other creatures can also become zombies. Such monstrous zombies might possess the strength they had in life or a measure of their supernatural abilities, but they employ such abilities haphazardly at best.

> [!quote] A quote from Account of the Night of the Walking Dead  
> 
> Then, by a spectacular crack of lightning, the figures came into view, moving slowly toward the village. Over driving winds a voice cried out, "The dead come for Marais d'Tarascon! An army of the walking dead!"

## Statblock

```statblock
"name": "Ogre Zombie (XMM)"
"size": "Large"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "8"
"hp": !!int "85"
"hit_dice": "9d10 + 36"
"modifier": !!int "-2"
"stats":
  - !!int "19"
  - !!int "6"
  - !!int "18"
  - !!int "3"
  - !!int "6"
  - !!int "5"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "0"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 8"
"languages": "understands Common and Giant but can't speak"
"cr": "2"
"traits":
  - "desc": "If damage reduces the zombie to 0 [[hit-points-xphb|Hit Points]],\
      \ it makes a Constitution saving throw (DC 5 plus the damage taken) unless the\
      \ damage is Radiant or from a [[critical-hit-xphb|Critical Hit]].\
      \ On a successful save, the zombie drops to 1 [[hit-points-xphb|Hit Point]]\
      \ instead."
    "name": "Undead Fortitude"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 13 (2d8 + 4) Bludgeoning\
      \ damage."
    "name": "Slam"
"source":
  - "XMM"
"image": "Compendium/bestiary/undead/token/ogre-zombie-xmm.webp"
```
^statblock
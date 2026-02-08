---
title: Water Weird
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Water Weird"]
---
# Water Weird
*Source: Monster Manual (2024) p. 323*  

![](Compendium/bestiary/elemental/img/water-weird.webp#right)  
## Water Weird

*Servant of Primeval Magic*

- **Habitat.** Underdark, Urban  
- **Treasure.** Any  

Serpentine nature spirits, water weirds protect pools, fountains, and magical bodies of water. In the water, these creatures are indistinguishable from the liquid surrounding them. Should their aquatic territory be disturbed, they rise as animate water spouts with vague snake- or dragon-like features. Often their appearance is enough to drive off foes, but if forced to fight, water weirds crush enemies within their fluid coils.

Water weirds might protect a site for generations and learn much about their surroundings. Some gain reputations as oracles and might respond to questions posed to them in Primordial. Since water weirds don't speak, they often communicate using spouts of water or objects submerged in their pools.

> [!quote]  
> 
> Rule 2: Before you drink from a fountain or pool, toss a copper coin into it. It's a small price to pay for your life!

```statblock
"name": "Water Weird (XMM)"
"size": "Large"
"type": "elemental"
"alignment": "Neutral"
"ac": !!int "13"
"hp": !!int "65"
"hit_dice": "10d10 + 10"
"modifier": !!int "3"
"stats":
  - !!int "17"
  - !!int "16"
  - !!int "13"
  - !!int "11"
  - !!int "10"
  - !!int "10"
"speed": "5 ft., swim 60 ft."
"damage_resistances": "fire"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [grappled](Compendium/rules/conditions.md#Grappled), [paralyzed](Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](Compendium/rules/conditions.md#Petrified), [poisoned](Compendium/rules/conditions.md#Poisoned),\
  \ [prone](Compendium/rules/conditions.md#Prone), [restrained](Compendium/rules/conditions.md#Restrained),\
  \ [unconscious](Compendium/rules/conditions.md#Unconscious)"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 30 ft., passive Perception\
  \ 10"
"languages": "understands Primordial but can't speak"
"cr": "3"
"traits":
  - "desc": "The water weird has the [Invisible](Compendium/rules/conditions.md#Invisible)\
      \ condition while fully immersed in water."
    "name": "Invisible in Water"
  - "desc": "The water weird dies if it leaves the water to which it is bound or if\
      \ that water is destroyed."
    "name": "Water Bound"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 10 ft. *Hit:* 13 (3d6 + 3) Cold damage.\
      \ If the target is a Medium or smaller creature, it has the [Grappled](Compendium/rules/conditions.md#Grappled)\
      \ condition (escape DC 13), and it has the [Restrained](Compendium/rules/conditions.md#Restrained)\
      \ condition until the grapple ends."
    "name": "Surge"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/water-weird-xmm.webp"
```
^statblock
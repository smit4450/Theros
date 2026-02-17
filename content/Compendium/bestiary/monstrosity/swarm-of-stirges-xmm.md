---
title: Swarm of Stirges
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/desert
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/environment/mountain
- monster/environment/swamp
- monster/environment/underdark
- monster/environment/urban
- monster/size/medium
- monster/type/monstrosity
statblock: inline
aliases: ["Swarm of Stirges"]
---
# Swarm of Stirges
*Source: Monster Manual (2024) p. 299*  

![](Compendium/bestiary/monstrosity/img/stirges.webp#right|850)  
Swarms of stirges sometimes form in swamps and Underdark caverns, draining livestock and any other creatures that can't escape them.

## Stirges

*Notorious, Clinging Bloodsuckers*

- **Habitat.** Desert, Forest, Grassland, Hill, Mountain, Swamp, Underdark, Urban  
- **Treasure.** None  

Stirges are bat-size vermin with dagger-length proboscises that attach to other creatures and drain life from them. Stirges are most active at night and hide in shadowy places during the day. If disturbed, they take flight and defend themselves. Roll on or choose a result from the Stirge Roosts table to inspire where stirges might lurk.

**Stirge Roosts**

| dice: 1d4 | Between Hunts, the Stirge Lurks In... |
|-----------|---------------------------------------|
| 1 | The attic or furniture of a ruined building. |
| 2 | A cave or narrow crevice. |
| 3 | A hollow tree or thicket. |
| 4 | The remains of a gigantic, dead creature. |
^stirge-roosts
## Statblock

```statblock
"name": "Swarm of Stirges (XMM)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "36"
"hit_dice": "8d8"
"modifier": !!int "3"
"stats":
  - !!int "4"
  - !!int "16"
  - !!int "11"
  - !!int "2"
  - !!int "8"
  - !!int "6"
"speed": "10 ft., fly 40 ft."
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]],\
  \ [[conditions#Grappled|grappled]], [[conditions#Paralyzed|paralyzed]],\
  \ [[conditions#Petrified|petrified]], [[conditions#Prone|prone]],\
  \ [[conditions#Restrained|restrained]], [[conditions#Stunned|stunned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 9"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The swarm can occupy another creature's space and vice versa, and the\
      \ swarm can move through any opening large enough for a Tiny creature. The swarm\
      \ can't regain [[hit-points-xphb|Hit Points]]\
      \ or gain [[temporary-hit-points-xphb|Temporary Hit Points]]."
    "name": "Swarm"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 14 (2d10 + 3) Piercing\
      \ damage, or 8 (1d10 + 3) Piercing damage if the swarm is [[conditions#Bloodied|Bloodied]].\
      \ If the target is a Medium or smaller creature in the swarm's space, the target\
      \ has the [[conditions#Grappled|Grappled]] condition (escape\
      \ DC 13). Until the grapple ends, the target takes 7 (2d6) Necrotic damage\
      \ at the end of each of its turns."
    "name": "Swarm of Proboscises"
"source":
  - "XMM"
"image": "Compendium/bestiary/monstrosity/token/swarm-of-stirges-xmm.webp"
```
^statblock
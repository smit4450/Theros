---
title: Tree Blight
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/plant
statblock: inline
aliases: ["Tree Blight"]
---
# Tree Blight
*Source: Monster Manual (2024) p. 44*  

![](Compendium/bestiary/plant/img/vine-needle-and-tree-blights.webp#right|850)  
Tree blights look like ancient, dead trees with gnarled limbs and splintered hollows. Imbued with bloodlust, these blights feed on the living. Evidence of their past meals is often tangled amid their branches and roots. Tree blights cooperate with other blights, but they attack other tree-shaped beings they encounter, such as awakened trees and treants.

## Blights

*Plants Sprouted from Evil*

- **Habitat.** Forest  
- **Treasure.** None  

Blights are malicious plants that sprout from deep-rooted evil. Their gnarled forms twist with fearsome features suggestive of human limbs and vicious maws. Blights lurk in ambush amid mundane vegetation and lash out at non-Plant creatures. While blights can act independently, they're usually motivated by whatever sinister forces spawned them or by wicked creatures with control over nature. The magic that creates blights often affects other vegetation as well, causing brambles, vines, and gnarled trees to overwhelm roads and fields, choke wells and streams, and force animals from their natural habitat. This might make blights the first sign of an oncoming wave of corruption.

> [!quote] A quote from Belak the Outcast, Druid of the Twilight Grove  
> 
> It lives, though it looks dead. In an age long past, someone staked a vampire to the earth on this very spot. The wooden stake was yet green and took root. And so grew the Gulthias Tree, reverberating with primal power.

## Statblock

```statblock
"name": "Tree Blight (XMM)"
"size": "Huge"
"type": "plant"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "115"
"hit_dice": "10d12 + 50"
"modifier": !!int "3"
"stats":
  - !!int "23"
  - !!int "10"
  - !!int "20"
  - !!int "6"
  - !!int "10"
  - !!int "3"
"speed": "30 ft."
"condition_immunities": "[[conditions#Deafened|deafened]]"
"senses": "[[senses#Blindsight|Blindsight]] 60 ft., passive Perception\
  \ 10"
"languages": "understands Common and Druidic but can't speak"
"cr": "7"
"actions":
  - "desc": "The blight makes two Branch attacks and uses Grasping Root."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +9, reach 15 ft. *Hit:* 16 (3d6 + 6) Bludgeoning\
      \ damage."
    "name": "Branch"
  - "desc": "*Strength Saving Throw:* DC 17, one Large or smaller creature the blight\
      \ can see within 15 feet. *Failure:* The target is pulled up to 10 feet straight\
      \ toward the blight and has the [[conditions#Grappled|Grappled]]\
      \ condition (escape DC 16) from one of six roots. Until the grapple ends, the\
      \ target takes 13 (2d6 + 6) Bludgeoning damage at the start of each of its\
      \ turns."
    "name": "Grasping Root"
"bonus_actions":
  - "desc": "*Dexterity Saving Throw:* DC 17, one creature [[conditions#Grappled|Grappled]]\
      \ by the blight. *Failure:* 19 (3d8 + 6) Piercing damage. *Success:* Half\
      \ damage."
    "name": "Gnash"
"source":
  - "XMM"
"image": "Compendium/bestiary/plant/token/tree-blight-xmm.webp"
```
^statblock
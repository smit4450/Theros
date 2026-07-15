---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1
- monster/environment/abyss
- monster/environment/planar
- monster/size/medium
- monster/type/fiend/demon
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Manes Vaporspawn"
---
# Manes Vaporspawn
*Source: Monster Manual (2024) p. 201*
![](/Compendium/bestiary/fiend/img/manes.webp#right)

Vaporspawn arise from evil souls shattered by unspeakable torments or the depredations of more powerful demons. These distorted manes undergo endless, painful contortions, and they share their torment with whatever creatures they encounter.

## Manes

*Demons of Panic and Frenzy*

- **Habitat.** Planar (Abyss)  
- **Treasure.** None  

The lowest form of demons, manes appear when truly loathsome souls are condemned to the Abyss. These misshapen demons have distorted features and bodies that crawl with Abyssal parasites. Overwhelmed by demonic urges and constant terror, manes know only shock and frenzied outbursts.

## Statblock

```statblock
"name": "Manes Vaporspawn"
"size": "Medium"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"hp": !!int "19"
"hit_dice": "3d8 + 6"
"modifier": !!int "1"
"stats":
  - !!int "14"
  - !!int "12"
  - !!int "15"
  - !!int "5"
  - !!int "8"
  - !!int "3"
"speed": "30 ft."
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "poison"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](/Compendium/rules/conditions.md#Frightened), [grappled](/Compendium/rules/conditions.md#Grappled),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned), [restrained](/Compendium/rules/conditions.md#Restrained)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 9"
"languages": "understands Abyssal but can't speak"
"cr": "1"
"traits":
  - "desc": "The manes can move through a space as narrow as 1 inch without expending\
      \ extra movement to do so."
    "name": "Contortionist"
  - "desc": "*Constitution Saving Throw:* DC 12, each creature in a 5-foot [Emanation](/Compendium/rules/variant-rules/emanation-area-of-effect-xphb.md)\
      \ originating from the manes at the end of the manes's turn. *Failure:* The\
      \ target has the [Incapacitated](/Compendium/rules/conditions.md#Incapacitated)\
      \ condition until the end of its next turn. *Success:* The target is immune\
      \ to this manes's Sickening Vapors for 24 hours."
    "name": "Sickening Vapors"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 5 (1d6 + 2) Slashing damage\
      \ plus 5 (2d4) Necrotic damage."
    "name": "Claw"
"bonus_actions":
  - "desc": "While in [Dim Light](/Compendium/rules/variant-rules/dim-light-xphb.md)\
      \ or [Darkness](/Compendium/rules/variant-rules/darkness-xphb.md), the manes\
      \ takes the [Hide](/Compendium/rules/actions.md#Hide) action."
    "name": "Shadow Stealth"
"source":
  - "XMM"
"image": "/Compendium/bestiary/fiend/token/manes-vaporspawn-xmm.webp"
```
^statblock

## Environment

planar, abyss
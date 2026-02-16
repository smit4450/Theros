---
title: Dretch
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/abyss
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Dretch"]
---
# Dretch
*Source: Monster Manual (2024) p. 103. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/fiend/img/dretches.webp#right|850)  
Lone dretches serve other demons or evil magic-users. They are erratic, filthy, and violent, and they demonstrate little sense of self-preservation.

## Dretches

*Demons of Frenzy and Vulgarity*

- **Habitat.** Planar (Abyss)  
- **Treasure.** None  

The servants and victims of greater demons, dretches embody petty instincts, chaotic impulses, and violent urges. Dretches exist in unfathomable numbers in the depths of the Abyss, where their reeking throngs fill vast demonic hordes.

> [!quote] A quote from Jaranda, Expert on the Abyss  
> 
> Ah, the infinite wonders of the Abyss. If there's anything you don't like, you'll find it here.

## Statblock

```statblock
"name": "Dretch (XMM)"
"size": "Small"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "11"
"hp": !!int "18"
"hit_dice": "4d6 + 4"
"modifier": !!int "0"
"stats":
  - !!int "12"
  - !!int "11"
  - !!int "12"
  - !!int "5"
  - !!int "8"
  - !!int "3"
"speed": "20 ft."
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 9"
"languages": "Abyssal; telepathy 60 ft. (works only with creatures that understand\
  \ Abyssal)"
"cr": "1/4"
"actions":
  - "desc": "*Melee Attack Roll:* +3, reach 5 ft. *Hit:* 4 (1d6 + 1) Slashing\
      \ damage."
    "name": "Rend"
  - "desc": "*Constitution Saving Throw:* DC 11, each creature in a 10-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the dretch. *Failure:* The target has the [[conditions#Poisoned|Poisoned]]\
      \ condition until the end of its next turn. While [[conditions#Poisoned|Poisoned]],\
      \ the creature can take either an action or a [[bonus-action-xphb|Bonus Action]]\
      \ on its turn, not both, and it can't take Reactions."
    "name": "Fetid Cloud (1/Day)"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/dretch-xmm.webp"
```
^statblock
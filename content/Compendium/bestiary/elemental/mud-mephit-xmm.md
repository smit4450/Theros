---
title: Mud Mephit
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/elemental
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Mud Mephit"]
---
# Mud Mephit
*Source: Monster Manual (2024) p. 207*  

![](Compendium/bestiary/elemental/img/mephits.webp#right|850)  
A combination of earth and water, mud mephits are crude, disgusting creatures. They take every opportunity to ruin objects and pollute food with muck.

## Mephits

*Malicious Elemental Hooligans*

- **Habitat.** Planar (Elemental Planes)  
- **Treasure.** None  

Mephits are mean-spirited tricksters that dwell on the Elemental Planes. The six most prominent types of mephits resemble halfling-size gargoyles with wings, exaggerated features, and bodies composed of two elements. Most live self-interested existences, indulging their warped senses of humor or overblown egos on their home planes of existence. Some serve as messengers or spies for genies or magic-users.

Mephits resent leaving the elemental extremes where they make their homes. If loosed on the Material Plane or other realms, they lash out with nasty pranks or by tormenting weaker creatures. When destroyed, mephits explode in a burst of elemental magic.

> [!quote] A quote from Seamusxanthuszenus, smoke mephit with a typically inflated impression of itself  
> 
> I am Seamusxanthuszenus, Slayer of Fiends, Merchant Most Excellent, Purveyor of Death!

## Statblock

```statblock
"name": "Mud Mephit (XMM)"
"size": "Small"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "11"
"hp": !!int "13"
"hit_dice": "3d6 + 3"
"modifier": !!int "1"
"stats":
  - !!int "8"
  - !!int "12"
  - !!int "12"
  - !!int "9"
  - !!int "11"
  - !!int "7"
"speed": "20 ft., fly 20 ft., swim 20 ft."
"skillsaves":
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+3"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 10"
"languages": "Primordial (Aquan, Terran)"
"cr": "1/4"
"traits":
  - "desc": "The mephit explodes when it dies. *Dexterity Saving Throw:* DC 11, each\
      \ creature in a 5-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the mephit. *Failure:* The target has the [[conditions#Restrained|Restrained]]\
      \ condition until the end of its next turn."
    "name": "Death Burst"
"actions":
  - "desc": "*Melee Attack Roll:* +3, reach 5 ft. *Hit:* 4 (1d6 + 1) Bludgeoning\
      \ damage."
    "name": "Slam"
  - "desc": "*Dexterity Saving Throw:* DC 11, one creature the mephit can see within\
      \ 15 feet. *Failure:* The target has the [[conditions#Restrained|Restrained]]\
      \ condition until the end of the mephit's next turn."
    "name": "Mud Breath (Recharge 6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/mud-mephit-xmm.webp"
```
^statblock
---
title: Ice Mephit
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/elemental
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Ice Mephit"]
---
# Ice Mephit
*Source: Monster Manual (2024) p. 206. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/elemental/img/mephits.webp#right|850)  
Ice mephits have bodies made of frigid air and frozen water. They delight in freezing things and dropping ice into peoples' clothes.

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
"name": "Ice Mephit (XMM)"
"size": "Small"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "11"
"hp": !!int "21"
"hit_dice": "6d6"
"modifier": !!int "1"
"stats":
  - !!int "7"
  - !!int "13"
  - !!int "10"
  - !!int "9"
  - !!int "11"
  - !!int "12"
"speed": "30 ft., fly 30 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+2"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+3"
"damage_vulnerabilities": "fire"
"damage_immunities": "cold, poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 12"
"languages": "Primordial (Aquan, Auran)"
"cr": "1/2"
"traits":
  - "desc": "The mephit explodes when it dies. *Constitution Saving Throw:* DC 10,\
      \ each creature in a 5-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the mephit. *Failure:* 5 (2d4) Cold damage. *Success:*\
      \ Half damage."
    "name": "Death Burst"
"actions":
  - "desc": "*Melee Attack Roll:* +3, reach 5 ft. *Hit:* 3 (1d4 + 1) Slashing\
      \ damage plus 2 (1d4) Cold damage."
    "name": "Claw"
  - "desc": "*Constitution Saving Throw:* DC 10, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 7 (3d4) Cold damage. *Success:* Half damage."
    "name": "Frost Breath (Recharge 6)"
  - "desc": "The mephit casts [[fog-cloud-xphb|Fog Cloud]], requiring\
      \ no spell components and using Charisma as the spellcasting ability.\n"
    "name": "Fog Cloud (1/Day)"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/ice-mephit-xmm.webp"
```
^statblock
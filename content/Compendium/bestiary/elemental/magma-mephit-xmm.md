---
title: Magma Mephit
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1-2
- monster/environment/elemental
- monster/environment/planar
- monster/size/small
- monster/type/elemental
statblock: inline
aliases: ["Magma Mephit"]
---
# Magma Mephit
*Source: Monster Manual (2024) p. 207. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/elemental/img/mephits.webp#right|850)  
These mephits embody the merging of earth and fire as glowing magma. They love melting things, but they loathe magmins and attack them on sight.

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
"name": "Magma Mephit (XMM)"
"size": "Small"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "11"
"hp": !!int "18"
"hit_dice": "4d6 + 4"
"modifier": !!int "1"
"stats":
  - !!int "8"
  - !!int "12"
  - !!int "12"
  - !!int "7"
  - !!int "10"
  - !!int "10"
"speed": "30 ft., fly 30 ft."
"skillsaves":
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+3"
"damage_vulnerabilities": "cold"
"damage_immunities": "fire, poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 10"
"languages": "Primordial (Ignan, Terran)"
"cr": "1/2"
"traits":
  - "desc": "The mephit explodes when it dies. *Dexterity Saving Throw:* DC 11, each\
      \ creature in a 5-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the mephit. *Failure:* 7 (2d6) Fire damage. *Success:*\
      \ Half damage."
    "name": "Death Burst"
"actions":
  - "desc": "*Melee Attack Roll:* +3, reach 5 ft. *Hit:* 3 (1d4 + 1) Slashing\
      \ damage plus 3 (1d6) Fire damage."
    "name": "Claw"
  - "desc": "*Dexterity Saving Throw:* DC 11, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 7 (2d6) Fire damage. *Success:* Half damage."
    "name": "Fire Breath (Recharge 6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/magma-mephit-xmm.webp"
```
^statblock
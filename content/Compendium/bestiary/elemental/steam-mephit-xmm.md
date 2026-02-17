---
title: Steam Mephit
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1-4
- monster/environment/elemental
- monster/environment/planar
- monster/size/small
- monster/type/elemental
statblock: inline
aliases: ["Steam Mephit"]
---
# Steam Mephit
*Source: Monster Manual (2024) p. 208. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/elemental/img/smoke-and-steam-mephits.webp#right|850)  
These arrogant mephits are made of heat and vaporous water. They often trick creatures into doing them favors, then renege on promised rewards.

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
"name": "Steam Mephit (XMM)"
"size": "Small"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "10"
"hp": !!int "17"
"hit_dice": "5d6"
"modifier": !!int "0"
"stats":
  - !!int "5"
  - !!int "11"
  - !!int "10"
  - !!int "11"
  - !!int "10"
  - !!int "12"
"speed": "30 ft., fly 30 ft."
"skillsaves":
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+2"
"damage_immunities": "fire, poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 10"
"languages": "Primordial (Aquan, Ignan)"
"cr": "1/4"
"traits":
  - "desc": "Attack rolls against the mephit are made with [[disadvantage-xphb|Disadvantage]]\
      \ unless the mephit has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition."
    "name": "Blurred Form"
  - "desc": "The mephit explodes when it dies. *Dexterity Saving Throw:* DC 10, each\
      \ creature in a 5-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the mephit. *Failure:* 5 (2d4) Fire damage. *Success:*\
      \ Half damage."
    "name": "Death Burst"
"actions":
  - "desc": "*Melee Attack Roll:* +2, reach 5 ft. *Hit:* 2 (1d4) Slashing damage\
      \ plus 2 (1d4) Fire damage."
    "name": "Claw"
  - "desc": "*Constitution Saving Throw:* DC 10, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 5 (2d4) Fire damage, and the target's [[speed-xphb|Speed]]\
      \ decreases by 10 feet until the end of the mephit's next turn. *Success:* Half\
      \ damage only. *Failure or Success:* Being underwater doesn't grant [[resistance-rules-xphb|Resistance]]\
      \ to this Fire damage."
    "name": "Steam Breath (Recharge 6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/elemental/token/steam-mephit-xmm.webp"
```
^statblock
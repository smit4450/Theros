---
title: Graveyard Revenant
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Graveyard Revenant"]
---
# Graveyard Revenant
*Source: Monster Manual (2024) p. 260*  

![](Compendium/bestiary/undead/img/revenant-and-graveyard-revenant.webp#right|850)  
Graveyard revenants possess dozens of bodies that combine to form grotesque masses. They take revenge on those responsible for mass deaths or institutions that callously ruin lives.

## Revenants

*Vengeance from beyond the Grave*

- **Habitat.** Forest, Swamp, Urban  
- **Treasure.** Any  

Wrathful spirits bent on revenge, revenants possess corpses and other materials, using them to seek justice or vent their rage on those who wronged them. Revenants refuse to rest until those they seek to punish are no more. If their bodies are destroyed, revenants claim new forms and continue their ruthless quests.
## Statblock

```statblock
"name": "Graveyard Revenant (XMM)"
"size": "Huge"
"type": "undead"
"alignment": "Neutral"
"ac": !!int "14"
"hp": !!int "161"
"hit_dice": "14d12 + 70"
"modifier": !!int "2"
"stats":
  - !!int "20"
  - !!int "14"
  - !!int "20"
  - !!int "13"
  - !!int "16"
  - !!int "18"
"speed": "40 ft."
"saves":
  - "strength": !!int "8"
  - "constitution": !!int "8"
  - "wisdom": !!int "6"
  - "charisma": !!int "7"
"damage_resistances": "necrotic, psychic"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Frightened|frightened]], [[conditions#Paralyzed|paralyzed]],\
  \ [[conditions#Petrified|petrified]], [[conditions#Poisoned|poisoned]],\
  \ [[conditions#Stunned|stunned]], [[conditions#Unconscious|unconscious]]"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception\
  \ 13"
"languages": "Common plus two other languages"
"cr": "7"
"traits":
  - "desc": "If the revenant dies, it revives 24 hours later unless [[dispel-evil-and-good-xphb|Dispel Evil and\
      \ Good]] is cast on its remains.\
      \ If it revives, it animates another group of corpses elsewhere on the same\
      \ plane of existence; it now looks different but uses the same stat block and\
      \ returns with all its [[hit-points-xphb|Hit Points]]."
    "name": "Undead Restoration"
"actions":
  - "desc": "The revenant makes two Suffocate attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +8, reach 10 ft. *Hit:* 10 (1d10 + 5) Bludgeoning\
      \ damage plus 10 (3d6) Necrotic damage. If the target is a Large or smaller\
      \ creature, it has the [[conditions#Grappled|Grappled]] condition\
      \ (escape DC 15). Until the grapple ends, the target is suffocating. The revenant\
      \ can have up to two targets [[conditions#Grappled|Grappled]]\
      \ in this way at a time."
    "name": "Suffocate"
  - "desc": "*Wisdom Saving Throw:* DC 15, each creature in a 30-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the revenant. *Failure:* The target has the [[conditions#Paralyzed|Paralyzed]]\
      \ condition and repeats the save at the end of each of its turns, ending the\
      \ effect on itself on a success. After 1 minute, it succeeds automatically."
    "name": "Haunting Glare (Recharge 5-6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/undead/token/graveyard-revenant-xmm.webp"
```
^statblock
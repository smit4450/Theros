---
title: Champion of Stray Souls
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvv
- monster/cr/1
- monster/size/m
- monster/type/undead
statblock: inline
aliases: ["Champion of Stray Souls"]
---
# Champion of Stray Souls
*Source: Theros Bestiary TBVV*  

Wandering spirits seeking a more complete return to life might seek out a champion of stray souls. The champion is able to assist them by channeling their soul into a corpse and resurrecting that corpse.

Any creature might choose to take part in the champion's ritual, however. For example, a power-hungry madman could enlist the service of the champion to possess the dead body of a hydra or kraken.

![Champion of Stray Souls](https://img.scryfall.com/cards/art_crop/front/3/4/342196b9-ab65-4922-864e-00f067153261.jpg?1593091890#right)  

```statblock
"name": "Champion of Stray Souls (TBVV)"
"size": "Medium"
"type": "undead"
"alignment": "Any alignment"
"ac": !!int "13"
"ac_class": "armor scraps"
"hp": !!int "48"
"hit_dice": "8d8 + 16"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "15"
  - !!int "15"
  - !!int "6"
  - !!int "8"
  - !!int "5"
"speed": "30 ft."
"damage_vulnerabilities": "bludgeoning"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]], [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": "Understands the languages it knew in life, but can only speak certain phrases (see "Limited Vocabulary" below)"
"cr": "1"
"traits":
  - "desc": "The skeleton is unable to speak except for the phrases \"transfer soul\" and \"yes or no\" and must use gestures extensively."
    "name": "Limited Vocabulary"
  - "desc": "A dead champion of stray souls comes back to life with all its [[hit-points-xphb|Hit Points]] in 1d10 days unless it dies holding a gold coin."
    "name": "Cursed Rejuvenation"
"actions":
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands to make a melee attack."
    "name": "Longsword"
  - "desc": "_Ranged Weapon Attack:_ +4 to hit, range 150/600 ft., one target. _Hit:_ 7 (1d8 + 3) piercing damage."
    "name": "Longbow"
  - "desc": "The skeleton touches a willing living target and a dead target that has no soul but has all the other parts needed for resurrection. In the event the living target then changes its mind before the transference can take place, it may succeed on a DC 12 Dexterity saving throw in order to escape the skeleton's touch. The living target becomes a dead and soulless corpse, but its soul remains living. The soul enters the dead target, which returns to life with [[hit-points-xphb|Hit Points]] equal to amount the source target had. Once a soul is transferred to a new body, the owner of that soul controls the body. The elements retained by the soul from its old body include the Intelligence, Wisdom, and Charisma scores; alignment; and the benefit of class features. The new body does not retain any of these elements that its former soul had. If, prior to the transference, the new body had any wounds, conditions, or any type of decay, these persist. Depending on the nature of decay, the new body might have additional conditions at the DM's discretion, such as a fungal or parasitic disease."
    "name": "Transfer Soul (3/day)"
"source":
  - "TBVV"
"image": "Compendium/bestiary/undead/token/champion-of-stray-souls-tbvv.webp"
```
^statblock
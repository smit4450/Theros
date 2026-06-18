---
title: Shipbreaker Kraken
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxi
- monster/cr/25
- monster/size/g
- monster/type/monstrosity
statblock: inline
aliases: ["Shipbreaker Kraken"]
---
# Shipbreaker Kraken
*Source: Theros Bestiary TBVXXI*  

The shipbreaker kraken is a serpent with a six-clawed crab where its head should be.

![Shipbreaker Kraken](Homebrew/bestiary/monstrosity/img/shipbreaker-kraken.webp#right)  

```statblock
"name": "Shipbreaker Kraken (TBVXXI)"
"size": "Gargantuan"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "20"
"ac_class": "natural armor"
"hp": !!int "960"
"hit_dice": "60d20 + 360"
"modifier": !!int "1"
"stats":
  - !!int "22"
  - !!int "12"
  - !!int "22"
  - !!int "1"
  - !!int "9"
  - !!int "17"
"speed": "40 ft., swim 120 ft."
"saves":
  - "charisma": !!int "11"
"damage_immunities": "lightning, bludgeoning, piercing, and slashing from nonmagical attacks"
"condition_immunities": "[[conditions#Frightened|frightened]], [[conditions#Paralyzed|paralyzed]]"
"senses": "passive Perception 10"
"languages": ""
"cr": "25"
"traits":
  - "desc": "The kraken can breathe air and water."
    "name": "Amphibious"
  - "desc": "When the kraken is reduced to 0 [[hit-points-xphb|Hit Points]], it doesn’t die or fall [[conditions#Unconscious|unconscious]]. Instead, the damage creates tears in its hide, revealing its hearts, and the kraken. The kraken has four hearts: two on its chest, one on its back, and one at the base of its tail. A heart has an AC of 20 and 165 (10d20+60) [[hit-points-xphb|Hit Points]]. It is immune to bludgeoning, piercing, and slashing damage from nonmagical attacks, and it is immune to all conditions. If it is forced to make a saving throw, treat its ability scores as 10 (+0). If it finishes a short or long rest, the carapace heals, any destroyed hearts regenerate, and the hearts are covered again. The kraken dies when all the hearts are destroyed."
    "name": "Hearts of the Kraken (Mythic Trait; Recharges after a Short or Long Rest)"
  - "desc": "The kraken deals double damage to objects and structures."
    "name": "Siege Monster"
"actions":
  - "desc": "The kraken makes two claw attacks, each of which it can replace with one use of Fling."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +14 to hit, reach 5 ft., one target. Hit: 60 (12d8 + 6) piercing damage. If the target is a Large or smaller creature [[conditions#Grappled|grappled]] by the kraken, that creature is swallowed, and the grapple ends. While swallowed, the creature is [[conditions#Blinded|blinded]] and [[conditions#Restrained|restrained]], it has total cover against attacks and other effects outside the kraken, and it takes 42 (12d6) acid damage at the start of each of the kraken's turns. If the kraken takes 50 damage or more on a single turn from a creature inside it, the kraken must succeed on a DC 22 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall [[conditions#Prone|prone]] in a space within 10 feet of the kraken. If the kraken dies, a swallowed creature is no longer [[conditions#Restrained|restrained]] by it and can escape from the corpse using 15 feet of movement, exiting [[conditions#Prone|prone]]."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 27 (6d6 + 6) bludgeoning damage, and the target is [[conditions#Grappled|grappled]] (escape DC 16). Until this grapple ends, the target is [[conditions#Restrained|restrained]] and the kraken cannot constrict another target."
    "name": "Constrict"
  - "desc": "One Large or smaller object held or creature [[conditions#Grappled|grappled]] by the kraken's claw is thrown up to 60 feet in a random direction and knocked [[conditions#Prone|prone]]. If a thrown target strikes a solid surface, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 17 Dexterity saving throw or take the same damage and be knocked [[conditions#Prone|prone]]."
    "name": "Fling"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 50 (8d10 + 6) bludgeoning damage, and the target is [[conditions#Grappled|grappled]], escape DC 22. The crab has six claws, each of which can grapple only one target."
    "name": "Claw"
"legendary_actions":
  - "desc": "The kraken makes one claw attack or uses its Fling."
    "name": "Claw Attack or Fling"
  - "desc": "The kraken uses Constrict."
    "name": "Constrict (Costs 2 Actions)"
  - "desc": "The kraken moves up to its speed. **Mythic Actions**If Tromokratis’s mythic trait is active, it can use the options below as legendary actions for 1 hour after using Hearts of the Kraken. **_Rampage._** Tromokratis makes four attacks with its claws."
    "name": "Move"
"source":
  - "TBVXXI"
"image": "Homebrew/bestiary/monstrosity/token/shipbreaker-kraken-tbvxxi.webp"
```
^statblock
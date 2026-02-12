---
title: Nessian Wilds Ravager
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxiv
- ttrpg-cli/monster/cr/20
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Nessian Wilds Ravager"]
---
# Nessian Wilds Ravager
*Source: Theros Bestiary TBVXXIV*  

<b><big>Usage Notes</big></b>
Players familiar with this monster may find the choice too simple. In order to add greater relevance to the tribute, consider the following scenarios:

<li>One or more hydra cultists might be nearby who will pay tribute.
<li>A quest goal might involve securing a hydra head trophy.
<li>A quest goal might involve vanquishing or protecting the hydra.
<li>The hydra could be positioned near a particularly difficult-to-fight creature and engage in combat with it.

For a more interactive version of this creature, see the "Face the Hydra" bestiary, which starts with three heads, doesn't accept tribute, and treats the hydra's body and heads as individual creatures.

![Nessian Wilds Ravager](Compendium/bestiary/monstrosity/img/nessian-wilds-ravager.webp#right)  

```statblock
"name": "Nessian Wilds Ravager (TBVXXIV)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "360"
"hit_dice": "30d12 + 180"
"modifier": !!int "1"
"stats":
  - !!int "22"
  - !!int "12"
  - !!int "22"
  - !!int "2"
  - !!int "10"
  - !!int "7"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+11"
"damage_immunities": "fire, poison, acid"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": ""
"cr": "20"
"traits":
  - "desc": "If by the beginning of the hydra's first turn in combat the creature it selected (see \"Expect Tribute\") has paid it tribute, the hydra uses an action to attack itself 6 times, dealing 25 damage to itself each time."
    "name": "Accept Tribute"
  - "desc": "When the hydra takes piercing or slashing damage, each creature within 5 feet of the hydra takes 9 (2d8) acid damage."
    "name": "Acidic Blood"
  - "desc": "The hydra can hold its breath for 1 hour."
    "name": "Hold Breath"
  - "desc": "The hydra has ten heads. While it has more than one head, the hydra has advantage on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious. Whenever the hydra takes 25 or more damage in a single turn, one of its heads dies. If all its heads die, the hydra dies. At the end of its turn, it grows two heads for each of its heads that died since its last turn, unless it has taken fire damage since its last turn. The hydra regains 10 hit points for each head regrown in this way."
    "name": "Multiple Heads"
  - "desc": "For each head the hydra has beyond one, it gets an extra reaction that can be used only for opportunity attacks."
    "name": "Reactive Heads"
  - "desc": "Of the hydra's original ten heads, one can breathe fire and one can breathe poisonous gas. If one of these heads falls off, the two heads that replace it have the same breath traits as the one that was severed. When a head with poisonous breath makes a bite attack, it deals an additional 7 (2d6) poison damage, and when a head with fire breath makes a bite attack, it deals an additional 7 (2d6) fire damage."
    "name": "Special Heads"
  - "desc": "While the hydra sleeps, at least one of its heads is awake."
    "name": "Wakeful"
"actions":
  - "desc": "The hydra makes as many bite attacks as it has heads. For up to one special head (see \"Special Heads\"), it may replace the bite attack with the appropriate breath attack."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) piercing damage. (See \"Special Heads\".)"
    "name": "Bite"
  - "desc": "The hydra exhales fire in a 60-foot cone. Each creature in that area must make a DC 18 Dexterity saving throw, taking 63 (18d6) fire damage on a failed save, or half as much damage on a successful one."
    "name": "Fire Breath (Recharge 5-6, Fire Breath Head Only)"
  - "desc": "The hydra exhales poisonous gas in a 60-foot cone. Each creature in that area must make a DC 18 Constitution saving throw, taking 56 (16d6) poison damage on a failed save, or half as much damage on a successful one."
    "name": "Poison Breath (Recharge 5-6, Poison Breath Head Only)"
"reactions":
  - "desc": "Immediately after initiative rolls in which the hydra participates, it expects tribute from a creature within 60 feet that it can see, but does not reveal which one or indicate it expects the tribute. Tribute may be paid by bowing, genuflecting, saluting, or a similar gesture."
    "name": "Expect Tribute"
"source":
  - "TBVXXIV"
"image": "Compendium/bestiary/monstrosity/token/nessian-wilds-ravager-tbvxxiv.webp"
```
^statblock
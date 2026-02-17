---
title: Theran Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/mot
- monster/cr/7
- monster/size/large
- monster/type/monstrosity
statblock: inline
aliases: ["Theran Chimera"]
---
# Theran Chimera
*Source: Mythic Odysseys of Theros p. 216*  

![](Compendium/bestiary/monstrosity/img/theran-chimera.webp#right|850)  
The term chimera applies to a wide variety of disparate monsters that combine the features of multiple beasts. While many artistic depictions represent chimeras as an amalgam of lion, ram, and dragon, these beasts appear with nearly endless variations.

The Akroans tell a tale of the first chimera's origin, wherein the god Keranos sought to test Nylea's favorite champion, Renata of Setessa, by creating a beast so deadly that even she would balk at trying to hunt it. When Renata slayed this lion-ram-dragon creation effortlessly, Keranos created another combination of deadlier beasts to challenge her. She slayed that beast, too. Despite countless attempts, Keranos was unable to create a beast that Renata couldn't best.

Chimeras typically roam the deep wilds of the world, constantly seeking a lair that would perfectly suit one of its heads, but then finding it unsatisfying to two-thirds of its being. As a result, a hungry chimera might appear out of a clear sky to pick off prey nearly anywhere. This threat grows even more significant in regions where magic runs rampant or where portals to the realm of Nyx exist, as unrestrained magical energy often causes more chimeras to appear in a region. As such chaotic magic is inherent to a chimera's being, these monsters often manage to shrug off spells cast against them.

## Customizing a Chimera

The Theran chimera stat block presents one possible chimera configuration. You may customize these statistics to design your own unique chimera. To do so, simply roll once on one or all of the following tables. Results from the Body Composition table adjust the Theran chimera as described, while results on the Breath Weapons, Head Attacks, and Tail Attacks tables replace those respective actions in the stat block. Theran chimeras always have the Claws action. If the results of multiple tables conflict, chose your preferred result.

**Body Composition**

| dice: d4 | Attack |
|----------|--------|
| 1 | **Plains Creature.** The chimera's body is that of a large lowland creature, such as a bull or a bear, and it lacks wings and a flying speed. The chimera is especially resilient, gaining resistance to cold and fire damage. |
| 2 | **Coast Creature.** The chimera's body is that of a coastal or aquatic creature, such as a heron or a shark. The chimera gains a swimming speed equal to its walking speed and can breathe air and water. |
| 3 | **Mountain Creature.** The chimera's body is that of a mountain-dwelling creature, such as a ram or a dragon. The chimera doesn't provoke an opportunity attack when it flies out of an enemy's reach. |
| 4 | **Swamp Creature.** The chimera's body is that of a swamp creature or a cavern-dweller, such as a giant lizard or spider. The chimera gains a climbing speed equal to its walking speed and it can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check. |
^body-composition

**Head Attacks**

| dice: d4 | Attack |
|----------|--------|
| 1 | **Bull Horns.** If the chimera moves at least 20 feet straight toward a target and then hits it with a head attack on the same turn, the target takes an extra 7 (`2d6`) piercing damage. If the target is a creature, it must succeed on a DC 15 Strength saving throw or be knocked prone. |
| 2 | **Shark Bite.** The chimera has advantage on a head attack roll against any creature that doesn't have all its hit points. |
| 3 | **Unicorn Horn.** The chimera's head attack is magical and deals an extra 4 (`1d8`) radiant damage. |
| 4 | **Cockatrice Beak.** A creature hit by the chimera's head attack must succeed on a DC 15 Constitution saving throw or be restrained as it begins to turn to stone. The restrained creature must repeat the saving throw at the end of its next turn. On a success, the effect ends. On a failure, the creature is petrified for 24 hours. |
^head-attacks

**Breath Weapons**

| dice: d4 | Attack |
|----------|--------|
| 1 | **Lightning Breath (Recharge 5-6).** The chimera exhales lightning in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 15 Dexterity saving throw, taking 36 (`8d8`) lightning damage on a failed save, or half as much damage on a successful one. |
| 2 | **Tidal Wave Breath (Recharge 5-6).** The chimera has an aquatic creature's head that exhales a torrent of acidic water in a 60-foot line that is 5 feet wide. Each creature in the line must make a DC 15 Dexterity saving throw. On failed save, a creature takes 27 (`5d10`) acid damage and is knocked prone. On a successful save, it takes half as much damage and isn't knocked prone. |
| 3 | **Venom Spray (Recharge 5-6).** The chimera has a venomous creature's head that exhales a spray of poison in a 15-foot cone. Each creature in that area must succeed on a DC 15 Constitution saving throw or be poisoned for 1 minute. While poisoned in this way, a target takes 35 (`10d6`) poison damage at the start of each of its turns. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. |
| 4 | **Necrotic Breath (Recharge 5-6).** The chimera exhales necrotic energy in a 15-foot cone. Each creature in that area must succeed on a DC 15 Constitution saving throw, or it takes 31 (`7d8`) necrotic damage and is unable to regain hit points until the end of its next turn. |
^breath-weapons

**Tail Attacks**

| dice: d4 | Attack |
|----------|--------|
| 1 | **Venomous Tail.** The chimera's tail ends in a snake's head or a stinger, which deals piercing damage instead of bludgeoning damage. In addition, when the chimera hits a creature with its tail, the creature must succeed on a DC 15 Constitution saving throw or become poisoned for 1 minute. A poisoned target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. |
| 2 | **Perplexing Tail.** The chimera has an additional head where its tail should be. The chimera loses its tail attack and makes two head attacks when it takes the Multiattack action. Use the Head Attacks table to determine the nature of the new head. |
| 3 | **Shark Tail.** The chimera's tail is a large fin. When the chimera hits a creature with its tail, the creature is also pushed up to 10 feet away. |
| 4 | **Constricting Tail.** The chimera's tail can constrict prey. If the chimera hits a creature with its tail, the target is grappled (escape DC 15) if it is Large or smaller. Until this grapple ends, the target is restrained, and the chimera can't use its tail on another target. |
^tail-attacks
## Statblock

```statblock
"name": "Theran Chimera (MOT)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "95"
"hit_dice": "10d10 + 40"
"modifier": !!int "1"
"stats":
  - !!int "18"
  - !!int "13"
  - !!int "19"
  - !!int "3"
  - !!int "14"
  - !!int "10"
"speed": "30 ft., fly 60 ft."
"saves":
  - "constitution": !!int "7"
  - "wisdom": !!int "5"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
"senses": "[[senses#Darkvision|darkvision]] 60 ft., passive Perception\
  \ 15"
"languages": "understands Draconic but can't speak"
"cr": "7"
"traits":
  - "desc": "The chimera has advantage on a saving throw against any spell that targets\
      \ only the chimera (not an area). If the chimera's saving throw is successful\
      \ and the spell is of 4th level or lower, the spell has no effect on the chimera\
      \ and instead targets the caster."
    "name": "Spell Turning"
"actions":
  - "desc": "The chimera makes three attacks: one with its claws, one with its head,\
      \ and one with its tail. When its breath weapon is available, it can use the\
      \ breath in place of its head or its claws."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 13\
      \ (2d8 + 4) slashing damage."
    "name": "Claws"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 10\
      \ (1d12 + 4) piercing damage."
    "name": "Head"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 10 ft., one target. *Hit:*\
      \ 11 (2d6 + 4) bludgeoning damage."
    "name": "Tail"
  - "desc": "The chimera exhales fire in a 15-foot cone. Each creature in that area\
      \ must make a DC 15 Dexterity saving throw, taking 32 (5d12) fire damage on\
      \ a failed save, or half as much damage on a successful one."
    "name": "Breath Weapon (Recharge 5-6)"
"source":
  - "MOT"
"image": "Compendium/bestiary/monstrosity/token/theran-chimera-mot.webp"
```
^statblock
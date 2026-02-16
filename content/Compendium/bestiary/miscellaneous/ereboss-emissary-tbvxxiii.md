---
title: Erebos's Emissary
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxiii
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Erebos's Emissary"]
---
# Erebos's Emissary
*Source: Theros Bestiary TBVXXIII*  

A giant cobra provides Erebos with a much-coveted view of the outside world and a chance to invite new guests to the Realm of the Dead.

![Erebos's Emissary](https://img.scryfall.com/cards/art_crop/front/5/a/5aa96f63-d5c3-47d3-a54d-a67883406fc5.jpg?1562818582#right)  

```statblock
"name": "Erebos's Emissary (TBVXXIII)"
"size": "Huge"
"type": "4th-level transmutation beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "56"
"hit_dice": "8d12 + 8"
"modifier": !!int "2"
"stats":
  - !!int "19"
  - !!int "14"
  - !!int "12"
  - !!int "2"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+2"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 10 ft., passive Perception 10"
"languages": ""
"cr": "4"
"traits":
  - "desc": "The emissary's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "In addition to being a creature, the emissary is a 4th-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The emissary glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
  - "desc": "While the emissary is in any of Theros's three realms, it can magically convey what it senses to Erebos."
    "name": "Telepathic Bond"
"actions":
  - "desc": "The emissary makes two attacks: one with its bite and one with its stinger."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) piercing damage, and the target must make a DC 13 Constitution saving throw, taking 7 (2d6) poison damage on a failed save, or half as much damage on a successful one. If the target is a Large or smaller creature, it must succeed on a DC 13 Dexterity saving throw or be swallowed by the emissary. A swallowed creature is [blinded](Compendium/rules/conditions.md#Blinded) and [restrained](Compendium/rules/conditions.md#Restrained), it has total cover against attacks and other effects outside the emissary, and it takes 21 (6d6) acid damage at the start of each of the emissary's turns. If the emissary takes 30 damage or more on a single turn from a creature inside it, the emissary must succeed on a DC 21 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall [prone](Compendium/rules/conditions.md#Prone) in a space within 10 feet of the emissary. If the emissary dies, a swallowed creature is no longer [restrained](Compendium/rules/conditions.md#Restrained) by it and can escape from the corpse by using 20 feet of movement, exiting [prone](Compendium/rules/conditions.md#Prone)."
    "name": "Bite"
  - "desc": "Constrict. Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 13 (2d8 + 4) bludgeoning damage, and the target is [grappled](Compendium/rules/conditions.md#Grappled) (escape DC 16). Until this grapple ends, the creature is [restrained](Compendium/rules/conditions.md#Restrained), and the emissary can't constrict another target."
    "name": "Constrict"
"source":
  - "TBVXXIII"
"image": "Compendium/bestiary/miscellaneous/token/ereboss-emissary-tbvxxiii.webp"
```
^statblock
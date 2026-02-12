---
title: Tromokratis
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/26
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/monstrosity/titan
statblock: inline
aliases: ["Tromokratis"]
---
# Tromokratis
*Source: Mythic Odysseys of Theros p. 254*  

![](Compendium/bestiary/npc/img/tromokratis.webp#right|850)  
Most krakens roam the seas, shattering hulls and scattering fleets, but the kraken Tromokratis notoriously vents its wrath on coastal settlements. Whether it acts at the command of the god Thassa or to sate its own hunger, Tromokratis numbers among the most feared threats in the sea, having no fixed lair and wandering where it will. In recent memory, the massive menace rose from the waves to topple the Pyrgnos, Meletis's great repository of scholarly knowledge. Since that day, the polis keeps a watch specifically for Tromokratis.
```statblock
"name": "Tromokratis (MOT)"
"size": "Gargantuan"
"type": "monstrosity"
"subtype": "titan"
"alignment": "Any alignment"
"ac": !!int "22"
"ac_class": "natural armor"
"hp": !!int "409"
"hit_dice": "21d20 + 189"
"modifier": !!int "0"
"stats":
  - !!int "30"
  - !!int "11"
  - !!int "29"
  - !!int "22"
  - !!int "11"
  - !!int "10"
"speed": "30 ft., swim 80 ft."
"saves":
  - "intelligence": !!int "14"
  - "wisdom": !!int "8"
"damage_resistances": "cold, lightning, thunder"
"damage_immunities": "fire; bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened),\
  \ [paralyzed](Compendium/rules/conditions.md#Paralyzed), [restrained](Compendium/rules/conditions.md#Restrained)"
"senses": "[blindsight](Compendium/rules/senses.md#Blindsight) 120 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "26"
"traits":
  - "desc": "Tromokratis can breathe air and water."
    "name": "Amphibious"
  - "desc": "When Tromokratis is reduced to 0 hit points, it doesn't die or fall [unconscious](Compendium/rules/conditions.md#Unconscious).\
      \ Instead, the damage creates cracks in its carapace, revealing its hearts.\
      \ Tromokratis has four hearts: two on its chest, one on its back, and one at\
      \ the base of its tail. A heart has an AC of 22 and 100 hit points. It is immune\
      \ to bludgeoning, piercing, and slashing damage from nonmagical attacks, and\
      \ it is immune to all conditions. If it is forced to make a saving throw, treat\
      \ its ability scores as 10 (+0). If it finishes a short or long rest, the carapace\
      \ heals, any destroyed hearts regenerate, and the hearts are covered again.\
      \ Tromokratis dies when all the hearts are destroyed."
    "name": "Hearts of the Kraken (Mythic Trait; Recharges after a Short or Long Rest)"
  - "desc": "If Tromokratis fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (3/Day)"
  - "desc": "Tromokratis's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "Tromokratis deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "Tromokratis has advantage on saving throws against spells, and any creature\
      \ that makes a spell attack against Tromokratis has disadvantage on the attack\
      \ roll."
    "name": "Spell-Resistant Carapace"
"actions":
  - "desc": "Tromokratis makes three attacks: one with its pincer, one with its tail,\
      \ and one with its tentacle grasp."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +18 to hit, reach 20 ft., one target. *Hit:*\
      \ 20 (3d6 + 10) bludgeoning damage, and if the target is a creature, it is\
      \ [grappled](Compendium/rules/conditions.md#Grappled) (escape DC 26). Until\
      \ the grapple ends, the target is [restrained](Compendium/rules/conditions.md#Restrained),\
      \ and Tromokratis can't use this attack on anyone else."
    "name": "Pincer"
  - "desc": "*Melee Weapon Attack:* +18 to hit, reach 20 ft., one target. *Hit:*\
      \ 23 (3d8 + 10) bludgeoning damage, and if the target is a creature, it is\
      \ knocked [prone](Compendium/rules/conditions.md#Prone)."
    "name": "Tail"
  - "desc": "*Melee Weapon Attack:* +18 to hit, reach 20 ft., one creature. *Hit:*\
      \ 20 (3d6 + 10) bludgeoning damage, and the target is [grappled](Compendium/rules/conditions.md#Grappled)\
      \ (escape DC 26). If the target doesn't escape by the end of its next turn,\
      \ Tromokratis throws the target up to 60 feet in a straight line. The target\
      \ lands [prone](Compendium/rules/conditions.md#Prone) and takes 21 (6d6) bludgeoning\
      \ damage."
    "name": "Tentacle Grasp"
  - "desc": "*Melee Weapon Attack:* +18 to hit, reach 5 ft., one target. *Hit:*\
      \ 29 (3d12 + 10) piercing damage. If the target is a Large or smaller creature\
      \ [grappled](Compendium/rules/conditions.md#Grappled) by Tromokratis, that creature\
      \ is swallowed, and the grapple ends. While swallowed, the creature is [blinded](Compendium/rules/conditions.md#Blinded)\
      \ and [restrained](Compendium/rules/conditions.md#Restrained), it has total\
      \ cover against attacks and other effects outside Tromokratis, and it takes\
      \ 42 (12d6) acid damage at the start of each of Tromokratis's turns. If Tromokratis\
      \ takes 50 damage or more on a single turn from a creature inside it, Tromokratis\
      \ must succeed on a DC 20 Constitution saving throw at the end of that turn\
      \ or regurgitate all swallowed creatures, which fall [prone](Compendium/rules/conditions.md#Prone)\
      \ in a space within 10 feet of Tromokratis. If Tromokratis dies, a swallowed\
      \ creature is no longer [restrained](Compendium/rules/conditions.md#Restrained)\
      \ by it and can escape from the corpse by using 15 feet of movement, exiting\
      \ [prone](Compendium/rules/conditions.md#Prone)."
    "name": "Bite"
"legendary_description": "Legendary Action Uses: 3. Immediately after another creature's\
  \ turn, Tromokratis can expend a use to take one of the following actions. Tromokratis\
  \ regains all expended uses at the start of each of their turns."
"legendary_actions":
  - "desc": "Tromokratis moves up to half its speed."
    "name": "Move"
  - "desc": "Tromokratis makes one tail attack."
    "name": "Tail"
  - "desc": "Tromokratis makes one bite attack."
    "name": "Bite (Costs 3 Actions)"
"mythic_description": "If Tromokratis's mythic trait is active, it can use the options\
  \ below as legendary actions for 1 hour after using Hearts of the Kraken."
"mythic_actions":
  - "desc": "Tromokratis makes two attacks: one with its tail and one with its tentacle\
      \ grasp."
    "name": "Rampage"
  - "desc": "Each creature within 10 feet of Tromokratis must make a DC 25 Dexterity\
      \ saving throw, taking 13 (3d8) slashing damage on a failed save, or half\
      \ as much damage on a successful one. Until the start of its next turn, Tromokratis\
      \ and its hearts gain a +2 bonus to AC."
    "name": "Coral Growth (Costs 2 Actions)"
"source":
  - "MOT"
"image": "Compendium/bestiary/npc/token/tromokratis-mot.webp"
```
^statblock
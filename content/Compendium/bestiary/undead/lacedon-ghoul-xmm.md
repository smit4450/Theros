---
title: Lacedon Ghoul
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Lacedon Ghoul"]
---
# Lacedon Ghoul
*Source: Monster Manual (2024) p. 132*  

![](Compendium/bestiary/undead/img/lacedon-ghoul.webp#right)  
Lacedons are loose-skinned, aquatic ghouls. They often arise from the corpses of greedy pirates, those who starved on deserted islands, or scoundrels who met their end by drowning.

## Ghouls

*Eaters of the Dead*

- **Habitat.** Swamp, Underdark, Urban  
- **Treasure.** Any  

Packs of ghouls haunt the rotten corners of the world, ravenously hunting for corpses and those soon to be corpses. These gaunt, animate cadavers with unnaturally long tongues dwell in catacombs and ruins where they devour the contents of graves and paralyze foes with vicious claws.

> [!quote]  
> 
> On a plain of teeth, in a temple of filth, the starving king wastes no morsel. Every coffin a banquet. Every slab a platter. Now is the time of feasting!

![](Compendium/bestiary/undead/img/ghouls.webp#center)  
## Statblock

```statblock
"name": "Lacedon Ghoul (XMM)"
"size": "Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "12"
"hp": !!int "22"
"hit_dice": "5d8"
"modifier": !!int "2"
"stats":
  - !!int "13"
  - !!int "15"
  - !!int "10"
  - !!int "7"
  - !!int "10"
  - !!int "6"
"speed": "30 ft., swim 30 ft."
"damage_resistances": "cold"
"damage_immunities": "poison"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Common"
"cr": "1"
"actions":
  - "desc": "The ghoul makes two Icy Bite attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 9 (2d6 + 2) Cold damage,\
      \ and the target's [Speed](Compendium/rules/variant-rules/speed-xphb.md) decreases\
      \ by 5 feet until the start of the ghoul's next turn."
    "name": "Icy Bite"
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 4 (1d4 + 2) Slashing\
      \ damage. If the target is a creature that isn't an Undead or elf, it is subjected\
      \ to the following effect. *Constitution Saving Throw:* DC 10. *Failure:* The\
      \ target has the [Paralyzed](Compendium/rules/conditions.md#Paralyzed) condition\
      \ until the end of its next turn."
    "name": "Claw"
"bonus_actions":
  - "desc": "While underwater, the ghoul moves up to half its [Swim Speed](Compendium/rules/variant-rules/swim-speed-xphb.md)\
      \ without provoking [Opportunity Attacks](Compendium/rules/actions.md#Opportunity%20Attack)."
    "name": "Watery Rush"
"source":
  - "XMM"
"image": "Compendium/bestiary/undead/token/lacedon-ghoul-xmm.webp"
```
^statblock
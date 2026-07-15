---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1
- monster/environment/any
- monster/size/small-or-medium
- monster/type/humanoid
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Spy"
---
# Spy
*Source: Monster Manual (2024) p. 295. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/humanoid/img/spies.webp#right)

Spies use charm and deception to veil their true intentions. If forced into combat, they seek to end such conflicts quietly and decisively.

## Spies

*Infiltrators and Informants*

- **Habitat.** Any  
- **Treasure.** [Implements](/Compendium/tables/random-magic-items-implements.md), Individual  

Spies gather information and disseminate lies, manipulating people to gain the results the spies' patrons desire. They're trained to manipulate, infiltrate, and—when necessary—escape in a hurry. Many adopt disguises, aliases, or code names to maintain anonymity. Roll on or choose a result from the Spy Personas table to inspire a spy's disguise.

**Spy Personas**

| dice: 1d4 | The Spy Disguises Themself As... |
|-----------|----------------------------------|
| 1 | A bard or traveling performer. |
| 2 | A captive or servant of a monster or villain. |
| 3 | A dignitary or traveler from a distant land. |
| 4 | A visitor from a different time or world. |
^spy-personas

## Statblock

```statblock
"name": "Spy"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "12"
"hp": !!int "27"
"hit_dice": "6d8"
"modifier": !!int "4"
"stats":
  - !!int "10"
  - !!int "15"
  - !!int "10"
  - !!int "12"
  - !!int "14"
  - !!int "16"
"speed": "30 ft., climb 30 ft."
"skillsaves":
  - "name": "[Deception](/Compendium/rules/skills.md#Deception)"
    "desc": "+5"
  - "name": "[Insight](/Compendium/rules/skills.md#Insight)"
    "desc": "+4"
  - "name": "[Investigation](/Compendium/rules/skills.md#Investigation)"
    "desc": "+5"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+6"
  - "name": "[Sleight of Hand](/Compendium/rules/skills.md#Sleight%20of%20Hand)"
    "desc": "+4"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+6"
"gear":
  - "[hand crossbow](/Compendium/items/hand-crossbow-xphb.md)"
  - "[shortsword](/Compendium/items/shortsword-xphb.md)"
  - "[thieves' tools](/Compendium/items/thieves-tools-xphb.md)"
"senses": "passive Perception 16"
"languages": "Common plus one other language"
"cr": "1"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 5 (1d6 + 2) Piercing damage\
      \ plus 7 (2d6) Poison damage."
    "name": "Shortsword"
  - "desc": "*Ranged Attack Roll:* +4, range 30/120 ft. *Hit:* 5 (1d6 + 2) Piercing\
      \ damage plus 7 (2d6) Poison damage."
    "name": "Hand Crossbow"
"bonus_actions":
  - "desc": "The spy takes the [Dash](/Compendium/rules/actions.md#Dash), [Disengage](/Compendium/rules/actions.md#Disengage),\
      \ or [Hide](/Compendium/rules/actions.md#Hide) action."
    "name": "Cunning Action"
"source":
  - "XMM"
"image": "/Compendium/bestiary/humanoid/token/spy-xmm.webp"
```
^statblock

## Environment

any
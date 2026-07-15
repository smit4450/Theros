---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/2
- monster/environment/underdark
- monster/size/large
- monster/type/ooze
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Ochre Jelly"
---
# Ochre Jelly
*Source: Monster Manual (2024) p. 230. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/ooze/img/ochre-jelly.webp#right)

## Ochre Jelly

*Multiplying Amoeboid Hunter*

- **Habitat.** Underdark  
- **Treasure.** None  

Ochre jellies are giant, yellow-brown amoebas that digest organic creatures. They tirelessly hunt any prey smaller than themselves, oozing over, under, and around obstacles in their path. Once they overwhelm their quarry, these acidic slimes dissolve the flesh, hair, and scales of their prey, leaving behind clothing, equipment, treated leather, and bone.

If damaged by lightning or a slashing weapon, an ochre jelly splits in two. These smaller jellies work together to consume foes, but afterward they move on to hunt independently. Both eventually grow into full-size jellies.

What ochre jellies can't dissolve they leave behind. Roll on or choose a result from the Ochre Jelly Leftovers table to inspire such remains.

**Ochre Jelly Leftovers**

| dice: 1d6 | After a Meal, the Ochre Jelly Leaves Behind... |
|-----------|------------------------------------------------|
| 1 | A bone etched with a word or an eerie symbol. |
| 2 | Broken dragonborn or tiefling horns. |
| 3 | An ornate prosthetic limb. |
| 4 | The skeleton of an explorer's pet (perhaps a small dog, monkey, or parrot). |
| 5 | A skull with gold teeth worth `1d4` GP. |
| 6 | A spotless suit of metal armor. |
^ochre-jelly-leftovers

```statblock
"name": "Ochre Jelly"
"size": "Large"
"type": "ooze"
"alignment": "Unaligned"
"ac": !!int "8"
"hp": !!int "52"
"hit_dice": "7d10 + 14"
"modifier": !!int "-2"
"stats":
  - !!int "15"
  - !!int "6"
  - !!int "14"
  - !!int "2"
  - !!int "6"
  - !!int "1"
"speed": "20 ft., climb 20 ft."
"damage_resistances": "acid"
"damage_immunities": "lightning, slashing"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [deafened](/Compendium/rules/conditions.md#Deafened),\
  \ [exhaustion](/Compendium/rules/conditions.md#Exhaustion), [frightened](/Compendium/rules/conditions.md#Frightened),\
  \ [grappled](/Compendium/rules/conditions.md#Grappled), [prone](/Compendium/rules/conditions.md#Prone),\
  \ [restrained](/Compendium/rules/conditions.md#Restrained)"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 60 ft., passive Perception\
  \ 8"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The jelly can move through a space as narrow as 1 inch without expending\
      \ extra movement to do so."
    "name": "Amorphous"
  - "desc": "The jelly can climb difficult surfaces, including along ceilings, without\
      \ needing to make an ability check."
    "name": "Spider Climb"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 12 (3d6 + 2) Acid damage."
    "name": "Pseudopod"
"reactions":
  - "desc": "Trigger: While the jelly is Large or Medium and has 10+ [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md),\
      \ it becomes [Bloodied](/Compendium/rules/conditions.md#Bloodied) or is subjected\
      \ to Lightning or Slashing damage. _Response:_ The jelly splits into two new\
      \ Ochre Jellies. Each new jelly is one size smaller than the original jelly\
      \ and acts on its [Initiative](/Compendium/rules/variant-rules/initiative-xphb.md).\
      \ The original jelly's [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ are divided evenly between the new jellies (round down)."
    "name": "Split"
"source":
  - "XMM"
"image": "/Compendium/bestiary/ooze/token/ochre-jelly-xmm.webp"
```
^statblock

## Environment

underdark
---
title: Ochre Jelly
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/ooze
statblock: inline
aliases: ["Ochre Jelly"]
---
# Ochre Jelly
*Source: Monster Manual (2024) p. 230. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/ooze/img/ochre-jelly.webp#right|850)  
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
"name": "Ochre Jelly (XMM)"
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
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Deafened|deafened]],\
  \ [[conditions#Exhaustion|exhaustion]], [[conditions#Frightened|frightened]],\
  \ [[conditions#Grappled|grappled]], [[conditions#Prone|prone]],\
  \ [[conditions#Restrained|restrained]]"
"senses": "[[senses#Blindsight|Blindsight]] 60 ft., passive Perception\
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
  - "desc": "Trigger: While the jelly is Large or Medium and has 10+ [[hit-points-xphb|Hit Points]],\
      \ it becomes [[conditions#Bloodied|Bloodied]] or is subjected\
      \ to Lightning or Slashing damage. _Response:_ The jelly splits into two new\
      \ Ochre Jellies. Each new jelly is one size smaller than the original jelly\
      \ and acts on its [[initiative-xphb|Initiative]].\
      \ The original jelly's [[hit-points-xphb|Hit Points]]\
      \ are divided evenly between the new jellies (round down)."
    "name": "Split"
"source":
  - "XMM"
"image": "Compendium/bestiary/ooze/token/ochre-jelly-xmm.webp"
```
^statblock
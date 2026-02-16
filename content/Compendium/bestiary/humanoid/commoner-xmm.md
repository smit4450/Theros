---
title: Commoner
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Commoner"]
---
# Commoner
*Source: Monster Manual (2024) p. 77. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/humanoid/img/commoner.webp#right|850)  
## Commoner

*Everyday Folk*

- **Habitat.** Any  
- **Treasure.** Individual  

Commoners constitute the majority of people who don't pursue magical talents, extraordinary training, or a life of adventure. Some are generous, helpful sorts, while others are more cautious in sharing what they have. Use the following list of jobs and roles to introduce commoners in your adventures:

Artist

Baker

Bartender

Blacksmith

Butcher

Captive

Carpenter

Castaway

Cobbler

Cook

Dyer

Farmer

Fisher

Fletcher

Flimflam artist

Gossip

Hermit

Hooligan

Hunter

Innkeeper

Laborer

Lamplighter

Mason

Merchant

Miner

Mud lark

Patient

Pilgrim

Resurrectionist

Rioter

Scribe

Servant

Shepherd

Student

Tailor

Tanner

Town crier

Weaver

Youngster
```statblock
"name": "Commoner (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "10"
"hp": !!int "4"
"hit_dice": "1d8"
"modifier": !!int "0"
"stats":
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"speed": "30 ft."
"senses": "passive Perception 10"
"languages": "Common"
"cr": "0"
"traits":
  - "desc": "The commoner has proficiency in one skill of the DM's choice and has\
      \ [[advantage-xphb|Advantage]] whenever it\
      \ makes an ability check using that skill."
    "name": "Training"
"actions":
  - "desc": "*Melee Attack Roll:* +2, reach 5 ft. *Hit:* 2 (1d4) Bludgeoning damage."
    "name": "Club"
"source":
  - "XMM"
"image": "Compendium/bestiary/humanoid/token/commoner-xmm.webp"
```
^statblock
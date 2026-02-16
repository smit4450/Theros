---
title: Crawling Claw
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Crawling Claw"]
---
# Crawling Claw
*Source: Monster Manual (2024) p. 83*  

![](Compendium/bestiary/undead/img/crawling-claws.webp#right|850)  
Lone crawling claws can continue killing sprees they perpetrated in life. Some recklessly attack the living, while others pursue specific victims. In rare cases, a crawling claw wreaks mayhem while the rest of its body still lives, with the original creature potentially unaware of its severed hand's crimes.

## Crawling Claws

*Severed Appendages with Malicious Will*

- **Habitat.** Any  
- **Treasure.** None  

Crawling claws are severed hands that move and act of their own murderous accord. These deathless appendages can spring to life from the severed limbs of killers and villains, and sinister magic-users might animate crawling claws as foul servants. Crawling claws appear in a variety of forms, from decaying human hands to the fresh appendages of animals or monsters

> [!quote] A quote from Ansolm Haas  
> 
> Is it possible for any creature, any living being, to be inherently evil? Such an assertion may itself facilitate the committing of evil acts. By defining a person as evil, we give them free rein to behave as they will, absolving them from the wickedness of their words and the evil of their hands.

## Statblock

```statblock
"name": "Crawling Claw (XMM)"
"size": "Tiny"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "12"
"hp": !!int "2"
"hit_dice": "1d4"
"modifier": !!int "2"
"stats":
  - !!int "13"
  - !!int "14"
  - !!int "11"
  - !!int "5"
  - !!int "10"
  - !!int "4"
"speed": "20 ft., climb 20 ft."
"damage_immunities": "necrotic, poison"
"condition_immunities": "[[conditions#Charmed|charmed]], [[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Frightened|frightened]], [[conditions#Incapacitated|incapacitated]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Blindsight|Blindsight]] 30 ft., passive Perception\
  \ 10"
"languages": "understands Common but can't speak"
"cr": "0"
"actions":
  - "desc": "*Melee Attack Roll:* +3, reach 5 ft. *Hit:* 2 Necrotic damage."
    "name": "Slam"
"source":
  - "XMM"
"image": "Compendium/bestiary/undead/token/crawling-claw-xmm.webp"
```
^statblock
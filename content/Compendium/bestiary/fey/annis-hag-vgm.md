---
title: Annis Hag
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/vgm
- monster/cr/6
- monster/environment/hill
- monster/environment/mountain
- monster/size/large
- monster/type/fey
statblock: inline
aliases: ["Annis Hag"]
---
# Annis Hag
*Source: Volo's Guide to Monsters p. 159, Mythic Odysseys of Theros*  

![](Compendium/bestiary/fey/img/annis-hag.webp#right|850)  
Annis hags lair in mountains or hills. Despite being hunchbacked and hump-shouldered, they are the largest and most physically imposing of their kind, standing eight feet tall.

## Tormenting the Weak

Although annis hags can easily tear a grown man apart, they love hunting children, preferring their flesh above all others. They use the flayed skin of such victims to make supple leather, and a hag's lair often shows the signs of this industry.

Annis hags leave tokens of their cruelty at the edges of forests and other areas they claim. In this way, they provoke fear and paranoia in nearby villages and settlements. To an annis hag, nothing is sweeter than turning a vibrant community into a place paralyzed with terror, where folk never venture out at night, strangers are met with suspicion and anger, and parents warn their children to "be good, or the annis will get you."

## Child Corrupter

When an annis feels especially cruel, she disguises herself as a kindly-looking elderly woman, approaches a child in a remote place, and gives it an iron token that it can use to confide in her. Over time, "Granny" convinces the child that it's okay to have bad thoughts and do bad deeds-starting with breaking things or wandering outside without permission, then graduating to pushing someone down the stairs or setting a house on fire. Sooner or later, the child's family and community become terrified of the "bad seed" and must face the awful decision of whether the child should be punished or exiled.

## Tribe Mother

Much in the way that they befriend children in order to corrupt them, annis hags have a tendency for adopting a group of ogres, trolls, or other loutish creatures, ruling them through brute strength, verbal abuse, and superstition.

## Covens

An annis hag that is part of a coven (see the "Hag Covens" sidebar in the Monster Manual) has a challenge rating of 8 (3,900 XP).

> [!note] Iron Token
> 
> An annis hag can pull out one of her iron teeth or nails and spend 1 minute shaping and polishing it into the form of a coin, a ring, or a tiny mirror. Thereafter, any creature that holds this iron token can have a whispered conversation with the hag, provided the creature and the hag are on the same plane of existence and within 10 miles of each other. The holder of the token can hear only the hag's voice, not those of any other creatures or any ambient noise around the hag. Similarly, the hag can hear the holder of the token and not the noise around it.
> 
> A hag can have up to three iron tokens active at one time. As an action, she can discern the direction and approximate distance to all of her active tokens. She can instantaneously deactivate any of her tokens at any distance (no action required), whereupon the token retains its current form but loses its magical properties.
^iron-token
## Statblock

```statblock
"name": "Annis Hag (VGM)"
"size": "Large"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "75"
"hit_dice": "10d10 + 20"
"modifier": !!int "1"
"stats":
  - !!int "21"
  - !!int "12"
  - !!int "14"
  - !!int "13"
  - !!int "14"
  - !!int "15"
"speed": "40 ft."
"saves":
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+5"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
"damage_resistances": "cold; bludgeoning, piercing, slashing from nonmagical attacks"
"senses": "[[senses#Darkvision|darkvision]] 60 ft., passive Perception\
  \ 15"
"languages": "Common, Giant, Sylvan"
"cr": "6"
"traits":
  - "desc": "The hag's innate spellcasting ability is Charisma (spell save DC 13).\
      \ She can innately cast the following spells:\n\n**3/day each:** [[disguise-self-xphb|disguise self]]\
      \ (including the form of a Medium humanoid), [[fog-cloud-xphb|fog cloud]]"
    "name": "Innate Spellcasting"
"actions":
  - "desc": "The annis makes three attacks: one with her bite and two with her claws."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 15\
      \ (3d6 + 5) piercing damage."
    "name": "Bite"
  - "desc": "*Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 15\
      \ (3d6 + 5) slashing damage."
    "name": "Claw"
  - "desc": "*Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 36\
      \ (9d6 + 5) bludgeoning damage, and the target is [[conditions#Grappled|grappled]]\
      \ (escape DC 15) if it is a Large or smaller creature. Until the grapple ends,\
      \ the target takes 36 (9d6 + 5) bludgeoning damage at the start of each of\
      \ the hag's turns. The hag can't make attacks while grappling a creature in\
      \ this way."
    "name": "Crushing Hug"
"source":
  - "VGM"
  - "MOT"
"image": "Compendium/bestiary/fey/token/annis-hag-vgm.webp"
```
^statblock
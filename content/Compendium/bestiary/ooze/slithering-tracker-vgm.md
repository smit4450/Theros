---
title: Slithering Tracker
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/ooze
statblock: inline
aliases: ["Slithering Tracker"]
---
# Slithering Tracker
*Source: Volo's Guide to Monsters p. 191, Mythic Odysseys of Theros*  

![](Compendium/bestiary/ooze/img/slithering-tracker.webp#right)  
The quest for revenge sometimes leads one to undergo a ritual whereby they transform into a body of semiliquid sentience known as a slithering tracker. Innocuous and insidious at the same time, a tracker flows into places where a normal creature can't go and brings its own brand of watery death down upon its quarry.

## Vengeance at Any Cost

The ritual for creating a slithering tracker is known to hags, liches, and priests who worship gods of vengeance. It can only be performed on a willing creature that hungers for revenge. The ritual sucks all the moisture from the person's body, killing it. Yet the mind lives on in the puddle of liquid that issues forth from the remains, and so too does the subject's insatiable need for retribution.

## Stealthy Assassins

A slithering tracker tastes the ground it courses over, seeking any trace of its prey. To kill, a slithering tracker rises up and enshrouds a creature, attempting to drown the prey while also draining it of blood. A slithering tracker that has killed in this fashion becomes much easier to locate for a time, since its liquid form becomes tinged with blood and its body leaves a visible trail of the stuff behind it.

## Descent into Madness

Achieving revenge against its target doesn't end a slithering tracker's existence, nor its hunger for blood. Some slithering trackers remain aware of their purpose and extend their quest for vengeance to others, such as anyone who supported or befriended the original target. Most of the time, though, a tracker's mind can't cope with being trapped in liquid form, unable to communicate, and driven by the desire for blood: after a tracker fulfills its duty, insanity takes over the creature, and it attacks indiscriminately until it is destroyed.
## Statblock

```statblock
"name": "Slithering Tracker (VGM)"
"size": "Medium"
"type": "ooze"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"hp": !!int "32"
"hit_dice": "5d8 + 10"
"modifier": !!int "4"
"stats":
  - !!int "16"
  - !!int "19"
  - !!int "15"
  - !!int "10"
  - !!int "14"
  - !!int "11"
"speed": "30 ft., climb 30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+8"
"damage_vulnerabilities": "cold, fire"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[blinded](Compendium/rules/conditions.md#Blinded), [deafened](Compendium/rules/conditions.md#Deafened),\
  \ [exhaustion](Compendium/rules/conditions.md#Exhaustion), [grappled](Compendium/rules/conditions.md#Grappled),\
  \ [paralyzed](Compendium/rules/conditions.md#Paralyzed), [petrified](Compendium/rules/conditions.md#Petrified),\
  \ [prone](Compendium/rules/conditions.md#Prone), [restrained](Compendium/rules/conditions.md#Restrained),\
  \ [unconscious](Compendium/rules/conditions.md#Unconscious)"
"senses": "[blindsight](Compendium/rules/senses.md#Blindsight) 120 ft., passive Perception\
  \ 12"
"languages": "understands languages it knew in its previous form but can't speak"
"cr": "3"
"traits":
  - "desc": "In the first round of a combat, the slithering tracker has advantage\
      \ on attack rolls against any creature it [surprised](Compendium/rules/conditions.md#Surprised)."
    "name": "Ambusher"
  - "desc": "While grappling a creature, the slithering tracker takes only haIf the\
      \ damage dealt to it, and the creature it is grappling takes the other half."
    "name": "Damage Transfer"
  - "desc": "While the slithering tracker remains motionless, it is indistinguishable\
      \ from a puddle, unless an observer succeeds on a DC 18 Intelligence ([Investigation](Compendium/rules/skills.md#Investigation))\
      \ check."
    "name": "False Appearance"
  - "desc": "The slithering tracker has advantage on Wisdom checks to track prey."
    "name": "Keen Tracker"
  - "desc": "The slithering tracker can enter an enemy's space and stop there. It\
      \ can also move through a space as narrow as 1 inch wide without squeezing."
    "name": "Liquid Form"
  - "desc": "The slithering tracker can climb difficult surfaces, including upside\
      \ down on ceilings, without needing to make an ability check."
    "name": "Spider Climb"
  - "desc": "While underwater, the slithering tracker has advantage on Dexterity ([Stealth](Compendium/rules/skills.md#Stealth))\
      \ checks made to hide, and it can take the Hide action as a bonus action."
    "name": "Watery Stealth"
"actions":
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 8\
      \ (1d10 + 3) bludgeoning damage."
    "name": "Slam"
  - "desc": "One Large or smaller creature that the slithering tracker can see within\
      \ 5 feet of it must succeed on a DC 13 Dexterity saving throw or be [grappled](Compendium/rules/conditions.md#Grappled)\
      \ (escape DC 13). Until this grapple ends, the target is [restrained](Compendium/rules/conditions.md#Restrained)\
      \ and unable to breathe unless it can breathe water. In addition, the [grappled](Compendium/rules/conditions.md#Grappled)\
      \ target takes 16 (3d10) necrotic damage at the start of each of its turns.\
      \ The slithering tracker can grapple only one target at a time."
    "name": "Life Leech"
"source":
  - "VGM"
  - "MOT"
"image": "Compendium/bestiary/ooze/token/slithering-tracker-vgm.webp"
```
^statblock
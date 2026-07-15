---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/6
- monster/environment/urban
- monster/size/large
- monster/type/elemental
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Invisible Stalker"
---
# Invisible Stalker
*Source: Monster Manual (2024) p. 180. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/books/monster-manual-2025/img/invisible-stalker.webp#right)

## Invisible Stalker

*Unseen Magical Assassin*

- **Habitat.** Urban  
- **Treasure.** None  

Magic and malice give form to invisible stalkers, bodiless spirits of the air. These elusive beings pass unseen with nothing more than a stirring of air. They control powerful winds capable of moving objects and battering foes. Magic-users conjure these creatures to serve as killers and thieves. [Invisible](/Compendium/rules/conditions.md#Invisible) stalkers relentlessly pursue their quarry, and they rarely leave evidence of their crimes.

In rare cases, an invisible stalker lingers in the world without a spellcaster controlling it. Roll on or choose a result from the Uncontrolled Invisible Stalkers table to inspire why one of these monsters lurks in an area without a direct command.

**Uncontrolled Invisible Stalkers**

| dice: 1d6 | The Invisible Stalker Is... |
|-----------|-----------------------------|
| 1 | The breath of an infamous god or monster. |
| 2 | A guardian of a hidden portal or magical site. |
| 3 | The lingering violent thoughts of someone killed in a great battle. |
| 4 | A manifestation of uncontrolled magic. |
| 5 | A servant of an evil elemental ruler such as Yan-C-Bin (the Elemental Prince of Evil Air). |
| 6 | Unable to complete its duty and tries to create circumstances allowing it to fulfill its task. |
^uncontrolled-invisible-stalkers

> [!quote]  
> 
> As detectives, we seek truth by eliminating the impossible, ever mindful that the impossible might also be seeking to eliminate us.


```statblock
"name": "Invisible Stalker"
"size": "Large"
"type": "elemental"
"alignment": "Neutral"
"ac": !!int "14"
"hp": !!int "97"
"hit_dice": "13d10 + 26"
"modifier": !!int "7"
"stats":
  - !!int "16"
  - !!int "19"
  - !!int "14"
  - !!int "10"
  - !!int "15"
  - !!int "11"
"speed": "50 ft., fly 50 ft. (hover)"
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+8"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+10"
"damage_resistances": "bludgeoning, piercing, slashing"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [grappled](/Compendium/rules/conditions.md#Grappled), [paralyzed](/Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](/Compendium/rules/conditions.md#Petrified), [poisoned](/Compendium/rules/conditions.md#Poisoned),\
  \ [prone](/Compendium/rules/conditions.md#Prone), [restrained](/Compendium/rules/conditions.md#Restrained),\
  \ [unconscious](/Compendium/rules/conditions.md#Unconscious)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 18"
"languages": "Common, Primordial (Auran)"
"cr": "6"
"traits":
  - "desc": "The stalker can enter an enemy's space and stop there. It can move through\
      \ a space as narrow as 1 inch without expending extra movement to do so."
    "name": "Air Form"
  - "desc": "The stalker has the [Invisible](/Compendium/rules/conditions.md#Invisible)\
      \ condition."
    "name": "Invisibility"
"actions":
  - "desc": "The stalker makes three Wind Swipe attacks. It can replace one attack\
      \ with a use of Vortex."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 11 (2d6 + 4) Force damage."
    "name": "Wind Swipe"
  - "desc": "*Constitution Saving Throw:* DC 14, one Large or smaller creature in\
      \ the stalker's space. *Failure:* 7 (1d8 + 3) Thunder damage, and the target\
      \ has the [Grappled](/Compendium/rules/conditions.md#Grappled) condition (escape\
      \ DC 13). Until the grapple ends, the target can't cast spells with a Verbal\
      \ component and takes 7 (2d6) Thunder damage at the start of each of the stalker's\
      \ turns."
    "name": "Vortex"
"source":
  - "XMM"
"image": "/Compendium/bestiary/elemental/token/invisible-stalker-xmm.webp"
```
^statblock

## Environment

urban
---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/4
- monster/environment/desert
- monster/size/large
- monster/type/fiend
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Lamia"
---
# Lamia
*Source: Monster Manual (2024) p. 192. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/fiend/img/lamia.webp#right)

## Lamia

*Accursed Bargainer and Ruin Raider*

- **Habitat.** Desert  
- **Treasure.** [Arcana](/Compendium/tables/random-magic-items-arcana.md)  

Legends say the first lamia was an ambitious ruler who made a sinister bargain with the demon lord Graz'zt for everlasting majesty. As a consequence, the ruler was transformed into a lamia, a monster with the body of a lion and an accursed touch.

Lamias either are descendants of that first lamia or have made similar deals. They often dwell near ruins, seeking mysterious magic they can use to gain riches and influence. Lamias use magical illusions and enchantments to trick others into serving them. They sometimes work with bandits to abduct travelers, releasing captives only if they accept a dangerous bargain. Roll on or choose a result from the Lamia Pacts table to inspire a lamia's desires.

**Lamia Pacts**

| dice: 1d6 | The Lamia Compels the Bargainer To... |
|-----------|---------------------------------------|
| 1 | Bring it a possession from a ruler or noble. |
| 2 | Create a map of a dungeon or ruin. |
| 3 | Escort it through a nearby community's gate. |
| 4 | Place a strange idol in a specific site or home. |
| 5 | Remove a magic item's curse, then return it. |
| 6 | Slay a monster and retrieve a specific organ. |
^lamia-pacts

```statblock
"name": "Lamia"
"size": "Large"
"type": "fiend"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"hp": !!int "97"
"hit_dice": "13d10 + 26"
"modifier": !!int "1"
"stats":
  - !!int "16"
  - !!int "13"
  - !!int "15"
  - !!int "14"
  - !!int "15"
  - !!int "16"
"speed": "40 ft."
"skillsaves":
  - "name": "[Deception](/Compendium/rules/skills.md#Deception)"
    "desc": "+7"
  - "name": "[Insight](/Compendium/rules/skills.md#Insight)"
    "desc": "+4"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 12"
"languages": "Abyssal, Common"
"cr": "4"
"actions":
  - "desc": "The lamia makes two Claw attacks. It can replace one attack with a use\
      \ of Corrupting Touch."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 7 (1d8 + 3) Slashing damage\
      \ plus 7 (2d6) Psychic damage."
    "name": "Claw"
  - "desc": "*Wisdom Saving Throw:* DC 13, one creature the lamia can see within 5\
      \ feet. *Failure:* 13 (3d8) Psychic damage, and the target is cursed for 1 hour.\
      \ Until the curse ends, the target has the [Charmed](/Compendium/rules/conditions.md#Charmed)\
      \ and [Poisoned](/Compendium/rules/conditions.md#Poisoned) conditions."
    "name": "Corrupting Touch"
  - "desc": "The lamia casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 13):\n\n**At\
      \ will:** [Disguise Self](/Compendium/spells/disguise-self-xphb.md) (can appear\
      \ as a Large or Medium biped), [Minor Illusion](/Compendium/spells/minor-illusion-xphb.md)\n\
      \n**1/day each:** [Geas](/Compendium/spells/geas-xphb.md), [Major Image](/Compendium/spells/major-image-xphb.md),\
      \ [Scrying](/Compendium/spells/scrying-xphb.md)"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The lamia jumps up to 30 feet by spending 10 feet of movement."
    "name": "Leap"
"source":
  - "XMM"
"image": "/Compendium/bestiary/fiend/token/lamia-xmm.webp"
```
^statblock

## Environment

desert
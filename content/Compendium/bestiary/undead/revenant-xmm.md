---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/5
- monster/environment/forest
- monster/environment/swamp
- monster/environment/urban
- monster/size/medium
- monster/type/undead
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Revenant"
---
# Revenant
*Source: Monster Manual (2024) p. 259*
![Revenant Followed by a Graveyard Revenant](/Compendium/bestiary/undead/img/revenant-and-graveyard-revenant.webp#right)

Revenants possess the bodies they had in life, using them to hunt down their killers. If their bodies are destroyed, they take control of new bodies that gradually change to resemble the revenants' original forms.

## Revenants

*Vengeance from beyond the Grave*

- **Habitat.** Forest, Swamp, Urban  
- **Treasure.** Any  

Wrathful spirits bent on revenge, revenants possess corpses and other materials, using them to seek justice or vent their rage on those who wronged them. Revenants refuse to rest until those they seek to punish are no more. If their bodies are destroyed, revenants claim new forms and continue their ruthless quests.

## Statblock

```statblock
"name": "Revenant"
"size": "Medium"
"type": "undead"
"alignment": "Neutral"
"ac": !!int "13"
"hp": !!int "127"
"hit_dice": "15d8 + 60"
"modifier": !!int "2"
"stats":
  - !!int "18"
  - !!int "14"
  - !!int "18"
  - !!int "13"
  - !!int "16"
  - !!int "18"
"speed": "30 ft."
"saves":
  - "strength": !!int "7"
  - "constitution": !!int "7"
  - "wisdom": !!int "6"
  - "charisma": !!int "7"
"damage_resistances": "necrotic, psychic"
"damage_immunities": "poison"
"condition_immunities": "[charmed](/Compendium/rules/conditions.md#Charmed), [exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](/Compendium/rules/conditions.md#Frightened), [paralyzed](/Compendium/rules/conditions.md#Paralyzed),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned), [stunned](/Compendium/rules/conditions.md#Stunned)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 13"
"languages": "Common plus one other language"
"cr": "5"
"traits":
  - "desc": "The revenant regains 10 [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ at the start of each of its turns. If the revenant takes Fire or Radiant damage,\
      \ this trait doesn't function at the start of its next turn. Its body is destroyed\
      \ only if it starts its turn with 0 [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ and doesn't regenerate."
    "name": "Regeneration"
  - "desc": "If the revenant dies, it revives 24 hours later in a different body unless\
      \ [Dispel Evil and Good](/Compendium/spells/dispel-evil-and-good-xphb.md) is\
      \ cast on its corpse. If it revives, it animates a Humanoid corpse elsewhere\
      \ on the same plane of existence; it now looks different but uses the same stat\
      \ block and returns with all its [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Undead Restoration"
"actions":
  - "desc": "The revenant uses Vengeful Glare and makes two Slam attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 11 (2d6 + 4) Necrotic damage."
    "name": "Slam"
  - "desc": "*Wisdom Saving Throw:* DC 15, one creature the revenant can see within\
      \ 30 feet. *Failure:* The target has the [Frightened](/Compendium/rules/conditions.md#Frightened)\
      \ condition and repeats the save at the end of each of its turns, ending the\
      \ effect on itself on a success. After 1 minute, it succeeds automatically.\
      \ If the [Frightened](/Compendium/rules/conditions.md#Frightened) target is\
      \ cursed by the revenant (see Vow of Revenge), the target also has the [Paralyzed](/Compendium/rules/conditions.md#Paralyzed)\
      \ condition for the duration."
    "name": "Vengeful Glare"
"bonus_actions":
  - "desc": "The revenant curses one creature it can see within 30 feet of itself.\
      \ The revenant knows the distance to and direction of the cursed target, even\
      \ if it is on a different plane of existence. The curse ends on the target if\
      \ the revenant uses this [Bonus Action](/Compendium/rules/variant-rules/bonus-action-xphb.md)\
      \ on a different creature."
    "name": "Vow of Revenge (1/Day)"
"source":
  - "XMM"
"image": "/Compendium/bestiary/undead/token/revenant-xmm.webp"
```
^statblock

## Environment

forest, swamp, urban
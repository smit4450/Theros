---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/2
- monster/environment/hill
- monster/environment/mountain
- monster/size/medium
- monster/type/monstrosity
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Peryton"
---
# Peryton
*Source: Monster Manual (2024) p. 238*
![](/Compendium/bestiary/monstrosity/img/peryton.webp#right)

## Peryton

*Winged Heart Hunter*

- **Habitat.** Hill, Mountain  
- **Treasure.** [Armaments](/Compendium/tables/random-magic-items-armaments.md)  

Perytons are monstrous predators that hunt people—particularly humans and elves—in favor of all other prey. With the bodies of mighty avian scavengers and fanged, stag-like heads, perytons use ambush tactics to dive-bomb travelers. Strangely, the shadows they cast resemble humanoid silhouettes. This supernatural oddity lends credence to stories that perytons are cursed humans or elves, or that they arise from carrion birds that feed on the corpses of villains.

Perytons tear out the hearts of those they slay, carrying the organs back to grisly lairs. This gives rise to numerous superstitions surrounding perytons. Roll on or choose a result from the Peryton Superstitions table to inspire why a peryton steals hearts.

**Peryton Superstitions**

| dice: 1d4 | If a Peryton Collects Enough Hearts... |
|-----------|----------------------------------------|
| 1 | The hearts grant an evil wish. |
| 2 | It reverts to its original form. |
| 3 | A new peryton hatches from each heart. |
| 4 | A portal opens to the Lower Planes. |
^peryton-superstitions

```statblock
"name": "Peryton"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"hp": !!int "33"
"hit_dice": "6d8 + 6"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "12"
  - !!int "13"
  - !!int "9"
  - !!int "12"
  - !!int "10"
"speed": "20 ft., fly 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+5"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+3"
"senses": "passive Perception 15"
"languages": "understands Common and Elvish but can't speak"
"cr": "2"
"traits":
  - "desc": "The peryton doesn't provoke an Opportunity Attack when it flies out of\
      \ an enemy's reach."
    "name": "Flyby"
"actions":
  - "desc": "The peryton makes one Gore attack and one Talons attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 7 (1d8 + 3) Piercing damage.\
      \ If the peryton moved 30+ feet straight toward the target immediately before\
      \ the hit, the target takes an extra 9 (2d8) Piercing damage."
    "name": "Gore"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 8 (2d4 + 3) Piercing damage.\
      \ If the attack reduces a Humanoid target to 0 [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md),\
      \ the peryton kills the target by removing its heart."
    "name": "Talons"
"source":
  - "XMM"
"image": "/Compendium/bestiary/monstrosity/token/peryton-xmm.webp"
```
^statblock

## Environment

hill, mountain
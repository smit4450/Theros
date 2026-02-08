---
title: Archdruid
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
aliases: ["Archdruid"]
---
# Archdruid
*Source: Volo's Guide to Monsters p. 210, Mythic Odysseys of Theros*  

Archdruids watch over the natural wonders of their domains. They seldom interact with civilized folk unless there is a great threat to the natural order. An archdruid typically has one or more pupils who are druids (see the Monster Manual for statistics), and the archdruid's lair is usually guarded by loyal beasts and fey creatures.
```statblock
"name": "Archdruid (VGM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "16"
"ac_class": "[hide armor](Compendium/items/hide-armor-xphb.md), [shield](Compendium/items/shield-xphb.md)"
"hp": !!int "132"
"hit_dice": "24d8 + 24"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "14"
  - !!int "12"
  - !!int "12"
  - !!int "20"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "5"
  - "wisdom": !!int "9"
"skillsaves":
  - "name": "[Medicine](Compendium/rules/skills.md#Medicine)"
    "desc": "+9"
  - "name": "[Nature](Compendium/rules/skills.md#Nature)"
    "desc": "+5"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+9"
"senses": "passive Perception 19"
"languages": "Druidic plus any two languages"
"cr": "12"
"traits":
  - "desc": "The archdruid is an 18th-level spellcaster. Its spellcasting ability\
      \ is Wisdom (spell save DC 17, +9 to hit with spell attacks). It has the following\
      \ druid spells prepared:\n\n**Cantrips (at will):** [druidcraft](Compendium/spells/druidcraft-xphb.md),\
      \ [mending](Compendium/spells/mending-xphb.md), [poison spray](Compendium/spells/poison-spray-xphb.md),\
      \ [produce flame](Compendium/spells/produce-flame-xphb.md)\n\n**1st level (4\
      \ slots):** [cure wounds](Compendium/spells/cure-wounds-xphb.md), [entangle](Compendium/spells/entangle-xphb.md),\
      \ [faerie fire](Compendium/spells/faerie-fire-xphb.md), [speak with animals](Compendium/spells/speak-with-animals-xphb.md)\n\
      \n**2nd level (3 slots):** [animal messenger](Compendium/spells/animal-messenger-xphb.md),\
      \ [beast sense](Compendium/spells/beast-sense-xphb.md), [hold person](Compendium/spells/hold-person-xphb.md)\n\
      \n**3rd level (3 slots):** [conjure animals](Compendium/spells/conjure-animals-xphb.md),\
      \ [meld into stone](Compendium/spells/meld-into-stone-xphb.md), [water breathing](Compendium/spells/water-breathing-xphb.md)\n\
      \n**4th level (3 slots):** [dominate beast](Compendium/spells/dominate-beast-xphb.md),\
      \ [locate creature](Compendium/spells/locate-creature-xphb.md), [stoneskin](Compendium/spells/stoneskin-xphb.md),\
      \ [wall of fire](Compendium/spells/wall-of-fire-xphb.md)\n\n**5th level (3 slots):**\
      \ [commune with nature](Compendium/spells/commune-with-nature-xphb.md), [mass\
      \ cure wounds](Compendium/spells/mass-cure-wounds-xphb.md), [tree stride](Compendium/spells/tree-stride-xphb.md)\n\
      \n**6th level (1 slots):** [heal](Compendium/spells/heal-xphb.md), [heroes'\
      \ feast](Compendium/spells/heroes-feast-xphb.md), [sunbeam](Compendium/spells/sunbeam-xphb.md)\n\
      \n**7th level (1 slots):** [fire storm](Compendium/spells/fire-storm-xphb.md)\n\
      \n**8th level (1 slots):** [animal shapes](Compendium/spells/animal-shapes-xphb.md)\n\
      \n**9th level (1 slots):** [foresight](Compendium/spells/foresight-xphb.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 5\
      \ (1d6 + 2) slashing damage."
    "name": "Scimitar"
  - "desc": "The archdruid magically polymorphs into a beast or elemental with a challenge\
      \ rating of 6 or less, and can remain in this form for up to 9 hours. The archdruid\
      \ can choose whether its equipment falls to the ground, melds with its new form,\
      \ or is worn by the new form. The archdruid reverts to its true form if it dies\
      \ or falls [unconscious](Compendium/rules/conditions.md#Unconscious). The archdruid\
      \ can revert to its true form using a bonus action on its turn.\n\nWhile in\
      \ a new form, the archdruid retains its game statistics and ability to speak,\
      \ but its AC, movement modes, Strength, and Dexterity are replaced by those\
      \ of the new form, and it gains any special senses, proficiencies, traits, actions,\
      \ and reactions (except class features, legendary actions, and lair actions)\
      \ that the new form has but that it lacks. It can cast its spells with verbal\
      \ or somatic components in its new form.\n\nThe new form's attacks count as\
      \ magical for the purpose of overcoming resistances and immunity to nonmagical\
      \ attacks."
    "name": "Change Shape (2/Day)"
"source":
  - "VGM"
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/archdruid-vgm.webp"
```
^statblock
---
title: Polypharmakon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxiv
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Polypharmakon"]
---
# Polypharmakon
*Source: Theros Bestiary TBVXIV*  

The polypharmakon specializes in pharmaceutical plants, which she uses for healing and for seducing men. When she is finished with a man, she turns him into an animal, which she adds to her menagerie. The sort of animal that the man becomes is usually related to their personality:
<li>Noble with magnanimous heart: lion
<li>Furious and rage-filled: bear
<li>Voracious and so starved that no food contents them: wolf
<li>Revels and sleeps instead of tending the fire: goat
<li>Malicious and annoying: fox
<li>Bending over for everyone: giraffe
<li>Proud: peacock
<li>Terrified of death: stag
<li>Shameless: pig
<li>A prophet or augur: woodpecker
<li>The possibilities are endless... oysters to elephants...

![Polypharmakon](https://img.scryfall.com/cards/art_crop/front/7/8/78831fc6-ea90-4546-b46a-9c192dbefc65.jpg?1562820142#right)  

```statblock
"name": "Polypharmakon (TBVXIV)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "16"
"ac_class": "hide armor, shield"
"hp": !!int "120"
"hit_dice": "24d8 + 24"
"modifier": !!int "2"
"stats":
  - !!int "11"
  - !!int "15"
  - !!int "13"
  - !!int "13"
  - !!int "21"
  - !!int "12"
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
"senses": "passive Perception 10"
"languages": "Druidic, Common, Sylvan, Elvish"
"cr": "12"
"traits":
  - "desc": "The polypharmakon is a 18th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 17, +9 to hit with spell attacks). The polypharmakon has the following druid spells prepared: Cantrip (at will): [Mending](Compendium/spells/mending-xphb.md), _poison spray_, [Resistance](Compendium/spells/resistance-xphb.md) 1st level (4 slots): _animal friendship_, [Charm Person](Compendium/spells/charm-person-xphb.md), [Cure Wounds](Compendium/spells/cure-wounds-xphb.md), [Speak With Animals](Compendium/spells/speak-with-animals-xphb.md) 2nd level (3 slots): _animal messenger_, [Lesser Restoration](Compendium/spells/lesser-restoration-xphb.md), [Protection From Poison](Compendium/spells/protection-from-poison-xphb.md) 3rd level (3 slots): [Plant Growth](Compendium/spells/plant-growth-xphb.md), [Speak With Plants](Compendium/spells/speak-with-plants-xphb.md) 4th level (3 slots): [Confusion](Compendium/spells/confusion-xphb.md), [Dominate Beast](Compendium/spells/dominate-beast-xphb.md), [Locate Creature](Compendium/spells/locate-creature-xphb.md), [Polymorph](Compendium/spells/polymorph-xphb.md) 5th level (2 slots): [Geas](Compendium/spells/geas-xphb.md), [Greater Restoration](Compendium/spells/greater-restoration-xphb.md), [Mass Cure Wounds](Compendium/spells/mass-cure-wounds-xphb.md) 6th level (1 slots): [Heal](Compendium/spells/heal-xphb.md), _heroes' feast_ 7th level (1 slots): [Regenerate](Compendium/spells/regenerate-xphb.md) 8th level (1 slots): _animal shapes_ 9th level (1 slots): [Shapechange](Compendium/spells/shapechange-xphb.md)"
    "name": "Spellcasting"
"actions":
  - "desc": "_Melee Weapon Attack:_ +6 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) slashing damage."
    "name": "Scimitar"
  - "desc": "The polypharmakon magically polymorphs into a beast or elemental with a challenge rating of 6 or less, and can remain in this form for up to 9 hours. The polypharmakon can choose whether its equipment falls to the ground, melds with its new form, or is worn by the new form. The polypharmakon reverts to its true form if it dies or falls [unconscious](Compendium/rules/conditions.md#Unconscious). The polypharmakon can revert to its true form using a bonus action on its turn. While in a new form, the polypharmakon retains its game statistics and ability to speak, but its AC, movement modes, Strength, and Dexterity are replaced by those of the new form, and it gains any special senses, proficiencies, traits, actions, and reactions (except class features, legendary actions, and lair actions) that the new form has but that it lacks. It can cast its spells with verbal or somatic components in its new form. The new form’s attacks count as magical for the purpose of overcoming resistances and immunity to nonmagical attacks."
    "name": "Change Shape (2/Day)"
"source":
  - "TBVXIV"
"image": "Compendium/bestiary/humanoid/token/polypharmakon-tbvxiv.webp"
```
^statblock
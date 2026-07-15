---
obsidianUIMode: preview
cssclasses:
- json5e-object
tags:
- compendium/src/5e/xdmg
- object/size/large
- object/type/siege-weapon
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Suspended Cauldron"
---
# Suspended Cauldron
*Source: Dungeon Master's Guide (2024) p. 97*

An iron pot is suspended so that it can be tipped easily, spilling its contents. Once emptied, a cauldron must be refilled before it can be used again. Filling the cauldron requires three [Utilize](/Compendium/rules/actions.md#Utilize) actions. Then a crew member can take the Spill action.

Cauldrons are typically filled with boiling oil but can be filled with other substances, such as acid or [green slime](/Compendium/traps-hazards/green-slime-xdmg.md) (see ""Hazards""), with different effects.
```statblock
"name": "Suspended Cauldron"
"size": "Large"
"ac": !!int "19"
"hp": !!int "20"
"stats":
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"actions":
  - "desc": "Dexterity Saving Throw: DC 15, each creature in a 10-foot square directly\
      \ below the cauldron. Failure: 10 (3d6) Fire damage. Success: Half damage."
    "name": "Spill (Requires a Full Cauldron)"
"source":
  - "XDMG"
"image": "/Compendium/objects/token/suspended-cauldron-xdmg.webp"
```
^statblock
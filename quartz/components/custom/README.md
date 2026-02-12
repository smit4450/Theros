# Folder Note Explorer

A custom Quartz component that adds Obsidian-style folder note functionality to the Explorer.

## Features

- **Folder Notes**: When a folder contains an `index.md` or a file matching the folder name (e.g., `Compendium/Compendium.md`), clicking the folder name navigates to that note
- **Folder Listing Button**: A subtle list icon (📋) appears to the right of each folder name that always links to the folder listing page (showing all files and their tags)
- **Smart Hiding**: Folder note files are automatically hidden from the folder's child list to avoid duplication
- **Standard Behavior**: The folder icon (▼ arrow) still toggles expand/collapse as expected

## Installation

The component is already created in `quartz/components/custom/`. To use it:

### 1. Update your layout

In your `quartz.layout.ts`, replace `Component.Explorer()` with the custom component:

```typescript
import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import FolderNoteExplorer from "./quartz/components/custom/FolderNoteExplorer"

export const defaultContentPageLayout: PageLayout = {
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    // ... other components
    FolderNoteExplorer(),  // Replace Component.Explorer() with this
  ],
  // ... rest of layout
}
```

### 2. Rebuild

After updating your layout, rebuild your Quartz site:

```bash
npx quartz build
```

## Options

All standard Explorer options are supported:

```typescript
FolderNoteExplorer({
  title: "Explorer",                    // Title of the explorer
  folderDefaultState: "collapsed",      // "collapsed" | "open"
  folderClickBehavior: "link",          // "link" | "collapse"
  useSavedState: true,                  // Save state in localStorage
  sortFn: (a, b) => { /* ... */ },     // Custom sort function
  filterFn: (node) => { /* ... */ },   // Custom filter function
  mapFn: (node) => { /* ... */ },      // Custom map function
  order: ["filter", "map", "sort"],    // Order of operations
})
```

## How It Works

### Folder Note Detection

The component checks each folder for:
1. An `index.md` file in the folder
2. A file with the same name as the folder (e.g., `Compendium/Compendium.md`)

When either exists, that file is considered the "folder note" and:
- Clicking the folder name navigates to the note
- The note is hidden from the folder's child list
- The folder-list button still shows the full folder listing

### UI Elements

- **Folder Name**: Links to folder note (if exists) or folder page (if no note)
- **Folder Icon (▼)**: Toggles expand/collapse of folder contents
- **Folder List Button (📋)**: Always links to the folder listing page

## Maintenance

This component is self-contained in the `quartz/components/custom/` directory:
- `FolderNoteExplorer.tsx` - Main component
- `scripts/folderNoteExplorer.inline.ts` - Client-side logic
- `styles/folderNoteExplorer.scss` - Styling
- `index.ts` - Export point

The original Explorer component remains unchanged, so you can easily switch back if needed.

## Updating Quartz

When updating Quartz to a new version:
1. The custom component is separate from core files, so updates won't break it
2. If the core Explorer receives significant changes, you may need to merge them manually
3. All custom files are in the `custom/` directory for easy identification

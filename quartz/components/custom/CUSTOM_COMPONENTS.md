# Custom Quartz Components

This directory contains custom components that extend Quartz functionality with features specific to this site. All custom components are self-contained to avoid conflicts during Quartz updates.

## Components Overview

### 1. Tag Display Components (Tag Shortening)

Custom components that shorten hierarchical tag names for cleaner display across all pages.

#### Components

- **TagListCustom.tsx** - Displays tags on individual content pages
- **PageListCustom.tsx** - Displays pages with tags in folder and tag listings
- **RecentNotesCustom.tsx** - Displays recent notes with shortened tags

#### Features

- **Tag Shortening**: Displays only the last segment of hierarchical tags
  - Example: `ttrpg-cli/spell/class/sorcerer` → displays as `sorcerer`
- **Hover Full Tag**: Full tag path shown in tooltip on hover (via `title` attribute)
- **Consistent Styling**: Maintains all original styling and functionality
- **Shared Utility**: `getTagDisplayName()` function prevents code duplication

#### Installation

**Step 1**: Import custom components in `quartz.layout.ts`:

```typescript
import TagListCustom from "./quartz/components/custom/TagListCustom"
import RecentNotesCustom from "./quartz/components/custom/RecentNotesCustom"

export const defaultContentPageLayout: PageLayout = {
  left: [
    RecentNotesCustom(),  // Instead of Component.RecentNotes()
  ],
  right: [
    TagListCustom(),      // Instead of Component.TagList()
  ],
}
```

**Step 2**: Custom page components are automatically used

The following files are already configured to use custom components:
- `quartz/plugins/emitters/tagPage.tsx` → uses `TagContentCustom`
- `quartz/plugins/emitters/folderPage.tsx` → uses `FolderContentCustom`

No additional configuration needed for folder and tag pages!

#### Usage Example

```typescript
import { getTagDisplayName } from "./quartz/components/custom/PageListCustom"

// In any component that displays tags:
const displayName = getTagDisplayName("ttrpg-cli/spell/class/sorcerer")
// Returns: "sorcerer"

// In JSX:
<a href={tagUrl} title={fullTag}>
  {getTagDisplayName(fullTag)}
</a>
```

### 2. Folder Note Explorer

A custom Quartz component that adds Obsidian-style folder note functionality to the Explorer.

#### Features

- **Folder Notes**: When a folder contains an `index.md` or a file matching the folder name (e.g., `Compendium/Compendium.md`), clicking the folder name navigates to that note
- **Folder Listing Button**: A list icon (📋) appears that links to the folder listing page
- **Smart Hiding**: Folder note files are automatically hidden from the folder's child list
- **Standard Behavior**: The folder icon (▼) still toggles expand/collapse

#### Installation

In `quartz.layout.ts`:

```typescript
import FolderNoteExplorer from "./quartz/components/custom/FolderNoteExplorer"

export const defaultContentPageLayout: PageLayout = {
  left: [
    FolderNoteExplorer(),  // Instead of Component.Explorer()
  ],
}
```

### 3. Spell Table

Custom component for displaying D&D spells in a structured table format.

## File Structure

```
quartz/components/custom/
├── TagListCustom.tsx            # Custom tag list for content pages
├── PageListCustom.tsx           # Custom page list with tag shortening
├── RecentNotesCustom.tsx        # Custom recent notes
├── FolderNoteExplorer.tsx       # Folder note component
├── SpellTable.tsx               # Spell display component
├── index.ts                     # Component exports
├── README.md                    # Original FolderNoteExplorer docs
├── CUSTOM_COMPONENTS.md         # This file
├── pages/
│   ├── FolderContentCustom.tsx  # Custom folder page component
│   └── TagContentCustom.tsx     # Custom tag page component
├── scripts/                     # Client-side scripts
└── styles/                      # Component styles
```

## Core File Modifications

To use the custom components, the following core files have been modified:

### Plugin Emitters (Configuration Files)

✅ `quartz/plugins/emitters/tagPage.tsx`
- Imports and uses `TagContentCustom` instead of `TagContent`
- Automatically applies to all tag pages
- Tag listing pages show shortened tags

✅ `quartz/plugins/emitters/folderPage.tsx`
- Imports and uses `FolderContentCustom` instead of `FolderContent`  
- Automatically applies to all folder listing pages
- Folder listings show shortened tags

These emitter files are the only core modifications required - they wire up the custom page components automatically during the build process.

## Maintenance & Updates

### Benefits of This Architecture

1. **Update-Safe**: Core Quartz files remain mostly unchanged
2. **Portable**: All customizations in one directory
3. **Reusable**: Shared utilities prevent code duplication
4. **Documented**: Clear documentation of changes
5. **Reversible**: Easy to switch back to core components

### Updating Quartz

When updating Quartz toin `quartz/components/custom/` won't be overwritten
2. ⚠️ Check if these emitter files have significant changes:
   - `quartz/plugins/emitters/tagPage.tsx`
   - `quartz/plugins/emitters/folderPage.tsx`
3. ⚠️ If updated, ensure they still import custom components:
   ```typescript
   import { TagContentCustom } from "../../components"
   import { FolderContentCustom } from "../../components"
   ```
4. ✅ Test all custom components after updating

### Reverting Changes

To revert to standard Quartz components:

**Emitter Files**: Update imports in:
- `quartz/plugins/emitters/tagPage.tsx`:
  ```typescript
  import { TagContent } from "../../components"
  // and use TagContent() instead of TagContentCustom()
  ```

- `quartz/plugins/emitters/folderPage.tsx`:
  ```typescript
  import { FolderContent } from "../../components"
  // and use FolderContent() instead of FolderContentCustom()
  ```

**Layout File**: Update `quartz.layout.ts`:
```typescript
Component.Explorer()
Component.RecentNotes()
Component.TagList()sx` and `TagContent.tsx`:
```typescript
import { PageList, SortFn } from "../PageList"
```

## Component Options

### TagListCustom

No options, uses default behavior:

```typescript
TagListCustom()
```

### PageListCustom

Used automatically via FolderContent/TagContent. Exports same types as PageList:

```typescript
import { PageListCustom, SortFn, byDateAndAlphabetical, byDateAndAlphabeticalFolderFirst } from "../custom/PageListCustom"
```

### RecentNotesCustom

All standard RecentNotes options:

```typescript
RecentNotesCustom({
  title: "Recent Notes",
  limit: 3,
  showTags: true,
  linkToMore: "notes" as SimpleSlug,
  filter: (f) => true,
  sort: byDateAndAlphabetical(cfg),
})
```

### FolderNoteExplorer

All standard Explorer options:

```typescript
FolderNoteExplorer({
  title: "Explorer",
  folderDefaultState: "collapsed",
  folderClickBehavior: "link",
  useSavedState: true,
  sortFn: (a, b) => { /* ... */ },
  filterFn: (node) => { /* ... */ },
  mapFn: (node) => { /* ... */ },
  order: ["filter", "map", "sort"],
})
```

## Tag Shortening Implementation Details

### The `getTagDisplayName` Function

Located in `PageListCustom.tsx` and exported for reuse:

```typescript
export function getTagDisplayName(tag: string): string {
  const segments = tag.split("/")
  return segments[segments.length - 1]
}
```

### Where It's Used

1. **TagListCustom**: Individual content pages
2. **PageListCustom**: Folder and tag listing pages  
3. **RecentNotesCustom**: Recent notes sidebar

### Benefits

- Consistent tag display across all pages
- Cleaner UI with shorter tag names
- Full context available on hover
- Original tag paths preserved for navigation

## Testing

After implementing or updating custom components:

1. **Build**: `npx quartz build`
2. **Serve**: `npx quartz build --serve`
3. **Test**:
   - Individual content pages (TagListCustom)
   - Folder listing pages (PageListCustom via FolderContent)
   - Tag listing pages (PageListCustom via TagContent)
   - Recent notes sidebar (RecentNotesCustom)
   - Verify shortened tags display correctly
   - Verify hover shows full tag path
   - Verify tag links work correctly

## Support

For issues with custom components:
1. Check this documentation
2. Review component source code in `quartz/components/custom/`
3. Verify imports in `quartz.layout.ts`
4. Check browser console for errors
5. Rebuild with `npx quartz build`

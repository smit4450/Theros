/**
 * Folder Note Explorer - Custom Component
 * 
 * This component extends the standard Quartz Explorer with folder-note functionality
 * similar to Obsidian's folder notes feature.
 * 
 * Features:
 * - When a folder contains an index.md or a file matching the folder name (e.g., Compendium/Compendium.md),
 *   clicking the folder name will navigate to that note
 * - A folder-list button (📋 icon) appears on the right side of each folder that always
 *   links to the folder listing page (original behavior)
 * - The folder note file is automatically hidden from the folder's child list to avoid duplication
 * - The folder icon (▼ arrow) still toggles expand/collapse
 * 
 * Usage:
 * In your quartz.layout.ts, import and use:
 * 
 * ```typescript
 * import FolderNoteExplorer from "./quartz/components/custom/FolderNoteExplorer"
 * 
 * export const defaultContentPageLayout: PageLayout = {
 *   left: [
 *     // ... other components
 *     FolderNoteExplorer(),
 *   ],
 *   // ... rest of layout
 * }
 * ```
 * 
 * All standard Explorer options are supported:
 * - title: Title of the explorer
 * - folderDefaultState: "collapsed" | "open"
 * - folderClickBehavior: "collapse" | "link" (default: "link")
 * - useSavedState: Save expand/collapse state in localStorage
 * - sortFn: Custom sort function
 * - filterFn: Custom filter function
 * - mapFn: Custom map function
 */

export { default } from "./FolderNoteExplorer"

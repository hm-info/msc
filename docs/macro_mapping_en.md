---
title: MSC — Macro Mapping
lang: en
pdf: msc-macro-mapping-en.pdf
---

# Macro Mapping

<div class="document-tools" markdown="1">
[Türkçe](macro_mapping_tr.md) · **[Download PDF](downloads/msc-macro-mapping-en.pdf)**
</div>
## MSC

**Date:** December 30, 2025  
**Company:** HAFFNER MAKINE  
**Author:** ERKAN BÜKER

---

## Table of Contents

1. [INTRODUCTION](#1-introduction)
2. [MENU USAGE](#2-menu-usage)
   - 2.1) [ADD MACRO](#21-add-macro)
   - 2.2) [UPDATE MACRO](#22-update-macro)
   - 2.3) [DELETE MACRO](#23-delete-macro)
   - 2.4) [IMPORT](#24-import)
   - 2.5) [EXPORT](#25-export)
   - 2.6) [PROFILE SELECTION](#26-profile-selection)
   - 2.7) [ADD UNIVERSAL MACRO](#27-add-universal-macro)
   - 2.8) [ADD IGNORE OTHERS MACRO](#28-add-ignore-others-macro)
   - 2.9) [ADD REVERSE MACRO](#29-add-reverse-macro)
   - 2.10) [ACTIVE MACRO DEFINITION](#210-active-macro-definition)
   - 2.11) [REVERSE MACRO DEFINITION](#211-reverse-macro-definition)
3. [USAGE](#3-usage)
   - 3.1) [IGNORED MACRO](#31-ignored-macro)
   - 3.2) [SINGLE MACRO IGNORE](#32-single-macro-ignore)
   - 3.3) [ADD REVERSE MACRO](#33-add-reverse-macro)
4. [IMPORT/EXPORT](#4-importexport)

---

## 1) INTRODUCTION

Some adjustments are required to read common job files on different machines. A mapping table is needed to make these adjustments. The mapping table ensures that macros defined differently on different machines are converted correctly for the relevant machine. This makes it possible to operate different machines with a single job file. In addition, different types of macros are used in operations in different directions on the same type of machines. This also ensures that the correct operation is transferred by undergoing conversion through the mapping table.

![Mapping Table Introduction](_media/macro_mapping/1-giris-eslesme-tablosu.png)

---

## 2) MENU USAGE

Descriptions of the objects in the menu are as follows.

![Menu Usage](_media/macro_mapping/2-menu-kullanimi.png)

### 2.1) ADD MACRO

Allows adding macro pairs to the table. Macro information is entered and the desired information is added to the table with the add command.

### 2.2) UPDATE MACRO

Allows updating changes made to the selected macro in the table. A row must be selected from the table for updating. After selection, the relevant information is transferred to the objects in the menu, and if changes are made, the update command updates the relevant cells in the table with the information in the objects.

### 2.3) DELETE MACRO

Allows deletion of an object from the table. The desired row is selected and deletion is performed by running the command.

### 2.4) IMPORT

Allows adding new objects to the table via CSV (UTF-16 LE BOM, TAB-separated) file.

### 2.5) EXPORT

Allows exporting a TAB-separated file in UTF-16 LE BOM format with CSV extension of the objects in the table.

### 2.6) PROFILE SELECTION

If you want to add a profile-specific macro to the table, the relevant profile selection is made here.

### 2.7) ADD UNIVERSAL MACRO

This option is selected when adding a globally defined macro. When this option is selected, profile code selection is hidden. The profile code is added as "0". During matching, mappings are applied to all profiles regardless of profile code. Priority in matching is the profile code. In matches with a profile code, the priority is to perform the match belonging to the profile code. If there is no match for the profile code, global matching is checked.

### 2.8) ADD IGNORE OTHERS MACRO

This option is designed to ignore macros outside the selections. Here, no macro definition is made except for macros with the relevant profile code or globally defined macros. If the ignore option exists, matches without ignore selection are not taken into account.

### 2.9) ADD REVERSE MACRO

In this option, macro matches are only used in the reversed job file. These matches are not used during project loading. During reversal, the X position in all macros is changed according to part length.

### 2.10) ACTIVE MACRO DEFINITION

This is the field where the macro information to be converted is entered.

### 2.11) REVERSE MACRO DEFINITION

This is the field where information about which macro the macro to be converted will convert to is entered. If "0" is entered in this field, the relevant active macro is deleted during matching/loading.

---

## 3) USAGE

### 3.1) IGNORED MACRO

Below are some examples according to the definitions in the table.

![Ignored Macro Example](_media/macro_mapping/3-1-yoksayilacak-makro.png)

#### Example Table 1: Macro with Universal Ignore

| INPUT | PROFILE | RESULT |
|-------|---------|--------|
| H01020100000 | H01010600000 | test | H01060200000 |
| H01050100000 | H01030300000 | test |  |
| H01010100000 | H01010600000 | test2 |  |
| H01020100000 | H01060100000 | test2 | H01060200000 |
| H01020100000 | H01030600000 | test3 | H01060200000 |

**Explanation:**  
Since the table contains macros with universal ignore, all input macros go through control and macros that do not match the table are ignored. Therefore, although there are matching macros in the table above, since ignore has priority, the system only matches macros with "ignore others" selected and deletes external ones. When there is profile-based ignoring, first the profile-internal "ignore others" feature macros are checked, then the universal ones are checked.

---

### 3.2) SINGLE MACRO IGNORE

Below are some examples according to the definitions in the table.

![Single Macro Ignore](_media/macro_mapping/3-2-tek-makro-yoksayma.png)

#### Example Table 2: Single Macro Ignore

| INPUT | PROFILE | RESULT |
|-------|---------|--------|
| H01020100000H01010600000 | test | H01060200000|
| H01050100000H01030300000 | test | |
| H01010100000H01010600000 | test2 | |
| H01020100000H01060100000 | test2 | H01060200000 |
| H01020100000H01030600000 | test3 | H01060200000 |

**Explanation:**  
Since there is no ignore in the table, no macro deletion occurs. To specifically ignore macros, the tool code in the reverse macro definition should be entered as "0". Since the only macro content that matches this definition is in the "test" profile macro definitions, the macro was deleted in only one match belonging to it.

---

### 3.3) ADD REVERSE MACRO

![Reverse Macro Settings](_media/macro_mapping/3-3-terslenecek-makro-ayarlari.png)

For active use of macros with this option selected, the "Reverse Batch File" option must be active in machine settings. When this option is in the off position, the relevant conversion is not used.

![Reverse Macro Example Table](_media/macro_mapping/3-3-terslenecek-makro.png)

#### Example Table 3a: When "Reverse Batch File" Option is OFF

| INPUT | PROFILE | RESULT |
|-------|---------|--------|
| H01020100000H01010600000 | test | H01060200000H01010600000 |
| H01050100000H01030300000 | test | H01050100000H01030300000 |
| H01060100000H01010600000 | test2 | H01060100000H01010600000 |
| H01020100000H01060100000 | test2 | H01010200000H01030300000 |
| H01020100000H01030600000 | test3 | H01060200000H01030600000 |

#### Example Table 3b: When "Reverse Batch File" Option is ON

| INPUT | PROFILE | RESULT |
|-------|---------|--------|
| H01020100000H01060100000 | test | H01060205000H01030205000 |
| H01050100000H01030300000 | test | H01030305000 |
| H01060100000H01010600000 | test2 | H01060105000H01010605000 |
| H01020100000H01060100000 | test2 | H01010205000H01030305000 |
| H01020100000H01030600000 | test3 | H01060205000H01030605000 |

**Explanation:**  
If the option is active in machine settings, matches in the table undergo changes, then the mapping table is activated for reversal. At the same time, the x position is reversed according to part length. In the example tables, part length is taken as 500 units.

---

## 4) IMPORT/EXPORT

If you want to fill the table using Excel or any text editor, you can easily obtain a sample format with the export button.

![Import/Export Screen](_media/macro_mapping/4-ice-disa-aktarim.png)

### File Format

**Import/Export Format:** CSV (UTF-16 LE BOM, TAB-separated)

---

## Technical Summary

### Document Purpose

This guide describes the Mapping Table system for Haffner Makine's MSC machines. The system provides:

- Conversion of macro definitions between different machines
- Use of a single job file on multiple machines
- Processing of different macro types for operations in different directions
- Profile-based and universal macro management
- Import/export functionality for batch operations

### Key Features

1. **Profile-Based Mapping:** Allows machine-specific macro conversions
2. **Universal Macros:** Global definitions applicable to all profiles
3. **Ignore Function:** Selective macro processing with ignore rules
4. **Reverse Macros:** Special processing for reversed job files with X-position transformation
5. **Import/Export:** CSV UTF-16 LE BOM format support

### Workflow Priorities

1. Profile-specific mappings take priority
2. If no profile match exists, universal (global) mappings are checked
3. Ignore rules have the highest priority when active
4. Reverse batch file option must be enabled for reverse macro functionality

---

## Image Directory

All images used in this document are located in the `_media/macro_mapping/` folder:

- `1-giris-eslesme-tablosu.png` - Introduction screen
- `2-menu-kullanimi.png` - Menu usage interface
- `3-1-yoksayilacak-makro.png` - Ignored macro example
- `3-2-tek-makro-yoksayma.png` - Single macro ignore table
- `3-3-terslenecek-makro-ayarlari.png` - Reverse macro settings screen
- `3-3-terslenecek-makro.png` - Reverse macro example table
- `4-ice-disa-aktarim.png` - Import/Export screen

Total **7 images** used (19 images extracted from PDF, relevant ones selected).

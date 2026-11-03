---
title: SC220-40 / SC220-80 — Job File Guide
lang: en
pdf: msc-sc220-job-file-en.pdf
---

# SC220-40 / SC220-80 — Job File Guide

<div class="document-tools" markdown="1">
[Türkçe](sc220_job_file_tr.md) · **[Download PDF](downloads/msc-sc220-job-file-en.pdf)**
</div>

This guide describes the job file of **SC220-40 and SC220-80 machines with the MSC interface**. The file layout is **identical to the NR241 job file**; the only difference is the structure of the **operation / macro block** in the `nccode` field.

## File fields

The file has the same **30 columns** as NR241:

```text
id;ksn;ksnbar;ktn;ktnbar;l;r;code;info;width;height;trolley;box;orientation;reinf;reinfbar;pos;prono;offno;agent;customer;date;nccode;isfix;colorcode;colorinfo;mainprofile;subcust;image;DATA1
```

For field meanings, bar and part sequence, and length and angle notation, see the [NR241 / NR242 / NR210 guide](nr_job_file_en.md). In short:

- Each data row is one part to be cut; rows with the same `ksn` value are cut from the same bar.
- In `ksnbar` and `ktnbar`, the last digit is the decimal: `4710` = **471.0 mm**.
- `l` and `r` are the start and end cutting angles, written as a single number (`45`, `135`).
- If a field is empty, keep its column position; do not shift the following values to the left.

## `nccode` — operation / macro field

On SC220 machines each operation is a **12-character** block. If a part has more than one operation, the blocks are written one after another.

```text
H | 02 | 01 | 01 | 05000
```

The vertical bars are for explanation only; they are not part of the field.

| Part | Character position | Length | Description |
|---|---|---:|---|
| `H` | 1 | 1 | Block start character |
| `02` | 2–3 | 2 | Tool code |
| `01` | 4–5 | 2 | Operation code |
| `01` | 6–7 | 2 | Accessory code |
| `05000` | 8–12 | 5 | Operation position; the last digit is the decimal: **500.0 mm** |

The full block for this example:

```text
H02010105000
```

Keep leading zeros: write Tool `02`, not `2`, and position `05000`, not `5000`.

### Difference from NR241

| | NR241 / NR242 / NR210 | SC220-40 / SC220-80 |
|---|---|---|
| Block length | 18 characters | **12 characters** |
| Tool code | 3 digits (`002`) | **2 digits** (`02`) |
| Operation / Accessory | 2 + 2 digits | 2 + 2 digits |
| Position | 5 digits, 0.1 mm | 5 digits, 0.1 mm |
| Slot length | 5 digits | **None** |

The same operation in both formats:

```text
NR241 : H00201010500001000
SC220 : H02010105000
```

Do not import an NR-format `nccode` field into an SC220 machine as is; the blocks will be read incorrectly.

### Hole example

```text
H16010110000
```

Tool **`16`**, Operation **`01`**, Accessory **`01`**; position **1000.0 mm**.

### Several operations on one part

```text
H02010105000H16010110000
```

Two 12-character blocks, **24 characters** in total. Blocks are split at the `H` character, so `H` must not appear inside a block.

If a block is shorter than 12 characters or contains non-numeric characters, the machine cannot read **any operation** of that part. The operations will be missing even if the cutting lengths are correct.

These codes are examples, not a universal operation code list for every profile and machine. Check what each operation code means on your machine together with [Macro Mapping](macro_mapping_en.md) and the profile's operation definitions.

## Example file

[Download the 30-column SC220 example CSV](downloads/SC220_Job_Example.csv)

Dealer, customer, order, profile and image path values in the example are fictitious. The separator is `;`. Match it to your machine's profile, operation and import settings before production.

## Before importing

1. Compare the column headers and the number of fields per row with the NR241 layout.
2. Check bar numbers, part sequence within each bar, bar / part lengths and cutting angles.
3. Check that `nccode` blocks are **12 characters** and the Tool code is written with **2 digits**; keep leading zeros.
4. Make sure the file was not prepared in NR format (18-character blocks).
5. After importing, check the lengths and operation view in the part list.

[MSC home page](home-en.md) · [NR241 / NR242 / NR210](nr_job_file_en.md) · [Macro Mapping](macro_mapping_en.md)

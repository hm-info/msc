# NR241 / NR242 / NR210 — Job File Guide

[Türkçe](nr_job_file_tr.md)

This guide describes the job file used by **NR241, NR242, NR210 and variants using this format with the MSC interface**. Field definitions come from `NR24X- job file description.xlsx`. Each data row represents one part to be cut; rows with the same bar number represent parts produced from the same bar.

**These machines use `nccode`:** it carries machining information such as holes, drainage and slots. The “macros are not used” guidance for TT machines with the HMS_W interface does not apply to the NR machines covered here.

## File fields

The reference document contains **30 columns**:

```text
id;ksn;ksnbar;ktn;ktnbar;l;r;code;info;width;height;trolley;box;orientation;reinf;reinfbar;pos;prono;offno;agent;customer;date;nccode;isfix;colorcode;colorinfo;mainprofile;subcust;image;DATA1
```

This illustration uses `;` as the separator. Match the separator and numeric format to the machine's import settings. The Excel document describes the fields; it does not define every machine's import configuration. When a value is empty, preserve its column position rather than shifting later values to the left.

Fields marked **Machine** below are marked with `>` as related to machine operation in the source document. This is not a list of mandatory columns. **Label / extra information** fields describe order tracking and label content; their use depends on the machine and label configuration.

| Field | Use | Description |
|---|---|---|
| `id` | Machine | Part identifier; increases through the job file. |
| `ksn` | Machine | Bar number. Rows sharing the same value are cut from the same bar. |
| `ksnbar` | Machine | Bar length. The last digit is the decimal place: `59800` = **5980.0 mm**. |
| `ktn` | Machine | Part sequence within the same bar. |
| `ktnbar` | Machine | Cut part length. The last digit is the decimal place: `4710` = **471.0 mm**. |
| `l` | Machine | Cutting angle at the start of the part; `45` in the source example. |
| `r` | Machine | Cutting angle at the end of the part; `135` in the source example. |
| `code` | Machine | Profile / bar code for the part. |
| `info` | Label / extra information | Profile or bar description. |
| `width` | Label / extra information | Window / frame width. |
| `height` | Label / extra information | Window / frame height. |
| `trolley` | Label / extra information | Trolley number for the part. |
| `box` | Label / extra information | Box / compartment number on the trolley. |
| `orientation` | Label / extra information | Part location in the frame, such as top, bottom, right or left. |
| `reinf` | Label / extra information | Reinforcement code. |
| `reinfbar` | Label / extra information | Reinforcement length. |
| `pos` | Label / extra information | Window / position number; parts of the same window share the value. |
| `prono` | Label / extra information | Production number. |
| `offno` | Label / extra information | Contract number. |
| `agent` | Label / extra information | Dealer / distributor information. |
| `customer` | Label / extra information | Customer information. |
| `date` | Label / extra information | Date information; check its representation with the system creating the file. |
| `nccode` | **Machine** | **Machining / macro information.** One or more 18-character operation blocks. |
| `isfix` | Label / extra information | The source example contains `0`; its function is not separately explained. |
| `colorcode` | Label / extra information | Colour code. |
| `colorinfo` | Label / extra information | Colour description. |
| `mainprofile` | Machine | Main profile / bar code. |
| `subcust` | Label / extra information | Additional customer information. |
| `image` | Label / extra information | Path to the image printed on the label. |
| `DATA1` | Label / extra information | Additional information that may be printed on the label. |

`agent` is a separate column. Do not confuse this 30-column file with other SC examples that omit it. The Excel document does not provide a detailed colour-code table, so another machine's colour mapping should not be applied directly.

## Bar and part sequence

| `id` | `ksn` | `ktn` | Meaning |
|---:|---:|---:|---|
| 1 | 1 | 1 | First part of the first bar |
| 2 | 1 | 2 | Second part of the first bar |
| 3 | 2 | 1 | First part of the second bar |

`id` identifies the part across the file. `ktn` identifies its sequence within a bar. In the reference sample, bar 1 contains four parts and bar 2 contains five parts.

## Length and angle notation

- `ksnbar = 59800` → **5980.0 mm** bar length.
- `ktnbar = 4710` → **471.0 mm** part length.
- `l = 45`, `r = 135` → start and end cutting angles.

The source defines the final digit as the decimal place for `ksnbar` and `ktnbar`. Do not automatically extend this rule to `width`, `height` or `reinfbar`. The angle examples here are single numbers; do not replace them with the `45|90` notation from HMS_W SC examples.

## `nccode` — machining / macro field

Each operation is an **18-character** block. For multiple operations on the same part, concatenate the blocks.

```text
H0 | 020101 | 05000 | 01000
```

Vertical bars are explanatory and are not part of the actual field.

| Section | Character positions | Length | Meaning |
|---|---|---:|---|
| `H0` | 1–2 | 2 | Fixed prefix |
| `020101` | 3–8 | 6 | Operation type / code |
| `05000` | 9–13 | 5 | Operation position: **500.0 mm** |
| `01000` | 14–18 | 5 | Slot length: **100.0 mm** |

### Drainage / slot example

```text
H00201010500001000
```

Operation type `020101` has position **500.0 mm** and slot length **100.0 mm**. For drainage or a slot, the position indicates the **start of the operation**.

### Hole example

```text
H01601011000000000
```

Operation type `160101` has position **1000.0 mm**. The last five digits are `00000`, so there is no slot length. In this non-drainage / non-slot example, the position indicates the **hole centre**.

### Multiple operations on the same part

```text
H00201010500001000H01601011000000000
```

This field contains two 18-character blocks, **36 characters** in total. The first describes drainage / a slot; the second describes a hole. Interpret the position according to the operation type.

These codes are examples from the reference document, not a universal operation list for every profile and machine. Check the code's machine operation against [Macro Mapping](macro_mapping_en.md) and the profile's operation definitions. Correct cutting lengths alone are not enough: an empty or incorrect `nccode` can leave required operations missing.

## Illustrative file

[Download the 30-column example CSV](downloads/NR_Series_Job_Example.csv)

Dealer, customer, order, profile and image-path values are fictitious. The separator is `;`. This example illustrates the fields; match it to your own machine's profile, machining and import settings before production.

## Checks before import

1. Confirm that the file uses the NR job-file layout prepared for your machine.
2. Compare the headers and field count in every row; empty fields must not shift later values.
3. Check bar numbers, part sequence within each bar, bar / part lengths and cutting angles.
4. Verify that profile and main-profile codes match the correct machine definitions.
5. Check the 18-character `nccode` blocks, operation codes, positions and slot lengths where applicable. Preserve leading zeros.
6. After import, review the part lengths and machining display.

[MSC home](index.md) · [Macro Mapping](macro_mapping_en.md) · [Profile Definitions](profile_definitions_en.md)

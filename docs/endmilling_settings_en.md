---
title: MSC — End Milling Settings
lang: en
pdf: msc-endmilling-settings-en.pdf
---

# End Milling Settings

<div class="document-tools" markdown="1">
[Türkçe](endmilling_settings_tr.md) · **[Download PDF](downloads/msc-endmilling-settings-en.pdf)**
</div>

## PLC

**I.** The end milling axis, namely `1K1`, is a homed axis.

**II.** Required options are activated.

_(* PLC → GV_Definitons.exp *)_

- `C_OPTION_END_MILLING` (* End milling option in the machine *)
- `C_REVERSE_ENDMILLING` (* End milling blade reverse *)
- `C_ENDMILLING_BLADE_COMPRESS_SENSOR` (* End milling blade compression sensor option *)

## MSC

**I.** Required parameters for end milling positioning must be set.

_(* Parameters → Cutting Station *)_

- `stKaliciData.PosLmtMin_1K1`
- `stKaliciData.PosLmtMax_1K1`
  - _(* 1K1 limits are changed from persistent data, limits cannot be changed from TSM program. *)_
  - _(* Max. limit position should be set so that the End Milling Forward Sensor will not detect it. *)_
- `stKaliciData.fKertmeOffset`
  - _(* Offset value used for the profile to reach the end milling position *)_
- `stKaliciData.fKertmeCenterPosition`
  - _(* Position where the end milling blade passes through the zero point of the table *)_
- `stKaliciData.fKertmeProfilGenislik`
  - _(* Maximum width dimension of the profiles to be end milled *)_
- `stKaliciData.fKertmeBicakCap`
  - _(* Diameter of the large blade in end milling *)_
- `stKaliciData.fKertmeTolerans`
  - _(* Blade clearance value from the profile after end milling operation *)_
- `stKaliciData.fKertmeMaxVelocity`
- `stKaliciData.fKertmeMidVelocity`
- `stKaliciData.fKertmeSlowVelocity`

**II.** If `Tool23` and `Tool24` do not exist in the tool page, they are added to the database. _(* Master → DBMaster.mdb *)_

![image001](_media/endmilling/image001.png)

**III.** In profile definitions, the **end milling column** and **end milling step (0,1,2)** are selected for the desired profile.

![image003](_media/endmilling/image003.png)
_(* Profiles and Macros → Profile Definitions *)_

**IV.** End milling macros are defined. Select `Tool23` for part start; select `Tool24` for part end.

![image005](_media/endmilling/image005.png)
_(* Profiles and Macros → Macro Definitions *)_

**V.** End milling macros to be processed are defined for the profile to be end milled.

![image007](_media/endmilling/image007.png)
_(* Profiles and Macros → Profile-Macro Definitions *)_

**VI.** In the work file, `H043` must be used for part start and `H044` for part end.

![image009](_media/endmilling/image009.png)

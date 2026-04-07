[[_TOC_]]

# MSC_V2X Manual English

## 5. Profile Definitions

### 5.r. Profile Working Mode (Prf. Working Mode)

This column accepts numeric data. This data is used by dividing it into bits on the PLC side. The decimal (Dec) values of the operations to be used together are added and written to the column.


| Bit | Dec | Description                                           | SC220_80 plcvar                       |
| --- | --- | ----------------------------------------------------- | ------------------------------------- |
| 0   | 1   | *cancelled*                                           | *cancelled*                           |
| 1   | 2   | *cancelled*                                           | *cancelled*                           |
| 2   | 4   | *cancelled*                                           | *cancelled*                           |
| 3   | 8   | Unloading holder rear support clamp forward           | bBosaltmaTutucuArkaDayamaPistonuAktif |
| 4   | 16  | Feeding holder works vertically                       | bTutucu90DerecedeCalis                |
| 5   | 32  | Do not use loading side clamps while profile sliding | bYuklemeGrubuYanBaskilarSurmedeKapali |


### 5.t. Loading Clamp Mode (LoadClampModes)

This column takes values from the drop-down list. It changes the clamping scenarios of the clamps at the loading station.

| Option | Description                                              | SC220_80 plcvar                   |
| ------ | -------------------------------------------------------- | --------------------------------- |
| 0      | Description                                              |                                   |
| 2      | Loading station clamps **vertical clamps first**         | bYuklemeGrubuUstBaskilarOncelikli |
| 3      | Loading station ??????                                   | bProfilDesteklemeAktif            |
| 4      | Loading station profile straightening is activated first | bProfilDikmeAktif                 |



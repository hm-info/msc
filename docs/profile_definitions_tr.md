---
title: MSC — Profil Tanımları
lang: tr
pdf: msc-profile-definitions-tr.pdf
---

# MSC_V2X Manual Türkçe

<div class="document-tools" markdown="1">
[English](profile_definitions_en.md) · **[PDF indir](downloads/msc-profile-definitions-tr.pdf)**
</div>

## 5. Profil Tanımları

### 5.r. Profil Çalışma Modu (Prf. Çalışma Modu)

Bu sütun numerik veri alır. Bu veriler PLC tarafında bitlerine ayrılarak kullanılır. Ortak kullanılacak çalışmaların decimal(Dec) değerleri toplanarak sütuna yazılır.


| Bit | Dec |Açıklama                                        | SC220_80 plcvar                       |
| --- | --- |----------------------------------------------- | ------------------------------------- |
| 0   | 1   | *iptal*                                        | *iptal*                               |
| 1   | 2   | *iptal*                                        | *iptal*                               |
| 2   | 4   | *iptal*                                        | *iptal*                               |
| 3   | 8   | Boşaltma tutucudaki dayama baskı ileri         | bBosaltmaTutucuArkaDayamaPistonuAktif |
| 4   | 16  | Besleme Tutucu dik olarak çalışsın             | bTutucu90DerecedeCalis                |
| 5   | 32  | Yükleme yan baskıları profil sürerken kullanma | bYuklemeGrubuYanBaskilarSurmedeKapali |


### 5.t. Yükleme Baskı Modu (LoadClampModes)

Bu sütun aşağı açılan listeden değer alır. Yükleme istasyonundaki baskıların basma senaryolarını değiştirir.

| Option | Açıklama                                          | SC220_80 plcvar                   |
| ------ | ------------------------------------------------- | --------------------------------- |
| 0      | Açıklama                                          |                                   |
| 2      | Yükleme istasyonu **önce dikey baskılar** basar   | bYuklemeGrubuUstBaskilarOncelikli |
| 3      | Yükleme istasyonu ??????                          | bProfilDesteklemeAktif            |
| 4      | Yükleme istasyonu önce profili dikleme aktif olur | bProfilDikmeAktif                 |


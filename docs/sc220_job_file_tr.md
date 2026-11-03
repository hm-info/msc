---
title: SC220-40 / SC220-80 — İş Dosyası Rehberi
lang: tr
pdf: msc-sc220-job-file-tr.pdf
---

# SC220-40 / SC220-80 — İş Dosyası Rehberi

<div class="document-tools" markdown="1">
[English](sc220_job_file_en.md) · **[PDF indir](downloads/msc-sc220-job-file-tr.pdf)**
</div>

Bu rehber, **MSC arayüzü kullanılan SC220-40 ve SC220-80** makinelerinin iş dosyasını açıklar. Dosya düzeni **NR241 iş dosyasıyla birebir aynıdır**; tek fark `nccode` alanındaki **işlem / makro bloğunun yapısıdır**.

## Dosyanın alanları

Dosyada NR241 ile aynı **30 sütun** bulunur:

```text
id;ksn;ksnbar;ktn;ktnbar;l;r;code;info;width;height;trolley;box;orientation;reinf;reinfbar;pos;prono;offno;agent;customer;date;nccode;isfix;colorcode;colorinfo;mainprofile;subcust;image;DATA1
```

Alanların anlamı, çubuk ve parça sırası, boy ve açı gösterimi için [NR241 / NR242 / NR210 rehberine](nr_job_file_tr.md) bakın. Kısaca:

- Her veri satırı bir kesilecek parçadır; aynı `ksn` değerini taşıyan satırlar aynı çubuktan kesilir.
- `ksnbar` ve `ktnbar` değerlerinde son hane ondalıktır: `4710` = **471,0 mm**.
- `l` ve `r` başlangıç ve bitiş kesim açılarıdır; tek sayı olarak yazılır (`45`, `135`).
- Bir alan boşsa o sütunun yerini koruyun; sonraki verileri sola kaydırmayın.

## `nccode` — işlem / makro alanı

SC220 makinelerinde her işlem **12 karakterlik** bir bloktur. Aynı parçada birden fazla işlem varsa bloklar art arda yazılır.

```text
H | 02 | 01 | 01 | 05000
```

Dikey çizgiler yalnız açıklama içindir; gerçek alanda bulunmaz.

| Bölüm | Karakter sırası | Uzunluk | Açıklama |
|---|---|---:|---|
| `H` | 1 | 1 | Blok başlangıç karakteri |
| `02` | 2–3 | 2 | Tool kodu |
| `01` | 4–5 | 2 | Operasyon kodu |
| `01` | 6–7 | 2 | Aksesuar kodu |
| `05000` | 8–12 | 5 | İşlem konumu; son hane ondalıktır: **500,0 mm** |

Bu örneğin tam gösterimi:

```text
H02010105000
```

Baştaki sıfırları koruyun: Tool `2` değil `02`, konum `5000` değil `05000` yazılır.

### NR241 ile farkı

| | NR241 / NR242 / NR210 | SC220-40 / SC220-80 |
|---|---|---|
| Blok uzunluğu | 18 karakter | **12 karakter** |
| Tool kodu | 3 hane (`002`) | **2 hane** (`02`) |
| Operasyon / Aksesuar | 2 + 2 hane | 2 + 2 hane |
| Konum | 5 hane, 0,1 mm | 5 hane, 0,1 mm |
| Kanal boyu | 5 hane | **Yok** |

Aynı işlem iki biçimde şöyle yazılır:

```text
NR241 : H00201010500001000
SC220 : H02010105000
```

NR biçimindeki bir `nccode` alanını SC220 makinesine olduğu gibi aktarmayın; bloklar yanlış okunur.

### Delik örneği

```text
H16010110000
```

Tool **`16`**, Operasyon **`01`**, Aksesuar **`01`**; konum **1000,0 mm**.

### Aynı parçada birden fazla işlem

```text
H02010105000H16010110000
```

İki adet 12 karakterlik blok, toplam **24 karakter**. Bloklar `H` karakterinden ayrılır; bu yüzden blok içinde `H` kullanılmaz.

Bir blok 12 karakterden kısa veya sayısal olmayan karakter içeriyorsa makine o parçanın **hiçbir işlemini** okuyamaz. Kesim boyları doğru olsa bile işlemler eksik kalır.

Bu kodlar örnektir; her profil ve makine için evrensel bir işlem kodu listesi değildir. İşlem kodunun makinedeki karşılığını [Makro Eşleştirme](macro_mapping_tr.md) ve profilin işlem tanımlarıyla birlikte kontrol edin.

## Temsili dosya

[30 sütunlu SC220 örnek CSV'sini indir](downloads/SC220_Job_Example.csv)

Örnekte bayi, müşteri, sipariş, profil ve görsel yolu temsili değerlerdir. Ayırıcı `;` kullanılmıştır. Üretimden önce kendi makinenizin profil, işlem ve aktarım ayarlarıyla eşleştirin.

## Aktarımdan önce kontrol

1. Sütun başlıklarını ve satırlardaki alan sayısını NR241 düzeniyle karşılaştırın.
2. Çubuk numarası, çubuk içi parça sırası, çubuk / parça boyları ve kesim açılarını kontrol edin.
3. `nccode` bloklarının **12 karakter** olduğunu ve Tool kodunun **2 hane** yazıldığını kontrol edin; baştaki sıfırları koruyun.
4. Dosyanın NR biçiminde (18 karakterlik bloklar) hazırlanmadığından emin olun.
5. Aktarımdan sonra parça listesinde boyları ve işlem görünümünü kontrol edin.

[MSC ana sayfası](index.md) · [NR241 / NR242 / NR210](nr_job_file_tr.md) · [Makro Eşleştirme](macro_mapping_tr.md)

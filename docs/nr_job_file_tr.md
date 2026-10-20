---
title: NR241 / NR242 / NR210 — İş Dosyası Rehberi
lang: tr
pdf: msc-nr-job-file-tr.pdf
---

# NR241 / NR242 / NR210 — İş Dosyası Rehberi

<div class="document-tools" markdown="1">
[English](nr_job_file_en.md) · **[PDF indir](downloads/msc-nr-job-file-tr.pdf)**
</div>

Bu rehber, **MSC arayüzü kullanılan NR241, NR242, NR210 ve bu formatı kullanan varyasyonlarının** iş dosyasını açıklar. Referans, `NR24X- job file description.xlsx` belgesindeki alan tanımlarıdır. Her veri satırı bir kesilecek parçayı, aynı çubuk numarasını taşıyan satırlar ise aynı çubuktan üretilecek parçaları temsil eder.

**Bu makinelerde `nccode` kullanılır:** delik, su tahliye ve kanal gibi işlemlerin bilgileri bu alanda taşınır. HMS_W arayüzlü TT makinelerine ait “makro kullanılmaz” açıklaması bu rehberin kapsamındaki NR makinelerine uygulanmaz.

## Dosyanın alanları

Referans belgede **30 sütun** bulunur:

```text
id;ksn;ksnbar;ktn;ktnbar;l;r;code;info;width;height;trolley;box;orientation;reinf;reinfbar;pos;prono;offno;agent;customer;date;nccode;isfix;colorcode;colorinfo;mainprofile;subcust;image;DATA1
```

Bu gösterimde alanlar `;` ile ayrılmıştır. Dosya aktarımında makinenin kullandığı ayırıcı ve sayı biçimiyle uyumlu olun. Excel belgesi alanları açıklar; tek başına her makinenin dosya aktarım ayarlarını tanımlamaz. Bir alan boşsa o sütunun yerini koruyun ve sonraki verileri sola kaydırmayın.

Tabloda **Makine** olarak işaretlenen alanlar, kaynak belgede `>` ile makine çalışmasıyla ilişkili gösterilir. Bu işaret bir “zorunlu sütun” listesi değildir. **Etiket / ek bilgi** alanları sipariş takibi ve etiket içeriği için açıklanır; hangi ek alanların kullanılacağı makine ve etiket düzenine bağlıdır.

| Alan | Kullanım | Açıklama |
|---|---|---|
| `id` | Makine | Parça kimliği; dosyanın sonuna kadar artan parça numarası. |
| `ksn` | Makine | Çubuk numarası. Aynı değerli satırlar aynı çubuktan kesilir. |
| `ksnbar` | Makine | Çubuk boyu. Son hane ondalıktır: `59800` = **5980,0 mm**. |
| `ktn` | Makine | Parçanın aynı çubuk içindeki sırası. |
| `ktnbar` | Makine | Kesilecek parça boyu. Son hane ondalıktır: `4710` = **471,0 mm**. |
| `l` | Makine | Parçanın başlangıç kesim açısı; kaynak örnekte `45`. |
| `r` | Makine | Parçanın bitiş kesim açısı; kaynak örnekte `135`. |
| `code` | Makine | Parçanın profil / çubuk kodu. |
| `info` | Etiket / ek bilgi | Profil veya çubuk hakkında açıklama. |
| `width` | Etiket / ek bilgi | Pencere / çerçeve genişliği. |
| `height` | Etiket / ek bilgi | Pencere / çerçeve yüksekliği. |
| `trolley` | Etiket / ek bilgi | Parçanın konulacağı araba numarası. |
| `box` | Etiket / ek bilgi | Araba içindeki göz / kutu numarası. |
| `orientation` | Etiket / ek bilgi | Parçanın çerçevedeki konumu; örneğin üst, alt, sağ veya sol. |
| `reinf` | Etiket / ek bilgi | Destek sacı kodu. |
| `reinfbar` | Etiket / ek bilgi | Destek sacı boyu. |
| `pos` | Etiket / ek bilgi | Pencere / pozisyon numarası; aynı pencerenin parçaları aynı değeri alır. |
| `prono` | Etiket / ek bilgi | Üretim numarası. |
| `offno` | Etiket / ek bilgi | Sözleşme numarası. |
| `agent` | Etiket / ek bilgi | Bayi / dağıtıcı bilgisi. |
| `customer` | Etiket / ek bilgi | Müşteri bilgisi. |
| `date` | Etiket / ek bilgi | Tarih bilgisi; gösterim biçimini dosyayı hazırlayan sistemle birlikte kontrol edin. |
| `nccode` | **Makine** | **İşlem / makro bilgisi.** Bir veya birden fazla 18 karakterlik işlem bloğu. |
| `isfix` | Etiket / ek bilgi | Kaynak örnekte `0` bulunur; belgede işlevi ayrıca açıklanmamıştır. |
| `colorcode` | Etiket / ek bilgi | Renk kodu. |
| `colorinfo` | Etiket / ek bilgi | Renk açıklaması. |
| `mainprofile` | Makine | Ana profil / çubuk kodu. |
| `subcust` | Etiket / ek bilgi | İlave müşteri bilgisi. |
| `image` | Etiket / ek bilgi | Etikette basılacak görselin dosya yolu. |
| `DATA1` | Etiket / ek bilgi | Etikette basılabilecek ilave bilgi. |

`agent` ayrı bir sütundur; bu alanın bulunmadığı başka SC tipi örnekleri bu 30 sütunlu dosyayla karıştırmayın. Renk kodlarının anlamı bu Excel belgesinde ayrıntılı verilmediği için başka bir makinenin renk tablosu doğrudan uygulanmamalıdır.

## Çubuk ve parça sırası

| `id` | `ksn` | `ktn` | Anlamı |
|---:|---:|---:|---|
| 1 | 1 | 1 | Birinci çubuğun birinci parçası |
| 2 | 1 | 2 | Birinci çubuğun ikinci parçası |
| 3 | 2 | 1 | İkinci çubuğun birinci parçası |

`id` dosya genelindeki parça numarasıdır. `ktn`, yeni bir çubuğa geçildiğinde o çubuk içindeki parça sırasını gösterir. Referans örnekte birinci çubuk 4, ikinci çubuk 5 parça içerir.

## Boy ve açı gösterimi

- `ksnbar = 59800` → **5980,0 mm** çubuk boyu.
- `ktnbar = 4710` → **471,0 mm** parça boyu.
- `l = 45`, `r = 135` → başlangıç ve bitiş kesim açıları.

Kaynak belge son hanenin ondalık olduğu kuralını `ksnbar` ve `ktnbar` için açıklar. `width`, `height` ve `reinfbar` alanlarına aynı ölçek otomatik olarak genellenmemelidir. Buradaki açı örnekleri tek sayıdır; HMS_W SC örneklerindeki `45|90` biçimiyle değiştirmeyin.

## `nccode` — işlem / makro alanı

Her işlem **18 karakterlik** bir bloktur. Aynı parçada birden fazla işlem varsa bloklar art arda yazılır.

```text
H | 001 | 02 | 03 | 05000 | 01000
```

Dikey çizgiler yalnız açıklama içindir; gerçek alanda bulunmaz.

| Bölüm | Karakter sırası | Uzunluk | Açıklama |
|---|---|---:|---|
| `H` | 1 | 1 | Sabit makro başlangıç karakteri |
| `001` | 2–4 | 3 | Tool kodu |
| `02` | 5–6 | 2 | Operasyon kodu |
| `03` | 7–8 | 2 | Aksesuar kodu |
| `05000` | 9–13 | 5 | İşlem konumu: **500,0 mm** |
| `01000` | 14–18 | 5 | Kanal boyu: **100,0 mm** |

İlk 8 karakter olan **`H0010203`**, `H` + Tool `001` + Operasyon `02` + Aksesuar `03` olarak okunur. Baştaki sıfırları koruyun. Bu örneğin tam 18 karakterlik gösterimi:

```text
H00102030500001000
```

Sabit olan başlangıç yalnızca **`H`** karakteridir; sonraki `0`, üç haneli Tool kodunun parçasıdır. Sonraki 10 hane, 5 haneli konum ve 5 haneli kanal boyundan oluşur.

### Su tahliye / kanal örneği

```text
H00201010500001000
```

Bu örnekte Tool **`002`**, Operasyon **`01`**, Aksesuar **`01`**; konum **500,0 mm**, kanal boyu **100,0 mm**'dir. Su tahliye veya kanal işleminde konum, **işlemin başlangıç konumunu** gösterir.

### Delik örneği

```text
H01601011000000000
```

Bu örnekte Tool **`016`**, Operasyon **`01`**, Aksesuar **`01`**; konum **1000,0 mm**'dir. Son beş hane `00000` olduğundan kanal boyu yoktur. Su tahliye / kanal olmayan bu örnekte konum, **delik merkezini** gösterir.

### Aynı parçada birden fazla işlem

```text
H00201010500001000H01601011000000000
```

Bu alan iki adet 18 karakterlik bloktan, toplam **36 karakterden** oluşur. İlk blok kanal / su tahliye işlemini, ikinci blok deliği tanımlar. Başlangıç ve bitiş konumu yorumunu işlem tipine göre yapın.

Bu kodlar referans belgenin örnekleridir; her profil ve makine için evrensel bir işlem kodu listesi değildir. İşlem kodunun makinedeki karşılığını [Makro Eşleştirme](macro_mapping_tr.md) ve profilin işlem tanımlarıyla birlikte kontrol edin. Kesim boyları doğru olsa bile `nccode` boş veya yanlışsa istenen işlemler eksik kalabilir.

## Temsili dosya

[30 sütunlu örnek CSV'yi indir](downloads/NR_Series_Job_Example.csv)

Örnekte bayi, müşteri, sipariş, profil ve görsel yolu temsili değerlerdir. Ayırıcı `;` kullanılmıştır. Dosya alanları göstermek içindir; üretimden önce kendi makinenizin profil, işlem ve aktarım ayarlarıyla eşleştirin.

## Aktarımdan önce kontrol

1. Dosyanın makineniz için hazırlanan NR iş dosyası düzenini kullandığını kontrol edin.
2. Sütun başlıklarını ve satırlardaki alan sayısını karşılaştırın; boş alanlar sonraki sütunları kaydırmamalıdır.
3. Çubuk numarası, çubuk içi parça sırası, çubuk / parça boyları ve kesim açılarını kontrol edin.
4. Profil ve ana profil kodlarının makinede doğru tanımlarla eşleştiğini doğrulayın.
5. `nccode` bloklarının 18 karakterlik yapısını, Tool / Operasyon / Aksesuar kodlarını, konumunu ve gerekiyorsa kanal boyunu kontrol edin; baştaki sıfırları koruyun.
6. Aktarımdan sonra parça listesinde boyları ve işlem görünümünü kontrol edin.

[MSC ana sayfası](index.md) · [Makro Eşleştirme](macro_mapping_tr.md) · [Profil Tanımları](profile_definitions_tr.md)

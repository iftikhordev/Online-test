# 🎓 Online Test Platformasi

Professional, ishlab chiqarishga tayyor, bitta `index.html` faylida joylashgan web-based test platformasi. To'liq O'zbek tilida.

> **Iftikhor Software Solutions Inc.** — © 2026 All Rights Reserved

---

## 📊 Savollar bazasi

Savollar 3 ta Word hujjatidan avtomatik ajratib olingan (`extract.py` skripti orqali):

| Fan | Savollar soni |
|-----|:---:|
| Turizm loyihasini boshqarish | 95 |
| Menejmentga kirish | 99 |
| Madaniyatlararo muloqot | 98 |
| **Jami** | **292** |

> **Eslatma:** Word hujjatlarda taxminan 500 savol ko'zlangan bo'lsa-da, ayrim bo'limlar
> ("51–70 savollar shu formatda davom etadi…" kabi) to'ldirilmagan joy egallovchilar edi.
> Shu sababli barcha **292 ta to'liq, haqiqiy savol** ajratib olindi. Har bir test shu
> bankdan **200 ta tasodifiy savol** tanlaydi.

---

## ✨ Asosiy funksiyalar

### 🎯 Test tizimi
- 292 ta savoldan iborat bank, har testda **200 ta tasodifiy** savol
- Har safar yangi, **dublikatsiz** tasodifiy to'plam (Fisher–Yates aralashtirish)
- To'g'ri javob avtomatik **A, B, C, D** orasida aralashtiriladi (manbada doim A edi)
- **Kategoriya (fan) filtri** — barcha fanlar yoki bitta fan bo'yicha test
- **Savol bo'yicha vaqt cheklovi:** har bir savolga **60 soniya** (SVG halqali taymer).
  Vaqt tugaganda savol qulflanadi va avtomatik keyingi savolga o'tadi
- Umumiy vaqt hisoblagichi

### 🧭 Navigatsiya va boshqaruv
- Oldingi / Keyingi / Savolga sakrash (jump)
- Savollar bo'yicha **qidiruv**
- Savolni **belgilash** (review uchun)
- Javob berilgan / belgilangan / vaqti tugagan / bo'sh holatlar uchun rangli indikatorlar
- Yakunlashdan oldin **ko'rib chiqish (review)** oynasi

### 🎨 Dizayn / UX
- **Day/Night** (kunduzgi/tungi) rejim, `localStorage`da saqlanadi, silliq o'tish
- **Glassmorphism** effektlari, elegant gradientlar
- Mobile / Tablet / Desktop **responsive**
- TailwindCSS + Font Awesome

### 📈 Natijalar va tahlil
- Umumiy ball, foiz, to'g'ri/noto'g'ri javoblar, sarflangan vaqt
- **Chart.js** grafiklari: To'g'ri/Noto'g'ri (doughnut), Foiz (gauge), Fanlar bo'yicha (bar)
- Baholash va tavsiyalar (90/75/60% chegaralari bo'yicha)
- **PDF eksport** (jsPDF + AutoTable) va **Chop etish** (print)

### 🎉 Tabriklash effekti
- Natija **≥ 90%** bo'lsa to'liq ekranli tantana: konfetti + otashinlar
- "Tabriklaymiz, [Ism]!" + motivatsion tilaklar

### 🏆 Reyting (Leaderboard)
- `localStorage`da saqlanadigan reyting (eng yuqori natija birinchi)
- Medal tizimi 🥇🥈🥉, foydalanuvchi o'z o'rnini ko'radi
- Bir qurilmada bir nechta foydalanuvchi natijalari to'planadi
- Jami urinishlar, o'rtacha va eng yuqori natija statistikasi

---

## ⚙️ Sozlamalar

`index.html` ichidagi `CONFIG` obyektini o'zgartirib sozlash mumkin:

```javascript
const CONFIG = {
    TEST_SIZE: 200,            // testdagi savollar soni
    PASS_SCORE: 60,            // o'tish uchun kerakli to'g'ri javoblar
    CELEBRATION_PERCENT: 90,   // tabriklash effektining chegarasi (%)
    SECONDS_PER_QUESTION: 60,  // har bir savolga ajratilgan vaqt (soniya)
};
```

---

## 🗂️ Ma'lumotlar saqlash (localStorage)

| Kalit | Tavsif |
|-------|--------|
| `ot_theme` | Mavzu (light/dark) |
| `ot_profile` | Foydalanuvchi profili |
| `ot_leaderboard` | Reyting yozuvlari |
| `ot_history` | Test tarixi va statistika |

Barcha localStorage operatsiyalari `DataStore` qatlamida jamlangan — kelajakda
**Firebase yoki ma'lumotlar bazasiga** faqat shu qatlamni o'zgartirib ulanish mumkin.

---

## 🚀 Ishga tushirish

`index.html` faylini istalgan zamonaviy brauzerda oching. Hech qanday o'rnatish yoki build kerak emas.

```bash
# Mahalliy server (ixtiyoriy)
python3 -m http.server 8000
# so'ng brauzerda: http://localhost:8000
```

---

## 🔄 Savollarni yangilash (Word hujjatlardan qayta ajratish)

Word fayllarni yangilaganingizda savollarni qayta ajratib, `index.html`ga joylashtirish:

```bash
python3 extract.py   # .docx -> questions.json (292 savol)
python3 inject.py    # questions.json -> index.html (__QUESTION_BANK__ o'rniga)
```

- `extract.py` — `.docx` (ZIP) ichidan savollarni ikki formatda parse qiladi
- `inject.py` — `questions.json`ni `index.html`ga joylashtiradi

---

## 🛠️ Texnologiyalar

HTML5 · TailwindCSS (CDN) · Vanilla JavaScript · Chart.js · canvas-confetti · jsPDF + AutoTable · Font Awesome

---

## 📂 Fayllar

| Fayl | Tavsif |
|------|--------|
| `index.html` | To'liq, mustaqil platforma (savollar ichida) |
| `extract.py` | Word hujjatlardan savol ajratuvchi skript |
| `inject.py` | Savollarni HTMLga joylashtiruvchi skript |
| `questions.json` | Ajratilgan 292 savol (oraliq ma'lumot) |

---

**Iftikhor Software Solutions Inc.** · © 2026 All Rights Reserved

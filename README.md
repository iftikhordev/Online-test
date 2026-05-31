# 🎓 Online Test Platformasi

Professional, bitta `index.html` faylida joylashgan web-based test platformasi.
To'liq O'zbek tilida, **"Silk Road"** uslubidagi elegant dizayn bilan.

> **Iftikhor Software Solutions Inc.** — © 2026 All Rights Reserved

---

## ⚡ Asosiy xususiyat: DARHOL javob

Har bir savolga javob bosilganda natija **shu zahoti** ko'rinadi:
- To'g'ri variant **yashil** rangda belgilanadi
- Tanlangan noto'g'ri variant **qizil** rangda belgilanadi
- Pastda jonli **ball paneli** (to'g'ri / noto'g'ri / qolgan) yangilanadi

Savollar bitta sahifada, chiroyli kartalar ko'rinishida — scroll qilib yechiladi.

---

## 📊 Savollar bazasi

Savollar 3 ta Word hujjatidan avtomatik ajratib olingan (`extract.py`):

| Fan | Savollar soni |
|-----|:---:|
| Turizm loyihasini boshqarish | 95 |
| Menejmentga kirish | 99 |
| Madaniyatlararo muloqot | 98 |
| **Jami bank** | **292** |

To'g'ri javob manbada doimo birinchi variant edi — ish vaqtida **A, B, C, D** bo'ylab
tasodifiy aralashtiriladi. Har bir test uchun savollar ham tasodifiy tanlanadi (dublikatsiz).

---

## ✨ Funksiyalar

- ⚡ **Darhol javob feedback** (yashil/qizil + xabar)
- 🗂️ **Fan (kategoriya) filtri** — barcha fanlar yoki bitta fan
- 🔢 **Savollar soni tanlovi** — 20 / 40 / 60 / 100 / 200 / Hammasi
- 📊 **Jonli ball paneli** (sticky, pastda) + progress bar (yuqorida)
- 🌗 **Day/Night** rejim — `localStorage`da saqlanadi, silliq o'tish
- 📈 **Natija oynasi** — donut chart, fanlar bo'yicha bar chart, tavsiyalar
- 🎉 **Tabriklash** — natija **≥ 90%** bo'lsa konfetti + tabrik xabari
- 🏆 **Reyting (leaderboard)** — medal tizimi 🥇🥈🥉, o'rtacha/eng yuqori statistika
- 📄 **PDF eksport** (jsPDF + AutoTable)
- 📱 Mobile / Tablet / Desktop **responsive**

---

## ⚙️ Sozlamalar

`index.html` ichidagi `CONFIG` obyekti:

```javascript
const CONFIG = {
  DEFAULT_COUNT: 60,                       // boshlang'ich savollar soni
  COUNT_OPTIONS: [20, 40, 60, 100, 200],   // tanlov variantlari ("Hammasi" avtomatik)
  CELEBRATION_PERCENT: 90,                 // tabriklash chegarasi (%)
  PASS_PERCENT: 60,                        // o'tish chegarasi (%)
};
```

---

## 🗂️ Ma'lumotlar saqlash (localStorage)

| Kalit | Tavsif |
|-------|--------|
| `quiz-theme` | Mavzu (dark/light) |
| `quiz-leaderboard` | Reyting yozuvlari |

Reyting `saveToLeaderboard` / `openLB` funksiyalarida jamlangan — kelajakda
**Firebase yoki ma'lumotlar bazasiga** oson ulanadi.

---

## 🚀 Ishga tushirish

`index.html` faylini istalgan zamonaviy brauzerda oching. Build yoki o'rnatish kerak emas.

```bash
python3 -m http.server 8000   # ixtiyoriy: http://localhost:8000
```

---

## 🔄 Savollarni yangilash (Word hujjatlardan)

```bash
python3 extract.py   # .docx -> questions.json (292 savol)
python3 inject.py    # questions.json -> index.html (__RAW__ o'rniga)
```

---

## 🛠️ Texnologiyalar

HTML5 · Vanilla JavaScript · jsPDF + AutoTable · SVG/CSS grafiklar · Google Fonts (Playfair Display + DM Sans) · localStorage

---

## 📂 Fayllar

| Fayl | Tavsif |
|------|--------|
| `index.html` | To'liq, mustaqil platforma (292 savol ichida) |
| `extract.py` | Word hujjatlardan savol ajratuvchi skript |
| `inject.py` | Savollarni HTMLga joylashtiruvchi skript |
| `questions.json` | Ajratilgan 292 savol (oraliq ma'lumot) |

---

**Iftikhor Software Solutions Inc.** · © 2026 All Rights Reserved

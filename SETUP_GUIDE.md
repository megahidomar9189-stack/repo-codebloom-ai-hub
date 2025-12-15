# دليل إعداد وتشغيل CodeBloom Core

## المتطلبات الأساسية

- Node.js 18+ و npm أو pnpm
- حساب Supabase (للـ backend functions)
- API Keys للمودلات المطلوبة

## خطوات التثبيت

### 1. تثبيت Dependencies

```bash
npm install
# أو
pnpm install
```

### 2. إعداد Environment Variables

أنشئ ملف `.env.local` في المجلد الرئيسي وأضف:

```env
# Supabase Configuration (موجود بالفعل)
VITE_SUPABASE_PROJECT_ID="obzioxpqwjteudusfjat"
VITE_SUPABASE_PUBLISHABLE_KEY="your_key_here"
VITE_SUPABASE_URL="https://obzioxpqwjteudusfjat.supabase.co"

# AI Model API Keys (يجب إضافتها)
GEMINIGEN_API_KEY=your_geminigen_api_key_here
ZIMAGE_API_KEY=your_zimage_api_key_here
LOVABLE_API_KEY=your_lovable_api_key_here  # اختياري
```

### 3. إعداد Supabase Functions

يجب إضافة API Keys في Supabase Dashboard:

1. افتح مشروعك في Supabase Dashboard
2. اذهب إلى **Settings** > **Edge Functions** > **Secrets**
3. أضف المتغيرات التالية:
   - `GEMINIGEN_API_KEY`
   - `ZIMAGE_API_KEY`
   - `LOVABLE_API_KEY` (اختياري)

### 4. تشغيل المشروع

```bash
# Development mode
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## الحصول على API Keys

### GeminiGen API Key

1. زر موقع: https://geminigen.ai
2. سجل حساب جديد
3. اذهب إلى API Settings
4. انسخ API Key

**المودلات المدعومة:**
- Nano Banana Pro (imagen-pro)
- Gemini 2.5 Flash (imagen-flash)
- Imagen 4 Fast
- Imagen 4
- Imagen 4 Ultra
- Seedream 4.5

### Z-Image API Key

**الخيار 1: Managed API (مدفوع)**
1. زر موقع: https://zimageapi.com
2. اختر خطة اشتراك:
   - Basic: $7.99/شهر (~180 صورة)
   - Pro: $25.90/شهر (~660 صورة)
   - Max: $59.90/شهر (~1800 صورة)
3. احصل على API Key من Dashboard

**الخيار 2: Self-Hosted (مجاني)**
1. استنسخ المستودع: https://github.com/Tongyi-MAI/Z-Image
2. ثبت المتطلبات (Python 3.8+, CUDA GPU 16GB+)
3. شغل API محلياً
4. عدل endpoint في الكود

### Lovable API Key (اختياري)

1. زر: https://lovable.dev
2. سجل حساب
3. احصل على API Key للـ fallback

## اختبار المودلات

بعد التشغيل:

1. افتح المتصفح على `http://localhost:5173`
2. اذهب إلى **AI Hub** > **Image Generator**
3. اختر موديل من القائمة:
   - Nano Banana Pro
   - Seedream 4.5
   - Z-Image Turbo
   - وغيرها...
4. اكتب prompt واضغط Generate

## استكشاف الأخطاء

### خطأ: "API key not configured"

**الحل:**
- تأكد من إضافة API Keys في Supabase Secrets
- أعد تشغيل Edge Functions

### خطأ: "Rate limit exceeded"

**الحل:**
- انتظر قليلاً (GeminiGen لديه rate limits)
- استخدم موديل آخر
- ترقية الاشتراك

### خطأ: "CORS error"

**الحل:**
- تأكد من تشغيل المشروع من localhost
- تحقق من إعدادات CORS في Supabase

### الموديل لا يعمل

**الحل:**
1. تحقق من Console في المتصفح (F12)
2. تحقق من Supabase Logs
3. تأكد من صحة API Key
4. جرب موديل آخر

## البنية التقنية

```
codebloom-core-main/
├── src/
│   ├── components/
│   │   └── ai-hub/
│   │       ├── ImageGenerator.tsx    # واجهة توليد الصور
│   │       └── ModelSelector.tsx     # اختيار الموديل
│   ├── lib/
│   │   └── ai-models.ts             # تعريف المودلات
│   └── hooks/
│       └── useAIImage.ts            # Hook للتفاعل مع API
├── supabase/
│   └── functions/
│       └── ai-image/
│           └── index.ts             # Backend API handler
└── .env                             # Environment variables
```

## المودلات المتاحة

| الموديل | Provider | السرعة | الجودة | الصور المرجعية |
|---------|----------|--------|--------|----------------|
| Nano Banana Pro | GeminiGen | متوسطة | عالية جداً | ✅ |
| Gemini 2.5 Flash | GeminiGen | سريعة | جيدة | ✅ |
| Imagen 4 Fast | GeminiGen | سريعة | عالية | ✅ |
| Imagen 4 | GeminiGen | متوسطة | عالية | ✅ |
| Imagen 4 Ultra | GeminiGen | بطيئة | ممتازة | ✅ |
| Seedream 4.5 | GeminiGen | متوسطة | إبداعية | ✅ |
| Z-Image Turbo | ZImage | فائقة السرعة | جيدة | ❌ |

## الدعم

للمساعدة أو الإبلاغ عن مشاكل:
- افتح Issue في GitHub
- راجع التوثيق الرسمي للمودلات
- تحقق من Supabase Logs

## الترخيص

هذا المشروع يستخدم:
- React + Vite + TypeScript
- Supabase للـ backend
- Shadcn/ui للمكونات
- مودلات AI مختلفة (تحقق من ترخيص كل موديل)

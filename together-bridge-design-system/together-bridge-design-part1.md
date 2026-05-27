# 🎨 Together-Bridge Premium Design System
## PART 1: Logo, Colors, Typography

---

## 1️⃣ LOGO SYSTEM (6가지 변형)

### 1. Main Logo (Horizontal)
```html
<svg width="288" height="48" viewBox="0 0 288 48" fill="none">
  <defs>
    <linearGradient id="mainGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00B4D8"/>
      <stop offset="50%" stop-color="#0096C7"/>
      <stop offset="100%" stop-color="#0077B6"/>
    </linearGradient>
  </defs>
  
  <!-- Icon -->
  <circle cx="24" cy="24" r="20" fill="#00B4D8" opacity="0.1"/>
  <circle cx="14" cy="12" r="3.5" fill="url(#mainGrad)"/>
  <path d="M 14 16 L 14 24" stroke="url(#mainGrad)" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 14 18 L 8 18" stroke="url(#mainGrad)" stroke-width="1.5" stroke-linecap="round"/>
  
  <circle cx="34" cy="12" r="3.5" fill="url(#mainGrad)"/>
  <path d="M 34 16 L 34 24" stroke="url(#mainGrad)" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 34 18 L 40 18" stroke="url(#mainGrad)" stroke-width="1.5" stroke-linecap="round"/>
  
  <!-- Text -->
  <text x="56" y="30" font-size="20" font-weight="700" fill="#0A0E27" font-family="Inter">
    Together
  </text>
  <text x="56" y="42" font-size="10" font-weight="600" fill="#00B4D8" font-family="Inter" letter-spacing="1">
    BRIDGE
  </text>
  
  <!-- Badge -->
  <rect x="210" y="10" width="70" height="28" rx="14" fill="#F0F9FF" stroke="#00B4D8" stroke-width="1"/>
  <text x="245" y="32" font-size="9" font-weight="700" fill="#00B4D8" text-anchor="middle">
    AI POWERED
  </text>
</svg>
```

### 2. Vertical Logo
```html
<svg width="120" height="140" viewBox="0 0 120 140" fill="none">
  <defs>
    <linearGradient id="vertGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00B4D8"/>
      <stop offset="100%" stop-color="#0077B6"/>
    </linearGradient>
  </defs>
  
  <!-- Icon -->
  <g transform="translate(20, 10)">
    <path d="M 20 10 L 30 20 L 35 15" stroke="url(#vertGrad)" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M 40 10 L 30 20 L 25 15" stroke="url(#vertGrad)" stroke-width="2" fill="none" stroke-linecap="round"/>
  </g>
  
  <!-- Text -->
  <text x="60" y="110" font-size="18" font-weight="700" fill="#0A0E27" text-anchor="middle">
    Together
  </text>
  <text x="60" y="130" font-size="12" font-weight="600" fill="#00B4D8" text-anchor="middle">
    BRIDGE
  </text>
</svg>
```

### 3. Symbol Logo (Mark Only)
```html
<svg width="48" height="48" viewBox="0 0 48 48" fill="none">
  <defs>
    <linearGradient id="symGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00B4D8"/>
      <stop offset="100%" stop-color="#0077B6"/>
    </linearGradient>
  </defs>
  
  <circle cx="24" cy="24" r="22" fill="none" stroke="url(#symGrad)" stroke-width="1" opacity="0.2"/>
  
  <!-- Two hands -->
  <path d="M 16 22 Q 14 18 18 16 Q 22 14 24 18" fill="url(#symGrad)"/>
  <path d="M 32 22 Q 34 18 30 16 Q 26 14 24 18" fill="url(#symGrad)"/>
  
  <!-- Connection -->
  <path d="M 18 18 L 24 24 L 30 18" stroke="url(#symGrad)" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  
  <!-- Center heart -->
  <circle cx="24" cy="28" r="2" fill="url(#symGrad)"/>
</svg>
```

### 4. Favicon (32x32)
```html
<svg width="32" height="32" viewBox="0 0 32 32" fill="none">
  <rect width="32" height="32" rx="8" fill="#00B4D8"/>
  
  <path d="M 12 12 L 16 14 L 20 12" stroke="white" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <path d="M 16 14 L 16 22" stroke="white" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <circle cx="12" cy="12" r="1" fill="white"/>
  <circle cx="20" cy="12" r="1" fill="white"/>
</svg>
```

### 5. Monochrome Logo (Black)
```html
<svg width="288" height="48" viewBox="0 0 288 48" fill="none">
  <!-- Icon -->
  <circle cx="24" cy="24" r="20" fill="#000000" opacity="0.05"/>
  <circle cx="14" cy="12" r="3.5" fill="#000000"/>
  <path d="M 14 16 L 14 24" stroke="#000000" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 14 18 L 8 18" stroke="#000000" stroke-width="1.5" stroke-linecap="round"/>
  
  <circle cx="34" cy="12" r="3.5" fill="#000000"/>
  <path d="M 34 16 L 34 24" stroke="#000000" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 34 18 L 40 18" stroke="#000000" stroke-width="1.5" stroke-linecap="round"/>
  
  <!-- Text -->
  <text x="56" y="30" font-size="20" font-weight="700" fill="#000000" font-family="Inter">
    Together
  </text>
  <text x="56" y="42" font-size="10" font-weight="600" fill="#000000" font-family="Inter" letter-spacing="1">
    BRIDGE
  </text>
</svg>
```

### 6. White Logo (For Dark Backgrounds)
```html
<svg width="288" height="48" viewBox="0 0 288 48" fill="none">
  <!-- Icon -->
  <circle cx="24" cy="24" r="20" fill="#FFFFFF" opacity="0.1"/>
  <circle cx="14" cy="12" r="3.5" fill="#FFFFFF"/>
  <path d="M 14 16 L 14 24" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 14 18 L 8 18" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
  
  <circle cx="34" cy="12" r="3.5" fill="#FFFFFF"/>
  <path d="M 34 16 L 34 24" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 34 18 L 40 18" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
  
  <!-- Text -->
  <text x="56" y="30" font-size="20" font-weight="700" fill="#FFFFFF" font-family="Inter">
    Together
  </text>
  <text x="56" y="42" font-size="10" font-weight="600" fill="#FFFFFF" font-family="Inter" letter-spacing="1">
    BRIDGE
  </text>
</svg>
```

---

## 2️⃣ COLOR SYSTEM

### Primary Colors (프라이머리 - 신뢰, 전문성)
```css
--primary-0: #FFFFFF;
--primary-50: #E0F7FF;
--primary-100: #B3ECFF;
--primary-200: #80DEFD;
--primary-300: #4DD9FF;
--primary-400: #26D1E8;
--primary-500: #00B4D8;  /* ⭐ Main */
--primary-600: #0096C7;
--primary-700: #0077B6;
--primary-800: #006195;
--primary-900: #004B7B;
--primary-950: #003554;
```

### Gray Scale (구조적 회색)
```css
--gray-0: #FFFFFF;
--gray-50: #F8FAFC;
--gray-100: #F1F5F9;
--gray-200: #E2E8F0;
--gray-300: #CBD5E1;
--gray-400: #94A3B8;
--gray-500: #64748B;
--gray-600: #475569;
--gray-700: #334155;
--gray-800: #1E293B;
--gray-900: #0F172A;
--gray-950: #020617;
```

### Functional Colors (기능)
```css
--success: #10B981;
--warning: #F59E0B;
--danger: #EF4444;
--info: #3B82F6;
```

### Gradients (그래디언트)
```css
--gradient-primary: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%);
--gradient-hover: linear-gradient(135deg, #0096C7 0%, #006195 100%);
--gradient-success: linear-gradient(135deg, #10B981 0%, #059669 100%);
--gradient-danger: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
```

### Dark Mode Colors
```css
--dark-bg: #0A0E27;
--dark-surface: #141829;
--dark-border: #1E293B;
--dark-text: #FFFFFF;
--dark-text-secondary: #CBD5E1;
```

---

## 3️⃣ TYPOGRAPHY SYSTEM

### Font Family
```css
--font-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-code: 'Monaco', 'Courier New', monospace;
```

### Heading System
```css
/* H1 - 56px */
--h1-size: 3.5rem;
--h1-weight: 700;
--h1-line-height: 1.2;
--h1-letter-spacing: -0.02em;

/* H2 - 40px */
--h2-size: 2.5rem;
--h2-weight: 700;
--h2-line-height: 1.3;
--h2-letter-spacing: -0.01em;

/* H3 - 32px */
--h3-size: 2rem;
--h3-weight: 700;
--h3-line-height: 1.4;

/* H4 - 24px */
--h4-size: 1.5rem;
--h4-weight: 600;
--h4-line-height: 1.4;

/* H5 - 20px */
--h5-size: 1.25rem;
--h5-weight: 600;
--h5-line-height: 1.5;

/* H6 - 16px */
--h6-size: 1rem;
--h6-weight: 600;
--h6-line-height: 1.5;
```

### Body Text
```css
/* Large - 18px */
--body-lg-size: 1.125rem;
--body-lg-weight: 400;
--body-lg-line-height: 1.6;

/* Medium - 16px (Default) */
--body-md-size: 1rem;
--body-md-weight: 400;
--body-md-line-height: 1.6;

/* Small - 14px */
--body-sm-size: 0.875rem;
--body-sm-weight: 400;
--body-sm-line-height: 1.5;

/* Extra Small - 12px */
--body-xs-size: 0.75rem;
--body-xs-weight: 400;
--body-xs-line-height: 1.5;
```

### Special Text
```css
/* Label */
--label-size: 0.875rem;
--label-weight: 500;
--label-line-height: 1.4;

/* Button */
--button-size: 1rem;
--button-weight: 600;
--button-line-height: 1.5;

/* Code */
--code-size: 0.875rem;
--code-weight: 400;
--code-family: monospace;
```

---

## 4️⃣ SPACING & SIZING

### Space Scale (8px 기반)
```css
--space-xs: 4px;      /* 0.25rem */
--space-sm: 8px;      /* 0.5rem */
--space-md: 12px;     /* 0.75rem */
--space-lg: 16px;     /* 1rem */
--space-xl: 24px;     /* 1.5rem */
--space-2xl: 32px;    /* 2rem */
--space-3xl: 48px;    /* 3rem */
--space-4xl: 64px;    /* 4rem */
--space-5xl: 80px;    /* 5rem */
--space-6xl: 96px;    /* 6rem */
```

### Border Radius
```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-2xl: 20px;
--radius-3xl: 24px;
--radius-full: 9999px;
```

---

## 5️⃣ SHADOWS & ELEVATION

### Box Shadows
```css
--shadow-none: none;
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-base: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
--shadow-primary: 0 10px 25px -5px rgba(0, 180, 216, 0.2);
```

---

## 6️⃣ TRANSITIONS & ANIMATIONS

### Duration
```css
--duration-fast: 150ms;
--duration-base: 200ms;
--duration-slow: 300ms;
--duration-slower: 500ms;
```

### Easing
```css
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-linear: linear;
--ease-custom: cubic-bezier(0.23, 1, 0.32, 1);  /* Custom */
```

---

## 7️⃣ RESPONSIVE BREAKPOINTS

```css
--breakpoint-xs: 320px;   /* Mobile */
--breakpoint-sm: 640px;   /* Small tablet */
--breakpoint-md: 768px;   /* Tablet */
--breakpoint-lg: 1024px;  /* Large tablet */
--breakpoint-xl: 1280px;  /* Desktop */
--breakpoint-2xl: 1536px; /* Large desktop */
```

---

## 8️⃣ Z-INDEX SCALE

```css
--z-hide: -1;
--z-auto: auto;
--z-base: 0;
--z-dropdown: 1000;
--z-modal-backdrop: 1040;
--z-modal: 1050;
--z-popover: 1060;
--z-tooltip: 1070;
--z-notification: 1080;
```

---

## ✅ 사용 방법

### CSS Variables로 사용
```css
/* In your CSS */
:root {
  --primary-color: #00B4D8;
  --gradient-primary: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

/* Apply */
.button {
  background: var(--gradient-primary);
  box-shadow: var(--shadow-lg);
  border-radius: var(--radius-lg);
}
```

### Tailwind Config
```js
module.exports = {
  theme: {
    colors: {
      primary: {
        50: '#E0F7FF',
        500: '#00B4D8',
        600: '#0096C7',
      },
    },
  },
}
```

---

**다운로드 가능한 Part 1 완성!** ✅

**로고 (6가지) + 색상 + 타이포그래피**

**즉시 사용 가능한 코드!** 💻

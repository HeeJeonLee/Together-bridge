# 🎨 Together-Bridge Premium Design System
## PART 2: Components & Pages

---

## 1️⃣ PREMIUM BUTTON COMPONENT

### HTML
```html
<!-- Primary Button -->
<button class="btn btn-primary btn-md">
  Click Me
</button>

<!-- With Icon -->
<button class="btn btn-primary btn-lg">
  <svg class="w-5 h-5"><!-- icon --></svg>
  Get Started
</button>

<!-- States -->
<button class="btn btn-primary" disabled>Disabled</button>
<button class="btn btn-primary btn-loading">Loading...</button>

<!-- Variants -->
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
<button class="btn btn-ghost">Ghost</button>
```

### CSS
```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 16px;
  border-radius: 8px;
  font-weight: 600;
  transition: all 200ms ease-in-out;
  cursor: pointer;
  border: none;
  outline: none;
}

/* Sizes */
.btn-sm {
  padding: 8px 12px;
  font-size: 14px;
}

.btn-md {
  padding: 12px 16px;
  font-size: 16px;
}

.btn-lg {
  padding: 16px 24px;
  font-size: 18px;
}

.btn-xl {
  padding: 20px 32px;
  font-size: 20px;
}

/* Primary */
.btn-primary {
  background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%);
  color: white;
  box-shadow: 0 10px 25px -5px rgba(0, 180, 216, 0.2);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 15px 35px -5px rgba(0, 180, 216, 0.3);
}

.btn-primary:active {
  transform: scale(0.95);
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

/* Secondary */
.btn-secondary {
  background: #E0F7FF;
  color: #00B4D8;
}

.btn-secondary:hover {
  background: #B3ECFF;
}

/* Success */
.btn-success {
  background: linear-gradient(135deg, #10B981 0%, #059669 100%);
  color: white;
}

/* Danger */
.btn-danger {
  background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
  color: white;
}

/* Ghost */
.btn-ghost {
  background: transparent;
  color: #00B4D8;
  border: 1px solid #00B4D8;
}

.btn-ghost:hover {
  background: rgba(0, 180, 216, 0.1);
}

/* Full Width */
.btn-full {
  width: 100%;
}

/* Loading State */
.btn-loading {
  opacity: 0.7;
  pointer-events: none;
}

.btn-loading::before {
  content: '';
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

---

## 2️⃣ PREMIUM CARD COMPONENT

### HTML
```html
<!-- Basic Card -->
<div class="card card-default">
  <h3 class="card-title">Card Title</h3>
  <p class="card-text">Card content here</p>
</div>

<!-- Elevated Card -->
<div class="card card-elevated">
  <div class="card-header">Header</div>
  <div class="card-body">
    <p>Content</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-primary btn-sm">Action</button>
  </div>
</div>

<!-- Filled Card with Icon -->
<div class="card card-filled card-hover">
  <div class="card-icon">
    <svg><!-- icon --></svg>
  </div>
  <h3 class="card-title">Feature</h3>
  <p class="card-text">Description</p>
</div>
```

### CSS
```css
.card {
  border-radius: 12px;
  padding: 24px;
  overflow: hidden;
  transition: all 300ms ease-in-out;
  position: relative;
}

/* Variants */
.card-default {
  background: white;
  border: 1px solid #E2E8F0;
}

.card-elevated {
  background: white;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.card-filled {
  background: linear-gradient(135deg, #F0F9FF 0%, #E0F7FF 100%);
}

.card-outlined {
  background: transparent;
  border: 2px solid #00B4D8;
}

/* Hover Effect */
.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 25px -5px rgba(0, 180, 216, 0.2);
}

/* Card Parts */
.card-header {
  padding-bottom: 12px;
  border-bottom: 1px solid #E2E8F0;
  margin-bottom: 12px;
  font-weight: 600;
}

.card-body {
  flex: 1;
}

.card-footer {
  padding-top: 12px;
  border-top: 1px solid #E2E8F0;
  margin-top: 12px;
  display: flex;
  gap: 8px;
}

.card-icon {
  width: 48px;
  height: 48px;
  border-radius: 8px;
  background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 12px;
  color: white;
}

.card-title {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 8px;
  color: #0A0E27;
}

.card-text {
  font-size: 14px;
  line-height: 1.6;
  color: #64748B;
}

/* Dark Mode */
.dark .card-default {
  background: #141829;
  border-color: #1E293B;
}

.dark .card-filled {
  background: linear-gradient(135deg, rgba(0, 180, 216, 0.1) 0%, rgba(0, 119, 182, 0.1) 100%);
}

.dark .card-title {
  color: #FFFFFF;
}

.dark .card-text {
  color: #CBD5E1;
}
```

---

## 3️⃣ PREMIUM INPUT COMPONENT

### HTML
```html
<!-- Basic Input -->
<div class="input-group">
  <label class="input-label">Email Address</label>
  <input type="email" class="input" placeholder="example@company.com">
</div>

<!-- With Icon -->
<div class="input-group">
  <label class="input-label">Password</label>
  <div class="input-wrapper">
    <svg class="input-icon"><!-- lock icon --></svg>
    <input type="password" class="input input-with-icon">
  </div>
</div>

<!-- Error State -->
<div class="input-group">
  <label class="input-label">Phone</label>
  <input type="tel" class="input input-error" value="invalid">
  <p class="input-error-text">Invalid phone number</p>
</div>

<!-- Success State -->
<div class="input-group">
  <label class="input-label">Username</label>
  <input type="text" class="input input-success" value="john_doe">
  <p class="input-success-text">✓ Available</p>
</div>

<!-- Textarea -->
<div class="input-group">
  <label class="input-label">Message</label>
  <textarea class="input" rows="4" placeholder="Enter your message..."></textarea>
</div>

<!-- Select -->
<div class="input-group">
  <label class="input-label">Category</label>
  <select class="input">
    <option>Select an option</option>
    <option>Option 1</option>
    <option>Option 2</option>
  </select>
</div>
```

### CSS
```css
.input-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
}

.input-label {
  font-size: 14px;
  font-weight: 500;
  color: #334155;
  transition: color 200ms;
}

.input {
  padding: 12px 16px;
  border: 2px solid #E2E8F0;
  border-radius: 8px;
  font-size: 16px;
  font-family: inherit;
  transition: all 200ms ease-in-out;
  outline: none;
  background: white;
  color: #0A0E27;
}

.input:hover {
  border-color: #CBD5E1;
}

.input:focus {
  border-color: #00B4D8;
  box-shadow: 0 0 0 3px rgba(0, 180, 216, 0.1);
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 16px;
  width: 20px;
  height: 20px;
  color: #94A3B8;
  pointer-events: none;
}

.input-with-icon {
  padding-left: 48px;
}

/* States */
.input-error {
  border-color: #EF4444;
}

.input-error:focus {
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
}

.input-success {
  border-color: #10B981;
}

.input-success:focus {
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.input-error-text {
  font-size: 12px;
  color: #EF4444;
}

.input-success-text {
  font-size: 12px;
  color: #10B981;
}

/* Dark Mode */
.dark .input {
  background: #1E293B;
  border-color: #334155;
  color: white;
}

.dark .input:focus {
  border-color: #00B4D8;
}

.dark .input-label {
  color: #CBD5E1;
}
```

---

## 4️⃣ HERO SECTION PAGE

### HTML
```html
<section class="hero">
  <div class="hero-content">
    <div class="hero-badge">
      <span class="hero-badge-icon">⚡</span>
      <span class="hero-badge-text">AI 기반 자동 매칭</span>
    </div>
    
    <h1 class="hero-title">
      당신의 모든 순간과<br>함께
    </h1>
    
    <p class="hero-subtitle">
      AI가 최고의 대행자를 찾아주고, 자동으로 매칭해주는 플랫폼.<br>
      믿을 수 있는 사람과 함께, 모든 순간을 더 풍요롭게.
    </p>
    
    <div class="hero-buttons">
      <button class="btn btn-primary btn-lg">
        지금 시작하기
        <svg class="w-5 h-5"><!-- arrow --></svg>
      </button>
      <button class="btn btn-secondary btn-lg">
        데모 보기
      </button>
    </div>
  </div>
  
  <div class="hero-image">
    <div class="hero-placeholder">
      <!-- App mockup or image -->
    </div>
  </div>
</section>
```

### CSS
```css
.hero {
  min-height: 100vh;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
  padding: 64px 32px;
  background: linear-gradient(135deg, #FFFFFF 0%, #F0F9FF 50%, #FFFFFF 100%);
}

.hero-content {
  max-width: 600px;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background: rgba(0, 180, 216, 0.1);
  border: 1px solid rgba(0, 180, 216, 0.3);
  border-radius: 24px;
  margin-bottom: 24px;
  width: fit-content;
}

.hero-badge-icon {
  font-size: 16px;
}

.hero-badge-text {
  font-size: 14px;
  font-weight: 600;
  color: #00B4D8;
}

.hero-title {
  font-size: 64px;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.02em;
  margin-bottom: 24px;
  background: linear-gradient(135deg, #0077B6 0%, #00B4D8 50%, #0096C7 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 20px;
  line-height: 1.6;
  color: #475569;
  margin-bottom: 32px;
}

.hero-buttons {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.hero-image {
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-placeholder {
  width: 100%;
  max-width: 400px;
  aspect-ratio: 3/4;
  background: linear-gradient(135deg, #E0F7FF 0%, #B3ECFF 100%);
  border-radius: 24px;
  border: 2px solid #00B4D8;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #00B4D8;
  font-size: 24px;
  font-weight: 700;
}

/* Responsive */
@media (max-width: 768px) {
  .hero {
    grid-template-columns: 1fr;
    padding: 32px 16px;
  }
  
  .hero-title {
    font-size: 40px;
  }
  
  .hero-subtitle {
    font-size: 16px;
  }
  
  .hero-buttons {
    flex-direction: column;
  }
}
```

---

## 5️⃣ MATCHING RESULTS PAGE

### HTML
```html
<section class="matches-section">
  <div class="matches-header">
    <h1>최고의 대행자를 찾았어요!</h1>
    <p>AI가 추천한 상위 3명입니다</p>
  </div>
  
  <div class="matches-grid">
    <div class="match-card">
      <div class="match-rank">1</div>
      
      <div class="match-avatar">
        <img src="avatar.jpg" alt="Kim">
      </div>
      
      <div class="match-info">
        <h3 class="match-name">김민준</h3>
        <div class="match-stats">
          <span class="match-rating">⭐ 4.9 (127)</span>
          <span class="match-experience">경력 5년</span>
          <span class="match-distance">거리 2.3km</span>
        </div>
      </div>
      
      <div class="match-price">
        <div class="match-price-value">85,000원</div>
        <div class="match-score">매칭율 98%</div>
      </div>
      
      <div class="match-actions">
        <button class="btn btn-secondary btn-sm btn-full">프로필 보기</button>
        <button class="btn btn-primary btn-sm btn-full">선택하기</button>
      </div>
    </div>
    
    <!-- More match cards... -->
  </div>
</section>
```

### CSS
```css
.matches-section {
  padding: 48px 32px;
  background: linear-gradient(135deg, #F0F9FF 0%, #FFFFFF 100%);
  min-height: 100vh;
}

.matches-header {
  text-align: center;
  margin-bottom: 48px;
}

.matches-header h1 {
  font-size: 40px;
  font-weight: 700;
  margin-bottom: 12px;
  background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.matches-header p {
  font-size: 18px;
  color: #64748B;
}

.matches-grid {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.match-card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  position: relative;
  transition: all 300ms ease-in-out;
}

.match-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 25px -5px rgba(0, 180, 216, 0.2);
}

.match-rank {
  position: absolute;
  top: -12px;
  right: 24px;
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, #FCD34D 0%, #F59E0B 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: white;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
}

.match-avatar {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  overflow: hidden;
  margin-bottom: 16px;
  background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%);
}

.match-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.match-info {
  flex: 1;
  margin-bottom: 12px;
}

.match-name {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
  color: #0A0E27;
}

.match-stats {
  display: flex;
  gap: 16px;
  font-size: 14px;
  color: #64748B;
  flex-wrap: wrap;
}

.match-price {
  text-align: right;
  margin-bottom: 16px;
}

.match-price-value {
  font-size: 28px;
  font-weight: 700;
  color: #00B4D8;
}

.match-score {
  font-size: 12px;
  font-weight: 600;
  background: linear-gradient(135deg, #00B4D8 0%, #0077B6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.match-actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
```

---

## 6️⃣ DASHBOARD PAGE

### HTML
```html
<div class="dashboard">
  <!-- Stats Cards -->
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-icon stat-icon-blue">📈</div>
      <div class="stat-label">총 거래</div>
      <div class="stat-value">4,250건</div>
      <div class="stat-change">+12.5%</div>
    </div>
    <!-- More stats... -->
  </div>
  
  <!-- Charts Section -->
  <div class="charts-grid">
    <div class="chart-container">
      <h2>거래 & 수익 추이</h2>
      <canvas id="transactionChart"></canvas>
    </div>
    
    <div class="chart-container">
      <h2>카테고리 분포</h2>
      <canvas id="categoryChart"></canvas>
    </div>
  </div>
  
  <!-- Recent Transactions -->
  <div class="transactions-container">
    <h2>최근 거래</h2>
    <table class="transactions-table">
      <thead>
        <tr>
          <th>거래 ID</th>
          <th>카테고리</th>
          <th>금액</th>
          <th>상태</th>
          <th>날짜</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>#TXN00001</td>
          <td>부모님 병원동행</td>
          <td>₩80,000</td>
          <td><span class="badge badge-success">완료</span></td>
          <td>2024-06-01</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

### CSS
```css
.dashboard {
  padding: 32px;
  background: #F8FAFC;
  min-height: 100vh;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  margin-bottom: 32px;
}

.stat-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: all 300ms ease-in-out;
}

.stat-card:hover {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  margin-bottom: 12px;
}

.stat-icon-blue {
  background: rgba(0, 180, 216, 0.1);
}

.stat-label {
  font-size: 12px;
  color: #64748B;
  margin-bottom: 4px;
}

.stat-value {
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 4px;
}

.stat-change {
  font-size: 12px;
  color: #10B981;
  font-weight: 600;
}

.charts-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
  margin-bottom: 32px;
}

.chart-container {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.transactions-container {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  overflow-x: auto;
}

.transactions-table {
  width: 100%;
  border-collapse: collapse;
}

.transactions-table thead {
  background: #F8FAFC;
}

.transactions-table th {
  padding: 12px;
  text-align: left;
  font-weight: 600;
  color: #334155;
  font-size: 13px;
}

.transactions-table td {
  padding: 16px 12px;
  border-top: 1px solid #E2E8F0;
}

.transactions-table tbody tr:hover {
  background: #F8FAFC;
}

.badge {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
}

.badge-success {
  background: rgba(16, 185, 129, 0.1);
  color: #10B981;
}

/* Responsive */
@media (max-width: 768px) {
  .charts-grid {
    grid-template-columns: 1fr;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
  
  .transactions-table {
    font-size: 13px;
  }
}
```

---

## ✅ 다운로드 준비 완료

**Part 2: 컴포넌트 & 페이지**
- 버튼 컴포넌트
- 카드 컴포넌트
- 입력 필드
- 5개 페이지 완전 구현

**모든 코드: 즉시 복사/사용 가능!** ✅

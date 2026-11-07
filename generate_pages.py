from pathlib import Path
from html import escape
root=Path(__file__).parent

def header(active):
 links=[('index.html','მთავარი','home'),('projects.html','ნამუშევრები','projects'),('about.html','ჩვენ შესახებ','about'),('contact.html','კონტაქტი','contact')]
 nav=''.join(f'<a class="nav-link {"active" if n==active else ""}" href="{u}" {"aria-current=\"page\"" if n==active else ""}>{t}</a>' for u,t,n in links)
 return f'''<a class="skip-link" href="#main">მთავარ შიგთავსზე გადასვლა</a>
<header class="site-header" id="top">
 <div class="header-inner container">
  <a href="index.html" class="brand" aria-label="MODO — მთავარი გვერდი"><span class="brand-symbol" aria-hidden="true">✳</span><span>MODO<span class="brand-period">.</span></span></a>
  <nav class="desktop-nav" aria-label="მთავარი მენიუ">{nav}</nav>
  <div class="header-actions">
   <a class="saved-link" href="projects.html?favorites=1" title="რჩეული ნამუშევრები" aria-label="რჩეული ნამუშევრების ნახვა"><svg class="icon-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.8 4.6a5.6 5.6 0 0 0-7.9 0l-.9.9-.9-.9a5.6 5.6 0 0 0-7.9 7.9L12 21l8.8-8.5a5.6 5.6 0 0 0 0-7.9Z"/></svg><span class="saved-count">0</span></a>
   <button type="button" class="icon-btn theme-toggle" aria-label="თემის შეცვლა" title="ღია / მუქი თემა"><svg class="icon-svg sun-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4M2 12h2m16 0h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
   <button type="button" class="icon-btn menu-toggle" aria-label="მენიუს გახსნა" aria-expanded="false" aria-controls="mobile-nav"><span class="menu-bars"></span></button>
  </div>
 </div>
 <nav id="mobile-nav" class="mobile-nav" aria-label="მობილური მენიუ" hidden>{nav}</nav>
</header>'''

def footer():
 return '''<footer class="site-footer">
 <div class="container">
  <div class="footer-top"><div><a href="index.html" class="brand footer-brand"><span class="brand-symbol" aria-hidden="true">✳</span>MODO<span class="brand-period">.</span></a><p>იდეები იწყება ცნობისმოყვარეობით.<br>აღმოაჩინე, შეინახე, შთაგონდი.</p></div>
  <div class="footer-nav-group"><div><h3>გვერდები</h3><a href="index.html">მთავარი</a><a href="projects.html">ნამუშევრები</a><a href="about.html">ჩვენ შესახებ</a><a href="contact.html">კონტაქტი</a></div><div><h3>გაიგე მეტი</h3><a href="projects.html?favorites=1">ჩემი რჩეულები</a><a href="about.html#faq">ხშირი კითხვები</a><a href="contact.html#message">დაგვიკავშირდი</a></div></div></div>
  <div class="footer-bottom"><span>© 2026 MODO — სასწავლო დემო-პროექტი.</span><span>შექმნილია HTML · CSS · JavaScript-ით</span><a href="#top" class="back-to-top">ზემოთ ↑</a></div>
 </div>
</footer>
<div class="toast" role="status" aria-live="polite"></div>'''

def frame(title,description,active,content):
 html=f'''<!DOCTYPE html>
<html lang="ka">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width,initial-scale=1">
 <meta name="theme-color" content="#f7f6ef">
 <meta name="description" content="{escape(description)}">
 <title>{escape(title)} | MODO</title>
 <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
 <link rel="preconnect" href="https://fonts.googleapis.com">
 <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
 <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Georgian:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
 <link rel="stylesheet" href="style.css">
 <script src="data.js" defer></script>
 <script src="app.js" defer></script>
</head>
<body data-page="{active}">
{header(active)}
<main id="main">{content}</main>
{footer()}
</body>
</html>'''
 return html

home='''
<section class="hero-section"><div class="container hero-layout">
 <div class="hero-copy"><div class="eyebrow"><span class="eyebrow-dot"></span> დამოუკიდებელი კრეატიული გალერეა <span class="eyebrow-num">№ 001 / 2026</span></div>
  <h1>იდეებს<br><span class="headline-outline">ფორმა</span><br>აქვს<span class="hero-period">.</span></h1>
  <p class="hero-lead">ადგილი, სადაც დიზაინი, ფერი და ექსპერიმენტები ერთმანეთს ხვდება. დაათვალიერე ნამუშევრები და იპოვე შენი შემდეგი შთაგონება.</p>
  <div class="hero-actions"><a class="btn btn-accent" href="projects.html">აღმოაჩინე ნამუშევრები <span aria-hidden="true">↗</span></a><a class="text-cta" href="about.html">ვინ ვართ ჩვენ <span aria-hidden="true">↗</span></a></div>
  <div class="hero-bottom"><span class="round-star" aria-hidden="true">✳</span><span>ახალი ხედვა.<br>უსასრულო იდეები.</span><span class="hero-scroll" aria-hidden="true">SCROLL TO EXPLORE ↓</span></div>
 </div>
 <div class="hero-visual" aria-label="ფერადი გრაფიკული პოსტერების კომპოზიცია"><div class="visual-grid" aria-hidden="true"></div><div class="hero-poster hero-poster-back"><img src="assets/posters/02.svg" alt="Kinetic Type — აბსტრაქტული ნარინჯისფერი პოსტერი" width="800" height="900"></div><div class="hero-poster hero-poster-front"><img src="assets/posters/03.svg" alt="Bloom Club — იასამნისფერი ყვავილების პოსტერი" width="800" height="900"></div><div class="hero-stamp"><span>CREATIVE</span><span class="stamp-star">✳</span><span>UNIVERSE</span></div><span class="vertical-tag">MADE FOR CURIOUS MINDS · 2026</span></div>
 </div></section>
<div class="ticker" aria-label="კრეატიულობა, იდეები, დიზაინი"><div class="ticker-track" aria-hidden="true">EXPLORE MORE ✳ THINK DIFFERENT ✳ CREATE SOMETHING ✳ EXPLORE MORE ✳ THINK DIFFERENT ✳ CREATE SOMETHING ✳ </div></div>
<section class="section-pad featured-section" aria-labelledby="featured-title"><div class="container">
 <div class="section-head"><div><span class="section-kicker">01 / გამორჩეული</span><h2 id="featured-title">შერჩეული <em>ნამუშევრები.</em></h2></div><div class="section-head-right"><p>პროექტები, რომლებიც ფერებით, იდეებითა და განსხვავებული ხასიათით გამოირჩევა.</p><div class="carousel-controls"><button class="round-btn" id="feature-prev" type="button" aria-label="წინა ნამუშევრები">←</button><button class="round-btn" id="feature-next" type="button" aria-label="შემდეგი ნამუშევრები">→</button></div></div></div>
 <div class="project-grid featured-grid" id="featured-grid" aria-live="polite"></div>
 <div class="center-action"><a class="btn btn-dark" href="projects.html">ყველა ნამუშევრის ნახვა <span aria-hidden="true">↗</span></a></div>
 </div></section>
<section class="manifesto-section"><div class="container manifesto-grid"><div class="manifesto-art"><span class="man-sticker">IDEAS<br>IN<br>MOTION</span><span class="huge-asterisk" aria-hidden="true">✳</span><span class="art-corner">M/26 — DESIGN ARCHIVE</span></div><div class="manifesto-copy"><span class="section-kicker">02 / ჩვენი იდეა</span><h2>კრეატიულობას<br>საზღვრები <em>არ აქვს.</em></h2><p>ჩვენ გვჯერა, რომ კარგი დიზაინი მხოლოდ ლამაზი გამოსახულება არ არის. ეს არის ამბავი, რომელსაც საკუთარი ხასიათი და ხმა აქვს.</p><a class="link-arrow" href="about.html">გაიცანი MODO <span aria-hidden="true">↗</span></a><div class="manifesto-numbers"><div><strong>12</strong><span>დემო-პროექტი</span></div><div><strong>04</strong><span>კატეგორია</span></div><div><strong>∞</strong><span>იდეა</span></div></div></div></div></section>
<section class="section-pad categories-section"><div class="container"><div class="section-head"><div><span class="section-kicker">03 / მიმართულებები</span><h2>იპოვე <em>შენი ინტერესი.</em></h2></div><p class="intro-small">აირჩიე მიმართულება და აღმოაჩინე საინტერესო ნამუშევრები.</p></div><div class="category-tiles"><a href="projects.html?category=branding" class="category-tile tile-yellow"><span class="cat-number">01</span><span class="cat-graphic">◎</span><strong>ბრენდინგი</strong><span class="cat-arrow">↗</span></a><a href="projects.html?category=web" class="category-tile tile-lilac"><span class="cat-number">02</span><span class="cat-graphic">▧</span><strong>ვებ-დიზაინი</strong><span class="cat-arrow">↗</span></a><a href="projects.html?category=illustration" class="category-tile tile-pink"><span class="cat-number">03</span><span class="cat-graphic">✿</span><strong>ილუსტრაცია</strong><span class="cat-arrow">↗</span></a><a href="projects.html?category=type" class="category-tile tile-blue"><span class="cat-number">04</span><span class="cat-graphic">Aa</span><strong>ტიპოგრაფია</strong><span class="cat-arrow">↗</span></a></div></div></section>
<section class="callout-section"><div class="container"><div><span class="section-kicker">LET'S TALK / 2026</span><h2>ახალი იდეა<br>გაქვს<span>?</span></h2></div><a href="contact.html" class="callout-link" aria-label="კონტაქტის გვერდის გახსნა">↗</a><p>მოგვწერე და შენი იდეის შესახებ მოგვიყევი.</p></div></section>
'''

projects='''
<section class="page-hero projects-hero"><div class="container"><span class="section-kicker">MODO ARCHIVE / 2026</span><div class="page-hero-row"><h1>იდეების<br><em>კოლექცია.</em></h1><div class="page-hero-side"><span class="page-hero-symbol">✳</span><p>ათვალიერე, გაფილტრე და შეინახე ის, რაც ყველაზე მეტად მოგწონს.</p></div></div><div class="hero-rule"><span>EXPLORE THE ARCHIVE</span><span>12 PROJECTS / 04 CATEGORIES</span></div></div></section>
<section class="section-pad collection-section"><div class="container"><div class="collection-tools"><div class="search-field"><svg viewBox="0 0 24 24" class="icon-svg" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m16 16 5 5"/></svg><label class="sr-only" for="project-search">ნამუშევრების ძიება</label><input id="project-search" type="search" placeholder="მოძებნე ნამუშევარი..." autocomplete="off"></div><div class="tool-right"><label class="sr-only" for="project-sort">დალაგება</label><select id="project-sort" aria-label="ნამუშევრების დალაგება"><option value="newest">უახლესი ჯერ</option><option value="oldest">უძველესი ჯერ</option><option value="az">სახელით A–Z</option><option value="za">სახელით Z–A</option></select><button id="saved-only" type="button" class="saved-filter" aria-pressed="false"><span aria-hidden="true">♡</span> მხოლოდ რჩეულები</button></div></div>
 <div id="category-filters" class="filter-list" role="group" aria-label="კატეგორიით გაფილტვრა"></div>
 <div class="results-line"><span id="result-count" role="status" aria-live="polite">იტვირთება...</span><button type="button" id="reset-filters" class="reset-link">ფილტრების გასუფთავება ↗</button></div>
 <div class="project-grid all-projects-grid" id="all-projects"></div><div id="empty-state" class="empty-state" hidden><div class="empty-face">◌</div><h2>ვერაფერი მოიძებნა</h2><p>სცადე სხვა სიტყვა ან გაასუფთავე ფილტრები.</p><button class="btn btn-dark" type="button" id="empty-reset">ყველა ნამუშევრის ნახვა ↗</button></div>
 </div></section>
<dialog class="project-dialog" id="project-dialog" aria-labelledby="modal-title"><button type="button" class="dialog-close" aria-label="ფანჯრის დახურვა">✕</button><div class="dialog-body"><div class="dialog-art"><img id="modal-image" src="assets/posters/01.svg" alt="" width="800" height="900"></div><div class="dialog-info"><span class="section-kicker">PROJECT OVERVIEW / MODO</span><h2 id="modal-title"></h2><p class="modal-category" id="modal-category"></p><p id="modal-description"></p><dl class="modal-details"><div><dt>კლიენტი</dt><dd id="modal-client"></dd></div><div><dt>წელი</dt><dd id="modal-year"></dd></div><div><dt>მიმართულებები</dt><dd id="modal-services"></dd></div></dl><button type="button" class="btn btn-accent" id="modal-favorite">რჩეულებში შენახვა ♡</button></div></div></dialog>
'''

about='''
<section class="page-hero about-hero"><div class="container"><span class="section-kicker">A LITTLE ABOUT US / 2026</span><div class="page-hero-row"><h1>გაიცანი<br><em>MODO.</em></h1><span class="page-hero-symbol">✳</span></div><div class="hero-rule"><span>CURIOUS MINDS WELCOME</span><span>ABOUT / OUR STORY</span></div></div></section>
<section class="section-pad about-intro"><div class="container about-intro-grid"><div><span class="section-kicker">01 / იდეა</span><h2>ყველაფერი<br>იწყება <em>„რატომ?“</em></h2></div><div class="about-intro-text"><p class="large-para">MODO არის კრეატიული იდეების ციფრული გალერეის სასწავლო კონცეფცია.</p><p>ჩვენი მიზანია ვიზუალური ექსპერიმენტების, განსხვავებული ტიპოგრაფიისა და თანამედროვე დიზაინის ერთი სივრცის შექმნა. თითოეული ნამუშევარი ახალი პერსპექტივის ძიებაა.</p><p>აქ წარმოდგენილი ბრენდები და პროექტები გამოგონილია და შექმნილია პორტფოლიოს დემონსტრაციისთვის.</p></div></div></section>
<section class="values-section section-pad"><div class="container"><span class="section-kicker">02 / რაც გვამოძრავებს</span><div class="section-head"><h2>ჩვენი <em>პრინციპები.</em></h2></div><div class="value-grid"><article class="value-card"><span class="value-ico">✳</span><span class="value-n">01 /</span><h3>ცნობისმოყვარეობა</h3><p>ახალი იდეები იწყება კითხვებით და სამყაროს სხვა კუთხით დანახვით.</p></article><article class="value-card"><span class="value-ico">↗</span><span class="value-n">02 /</span><h3>ექსპერიმენტი</h3><p>ვეძებთ განსხვავებულ ფორმებს, ფერებსა და გზებს აზრის გადმოსაცემად.</p></article><article class="value-card"><span class="value-ico">◎</span><span class="value-n">03 /</span><h3>სიმარტივე</h3><p>კარგი იდეა ყველასთვის გასაგები, ხელმისაწვდომი და დასამახსოვრებელი უნდა იყოს.</p></article></div></div></section>
<section class="process-section section-pad"><div class="container"><div class="section-head"><div><span class="section-kicker">03 / როგორ ვმუშაობთ</span><h2>იდეიდან <em>შედეგამდე.</em></h2></div></div><div class="process-steps"><div><span>01</span><h3>აღმოჩენა</h3><p>კვლევა, ინსპირაცია და პრობლემის სწორად დანახვა.</p></div><div><span>02</span><h3>შექმნა</h3><p>ესკიზები, ფერები, ტიპოგრაფია და დიზაინის სისტემები.</p></div><div><span>03</span><h3>გაზიარება</h3><p>საბოლოო კონცეფციის ჩვენება და იდეების გაზიარება.</p></div></div></div></section>
<section class="faq-section section-pad" id="faq"><div class="container faq-grid"><div><span class="section-kicker">04 / ხშირად დასმული კითხვები</span><h2>კითხვები<br>და <em>პასუხები.</em></h2><p>გინდა მეტი გაიგო? მოგვწერე კონტაქტის გვერდიდან.</p></div><div class="faq-list"><details><summary>რა არის MODO? <span aria-hidden="true">+</span></summary><p>MODO არის Front-end-ის სასწავლო დემო-პროექტი: თანამედროვე, ინტერაქტიული ციფრული გალერეა.</p></details><details><summary>როგორ შევინახო ნამუშევარი? <span aria-hidden="true">+</span></summary><p>დააჭირე გულის სიმბოლოს ნებისმიერ ბარათზე. არჩევანი შენს ბრაუზერში, localStorage-ში შეინახება.</p></details><details><summary>შესაძლებელია ნამუშევრების გაფილტვრა? <span aria-hidden="true">+</span></summary><p>დიახ. ნამუშევრების გვერდზე ხელმისაწვდომია კატეგორია, ცოცხალი ძიება, დალაგება და რჩეულების ფილტრი.</p></details><details><summary>ნამდვილ კომპანიებს წარმოადგენს ეს პროექტები? <span aria-hidden="true">+</span></summary><p>არა. პროექტები და ბრენდების სახელები მხოლოდ დემონსტრაციისთვისაა გამოგონილი.</p></details></div></div></section>
<section class="about-end"><div class="container"><span>THE BEST IDEAS ARE STILL AHEAD</span><a href="projects.html">აღმოაჩინე ნამუშევრები <span>↗</span></a></div></section>
'''

contact='''
<section class="page-hero contact-hero"><div class="container"><span class="section-kicker">OPEN FOR IDEAS / 2026</span><div class="page-hero-row"><h1>მოდი,<br><em>ვისაუბროთ.</em></h1><span class="page-hero-symbol">↗</span></div><div class="hero-rule"><span>LET'S CREATE SOMETHING</span><span>CONTACT / SAY HELLO</span></div></div></section>
<section class="section-pad contact-section"><div class="container contact-grid"><div class="contact-aside"><span class="section-kicker">01 / კონტაქტი</span><h2>შენი იდეა<br>გვაინტერესებს<span class="colored-dot">.</span></h2><p>დაგვიტოვე შეტყობინება — ფორმა ამ სასწავლო ვებსაიტზე მუშაობის დემონსტრაციისთვისაა.</p><div class="contact-note"><span>✳</span><p>ფორმა მონაცემებს მხოლოდ შენს ბრაუზერში ინახავს. სერვერზე არაფერი იგზავნება.</p></div><div class="contact-graphic" aria-hidden="true"><span>HELLO<br>WORLD<span>!</span></span><i>✳</i></div></div><div class="form-panel" id="message"><div class="form-panel-title"><h2>მოგვწერე</h2><span>✳</span></div><p class="form-intro">შეავსე ველები და მიიღე დადასტურება.</p><form id="contact-form" novalidate><div class="form-row"><div class="field"><label for="full-name">სახელი და გვარი <span>*</span></label><input id="full-name" name="name" placeholder="მაგ. მარიამ გიორგაძე" required minlength="2" maxlength="70" autocomplete="name" aria-describedby="name-error"><span class="field-error" id="name-error" aria-live="polite"></span></div><div class="field"><label for="email">ელფოსტა <span>*</span></label><input type="email" id="email" name="email" placeholder="name@example.com" required autocomplete="email" aria-describedby="email-error"><span class="field-error" id="email-error" aria-live="polite"></span></div></div><div class="field"><label for="subject">თემა <span>*</span></label><select id="subject" name="subject" required aria-describedby="subject-error"><option value="">აირჩიე თემა</option><option value="თანამშრომლობა">თანამშრომლობა</option><option value="დიზაინის პროექტი">დიზაინის პროექტი</option><option value="უკუკავშირი">უკუკავშირი</option><option value="სხვა">სხვა</option></select><span class="field-error" id="subject-error" aria-live="polite"></span></div><div class="field"><label for="message-text">შეტყობინება <span>*</span></label><textarea id="message-text" name="message" rows="6" placeholder="მოგვიყევი შენი იდეის შესახებ..." required minlength="10" maxlength="1500" aria-describedby="message-error"></textarea><span class="field-error" id="message-error" aria-live="polite"></span></div><div class="form-bottom"><p><span>*</span> სავალდებულო ველი</p><button type="submit" class="btn btn-dark">შეტყობინების შენახვა <span aria-hidden="true">↗</span></button></div><div id="form-success" class="form-success" role="status" aria-live="polite" hidden></div></form></div></div></section>
<section class="contact-banner"><div class="container"><span>STAY CURIOUS</span><span>STAY CREATIVE</span><span>✳</span></div></section>
'''

pages=[('index.html','მთავარი — იდეებს ფორმა აქვს','MODO — კრეატიული გალერეა, რომელიც აერთიანებს ორიგინალურ დიზაინ-პროექტებს და იდეებს.','home',home),('projects.html','ნამუშევრები — იდეების კოლექცია','აღმოაჩინე დიზაინის ნამუშევრები: ძიება, ფილტრაცია, რჩეულები და ინტერაქტიული აღწერები.','projects',projects),('about.html','ჩვენ შესახებ — კრეატიული ხედვა','გაიგე მეტი MODO-ს იდეის, პრინციპებისა და დიზაინის პროცესის შესახებ.','about',about),('contact.html','კონტაქტი — მოგვწერე','დაუკავშირდი MODO-ს სასწავლო საკონტაქტო ფორმის საშუალებით.','contact',contact)]
for name,title,desc,key,content in pages:
 (root/name).write_text(frame(title,desc,key,content),encoding='utf-8')
 print('generated',name)

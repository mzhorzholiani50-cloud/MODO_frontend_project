/* MODO — Vanilla JavaScript. No external dependencies. */
'use strict';

const storage = {
  get(key, fallback) {
    try { const value = localStorage.getItem(key); return value === null ? fallback : JSON.parse(value); }
    catch { return fallback; }
  },
  set(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); return true; }
    catch { return false; }
  }
};

const FAVORITES_KEY = 'modo:favorites:v1';
const THEME_KEY = 'modo:theme:v1';
const MESSAGES_KEY = 'modo:messages:v1';
const categorySlugs = {branding:'ბრენდინგი',web:'ვებ-დიზაინი',illustration:'ილუსტრაცია',type:'ტიპოგრაფია'};

const state = {favorites:new Set(), filter:'ყველა',search:'',sort:'newest',savedOnly:false,featureStart:0};
let toastTimer;

function getFavorites() {
  const saved = storage.get(FAVORITES_KEY, []);
  return new Set(Array.isArray(saved) ? saved.filter(id => Number.isInteger(id) && PROJECTS.some(p=>p.id===id)) : []);
}
function toast(message) {
  const el=document.querySelector('.toast');
  if (!el) return;
  el.textContent=message;
  el.classList.add('visible');
  clearTimeout(toastTimer);
  toastTimer=setTimeout(()=>el.classList.remove('visible'),3100);
}
function refreshSavedCount(){
  document.querySelectorAll('.saved-count').forEach(el=>{el.textContent=String(state.favorites.size);});
  document.querySelectorAll('.saved-link').forEach(el=>{el.setAttribute('aria-label',`რჩეული ნამუშევრები: ${state.favorites.size}`);});
}
function isFavorite(id){return state.favorites.has(id);}
function updateFavoriteButtons(){
  document.querySelectorAll('[data-fav-id]').forEach(button=>{
    const id=Number(button.dataset.favId),active=isFavorite(id);
    button.setAttribute('aria-pressed',String(active));
    button.setAttribute('aria-label',active?'რჩეულებიდან წაშლა':'რჩეულებში დამატება');
    button.textContent=active?'♥':'♡';
  });
  const modalFavorite=document.getElementById('modal-favorite');
  if(modalFavorite&&modalFavorite.dataset.projectId){
    const active=isFavorite(Number(modalFavorite.dataset.projectId));
    modalFavorite.textContent=active?'რჩეულებიდან წაშლა ♥':'რჩეულებში შენახვა ♡';
    modalFavorite.setAttribute('aria-pressed',String(active));
  }
  refreshSavedCount();
}
function toggleFavorite(id){
  if(!PROJECTS.some(p=>p.id===id)) return;
  if(state.favorites.has(id)){state.favorites.delete(id);toast('ნამუშევარი რჩეულებიდან წაიშალა.');}
  else{state.favorites.add(id);toast('ნამუშევარი რჩეულებში შეინახა.');}
  if(!storage.set(FAVORITES_KEY,[...state.favorites])) toast('ბრაუზერში შენახვა ვერ მოხერხდა.');
  updateFavoriteButtons();
  if(document.body.dataset.page==='projects'&&state.savedOnly)renderProjects();
}
function projectCard(project){
  const active=isFavorite(project.id);
  const image=`assets/posters/${String(project.id).padStart(2,'0')}.svg`;
  return `<article class="project-card" data-project="${project.id}">
   <div class="card-image-wrap">
    <button type="button" class="card-open" data-open-id="${project.id}" aria-label="${project.title} — დეტალურად ნახვა">
     <img class="card-image" src="${image}" alt="${project.title} — ორიგინალური აბსტრაქტული პოსტერი" loading="lazy" width="800" height="900">
     <span class="card-overlay"><span class="card-view">დეტალურად ნახვა ↗</span></span>
    </button>
    <button type="button" class="favorite-btn" data-fav-id="${project.id}" aria-label="${active?'რჩეულებიდან წაშლა':'რჩეულებში დამატება'}" aria-pressed="${active}">${active?'♥':'♡'}</button>
   </div>
   <div class="card-meta"><div><h3>${project.title}</h3><span class="category-label">${project.category}</span></div><span class="card-year">${project.year}</span></div>
  </article>`;
}
function initCardsEvents(){
  document.addEventListener('click',e=>{
    const favorite=e.target.closest('[data-fav-id]');
    if(favorite){toggleFavorite(Number(favorite.dataset.favId));return;}
    const opener=e.target.closest('[data-open-id]');
    if(opener){openProject(Number(opener.dataset.openId));}
  });
}
function renderFeatured(){
  const container=document.getElementById('featured-grid');
  if(!container)return;
  const featured=[PROJECTS[0],PROJECTS[2],PROJECTS[4],PROJECTS[7],PROJECTS[9],PROJECTS[1]];
  const cards=[0,1,2].map(offset=>featured[(state.featureStart+offset)%featured.length]);
  container.innerHTML=cards.map(projectCard).join('');
  document.getElementById('feature-prev')?.addEventListener('click',()=>{
    state.featureStart=(state.featureStart+featured.length-1)%featured.length;renderFeatured();
  },{once:true});
  document.getElementById('feature-next')?.addEventListener('click',()=>{
    state.featureStart=(state.featureStart+1)%featured.length;renderFeatured();
  },{once:true});
}
function initFilters(){
  const container=document.getElementById('category-filters');
  if(!container) return;
  const params=new URLSearchParams(window.location.search);
  const requested=params.get('category');
  state.filter=categorySlugs[requested]||'ყველა';
  state.savedOnly=params.get('favorites')==='1';
  document.getElementById('saved-only').setAttribute('aria-pressed',String(state.savedOnly));
  container.innerHTML=CATEGORIES.map(category=>`<button type="button" class="filter-chip" data-category="${category}" aria-pressed="${category===state.filter}">${category}</button>`).join('');
  container.addEventListener('click',e=>{
    const chip=e.target.closest('[data-category]');
    if(!chip)return;
    state.filter=chip.dataset.category;
    container.querySelectorAll('[data-category]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.category===state.filter)));
    renderProjects();
  });
  const search=document.getElementById('project-search');
  search.addEventListener('input',e=>{state.search=e.target.value.trim().toLocaleLowerCase('ka');renderProjects();});
  document.getElementById('project-sort').addEventListener('change',e=>{state.sort=e.target.value;renderProjects();});
  document.getElementById('saved-only').addEventListener('click',e=>{
    state.savedOnly=!state.savedOnly;
    e.currentTarget.setAttribute('aria-pressed',String(state.savedOnly));
    renderProjects();
  });
  document.getElementById('reset-filters').addEventListener('click',resetFilters);
  document.getElementById('empty-reset').addEventListener('click',resetFilters);
  renderProjects();
}
function resetFilters(){
  state.filter='ყველა';state.search='';state.sort='newest';state.savedOnly=false;
  document.getElementById('project-search').value='';
  document.getElementById('project-sort').value='newest';
  document.getElementById('saved-only').setAttribute('aria-pressed','false');
  document.querySelectorAll('[data-category]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.category==='ყველა')));
  try{history.replaceState(null,'',location.pathname);}catch{}
  renderProjects();
}
function renderProjects(){
  const grid=document.getElementById('all-projects');
  if(!grid)return;
  const filtered=PROJECTS.filter(p=>{
    const matchCategory=state.filter==='ყველა'||p.category===state.filter;
    const phrase=`${p.title} ${p.description} ${p.category} ${p.client}`.toLocaleLowerCase('ka');
    const matchSearch=!state.search||phrase.includes(state.search);
    return matchCategory&&matchSearch&&(!state.savedOnly||isFavorite(p.id));
  });
  const sorters={
    newest:(a,b)=>b.year-a.year||a.id-b.id,
    oldest:(a,b)=>a.year-b.year||a.id-b.id,
    az:(a,b)=>a.title.localeCompare(b.title),
    za:(a,b)=>b.title.localeCompare(a.title)
  };
  filtered.sort(sorters[state.sort]||sorters.newest);
  grid.innerHTML=filtered.map(projectCard).join('');
  document.getElementById('result-count').textContent=`ნაპოვნია ${filtered.length} ნამუშევარი`;
  document.getElementById('empty-state').hidden=filtered.length!==0;
}
function openProject(id){
  const dialog=document.getElementById('project-dialog');
  const p=PROJECTS.find(p=>p.id===id);
  if(!dialog||!p)return;
  const img=document.getElementById('modal-image');
  img.src=`assets/posters/${String(p.id).padStart(2,'0')}.svg`;
  img.alt=`${p.title} — აბსტრაქტული ვიზუალური პროექტი`;
  document.getElementById('modal-title').textContent=p.title;
  document.getElementById('modal-category').textContent=p.category;
  document.getElementById('modal-description').textContent=p.description;
  document.getElementById('modal-client').textContent=p.client;
  document.getElementById('modal-year').textContent=String(p.year);
  document.getElementById('modal-services').textContent=p.services.join(', ');
  const fav=document.getElementById('modal-favorite');
  fav.dataset.projectId=String(id);
  updateFavoriteButtons();
  if(!dialog.open)dialog.showModal();
}
function initDialog(){
  const dialog=document.getElementById('project-dialog');
  if(!dialog)return;
  dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close();});
  document.getElementById('modal-favorite').addEventListener('click',e=>toggleFavorite(Number(e.currentTarget.dataset.projectId)));
}
function initTheme(){
  const theme=storage.get(THEME_KEY,null);
  if(theme==='dark'||theme==='light')document.documentElement.dataset.theme=theme;
  document.querySelectorAll('.theme-toggle').forEach(button=>button.addEventListener('click',()=>{
    const next=document.documentElement.dataset.theme==='dark'?'light':'dark';
    document.documentElement.dataset.theme=next;
    storage.set(THEME_KEY,next);
    button.setAttribute('aria-label',next==='dark'?'ღია თემაზე გადასვლა':'მუქ თემაზე გადასვლა');
    toast(next==='dark'?'მუქი თემა ჩაირთო.':'ღია თემა ჩაირთო.');
  }));
}
function initMobileNav(){
  const toggle=document.querySelector('.menu-toggle');
  const nav=document.getElementById('mobile-nav');
  if(!toggle||!nav)return;
  function close(){nav.hidden=true;toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','მენიუს გახსნა');}
  toggle.addEventListener('click',()=>{
    const open=nav.hidden;
    nav.hidden=!open;
    toggle.setAttribute('aria-expanded',String(open));
    toggle.setAttribute('aria-label',open?'მენიუს დახურვა':'მენიუს გახსნა');
  });
  nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',close));
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!nav.hidden){close();toggle.focus();}});
  document.addEventListener('click',e=>{if(!nav.hidden&&!nav.contains(e.target)&&!toggle.contains(e.target))close();});
  window.addEventListener('resize',()=>{if(window.innerWidth>800&&!nav.hidden)close();});
}
function validateField(field){
  const value=field.value.trim();
  let error='';
  switch(field.name){
    case 'name':
      if(value.length<2)error='შეიყვანე მინიმუმ 2 სიმბოლო.';
      else if(value.length>70)error='შეიყვანე მაქსიმუმ 70 სიმბოლო.';
      break;
    case 'email':
      if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value))error='შეიყვანე სწორი ელფოსტის მისამართი.';
      break;
    case 'subject':
      if(!value)error='აირჩიე შეტყობინების თემა.';
      break;
    case 'message':
      if(value.length<10)error='შეტყობინება მინიმუმ 10 სიმბოლოს უნდა შეიცავდეს.';
      else if(value.length>1500)error='შეტყობინება მაქსიმუმ 1500 სიმბოლოს უნდა შეიცავდეს.';
      break;
  }
  field.setAttribute('aria-invalid',String(Boolean(error)));
  const errorEl=document.getElementById(`${field.name==='name'?'name':field.name==='message'?'message':field.name}-error`);
  if(errorEl)errorEl.textContent=error;
  return !error;
}
function initContactForm(){
  const form=document.getElementById('contact-form');
  if(!form)return;
  const fields=[...form.querySelectorAll('input,select,textarea')];
  fields.forEach(field=>{
    field.addEventListener('blur',()=>validateField(field));
    field.addEventListener('input',()=>{if(field.getAttribute('aria-invalid')==='true')validateField(field);});
    field.addEventListener('change',()=>{if(field.getAttribute('aria-invalid')==='true')validateField(field);});
  });
  form.addEventListener('submit',e=>{
    e.preventDefault();
    const valid=fields.map(validateField).every(Boolean);
    const success=document.getElementById('form-success');
    success.hidden=true;
    if(!valid){fields.find(f=>f.getAttribute('aria-invalid')==='true')?.focus();return;}
    const data=Object.fromEntries(new FormData(form).entries());
    const old=storage.get(MESSAGES_KEY,[]);
    const messages=Array.isArray(old)?old:[];
    const saved=storage.set(MESSAGES_KEY,[...messages.slice(-19),{...data,createdAt:new Date().toISOString()}]);
    if(!saved){toast('შენახვა ვერ მოხერხდა. შეამოწმე ბრაუზერის პარამეტრები.');return;}
    form.reset();
    fields.forEach(field=>{field.removeAttribute('aria-invalid');});
    fields.forEach(field=>{const span=document.getElementById(`${field.name==='name'?'name':field.name==='message'?'message':field.name}-error`);if(span)span.textContent='';});
    success.textContent='✓ შეტყობინება წარმატებით შეინახა შენს ბრაუზერში! ეს არის დემო-ფორმა; წერილი არ იგზავნება.';
    success.hidden=false;
    toast('შეტყობინება ადგილობრივად შენახულია.');
    success.scrollIntoView({behavior:'smooth',block:'nearest'});
  });
}

function init(){
  state.favorites=getFavorites();
  initTheme();
  initMobileNav();
  initCardsEvents();
  initDialog();
  initFilters();
  initContactForm();
  renderFeatured();
  refreshSavedCount();
}
init();

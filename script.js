// Progressive enhancement: navigation remains visible if JavaScript is unavailable.
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
const mobile = window.matchMedia('(max-width: 900px)');
function closeMenu() { toggle.setAttribute('aria-expanded', 'false'); nav.dataset.collapsed = String(mobile.matches); }
toggle.hidden = false;
closeMenu();
toggle.addEventListener('click', () => { const open = toggle.getAttribute('aria-expanded') !== 'true'; toggle.setAttribute('aria-expanded', String(open)); nav.dataset.collapsed = String(!open); });
nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); } });
mobile.addEventListener('change', closeMenu);
document.querySelector('#year').textContent = String(new Date().getFullYear());

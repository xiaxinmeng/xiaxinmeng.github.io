/* ==========================================================================
   学术个人主页脚本
   1) 中英文切换（读取元素上的 data-zh / data-en）
   2) 深浅色主题切换（记忆在 localStorage）
   3) 侧边导航高亮（滚动监听）
   4) 页脚自动更新年份
   ========================================================================== */
(function () {
  'use strict';

  var LS_LANG  = 'xm_lang';
  var LS_THEME = 'xm_theme';
  var html = document.documentElement;

  /* ---------- 1. 语言切换 ---------- */
  function applyLang(lang) {
    var isEn = lang === 'en';
    html.setAttribute('lang', isEn ? 'en' : 'zh-CN');

    document.querySelectorAll('[data-zh][data-en]').forEach(function (el) {
      var val = el.getAttribute(isEn ? 'data-en' : 'data-zh');
      if (val != null) el.innerHTML = val;
    });

    document.querySelectorAll('[data-set-lang]').forEach(function (btn) {
      btn.classList.toggle('is-on', btn.getAttribute('data-set-lang') === lang);
    });

    try { localStorage.setItem(LS_LANG, lang); } catch (e) {}
  }

  /* ---------- 2. 主题切换 ---------- */
  function applyTheme(theme) {
    html.setAttribute('data-theme', theme);
    try { localStorage.setItem(LS_THEME, theme); } catch (e) {}
  }

  /* ---------- 初始化偏好 ---------- */
  var savedLang = null, savedTheme = null;
  try {
    savedLang  = localStorage.getItem(LS_LANG);
    savedTheme = localStorage.getItem(LS_THEME);
  } catch (e) {}

  var initialLang = savedLang || (navigator.language && navigator.language.toLowerCase().indexOf('zh') === -1 ? 'en' : 'zh');
  var initialTheme = savedTheme || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

  applyTheme(initialTheme);
  applyLang('zh');           // 先按中文渲染，避免闪烁
  if (initialLang !== 'zh') applyLang(initialLang);

  /* ---------- 事件绑定 ---------- */
  document.querySelectorAll('[data-set-lang]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      applyLang(btn.getAttribute('data-set-lang'));
    });
  });

  var themeBtn = document.getElementById('themeToggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      applyTheme(html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
    });
  }

  /* ---------- 3. 滚动高亮侧边导航 ---------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.topbar__nav a[href^="#"]'));
  var sections = navLinks
    .map(function (a) { return document.querySelector(a.getAttribute('href')); })
    .filter(Boolean);

  if ('IntersectionObserver' in window && sections.length) {
    var visible = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
      var current = null;
      for (var i = 0; i < sections.length; i++) {
        if (visible[sections[i].id]) { current = sections[i].id; break; }
      }
      navLinks.forEach(function (a) {
        a.classList.toggle('is-active', current && a.getAttribute('href') === '#' + current);
      });
    }, { rootMargin: '-84px 0px -65% 0px', threshold: 0 });
    sections.forEach(function (s) { io.observe(s); });
  }

  /* ---------- 4. 页脚年份 ---------- */
  var year = String(new Date().getFullYear());
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = year; });

  /* ---------- 5. 控制台留个小提示 ---------- */
  console.log('%cXinmeng Xia · xiaxinmeng.github.io', 'color:#2d5a8c;font-weight:600');
})();

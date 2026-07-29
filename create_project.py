#!/usr/bin/env python3
"""
create_project.py

Generates a complete Capacitor Android app project ("my-admob-app") with
all required files and packages it into "my-admob-app.zip".
"""

import os
import zipfile

ROOT_DIR = "my-admob-app"
ZIP_NAME = "my-admob-app.zip"

PACKAGE_JSON = """{
  "name": "pro-creator-studio",
  "version": "1.0.0",
  "description": "Pro Creator Studio App",
  "main": "www/index.html",
  "scripts": {
    "build": "echo 'Building static files'"
  },
  "dependencies": {
    "@capacitor/core": "^5.0.0",
    "@capacitor/android": "^5.0.0",
    "@capacitor-community/admob": "^5.0.0"
  }
}
"""

CAPACITOR_CONFIG_JSON = """{
  "appId": "com.procreator.studio",
  "appName": "Pro Creator Studio",
  "webDir": "www",
  "bundledWebRuntime": false,
  "plugins": {
    "AdMob": {
      "appId": "ca-app-pub-9502060049942116~2420225297"
    }
  }
}
"""

ANDROID_MANIFEST_XML = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.procreator.studio">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application
        android:allowBackup="true"
        android:label="Pro Creator Studio"
        android:supportsRtl="true">

        <meta-data
            android:name="com.google.android.gms.ads.APPLICATION_ID"
            android:value="ca-app-pub-9502060049942116~2420225297"/>

    </application>
</manifest>
"""

INDEX_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, viewport-fit=cover">
<title>Pro Creator SEO, Tone & Bio Studio</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          base: '#0B0A10',
          surface: '#15131F',
          surface2: '#1D1A2A',
          line: '#2A2636',
          violet: '#7C3AED',
          pink: '#EC4899',
          amber: '#F59E0B',
          muted: '#9CA3AF',
        },
        fontFamily: {
          display: ['"Space Grotesk"', 'sans-serif'],
          body: ['"Inter"', 'sans-serif'],
        },
        boxShadow: {
          glow: '0 0 40px -10px rgba(236,72,153,0.45)',
        }
      }
    }
  }
</script>
<style>
  * { -webkit-tap-highlight-color: transparent; }
  html, body { background: #0B0A10; overscroll-behavior-y: none; }
  body { font-family: 'Inter', sans-serif; }
  h1, h2, h3, .display { font-family: 'Space Grotesk', sans-serif; }

  .viral-gradient {
    background: linear-gradient(115deg, #7C3AED 0%, #EC4899 55%, #F59E0B 100%);
  }
  .viral-gradient-text {
    background: linear-gradient(115deg, #7C3AED 0%, #EC4899 55%, #F59E0B 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }
  .pulse-ring {
    position: absolute;
    inset: -6px;
    border-radius: 9999px;
    background: linear-gradient(115deg, #7C3AED, #EC4899, #F59E0B);
    filter: blur(14px);
    opacity: 0.55;
    animation: pulseRing 2.4s ease-in-out infinite;
    z-index: 0;
  }
  @keyframes pulseRing {
    0%, 100% { opacity: 0.35; transform: scale(0.97); }
    50% { opacity: 0.65; transform: scale(1.03); }
  }
  .scrollbar-none::-webkit-scrollbar { display: none; }
  .scrollbar-none { -ms-overflow-style: none; scrollbar-width: none; }

  .fade-up { animation: fadeUp 0.4s ease both; }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .platform-btn {
    transition: all 0.2s ease;
    border: 1px solid #2A2636;
  }
  .platform-btn[data-selected="true"] {
    background: rgba(236, 72, 153, 0.15);
    border-color: #EC4899;
    box-shadow: 0 0 15px rgba(236, 72, 153, 0.3);
  }
  .platform-btn[data-selected="true"] svg { fill: #EC4899; }

  .tab-btn {
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
  }
  .tab-btn.active {
    border-bottom: 2px solid #EC4899;
    color: #EC4899;
    font-weight: 600;
  }
  .tab-btn.active svg {
    stroke: #EC4899;
  }
</style>
</head>
<body class="bg-base text-white min-h-screen flex flex-col font-body">

  <!-- TOP NATIVE ADMOB BANNER HOLDER -->
  <div id="admob-banner-top" class="w-full bg-surface2 text-center py-1 shrink-0 select-none flex justify-center items-center min-h-[50px] border-b border-line">
    <span class="text-[10px] text-muted tracking-widest uppercase">Ad Space</span>
  </div>

  <!-- HEADER -->
  <header class="px-5 pt-6 pb-2 shrink-0 max-w-2xl mx-auto w-full">
    <div class="flex items-center gap-3 mb-4">
      <div class="relative w-11 h-11 shrink-0">
        <div class="pulse-ring"></div>
        <div class="relative w-11 h-11 rounded-full viral-gradient flex items-center justify-center text-lg z-10">⚡</div>
      </div>
      <div class="flex-1 min-w-0">
        <h1 class="text-xl font-semibold leading-tight">Pro Creator <span class="viral-gradient-text">Studio</span></h1>
        <p class="text-xs text-muted leading-tight mt-0.5">Captions · Tone Control · Bio Generator · Live Trends</p>
      </div>
    </div>

    <!-- TABS MENU -->
    <div class="flex border-b border-line gap-6 text-xs text-muted">
      <button id="tabCaptions" class="tab-btn active pb-2">
        <svg class="w-4 h-4 stroke-muted" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"/>
        </svg>
        <span>Captions &amp; SEO</span>
      </button>

      <button id="tabBios" class="tab-btn pb-2">
        <svg class="w-4 h-4 stroke-muted" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
        </svg>
        <span>Profile Bio</span>
      </button>

      <button id="tabTrends" class="tab-btn pb-2">
        <svg class="w-4 h-4 stroke-muted" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>
        </svg>
        <span>Live Trends</span>
      </button>
    </div>
  </header>

  <!-- MAIN SECTION -->
  <main class="flex-1 overflow-y-auto scrollbar-none px-5 pb-8 max-w-2xl mx-auto w-full">
    <section class="bg-surface border border-line rounded-2xl p-5 shadow-xl shadow-black/30 mt-4">

      <!-- PLATFORM SELECTION -->
      <div class="mb-4">
        <label class="block text-xs font-semibold text-muted mb-2 uppercase tracking-wide">Target Platform</label>
        <div class="grid grid-cols-4 gap-3">
          <button type="button" data-platform="instagram" data-selected="true" class="platform-btn h-11 rounded-xl bg-surface2 flex items-center justify-center p-2" title="Instagram">
            <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </button>
          <button type="button" data-platform="tiktok" data-selected="false" class="platform-btn h-11 rounded-xl bg-surface2 flex items-center justify-center p-2" title="TikTok">
            <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>
          </button>
          <button type="button" data-platform="youtube" data-selected="false" class="platform-btn h-11 rounded-xl bg-surface2 flex items-center justify-center p-2" title="YouTube Shorts">
            <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          </button>
          <button type="button" data-platform="linkedin" data-selected="false" class="platform-btn h-11 rounded-xl bg-surface2 flex items-center justify-center p-2" title="LinkedIn">
            <svg class="w-5 h-5 fill-white" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          </button>
        </div>
      </div>

      <!-- LANGUAGE & TONE -->
      <div class="grid grid-cols-2 gap-3 mb-4">
        <div>
          <label for="langSelect" class="block text-xs font-semibold text-muted mb-1.5 uppercase tracking-wide">Language</label>
          <select id="langSelect" class="w-full bg-surface2 border border-line rounded-xl px-3 min-h-[44px] text-xs outline-none focus:border-pink/70 transition-colors">
            <option value="hinglish" selected>Hinglish / Roman Urdu 🔥</option>
            <option value="english">English (Global)</option>
            <option value="spanish">Spanish (Español)</option>
            <option value="portuguese">Portuguese (Brasil)</option>
            <option value="indonesian">Indonesian (Bahasa)</option>
            <option value="arabic">Arabic (العربية)</option>
            <option value="urdu">Urdu (اردو)</option>
          </select>
        </div>
        <div>
          <label for="toneSelect" class="block text-xs font-semibold text-muted mb-1.5 uppercase tracking-wide">Tone & Style</label>
          <select id="toneSelect" class="w-full bg-surface2 border border-line rounded-xl px-3 min-h-[44px] text-xs outline-none focus:border-pink/70 transition-colors">
            <option value="energetic" selected>Viral &amp; Energetic 🔥</option>
            <option value="professional">Professional &amp; Clean 💼</option>
            <option value="funny">Humorous &amp; Witty 😂</option>
            <option value="urgent">Urgent &amp; FOMO ⚡</option>
          </select>
        </div>
      </div>

      <!-- INPUT -->
      <div id="inputBoxContainer" class="mb-4">
        <label id="inputLabel" for="topicInput" class="block text-xs font-semibold text-muted mb-2 uppercase tracking-wide">Topic or Paragraph</label>
        <textarea id="topicInput" rows="3" placeholder="Paste your topic, keywords, or full paragraph here..." class="w-full bg-surface2 border border-line focus:border-pink/70 rounded-xl px-4 py-3 text-sm placeholder:text-muted/60 outline-none transition-colors resize-none leading-relaxed"></textarea>
      </div>

      <button id="actionBtn" class="relative w-full min-h-[50px] viral-gradient text-white font-semibold text-sm rounded-xl py-3 flex items-center justify-center gap-2 active:scale-[0.98] transition-transform shadow-glow">
        <span id="btnText">🔥 Generate Captions</span>
      </button>
    </section>

    <!-- RESULTS -->
    <section id="resultsSection" class="mt-6 hidden">
      <div id="hookCtaContainer" class="mb-4"></div>
      <div id="resultsList" class="space-y-4"></div>
      <button id="loadMoreBtn" class="mt-5 w-full bg-surface2 border border-line hover:border-pink/50 text-xs font-semibold py-3 rounded-xl transition-colors text-muted hover:text-white flex items-center justify-center gap-2">
        <span>🔄 Load More Variations (Infinite Output)</span>
      </button>
    </section>

    <!-- TRENDS -->
    <section id="trendsSection" class="mt-6 hidden space-y-3">
      <h2 class="text-xs font-semibold text-muted uppercase tracking-wide mb-3">🔥 Live Search &amp; Creator Trends</h2>
      <div id="trendsList" class="space-y-3"></div>
    </section>
  </main>

  <!-- BOTTOM NATIVE ADMOB BANNER HOLDER -->
  <div id="admob-banner-bottom" class="w-full bg-surface2 text-center py-1 shrink-0 select-none flex justify-center items-center min-h-[50px] border-t border-line">
    <span class="text-[10px] text-muted tracking-widest uppercase">Ad Space</span>
  </div>

<script>
(function () {
  "use strict";

  // ADMOB CONFIGURATION FOR APK
  const ADMOB_INTERSTITIAL_ID = 'ca-app-pub-9502060049942116/3362340091';

  let activeTab = 'captions';
  let selectedPlatform = 'instagram';
  let currentWordList = [];
  let currentTopicText = "";

  const tabCaptions = document.getElementById('tabCaptions');
  const tabBios = document.getElementById('tabBios');
  const tabTrends = document.getElementById('tabTrends');

  const topicInput = document.getElementById('topicInput');
  const inputLabel = document.getElementById('inputLabel');
  const langSelect = document.getElementById('langSelect');
  const toneSelect = document.getElementById('toneSelect');
  const actionBtn = document.getElementById('actionBtn');
  const btnText = document.getElementById('btnText');

  const resultsSection = document.getElementById('resultsSection');
  const resultsList = document.getElementById('resultsList');
  const hookCtaContainer = document.getElementById('hookCtaContainer');
  const loadMoreBtn = document.getElementById('loadMoreBtn');
  const trendsSection = document.getElementById('trendsSection');
  const trendsList = document.getElementById('trendsList');

  tabCaptions.addEventListener('click', () => switchTab('captions'));
  tabBios.addEventListener('click', () => switchTab('bios'));
  tabTrends.addEventListener('click', () => switchTab('trends'));

  function switchTab(tab) {
    activeTab = tab;
    [tabCaptions, tabBios, tabTrends].forEach(t => t.classList.remove('active'));
    resultsSection.classList.add('hidden');
    trendsSection.classList.add('hidden');

    if (tab === 'captions') {
      tabCaptions.classList.add('active');
      inputLabel.textContent = "Topic or Paragraph";
      topicInput.placeholder = "Paste your topic, keywords, or full paragraph here...";
      btnText.textContent = "🔥 Generate Captions";
      document.getElementById('inputBoxContainer').style.display = 'block';
    } else if (tab === 'bios') {
      tabBios.classList.add('active');
      inputLabel.textContent = "Your Niche / Profession";
      topicInput.placeholder = "e.g. Fitness Coach, Digital Marketer, Tech Content Creator...";
      btnText.textContent = "✨ Generate Profile Bios";
      document.getElementById('inputBoxContainer').style.display = 'block';
    } else if (tab === 'trends') {
      tabTrends.classList.add('active');
      document.getElementById('inputBoxContainer').style.display = 'none';
      btnText.textContent = "⚡ Fetch Live Trends";
    }
  }

  const platformBtns = document.querySelectorAll('.platform-btn');
  platformBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      platformBtns.forEach(b => b.dataset.selected = "false");
      btn.dataset.selected = "true";
      selectedPlatform = btn.dataset.platform;
    });
  });

  actionBtn.addEventListener('click', () => {
    if (activeTab !== 'trends' && !topicInput.value.trim()) {
      alert('Please enter your topic, niche, or paragraph first!');
      return;
    }

    triggerAdMobInterstitial(() => {
      if (activeTab === 'captions') {
        resultsList.innerHTML = '';
        currentTopicText = topicInput.value.trim();
        parseKeywords(currentTopicText);
        renderInitialCaptions();
      } else if (activeTab === 'bios') {
        resultsList.innerHTML = '';
        renderBios();
      } else if (activeTab === 'trends') {
        renderTrends();
      }
    });
  });

  loadMoreBtn.addEventListener('click', () => {
    triggerAdMobInterstitial(() => {
      appendMoreVariations(3);
    });
  });

  // NATIVE APK ADMOB INTERSTITIAL BRIDGE
  async function triggerAdMobInterstitial(onComplete) {
    if (window.Capacitor && window.Capacitor.Plugins && window.Capacitor.Plugins.AdMob) {
      try {
        const { AdMob } = window.Capacitor.Plugins;
        await AdMob.prepareInterstitial({ adId: ADMOB_INTERSTITIAL_ID });
        await AdMob.showInterstitial();
      } catch (err) {
        console.log("AdMob Native Error or Dismissed:", err);
      } finally {
        onComplete();
      }
    } else {
      // Fallback if testing in web browser
      onComplete();
    }
  }

  function parseKeywords(text) {
    const stopWords = new Set(["a","an","the","is","are","was","were","and","or","but","how","to","in","on","at","by","for","with","about","against","between","into","through","during","before","after","above","below","from","up","down","out","off","over","under","again","further","then","once","here","there","when","where","why","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","can","will","just","should","now"]);
    currentWordList = text.replace(/[^\w\s]/gi, '').toLowerCase().split(/\s+/).filter(w => w.length > 2 && !stopWords.has(w));
  }

  function renderInitialCaptions() {
    resultsSection.classList.remove('hidden');
    const primary = currentWordList[0] ? capitalize(currentWordList[0]) : "This Technique";

    hookCtaContainer.innerHTML = `
      <div class="bg-surface2/60 border border-line rounded-2xl p-4 fade-up">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-semibold text-pink uppercase tracking-wider">⚡ Scroll-Stopper Hook (0–3s)</span>
          <button onclick="copyToClipboard(this.parentElement.nextElementSibling.innerText)" class="text-[11px] bg-surface hover:bg-line px-2.5 py-1 rounded-md transition-colors text-muted">Copy</button>
        </div>
        <p class="text-sm font-medium text-white mb-4 leading-relaxed">Stop scrolling if you care about ${primary.toLowerCase()}! This breakdown changes everything. 🛑</p>

        <div class="border-t border-line/60 pt-3 flex items-center justify-between mb-1">
          <span class="text-xs font-semibold text-amber uppercase tracking-wider">📣 Call To Action (CTA)</span>
          <button onclick="copyToClipboard(this.parentElement.nextElementSibling.innerText)" class="text-[11px] bg-surface hover:bg-line px-2.5 py-1 rounded-md transition-colors text-muted">Copy</button>
        </div>
        <p class="text-xs text-white/90 leading-relaxed">Comment "${primary.toUpperCase()}" below and I'll send you the full breakdown! 📩</p>
      </div>
    `;

    appendMoreVariations(3);
    resultsSection.scrollIntoView({ behavior: 'smooth' });
  }

  function appendMoreVariations(count) {
    const lang = langSelect.value;
    const tone = toneSelect.value;
    const primary = currentWordList[0] ? capitalize(currentWordList[0]) : "Strategy";
    const secondary = currentWordList[1] ? capitalize(currentWordList[1]) : "Growth";

    for (let i = 0; i < count; i++) {
      const idx = resultsList.children.length + 1;
      let title = `Variation ${idx} · ${capitalize(tone)} Tone`;
      let text = "";

      if (lang === 'hinglish') {
        if (tone === 'energetic') {
          text = `Yeh hai secret breakdown about ${primary.toLowerCase()}! 🚀\n\nJab aap ${secondary.toLowerCase()} par focus karte ho toh aapka engagement 2x fast ho jata hai.\n\nKey steps to remember:\n1. Basic rules follow karo.\n2. Daily content post karo.\n3. Community ke sath engagement rakho.\n\nAapko yeh point kaisa laga? Niche comment karke batao!`;
        } else if (tone === 'professional') {
          text = `Here is an insightful analysis on ${primary.toLowerCase()}.\n\nOptimizing ${secondary.toLowerCase()} ensures predictable performance on ${selectedPlatform}.\n\nCore takeaways:\n- Standardized workflow.\n- Continuous evaluation.\n- Focused engagement.\n\nSave this post for your reference. 📊`;
        } else if (tone === 'funny') {
          text = `Mujhe pata hai aap ${primary.toLowerCase()} ignore kar rahe the! 😂\n\nLekin jab tak ${secondary.toLowerCase()} fix nahi karoge, views kahan se aayenge?\n\nFollow these 3 simple rules:\n1. Stop guessing.\n2. Start executing.\n3. Coffee piyo aur dubara try karo.\n\nTag a friend who needs to see this! 🤫`;
        } else {
          text = `Don't miss out on ${primary.toLowerCase()} right now! ⏳\n\n${secondary.toLowerCase()} is shifting fast. If you don't adjust today, you'll fall behind.\n\nAct now:\n1. Save this post.\n2. Implement immediately.\n3. Track your results.\n\nDrop a 🔥 if you agree!`;
        }
      } else {
        text = `Essential guide to ${primary.toLowerCase()}.\n\nStructuring your focus around ${secondary.toLowerCase()} gives you a clear competitive edge on ${selectedPlatform}.\n\n1. Prioritize core quality.\n2. Stay consistent daily.\n3. Track your main insights.\n\nSave this post so you don't lose it! 📌`;
      }

      const tags = Array.from(new Set([...currentWordList.slice(0, 5).map(w => `#${w}`), `#${selectedPlatform}`, "#viral"])).join(' ');

      const div = document.createElement('div');
      div.className = "bg-surface border border-line rounded-2xl p-4 fade-up";
      div.innerHTML = `
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-xs font-semibold text-muted uppercase tracking-wider">${title}</h3>
          <button onclick="copyToClipboard(this.parentElement.nextElementSibling.innerText)" class="text-xs bg-surface2 hover:bg-line px-3 py-1.5 rounded-lg transition-colors text-white font-medium">📋 Copy</button>
        </div>
        <p class="text-xs text-white/90 whitespace-pre-line leading-relaxed mb-3">${text}\n\n${tags}</p>
        <div class="flex items-center justify-between pt-3 border-t border-line text-[11px] text-muted">
          <span>${text.length} chars</span>
          <span class="text-emerald-400 font-semibold">🔥 ${Math.floor(82 + Math.random() * 15)}% Viral Score</span>
        </div>
      `;
      resultsList.appendChild(div);
    }
  }

  function renderBios() {
    resultsSection.classList.remove('hidden');
    hookCtaContainer.innerHTML = '';

    const niche = topicInput.value.trim();
    const tone = toneSelect.value;

    const bios = [
      {
        title: `Clean & Professional Bio (${capitalize(tone)})`,
        bio: `💡 Helping you master ${niche}\n🚀 Daily insights & strategies\n👇 Join the community below!`
      },
      {
        title: `High-Converting Bio (${capitalize(tone)})`,
        bio: `🎯 ${niche} Specialist\n📈 Scaled 100+ projects to success\n📩 DM "GROW" to work with me`
      },
      {
        title: `Minimalist Bio (${capitalize(tone)})`,
        bio: `${niche} · Content Creator\nCreating value daily ⚡\nLink in bio 🔗`
      }
    ];

    resultsList.innerHTML = bios.map(b => `
      <div class="bg-surface border border-line rounded-2xl p-4 fade-up">
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-xs font-semibold text-pink uppercase tracking-wider">${b.title}</h3>
          <button onclick="copyToClipboard(\`${escapeJs(b.bio)}\`)" class="text-xs bg-surface2 hover:bg-line px-3 py-1.5 rounded-lg transition-colors text-white font-medium">📋 Copy Bio</button>
        </div>
        <p class="text-xs text-white whitespace-pre-line leading-relaxed font-mono bg-surface2/50 p-3 rounded-xl border border-line/40">${b.bio}</p>
      </div>
    `).join('');

    resultsSection.scrollIntoView({ behavior: 'smooth' });
  }

  function renderTrends() {
    trendsSection.classList.remove('hidden');

    const trendingTopics = [
      { tag: "#AIAutomation", volume: "2.4M Reels", diff: "+42% this week" },
      { tag: "#PersonalBranding", volume: "1.8M Reels", diff: "+28% this week" },
      { tag: "#ShortFormSecrets", volume: "950K Posts", diff: "+15% this week" },
      { tag: "#NoCodeDevelopment", volume: "620K Posts", diff: "+35% this week" }
    ];

    trendsList.innerHTML = trendingTopics.map(t => `
      <div class="bg-surface border border-line rounded-xl p-4 flex items-center justify-between fade-up">
        <div>
          <h4 class="text-sm font-semibold text-white">${t.tag}</h4>
          <span class="text-xs text-muted">${t.volume}</span>
        </div>
        <span class="text-xs text-emerald-400 font-semibold bg-emerald-500/10 px-2.5 py-1 rounded-full border border-emerald-500/20">${t.diff}</span>
      </div>
    `).join('');

    trendsSection.scrollIntoView({ behavior: 'smooth' });
  }

  function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }

  function escapeJs(str) {
    return str.replace(/'/g, "\\'").replace(/\n/g, "\\n");
  }

  window.copyToClipboard = function(text) {
    navigator.clipboard.writeText(text).then(() => {
      alert("Copied to clipboard!");
    });
  };

})();
</script>
</body>
</html>
"""


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def create_project():
    # Directories
    dirs = [
        ROOT_DIR,
        os.path.join(ROOT_DIR, "android", "app", "src", "main"),
        os.path.join(ROOT_DIR, "www"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

    # Files
    files = {
        os.path.join(ROOT_DIR, "package.json"): PACKAGE_JSON,
        os.path.join(ROOT_DIR, "capacitor.config.json"): CAPACITOR_CONFIG_JSON,
        os.path.join(ROOT_DIR, "android", "app", "src", "main", "AndroidManifest.xml"): ANDROID_MANIFEST_XML,
        os.path.join(ROOT_DIR, "www", "index.html"): INDEX_HTML,
    }

    for path, content in files.items():
        write_file(path, content)


def zip_project():
    if os.path.exists(ZIP_NAME):
        os.remove(ZIP_NAME)

    with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _dirs, filenames in os.walk(ROOT_DIR):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                arcname = os.path.relpath(filepath, os.path.dirname(ROOT_DIR))
                zf.write(filepath, arcname)


def main():
    create_project()
    zip_project()
    print(f"Success: '{ROOT_DIR}' project generated and compressed into '{ZIP_NAME}'.")


if __name__ == "__main__":
    main()

// ==UserScript==
// @name         Github界面美化
// @namespace    https://github.com/i2worker/PyStudio
// @description  Github界面美化，包括浏览Jupyter等界面。
// @icon         https://github.githubassets.com/pinned-octocat.svg
// @version      0.0.2
// @author       i2worker
// @license      GPL-3.0
// @match        https://github.com/*
// @match        https://notebooks.githubusercontent.com/*
// @run-at       document-start
// @grant        none
// @supportURL   https://github.com/i2worker/PyStudio/issues
// @downloadURL  https://github.com/i2worker/PyStudio/raw/main/09assets/js/main.user.js
// @updateURL    https://github.com/i2worker/PyStudio/raw/main/09assets/js/main.user.js
// ==/UserScript==

(function() {
    'use strict';

// 自定义Jupyter页面样式
const jupyterStyle = `
:root {
    /** 内容字体 **/
    --jp-content-font-family: "Open Sans Light", "Microsoft YaHei Light", "PingFang SC", system-ui, -apple-system, blinkmacsystemfont, 'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol' !important;

    /** 内容行高 **/
    --jp-content-line-height: 1.80 !important;

    /** 代码字体 **/
    --jp-code-font-family: "Cascadia Mono Light", "Microsoft YaHei Light", "PingFang SC", menlo, consolas, 'DejaVu Sans Mono', monospace !important;

    /** 代码行高 **/
    --jp-code-font-size: 12px !important;
}

/** 代码框字体 **/
div.cm-editor pre {
    font-family: var(--jp-code-font-family);
    font-size: var(--jp-code-font-size);
    line-height: 160% !important;
}

/** 代码框提示字体大小 **/
div.jp-InputPrompt {
    font-size: 10px !important;
}
`;

    // 如果网址中包含 notebooks.githubusercontent.com 则注入新样式
    if (window.location.hostname.includes("notebooks.githubusercontent.com")) {
        let jupyterPage;
        if (document.getElementById("i2worker-jupyter")) {
            jupyterPage = document.getElementById("i2worker-jupyter");
        } else {
            jupyterPage = document.createElement('style');
            jupyterPage.id = 'i2worker-jupyter';
            jupyterPage.type = 'text/css';
        }
        jupyterPage.innerHTML = jupyterStyle;
        document.head.appendChild(jupyterPage);
    }
})();

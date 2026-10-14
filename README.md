# 夏新梦 · 个人学术主页

一个**零依赖的纯静态**个人学术主页：只有 HTML / CSS / JS，没有框架、没有构建步骤、没有 npm 依赖。
放在任何静态托管上都能跑，改内容只需要编辑 `index.html`。

- 目标域名：**https://www.xiaxinmeng.com**
- 视觉风格：学术排版（衬线标题 + 细分隔线 + 留白），浅色 / 深色双主题
- 双语：右上角「中 / EN」一键切换
- 响应式：手机、平板、桌面都适配，支持打印导出为 PDF

---

## 一、目录结构

```
homepage/
├── index.html              ← 主页（所有文字内容都在这里改）
├── 404.html                ← 找不到页面时显示的页面
├── CNAME                   ← 自定义域名（值为 www.xiaxinmeng.com）
├── robots.txt              ← 搜索引擎抓取规则
├── sitemap.xml             ← 站点地图
├── .nojekyll               ← 告诉 GitHub Pages 不要用 Jekyll 处理
├── .gitignore
└── assets/
    ├── css/style.css       ← 所有样式（配色变量集中在文件顶部 :root）
    ├── js/main.js          ← 语言切换 / 主题切换 / 导航高亮
    ├── img/avatar.svg      ← 头像占位图（建议换成你的照片）
    ├── img/favicon.svg     ← 浏览器标签页图标
    └── files/cv.pdf        ← 简历占位 PDF（建议换成你自己的）
```

---

## 二、本地预览

直接双击 `index.html` 即可看到页面。
如果想用本地服务器（更接近线上环境），在项目目录执行：

```bash
# Python 3
python -m http.server 8000
# 然后浏览器打开 http://localhost:8000
```

---

## 三、托管方案怎么选（重要）

> **关键限制：GitHub 免费账号的 Pages 功能只能从「公开仓库」发布。**
> 想让仓库保持 **private** 同时又用 GitHub Pages，需要 GitHub Pro（约 $4/月）。
> 所以「私有仓库 + 完全免费」推荐走 **Cloudflare Pages**，它对私有仓库的支持是免费的。

| 方案 | 仓库是否私有 | 费用 | 难度 | 说明 |
|---|---|---|---|---|
| **A. 私有仓库 + Cloudflare Pages** | ✅ 私有 | 免费 | 易 | **推荐**，免费版支持私有仓库、自动 HTTPS、全球 CDN、带宽不限量 |
| B. 私有仓库 + GitHub Pro + Pages | ✅ 私有 | $4/月 | 易 | 全程留在 GitHub，配置最少 |
| C. 公开仓库 + GitHub Pages | ❌ 源码公开 | 免费 | 易 | 完全免费，但仓库里所有文件任何人可见 |
| D. 私有源码仓库 → Actions 推送到公开 pages 仓库 | ✅ 私有 | 免费 | 中 | 免费版的「私有源码」变通做法，需要配置一个 Token，见附录 |

关于「仅通过域名访问」的实际情况，请先看第六节。

---

## 四、方案 A（推荐）：私有仓库 + Cloudflare Pages

### 1. 把本地项目推到一个私有仓库

先在 GitHub 网页上新建一个仓库，例如 `homepage`，**Visibility 选 Private**，不要勾选任何初始化文件。
然后在本地项目目录执行（把 `你的用户名` 换掉）：

```bash
git init
git add .
git commit -m "init: academic homepage"
git branch -M main
git remote add origin https://github.com/你的用户名/homepage.git
git push -u origin main
```

### 2. 接入 Cloudflare Pages

1. 打开 https://dash.cloudflare.com/ 注册/登录（免费）
2. 左侧 **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
3. 授权 GitHub，选择刚才那个**私有**仓库
4. 构建设置：
   - Framework preset：**None**
   - Build command：**留空**
   - Build output directory：**/**
5. 点 **Save and Deploy**，一分钟后会得到一个 `xxx.pages.dev` 的临时地址，先点开确认页面正常

### 3. 绑定域名 www.xiaxinmeng.com

1. 在 Pages 项目里进入 **Custom domains** → **Set up a custom domain** → 填 `www.xiaxinmeng.com`
2. 按提示操作 DNS：
   - **域名 DNS 已托管在 Cloudflare**：会自动帮你加一条 CNAME 记录，点确认即可
   - **域名在阿里云 / 腾讯云等其他注册商**：把域名的 NS 改成 Cloudflare 给的两个名称服务器（推荐），或者手动添加
     `CNAME  www  →  你的项目名.pages.dev`
3. 等待状态变成 **Active**（通常几分钟）
4. 建议再加一条跳转：`xiaxinmeng.com`（不带 www）→ 301 跳到 `www.xiaxinmeng.com`
   - Cloudflare 后台 → **Rules** → **Redirect Rules** 新建一条即可
5. HTTPS 证书由 Cloudflare 自动签发，无需手动配置

以后每次 `git push`，Cloudflare Pages 会自动重新部署，通常 30 秒 ~ 2 分钟生效。

---

## 五、方案 B / C：用 GitHub Pages

### 步骤

1. 新建仓库。
   - 方案 C：选择 **Public**
   - 方案 B：选择 **Private**（需要 GitHub Pro 订阅，且要在 Settings → Billing 里确认账户支持）
   - 仓库名建议用 `<你的用户名>.github.io`，这样站点直接挂在根路径；用其他名字也可以（比如 `homepage`），只是默认地址会多一层 `/homepage/`
2. 推送代码（命令同方案 A 第 1 步）
3. 仓库 **Settings** → 左侧 **Pages**
   - **Source** 选 `Deploy from a branch`
   - **Branch** 选 `main`，目录选 `/ (root)` → **Save**
4. 等 1–2 分钟，访问 `https://<你的用户名>.github.io/` 应该能看到页面
5. 在 **Pages** 页面 → **Custom domain** 填入 `www.xiaxinmeng.com` → **Save**
   （仓库根目录的 `CNAME` 文件已经写好了同样的值，两边保持一致即可）
6. 等 DNS 检查通过（十几分钟到几小时），勾选 **Enforce HTTPS**

### DNS 记录怎么填

在域名注册商（阿里云、腾讯云、Cloudflare、Namecheap…）的解析设置里添加：

| 类型 | 主机记录 | 记录值 |
|---|---|---|
| CNAME | `www` | `<你的用户名>.github.io` |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |

- `www` 那条是主域名生效的关键；根域（`@`）的 A 记录是为了让 `xiaxinmeng.com` 也能访问，GitHub 会把它跳转到 www。
- 国内注册商注意：境外解析生效通常几分钟，最长可能 24 小时。如果注册商要求「域名实名认证」，先完成认证否则解析会被拦。
- 域名指向 GitHub / Cloudflare 这类境外服务器，**不需要 ICP 备案**；只有将来把站点迁到中国大陆境内的服务器才需要备案。

---

## 六、关于「仅通过域名访问」

几点实际情况，避免踩坑：

1. **GitHub Pages 绑定自定义域名后，访问 `<用户名>.github.io/...` 会自动 301 跳转到 `www.xiaxinmeng.com`**，所以对外来说只有你的域名这一个入口。
2. **Cloudflare Pages 的 `xxx.pages.dev` 默认地址仍然可以直接访问**。如果介意，在 Cloudflare 里加一条 Redirect Rule 把 `*.pages.dev` 跳到主域名；或者干脆只走方案 B/C。
3. **仓库是否 private 与网页是否公开是两件事**。`private` 保护的是源码；而个人主页本身只要挂在网上，任何知道域名的人都能打开。互联网上没有「只有我知道的公开网页」。
4. **不想被搜索引擎收录**：`index.html` 的 `<head>` 里已经留好了一行注释，把

   ```html
   <!-- <meta name="robots" content="noindex,nofollow"> -->
   ```

   的注释符去掉即可；同时可以把 `robots.txt` 改成 `Disallow: /`。
   反过来，学术主页通常**希望**被搜到（方便同行找到你），所以默认保持允许收录。

---

## 七、以后怎么改内容

### 换文字

所有文字都在 `index.html` 里，用中文注释标了分区（关于我 / 近期动态 / 研究方向 / 发表论文 / 科研项目 / 教学与学术服务 / 联系方式）。

双语元素长这样：

```html
<p data-zh="中文内容" data-en="English content">中文内容</p>
```

只改 `data-zh` 和 `data-en`，**标签中间那份也要一起改**（浏览器加载瞬间显示的是它，避免闪烁）。

### 增加一篇论文

复制 `index.html` 里任意一个 `<li class="pub"> … </li>` 整块，粘到对应年份的 `<ol class="pubs">` 里，改标题和作者即可。
把「本人姓名」用 `<b>…</b>` 包起来，样式已经处理好了。

### 增加一个新板块

1. 复制一整段 `<section id="xxx" class="section"> … </section>`，改 `id` 和内容
2. 在顶部导航 `<nav class="topbar__nav">` 里加一行 `<a href="#xxx" data-zh="…" data-en="…">…</a>`

按钮高亮、锚点跳转都是自动的，不用改 JS。

### 换头像 / 简历

- 头像：把 `assets/img/avatar.svg` 换成你的照片，命名保持一致即可（推荐正方形、≥400×400）。用 JPG/PNG 的话记得同时改 `index.html` 里 `<img class="avatar" src="...">` 的路径。
- 简历：把你的 CV 命名为 `cv.pdf` 覆盖掉 `assets/files/cv.pdf`。

### 换配色

打开 `assets/css/style.css`，最上面的 `:root` 里改这几个变量就能整体换风格：

```css
--accent: #1c4e8a;   /* 主色：链接、下划线、按钮 */
--text:   #1c1f24;   /* 正文颜色 */
--bg:     #ffffff;   /* 背景色 */
```

---

## 八、常见问题

**打开域名显示 404 / Not Found**
仓库里必须有一个叫 `index.html` 的**根目录**文件；确认 Pages 的 Source 选的是 `main` + `/ (root)`。

**域名打不开，浏览器提示 DNS 解析错误**
先用 `nslookup www.xiaxinmeng.com` 看是否解析到了 `185.199.108.153` 这一类地址。解析没生效通常是：记录填错、还没过 TTL、或者域名没完成实名认证。

**HTTPS 一直转圈 / 无法签发证书**
DNS 刚改完要等 GitHub 重新校验，通常几小时。确认 CNAME 里没有多余的空格，且只有一个域名。

**改了代码但网站没变**
浏览器缓存（Ctrl+F5 强刷），或部署还在队列里（GitHub Pages/Cloudflare 一般 1–2 分钟）。

**想让 www 和裸域都能开**
裸域用上表里的 A/AAAA 记录，然后以 `www` 为主域名；GitHub 会自动把裸域跳转到 www。Cloudflare 用 Redirect Rule 达到同样效果。

---

## 附录：方案 D —— 私有源码 + 免费的 GitHub Pages

原理：源码放在私有仓库，用 GitHub Actions 在云端把产物推送到另一个**公开**仓库，由那个公开仓库提供 Pages 服务。

1. 新建一个公开仓库（如 `xiaxinmeng.github.io`），用来承载网页
2. 生成一个 Personal Access Token（Settings → Developer settings → Fine-grained tokens），只授予对该公开仓库的 `Contents: Read and write` 权限
3. 在私有仓库里添加 Secret：Settings → Secrets and variables → Actions → `PAGES_TOKEN`
4. 在私有仓库新增 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to public pages repo
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Push site to public repo
        uses: peaceiris/actions-gh-pages@v4
        with:
          personal_token: ${{ secrets.PAGES_TOKEN }}
          external_repository: 你的用户名/xiaxinmeng.github.io
          publish_branch: main
          publish_dir: ./
          cname: www.xiaxinmeng.com
```

5. 之后在公开仓库的 Settings → Pages 里按第五节配置即可

> 注意：这个方案下网页文件在公开仓库中可见（这是 GitHub Pages 免费版的固有限制），只是「源码工程」保持私有。如果你的源码和网页本来就是同一份文件（本项目就是纯静态），那方案 C 和方案 D 的效果基本一样 —— 这种情况下推荐直接用方案 A 或方案 C。

---

最后更新：2026-10-14

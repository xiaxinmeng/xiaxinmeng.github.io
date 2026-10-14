# 夏新梦 · 个人学术主页

| | |
|---|---|
| 线上仓库 | `git@github.com:xiaxinmeng/xiaxinmeng.github.io.git` |
| 目标域名 | **https://www.xiaxinmeng.com** |
| 默认地址 | https://xiaxinmeng.github.io/ （绑定域名后会 301 跳转到你的域名） |
| 本地目录 | `C:\Users\xiaxi\Desktop\project\homepage` |

一个**零依赖的纯静态**个人学术主页：只有 HTML / CSS / JS，没有框架、没有构建步骤、没有 npm 依赖。
改内容只需要编辑 `index.html`。

- 学术排版：衬线标题 + 细分隔线 + 大留白，浅色 / 深色双主题
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
├── .gitattributes          ← 二进制文件不做换行符转换（别删）
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

直接双击 `index.html` 即可。想用本地服务器：

```bash
python -m http.server 8000
# 浏览器打开 http://localhost:8000
```

---

## 三、当前的部署方案

仓库 `xiaxinmeng.github.io` **已经存在、且是 public 的空仓库**，所以直接走 GitHub Pages 就行 —— 免费，不用配置任何 CI。

- 仓库名 `xiaxinmeng.github.io` 是 GitHub 的**用户站点仓库**，站点直接挂在根路径 `/`，所以 `index.html` 放在根目录是正确的。
- 文件名必须是 `<你的用户名>.github.io`，且在这个用户名下只能有一个。它**必须保持 public** 才能在免费账号下开启 Pages。

> ✅ 已确认仓库保持 **public**。免费账号的 GitHub Pages 只支持 public 仓库，这个选择刚好合适，不需要任何付费。附录 A 里保留了「将来想改成私有」的做法，用不到可以忽略。

---

## 四、推送代码

推送通道已经配好了，你只需要做三步。

### 1. 把公钥添加到 GitHub

浏览器打开 https://github.com/settings/keys → **New SSH key** → Title 随便填（例如 `xiaxi-desktop`），Key type 选 **Authentication Key**，把下面这一整行粘进去：

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJkInA3SdkmRwQLHJtDgF9Fs0o5czhJRXih6jKamzTYM 663979162@qq.com
```

> 如果打不开 github.com 网页：这是网络问题，跟仓库无关。可以试试手机热点，或者开代理/VPN 后再添加。

### 2. 验证连接

```bash
ssh -T git@github.com
```

出现 `Hi xiaxinmeng! You've successfully authenticated...` 就成功了（这句提示里不会给你 shell，[退出码是 1 属于正常](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)）。

### 3. 推送

```bash
cd "C:\Users\xiaxi\Desktop\project\homepage"
git push -u origin main
```

### 关于网络（已经替你处理好了）

实测你这台机器：国内站点 0.1 秒通，但 **`github.com:443` 直连超时**；而 SSH 的 22 端口和 `ssh.github.com:443` 都能连上。
所以 `C:\Users\xiaxi\.ssh\config` 里已经把 `github.com` 指向 `ssh.github.com:443`，走 SSH 推送比 HTTPS 稳得多，以后不用再改。

以后日常提交就是：

```bash
git add .
git commit -m "更新内容"
git push
```

### 如果 github.com 网页也打不开

这是网络问题，不是账号或仓库的问题。实测你这台机器（2026-10-14）：

| 访问目标 | 结果 |
|---|---|
| `www.baidu.com` | ✅ 通，0.1 秒 |
| `https://github.com` | ❌ 超时（换成美国/新加坡的 IP 重试也一样 → **是按域名拦截的，改 hosts 文件没用**） |
| `https://www.github.com`、`gist.github.com` | ❌ 超时 |
| `https://api.github.com` | ✅ 通，0.3 秒 |
| `codeload.github.com`、`objects.githubusercontent.com` | ✅ 通 |
| `ssh.github.com:443`、`github.com:22` | ✅ 通 |

所以：**命令行推代码没问题，但网页打不开。** 三条路，按省事程度排序：

**路线 1 · 挂代理 / VPN（最省事，推荐）**
后面「开启 Pages」「绑定域名」也都要在网页上点，所以迟早需要能打开 github.com。装一个代理软件，浏览器能打开 github.com 之后，按第五节操作即可。

**路线 2 · 用手机操作**
如果手机能打开 github.com，就在手机上完成「添加 SSH key」和「开启 Pages、绑定域名」这些网页操作。把公钥发到手机上最方便的方式是通过微信「文件传输助手」粘贴给自己。

**路线 3 · 完全不动网页，走 API（因为 api.github.com 是通的）**
只要有一个 GitHub Token，就能用接口一次性完成「登记 SSH 公钥 + 开启 Pages + 绑定域名」，全程不需要打开 github.com。

1. 在任意能打开 GitHub 的设备上（手机也行）创建 Token：
   - 打开 https://github.com/settings/tokens → **Generate new token (classic)**
   - 勾选两个 scope：**`repo`** 和 **`admin:public_key`**
   - 生成后复制那串 `ghp_...`（只显示一次）
2. 回到这台电脑，在项目目录执行（把 `ghp_xxx` 换成你的 Token）：

```bash
cd "C:\Users\xiaxi\Desktop\project\homepage"
export GITHUB_TOKEN=ghp_xxx
PYTHONIOENCODING=utf-8 python "$HOME/.workbuddy/skills/personal-homepage-site/scripts/configure_github_pages.py" \
  --repo xiaxinmeng/xiaxinmeng.github.io \
  --key ~/.ssh/id_ed25519.pub \
  --domain www.xiaxinmeng.com
```

脚本会依次：校验 Token → 登记 SSH 公钥（已登记过会自动跳过）→ 开启 Pages（`main` / 根目录）→ 绑定 `www.xiaxinmeng.com` 并开启强制 HTTPS → 打印最终状态。想先空跑看看做了什么，加 `--dry-run`。

3. 完事后建议把这个 Token 删掉：https://github.com/settings/tokens

> ⚠️ 不要为了打开 GitHub 去用不知名的「GitHub 镜像站 / 加速站」并登录账号——你的账号密码和 Token 会经过第三方服务器。要么挂代理，要么用手机，要么走上面这条 API 路线。


---

## 五、开启 GitHub Pages 并绑定域名

1. 仓库 **Settings** → 左侧 **Pages**
2. **Source** 选 `Deploy from a branch` → **Branch** 选 `main` → 目录选 `/ (root)` → **Save**
3. 等 1–2 分钟，浏览器打开 https://xiaxinmeng.github.io/ 应该能看到页面
4. 回到 **Pages** 页面 → **Custom domain** 填入 `www.xiaxinmeng.com` → **Save**
   （仓库根目录的 `CNAME` 文件已经写好了同样的值，两边保持一致即可）
5. 等 DNS 检查通过（十几分钟到几小时），勾选 **Enforce HTTPS**

---

## 六、DNS 记录

在域名注册商（阿里云、腾讯云、Cloudflare、Namecheap…）的解析设置里添加：

| 类型 | 主机记录 | 记录值 |
|---|---|---|
| CNAME | `www` | `xiaxinmeng.github.io` |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |

- `www` 那条是关键，必须填 `xiaxinmeng.github.io`，**不要**填完整 URL、不要带 `https://`、末尾不要加点。
- 根域（`@`）的 A/AAAA 记录是为了让 `xiaxinmeng.com` 也能访问，GitHub 会自动把它跳转到 www。
- 国内注册商注意：如果注册商要求域名实名认证，先完成认证，否则解析会被拦。
- 域名指向 GitHub 的境外服务器，**不需要 ICP 备案**；只有将来把站点搬到中国大陆境内的服务器才需要。
- 验证：`nslookup www.xiaxinmeng.com` 应该返回 `185.199.108.153` 这类地址。

### 关于「仅通过域名访问」

1. 绑定自定义域名后，访问 `xiaxinmeng.github.io` 会被 GitHub 自动 301 跳转到 `www.xiaxinmeng.com`，对外只有你的域名这一个入口。
2. **仓库 public ≠ 网页被索引**，但反过来也成立：**仓库 public 意味着源码任何人可见**。个人主页本身没什么秘密，一般不必在意。
3. **不想被搜索引擎收录**：把 `index.html` 的 `<head>` 里这一行的注释符去掉

   ```html
   <!-- <meta name="robots" content="noindex,nofollow"> -->
   ```

   同时把 `robots.txt` 改成 `Disallow: /`。学术主页通常**希望**被搜到（方便同行找到你），所以默认保持允许收录。

---

## 七、以后怎么改内容

### 换文字

所有文字都在 `index.html` 里，用中文注释标了分区（关于我 / 近期动态 / 研究方向 / 发表论文 / 科研项目 / 教学与学术服务 / 联系方式）。

双语元素长这样：

```html
<p data-zh="中文内容" data-en="English content">中文内容</p>
```

只改 `data-zh` 和 `data-en`，**标签中间那份也要一起改**（首屏在 JS 执行前显示的是它，避免闪烁）。

### 增加一篇论文

复制任意一个 `<li class="pub"> … </li>` 整块，粘到对应年份的 `<ol class="pubs">` 里，改标题和作者即可。
本人姓名用 `<b>…</b>` 包起来，样式已经处理好了。

### 增加一个新板块

1. 复制一整段 `<section id="xxx" class="section"> … </section>`，改 `id` 和内容
2. 在顶部导航 `<nav class="topbar__nav">` 里加一行 `<a href="#xxx" data-zh="…" data-en="…">…</a>`

按钮高亮、锚点跳转都是自动的，不用改 JS。

### 换头像 / 简历

- 头像：把 `assets/img/avatar.svg` 换成你的照片，文件名保持一致即可（推荐正方形、≥400×400）。如果用 JPG/PNG，记得同时改 `index.html` 里 `<img class="avatar" src="...">` 的路径。
- 简历：把你的 CV 命名为 `cv.pdf` 覆盖 `assets/files/cv.pdf`。

### 换配色

打开 `assets/css/style.css`，改最上面 `:root` 里的几个变量就能整体换风格：

```css
--accent: #1c4e8a;   /* 主色：链接、下划线、按钮 */
--text:   #1c1f24;   /* 正文颜色 */
--bg:     #ffffff;   /* 背景色 */
```

### 改完自检

```bash
PYTHONIOENCODING=utf-8 python "$HOME/.workbuddy/skills/personal-homepage-site/scripts/check_html.py" index.html 404.html
```

会检查标签是否闭合、`data-zh` / `data-en` 是否配对、引用的本地文件是否存在。

---

## 八、常见问题

**推送时提示 `Permission denied (publickey)`**
公钥还没加到 GitHub，回到第四节的第 1 步。

**推送时提示连接超时**
先 `ssh -T git@github.com` 看是否能认证。如果是网络原因，试试手机热点或代理。

**打开域名显示 404**
仓库里必须有一个叫 `index.html` 的**根目录**文件；确认 Pages 的 Source 选的是 `main` + `/ (root)`。

**域名打不开，提示 DNS 解析错误**
`nslookup www.xiaxinmeng.com` 看是否解析到 `185.199.108.153` 一类地址。没生效通常是：记录填错、TTL 没到、域名未实名认证。

**HTTPS 一直转圈 / 无法签发证书**
DNS 改完要等 GitHub 重新校验，通常几小时。确认 `CNAME` 文件里只有一个域名、前后没有空格。

**改了代码但网站没变**
浏览器缓存（Ctrl+F5 强刷），或部署还在队列里（一般 1–2 分钟）。

---

## 附录 A：想把仓库改成 private 怎么办

免费账号的 GitHub Pages 不支持 private 仓库。两条路：

**路线 1 · 升级 GitHub Pro**（约 $4/月）
把仓库改成 private，其余步骤完全不变。

**路线 2 · 换成 Cloudflare Pages**（免费，支持私有仓库）
1. 把仓库改成 private
2. https://dash.cloudflare.com → **Workers & Pages** → **Create** → **Pages** → **Connect to Git** → 选这个仓库
3. 构建设置：Framework preset **None**，Build command **留空**，Build output directory **/**
4. **Custom domains** 里绑定 `www.xiaxinmeng.com`，按提示加 DNS 记录
5. 以后每次 `git push` 自动重新部署，30 秒 ~ 2 分钟生效

注意：用 Cloudflare Pages 时，仓库名是不是 `xiaxinmeng.github.io` 就无所谓了，它只是个名字。

---

## 附录 B：本次完成情况

- [x] 站点搭建（首页 + 404 + 样式 + 脚本 + 占位头像/CV）
- [x] 部署配置文件（`CNAME` / `.nojekyll` / `robots.txt` / `sitemap.xml` / `.gitattributes`）
- [x] 本地 git 仓库初始化并完成首次提交
- [x] 远程地址关联到 `xiaxinmeng/xiaxinmeng.github.io`
- [x] 生成 SSH 密钥并配置 `~/.ssh/config`（走 `ssh.github.com:443` 绕过直连限制）
- [ ] **把公钥添加到 GitHub**（需要你在浏览器操作，见第四节）
- [ ] 推送代码
- [ ] 开启 Pages、绑定域名、配置 DNS 解析
- [ ] 用真实资料替换页面上的占位内容

最后更新：2026-10-14


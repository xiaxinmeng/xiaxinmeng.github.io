# 夏新梦 · 个人学术主页

| | |
|---|---|
| 访问地址 | **https://xiaxinmeng.github.io/** |
| 线上仓库 | `git@github.com:xiaxinmeng/xiaxinmeng.github.io.git` |
| 自定义域名 | 暂不购买，将来想用再加（例如 `www.xiaxinmeng.com`，见第五节） |
| 本地目录 | `C:\Users\xiaxi\Desktop\project\homepage` |

一个**零依赖的纯静态**个人学术主页：只有 HTML / CSS / JS，没有框架、没有构建步骤、没有 npm 依赖。
改内容只需要编辑 `index.html`。

- 学术排版：衬线标题 + 细分隔线 + 大留白，浅色 / 深色双主题
- 双语：右上角「中 / EN」一键切换
- 响应式：手机、平板、桌面都适配，支持打印导出为 PDF

### 当前进度（截至 2026-10-14）

| 步骤 | 状态 |
|---|---|
| 站点搭建 | ✅ 完成 |
| 代码推送到 GitHub | ✅ 完成（`main` 分支，与远程同步） |
| GitHub Pages 上线 | ✅ 自动开启并构建成功 |
| **访问地址** | ✅ **https://xiaxinmeng.github.io/** 已可访问，HTTPS 证书正常 |
| 自定义域名 | ⏸ 已调研免费方案（见第五节）：可用 `xiaxinmeng.is-a.dev`，**国内实测可访问**，待用户决定是否申请 |
| 页面内容 | ⏸ 仍是占位文字，等真实资料 |

> 说明：原先仓库里的 `CNAME` 曾把站点绑定到 `www.xiaxinmeng.com`，但该域名未注册，导致两个地址都打不开。
> 现已移除 `CNAME`，全站引用（canonical / og:url / sitemap / robots / 联系方式）统一改回 `xiaxinmeng.github.io`。


---

## 一、目录结构

```
homepage/
├── index.html              ← 主页（所有文字内容都在这里改）
├── 404.html                ← 找不到页面时显示的页面
├── robots.txt              ← 搜索引擎抓取规则
├── sitemap.xml             ← 站点地图
├── .nojekyll               ← 告诉 GitHub Pages 不要用 Jekyll 处理
├── .gitattributes          ← 二进制文件不做换行符转换（别删）
├── .gitignore
├── tools/
│   └── set-domain.py       ← 一键切换站点域名（将来绑域名时用）
└── assets/
    ├── css/style.css       ← 所有样式（配色变量集中在文件顶部 :root）
    ├── js/main.js          ← 语言切换 / 主题切换 / 导航高亮
    ├── img/avatar.svg      ← 头像占位图（建议换成你的照片）
    ├── img/favicon.svg     ← 浏览器标签页图标
    └── files/cv.pdf        ← 简历占位 PDF（建议换成你自己的）
```

> 没有 `CNAME` 文件是**故意**的：它只在绑定自定义域名时才需要。将来绑域名时 `tools/set-domain.py` 会自动创建。

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

## 五、免费自定义域名的真相（2026-10 调研）

先纠正一个常见误解：

> **GitHub Pages 支持免费「绑定」自定义域名，但 GitHub 本身不发域名。**

GitHub 提供的是：无限个自定义域名随便绑、免费自动签发 Let's Encrypt 证书、免费 HTTPS 强制跳转。
**域名本身**得从别处来——要么花钱买，要么从免费子域名服务白拿。

### 5.0 三条路对比

| 方案 | 费用 | 地址长相 | 国内可访问 | 风险 |
|---|---|---|---|---|
| **A. 保持现状** | 0 | `xiaxinmeng.github.io` | ✅ 已实测 | 无 |
| **B. is-a.dev 免费子域** | 0 | `xiaxinmeng.is-a.dev` | ✅ **已实测可用** | 需人工审核；服务由志愿者维护 |
| **C. 买 `.com`** | ¥60–90/年 | `www.xiaxinmeng.com` | ✅ | 每年续费；不续费会被人抢注 |
| ~~D. us.kg / DigitalPlat~~ | 0 | `xxx.us.kg` | ❌ **实测 DNS 解析失败** | 不要用 |
| ~~E. Freenom（.tk/.ml/.ga/.cf）~~ | 0 | — | — | **已停止新注册**，网上那些「镜像站」别碰 |

**其他被排除的选项**

- **eu.org**（1996 年至今的老牌免费域名）：`nic.eu.org` 申请入口能打开，但 `www.eu.org` 实测**连接失败（HTTP 000）**，国内可达性不确定；人工审核 3–7 天到数周。可以试，但不如 is-a.dev 稳。
- **GitHub Student Developer Pack**：认证学生可领 **Namecheap 免费 `.me` 域名一年**。真免费且是正规顶级域，但要学生身份证明，且**第二年开始收费**（约 $15/年），到期不转会丢失。如果你是学生，这条路比 is-a.dev 更正式。
- **js.org**：只给 JavaScript 开源项目，个人学术主页不符合。

### 5.1 路线 B：申请 `xiaxinmeng.is-a.dev`（推荐尝试）

**已核实的现状（2026-10-14）**

- 服务由社区志愿者运营，DNS 托管在 Cloudflare（Project Alexandria 赞助），仓库 10k+ star，活跃维护
- 用 GitHub **提 Pull Request** 的方式注册，不要钱、不要邮箱验证之外的东西
- **`xiaxinmeng.is-a.dev`、`xinmeng.is-a.dev` 目前都还没被占用**（已用 GitHub API 逐个查过 `domains/*.json`）
- **国内可访问性已实测**：随机抽了 4 个指向 GitHub Pages 的 is-a.dev 子域，从这台机器访问**全部 HTTP 200**，解析到 `185.199.10x.153`（GitHub Pages 的 IP），耗时 2.8–4.0 秒。也就是说「is-a.dev 子域 + GitHub Pages」这个组合在国内是能正常打开的。

**⚠️ 申请前必须知道的三件事**

1. **内容有领域限制。** ToS 规定「根子域（`yourname.is-a.dev`）**必须与软件开发相关**」，明确禁止「不是主要关于软件开发的博客」。如果你研究方向是计算机/软件，学术主页大概率能过；如果是其他学科，**有被拒的风险**，建议改用嵌套子域（如 `me.xiaxinmeng.is-a.dev`）或走路线 C。
2. **禁止用 AI 代写 PR。** ToS 原文：强烈反对用 Claude Code / Codex 等 AI 生成 Pull Request，违者**关闭 PR 并可能封禁账号**。所以下面这个文件**请你自己手动敲**（就 7 行），不要让我或任何 AI 代提交。这不是我推脱——替你提交等于把你账号架在火上。
3. **需要能打开 github.com 网页。** Fork、建文件、提 PR 都得在网页上操作，而这台机器打不开 github.com（见第四节）。**用手机完成，或者挂代理。**

**申请步骤**

1. 手机或代理打开 https://is-a.dev ，搜一下想要的名字确认没被占
2. Fork https://github.com/is-a-dev/register
3. 在 `domains/` 目录下新建 `xiaxinmeng.json`（名字换成你要的），手动写入：

   ```json
   {
       "owner": {
           "username": "xiaxinmeng",
           "email": "663979162@qq.com"
       },
       "records": {
           "CNAME": "xiaxinmeng.github.io"
       }
   }
   ```

   - 字段名是 `records`（复数），写成 `record` 会被 CI 直接刷掉
   - `username` 必须和提 PR 的 GitHub 账号一致，否则会被拒
   - CNAME 值**不要**带 `https://`、不要带末尾的点
   - JSON 提交前用 https://jsonlint.com 验一下语法

4. 提 Pull Request，**留意 review 意见**，被要求修改就照改，不改会被直接关闭
5. 合并后几分钟内 DNS 生效。**然后才**做下一步（顺序不能反）：

   ```bash
   cd "C:\Users\xiaxi\Desktop\project\homepage"
   python tools/set-domain.py xiaxinmeng.is-a.dev
   git add . && git commit -m "绑定 is-a.dev 子域" && git push
   ```

   脚本会自动创建 `CNAME` 文件并改齐全站引用。

6. 推送后如果打开是 404，去仓库 **Settings → Pages → Custom domain** 填 `xiaxinmeng.is-a.dev`（其实 `CNAME` 文件已经生效，通常不用手填），并勾上 **Enforce HTTPS**

> 🔁 **万一被拒或服务哪天没了**，一条命令回到默认地址，站点立刻恢复：
> ```bash
> python tools/set-domain.py xiaxinmeng.github.io
> ```

### 5.2 路线 C：买 `.com`

**`xiaxinmeng.com` 目前还没有被注册**（向 VeriSign 查询的结果是 `No match for "XIAXINMENG.COM"`），先买下来：

| 注册商 | 价格参考 | 说明 |
|---|---|---|
| 阿里云 / 腾讯云 | .com 首年约 ¥60–90 | 国内最省事，支付宝付款，DNS 解析免费；需要域名实名认证（一般几分钟到几小时） |
| Cloudflare / Namecheap | 约 $10/年 | 无实名要求，但需要外币支付方式 |

买完之后，域名会有一个**管理后台 → DNS 解析设置**的入口，下一步就在那里操作。

### 5.3 用脚本一次性改齐全站域名

站点地址散落在 5 个文件里（`CNAME` / `index.html` 的 canonical 与 og:url / `404.html` / `robots.txt` / `sitemap.xml`），手动改很容易漏。用脚本一条命令搞定，**路线 B 和路线 C 都用它**：

```bash
cd "C:\Users\xiaxi\Desktop\project\homepage"

# 路线 B：is-a.dev 免费子域
python tools/set-domain.py xiaxinmeng.is-a.dev

# 路线 C：买的 .com
python tools/set-domain.py www.xiaxinmeng.com
```

它会自动创建 `CNAME`，并把所有引用改到新域名（邮件地址不会被误改）。想先看会改什么，加 `--dry-run`。

改完提交推送：

```bash
git add . && git commit -m "绑定自定义域名" && git push
```

想改回默认地址，同样一条命令：

```bash
python tools/set-domain.py xiaxinmeng.github.io
```

> 脚本靠 `KNOWN_HOSTS` 列表识别旧域名。**如果换成上表之外的域名，先把新域名加进 `tools/set-domain.py` 顶部的 `KNOWN_HOSTS`**，否则下次再切换时旧域名认不出来、替换不掉。

### 5.4 加 DNS 记录（仅路线 C 需要）

> 走路线 B（is-a.dev）**不需要这一节**——DNS 由 is-a.dev 托管，你只在 PR 的 JSON 里写一条 CNAME。
> 下面这张表是买了 `.com` 之后在注册商后台填的。

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

- `www` 那条是关键。填 `xiaxinmeng.github.io`，**不要**带 `https://`、不要带路径、末尾不要加点。
- 主机记录：阿里云/腾讯云里 `www` 就填 `www`，根域填 `@`。
- 根域（`@`）的 A/AAAA 记录是为了让 `xiaxinmeng.com` 也能访问，GitHub 会自动把它跳转到 www。
- 如果注册商要求域名实名认证，先完成认证，否则解析会被拦。
- 域名指向 GitHub 的境外服务器，**不需要 ICP 备案**；只有将来把站点搬到中国大陆境内的服务器才需要。

### 5.5 验证解析是否生效

```bash
nslookup www.xiaxinmeng.com
```

返回 `185.199.108.153` 这类地址就说明生效了（通常几分钟，最长 24 小时）。也可以用：

```bash
PYTHONIOENCODING=utf-8 python -c "import socket; print(socket.gethostbyname('www.xiaxinmeng.com'))"
```

### 5.6 打开 HTTPS

解析生效后，到仓库 **Settings → Pages**：

- Custom domain 一栏应该已经是新域名（因为仓库里的 `CNAME` 文件已经生效，不用手动再填）
- 等状态变成 **Active** 后，勾选 **Enforce HTTPS**
- 证书由 Let's Encrypt 自动签发，如果一直转圈，通常是在等 DNS 重新校验，等几小时再看
- 如果报 SSL 错误，勾上 Enforce HTTPS 基本就能解决（is-a.dev 官方 FAQ 也是这么说的）

> 说明：Pages 本身在代码推送时就已经**自动开启**了（仓库名是 `<用户名>.github.io` 的用户站点仓库，GitHub 会自动处理），Source 是 `main` / 根目录，不需要再去设置。

> ⚠️ **顺序很重要：先拿到域名（PR 已合并 / 域名已解析），最后再改站点域名（5.3）。** 反过来做会让 `xiaxinmeng.github.io` 立刻 301 跳到一个并不存在的域名，站点整个打不开 —— 这次就踩过这个坑。
> 万一真踩了，执行 `python tools/set-domain.py xiaxinmeng.github.io` 改回来即可。

---

## 六、关于「仅通过域名访问」

1. 目前站点只有 `https://xiaxinmeng.github.io/` 一个地址，没有别的入口。
2. 将来绑定自定义域名后，访问 `xiaxinmeng.github.io` 会被 GitHub 自动 301 跳转到你的域名。
3. **仓库 public ≠ 网页被索引**，但反过来也成立：**仓库 public 意味着源码任何人可见**。个人主页本身没什么秘密，一般不必在意。
4. **不想被搜索引擎收录**：把 `index.html` 的 `<head>` 里这一行的注释符去掉

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

**网站打不开，浏览器一直跳到一个打不开的地址**
说明 `CNAME` 文件指向了一个没有注册、或还没解析的域名，而 GitHub 会无条件把 `github.io` 跳过去。
执行 `python tools/set-domain.py xiaxinmeng.github.io` 就能立刻恢复。

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
- [x] 部署配置文件（`.nojekyll` / `robots.txt` / `sitemap.xml` / `.gitattributes`）
- [x] 本地 git 仓库初始化，分支统一为 `main`
- [x] 远程地址关联到 `xiaxinmeng/xiaxinmeng.github.io`（SSH 形式）
- [x] 生成 SSH 密钥、配置 `~/.ssh/config`（走 `ssh.github.com:443`），公钥已添加到 GitHub
- [x] 代码已推送，`main` 与 `origin/main` 同步
- [x] GitHub Pages 自动开启并构建成功
- [x] **站点正式上线：https://xiaxinmeng.github.io/**（HTTPS 证书正常，各静态资源均 200）
- [x] 决定暂不购买域名，移除 `CNAME`，全站域名引用统一为 `xiaxinmeng.github.io`
- [x] 新增 `tools/set-domain.py`，将来绑定/切换域名一条命令搞定
- [ ] 用真实资料替换页面上的占位内容（姓名、单位、导师、论文、链接、CV、头像）

最后更新：2026-10-14



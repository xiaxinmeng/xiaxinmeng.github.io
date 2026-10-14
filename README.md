# 夏昕濛 · 个人学术主页

| | |
|---|---|
| 访问地址 | **https://xiaxinmeng.github.io/** |
| 仓库 | `git@github.com:xiaxinmeng/xiaxinmeng.github.io.git`（public，推送后 Pages 自动部署） |
| 本地目录 | `C:\Users\xiaxi\Desktop\project\homepage` |

零依赖纯静态站点：只有 HTML / CSS / JS，无框架、无构建。浅色 / 深色双主题、中 / EN 双语切换、响应式、可打印为 PDF。

## 目录结构

```
homepage/
├── index.html              ← 主页（所有文字内容都在这里改）
├── 404.html                ← 找不到页面时显示的页面
├── robots.txt              ← 搜索引擎抓取规则
├── sitemap.xml             ← 站点地图
├── .nojekyll               ← 告诉 GitHub Pages 不要用 Jekyll 处理
├── .gitattributes          ← 二进制文件不做换行符转换（别删）
├── tools/
│   └── set-domain.py       ← 一键切换站点域名（绑域名时用）
└── assets/
    ├── css/style.css       ← 所有样式（配色变量集中在顶部 :root）
    ├── js/main.js          ← 语言切换 / 主题切换 / 导航高亮
    ├── img/avatar.svg      ← 头像占位图（换成照片时保持文件名）
    ├── img/favicon.svg     ← 浏览器标签页图标
    └── files/cv.pdf        ← 简历占位 PDF（换成自己的时保持文件名）
```

## 本地预览

双击 `index.html` 即可，或：

```bash
python -m http.server 8000
```

## 日常改内容

所有文字都在 `index.html`，用中文注释分区。双语写法（**标签中间那份也要同步改**，首屏显示的是它）：

```html
<p data-zh="中文内容" data-en="English content">中文内容</p>
```

- **加论文**：复制一整块 `<li class="pub"> … </li>` 粘到对应年份的 `<ol class="pubs">` 里；本人姓名用 `<b>…</b>` 包裹。
- **加板块**：复制一段 `<section id="xxx" class="section"> … </section>`，再在顶部导航加一行 `<a href="#xxx" data-zh="…" data-en="…">…</a>`；JS 无需改动。
- **换头像 / 简历**：覆盖 `assets/img/avatar.svg`、`assets/files/cv.pdf`，文件名不变（JPG/PNG 需同步改 `index.html` 里的 `src`）。
- **换配色**：改 `assets/css/style.css` 顶部 `:root` 里的变量。

改完自检：

```bash
PYTHONIOENCODING=utf-8 python "$HOME/.workbuddy/skills/personal-homepage-site/scripts/check_html.py" index.html 404.html
```

## 推送与部署

```bash
git add . && git commit -m "更新内容" && git push
```

推送后 Pages 自动构建，1–2 分钟生效。SSH 通道已配好（`github.com` 走 `ssh.github.com:443`）。若 github.com **网页**打不开，是网络按域名拦截，与仓库无关：网页操作（设置、绑域名）用手机或代理完成，命令行推送不受影响。

## 自定义域名（可选，当前未绑定）

GitHub Pages 只免费**绑定**域名并签发 HTTPS 证书，**不发域名**。不绑定时仓库里**不要有 `CNAME` 文件**（有则 `github.io` 会 301 跳走）。

切换 / 回退都是一条命令（自动增删 `CNAME` 并改齐全站引用）：

```bash
python tools/set-domain.py <新域名>            # 如 xiaxinmeng.is-a.dev 或 www.xiaxinmeng.com
python tools/set-domain.py xiaxinmeng.github.io  # 回默认地址
```

> ⚠️ 顺序：先拿到域名（PR 已合并 / DNS 已生效），**最后**再改站点域名。反了会两个地址都打不开；万一踩坑，用上面第二条命令恢复。

### 方案 1 · is-a.dev 免费子域（国内实测可访问）

- `xiaxinmeng.is-a.dev` 未被占用；在 https://github.com/is-a-dev/register 提 PR 注册，免费。
- ToS 禁止 AI 生成 PR，**必须自己在网页上手提**（本机打不开 github.com，用手机或代理）。`domains/xiaxinmeng.json` 内容：

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

  字段名是 `records`（复数）；`username` 须与提 PR 的账号一致。
- PR 合并、DNS 生效后，再执行 `set-domain.py`。

### 方案 2 · 买 `.com`（`xiaxinmeng.com` 尚未被注册）

在注册商后台（阿里云 / 腾讯云，首年约 ¥60–90）添加解析：

| 类型 | 主机记录 | 记录值 |
|---|---|---|
| CNAME | `www` | `xiaxinmeng.github.io` |
| A | `@` | `185.199.108.153` / `185.199.109.153` / `185.199.110.153` / `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` / `2606:50c0:8001::153` / `2606:50c0:8002::153` / `2606:50c0:8003::153` |

解析生效后（`nslookup www.xiaxinmeng.com` 返回上述 IP），到仓库 **Settings → Pages** 勾选 **Enforce HTTPS**，证书由 Let's Encrypt 自动签发。

## 常见问题

- **站点跳转到打不开的地址**：`CNAME` 指向了未注册 / 未解析的域名，执行 `python tools/set-domain.py xiaxinmeng.github.io` 恢复。
- **改了代码网站没变**：Ctrl+F5 强刷，或等部署 1–2 分钟。
- **打开 404**：`index.html` 必须在仓库根目录。
- **不想被搜索引擎收录**：取消 `index.html` 里 `noindex` meta 的注释，并把 `robots.txt` 改为 `Disallow: /`。

最后更新：2026-10-14

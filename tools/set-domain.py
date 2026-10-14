#!/usr/bin/env python3
"""一键切换站点域名。

站点地址散落在 5 个文件中（CNAME / index.html / 404.html / robots.txt / sitemap.xml），
手动改很容易漏掉 sitemap 或 og:url，之后被搜索引擎收录成错的地址。这个脚本把它们一次改齐。

用法：
    # 换成自定义域名（同时写入 CNAME 文件）
    python tools/set-domain.py www.example.com

    # 不要自定义域名，用 GitHub Pages 默认地址
    python tools/set-domain.py xiaxinmeng.github.io

    # 只看会改什么，不真的写
    python tools/set-domain.py www.example.com --dry-run

注意：邮件地址（hello@xxx）不会被改动。
"""
import argparse
import os
import re
import sys

# 站点可能用过的域名，切换时全部归一化掉
KNOWN_HOSTS = [
    r"(?:www\.)?xiaxinmeng\.com",
    r"xiaxinmeng\.github\.io",
    # 免费子域名服务（is-a.dev 等）。换成别的免费域名时在这里补一行，
    # 否则下次切换认不出旧域名、替换不掉。
    r"[\w-]+\.is-a\.dev",
    r"[\w-]+\.eu\.org",
    r"(?:www\.)?example\.com",
]

TEXT_FILES = ["index.html", "404.html", "robots.txt", "sitemap.xml"]


def build_pattern(new_host):
    """一次匹配「完整 URL 或裸域名」，保证每个域名只被替换一次（这样计数才准）。

    开头的 (?<![@\\w.-]) 用来避开邮件地址里的 xiaxinmeng.com。
    """
    host_alt = "|".join(KNOWN_HOSTS)
    rx = re.compile(r"(?<![@\w.-])(https?://)?(?:" + host_alt + r")", re.I)

    def replace(m):
        scheme = "https://" if m.group(1) else ""
        return scheme + new_host

    return rx, replace


def apply_pattern(rx, replace, text):
    """返回 (新文本, 真正发生变化的处数)。

    只统计「替换结果和原文不同」的位置，这样把域名改成它自己时不会误报。
    """
    out = []
    last = 0
    changes = 0
    for m in rx.finditer(text):
        new = replace(m)
        out.append(text[last:m.start()])
        if new != m.group(0):
            changes += 1
        out.append(new)
        last = m.end()
    out.append(text[last:])
    return "".join(out), changes


def main():
    ap = argparse.ArgumentParser(description="统一修改站点中出现的域名。")
    ap.add_argument("host", help="新域名，例如 www.example.com 或 xiaxinmeng.github.io")
    ap.add_argument("--root", default=".", help="站点根目录，默认当前目录")
    ap.add_argument("--dry-run", action="store_true", help="只预览，不写入")
    args = ap.parse_args()

    host = args.host.strip().lower().lstrip("/")
    if host.startswith("http"):
        sys.exit("error: 只填域名，不要带 http:// 或 https://")
    if "/" in host:
        sys.exit("error: 只填域名，不要带路径")

    root = os.path.abspath(args.root)
    rx, replace = build_pattern(host)
    changed_total = 0

    for name in TEXT_FILES:
        path = os.path.join(root, name)
        if not os.path.exists(path):
            print("  跳过（不存在）: %s" % name)
            continue
        original = open(path, encoding="utf-8").read()
        text, hits = apply_pattern(rx, replace, original)
        if hits:
            if not args.dry_run:
                open(path, "w", encoding="utf-8", newline="\n").write(text)
            print("  已更新 %-14s %d 处" % (name, hits))
            changed_total += hits
        else:
            print("  无变化 %-14s" % name)

    # CNAME：自定义域名写文件，GitHub Pages 默认地址则删掉文件
    cname_path = os.path.join(root, "CNAME")
    is_pages_default = host.endswith(".github.io")
    if is_pages_default:
        if os.path.exists(cname_path):
            if not args.dry_run:
                os.remove(cname_path)
            print("  已删除 CNAME（改用 GitHub Pages 默认地址）")
        else:
            print("  CNAME 不存在，无需删除")
    else:
        old = ""
        if os.path.exists(cname_path):
            old = open(cname_path, encoding="utf-8").read().strip()
        if old != host:
            if not args.dry_run:
                open(cname_path, "w", encoding="utf-8", newline="\n").write(host + "\n")
            print("  已写入 CNAME -> %s" % host)
        else:
            print("  CNAME 无需修改")

    print()
    if args.dry_run:
        print("（预览模式，未写入任何文件）")
    else:
        print("完成：共修改 %d 处引用，站点地址 -> https://%s/" % (changed_total, host))
        if not is_pages_default:
            print("别忘了到域名注册商添加 DNS 解析，然后在仓库 Settings → Pages 勾选 Enforce HTTPS。")


if __name__ == "__main__":
    main()

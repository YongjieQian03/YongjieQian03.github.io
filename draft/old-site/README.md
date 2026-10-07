# YongjieQian03.github.io

个人主页，纯静态 HTML 与 CSS，无构建步骤，推送到 `main` 分支后由 GitHub Pages 发布。

线上地址 https://YongjieQian03.github.io/

## 目录结构

```
index.html              页面结构与全部文案
404.html                自定义 404
assets/css/style.css    全部样式，改 :root 变量即可换肤
assets/js/main.js       导航折叠、滚动细线、当前区块高亮
assets/img/avatar.png   头像，替换同名文件即可
draft/                  本地预览脚本与截图，不参与发布
.nojekyll               关闭 Jekyll 处理
```

## 修改内容

文案直接改 `index.html`，每个区块上方有注释标明用途。头像换成同名文件即可，建议正方形，不小于 400 像素。

占位内容集中在这些位置，上线前记得替换

- `hero` 区块里的一句话简介、机构、方向、所在地
- `#about` 两段自我介绍
- `#research` `#projects` 三张卡片
- `#papers` 两条论文条目
- `#contact` 的邮箱，以及 Google Scholar 链接

## 配色与字体

`assets/css/style.css` 顶部的 `:root` 变量控制全部颜色、圆角、阴影与字体。深色模式在同文件的 `prefers-color-scheme: dark` 块里，跟随系统自动切换。

## 本地预览

```bash
python3 -m http.server 8000
```

浏览器打开 http://localhost:8000

重新生成 `draft/` 下的桌面、移动与深色截图

```bash
python3 draft/shoot.py
```

## 部署

改完内容提交并推送，Pages 会自动重建

```bash
git add -A && git commit -m "update content" && git push
```

推送用的 SSH 别名是 `github-new`，对应密钥 `~/.ssh/id_ed25519_github_new`，配置写在 `~/.ssh/config`。

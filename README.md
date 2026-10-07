# YongjieQian03.github.io

个人主页，基于 [PRISM](https://github.com/xyjoey/PRISM) 模板，Next.js 静态导出后由 GitHub Pages 发布。

线上地址 https://YongjieQian03.github.io/

## 目录结构

```
content/            默认语言内容，TOML、Markdown、BibTeX 按需编辑
content_zh/         中文内容，文件名与 content/ 一一对应
public/             静态资源，头像 avatar.jpg 与站点图标 favicon.svg
src/                Next.js 源码，组件与样式
draft/              临时材料，旧版站点、模板文档与预览截图
out/                构建产物，不提交
```

## 内容修改

全部文案都在配置文件里，不需要改代码。

- `content/config.toml` 站点标题、作者信息、社交链接、顶部导航
- `content/about.toml` 首页结构与研究兴趣
- `content/bio.md` 自我介绍
- `content/news.toml` 动态列表
- `content/publications.bib` 论文，可直接从 Google Scholar 或 Zotero 导出
- `content/projects.toml` `content/awards.toml` `content/cv.md` 项目、奖项与简历

`content_zh/` 放中文版本，缺少的文件自动回退到 `content/`。

需要新页面时，在 `content/` 新建 TOML 并加进 `config.toml` 的 `navigation`。页面类型有 `text`、`card`、`publication` 三种。

论文里加 `selected = {true}` 会置顶到首页精选，`description` 显示摘要，`preview` 指定封面图。

## 本地预览

```bash
npm install
npm run dev
```

打开 http://localhost:3000

构建并本地检查导出结果

```bash
npm run build
npx serve out
```

重新生成 `draft/` 下的预览截图

```bash
python3 draft/shoot-prism.py
```

## 部署

推送到 `main` 后 GitHub Actions 自动构建并发布，工作流在 `.github/workflows/deploy.yml`。

仓库需要在 Settings 的 Pages 里把 Source 设为 GitHub Actions，只配置一次。若想改回从分支发布，构建产物在 `out/`，需要单独推到发布分支。

推送用的 SSH 别名是 `github-new`，对应密钥 `~/.ssh/id_ed25519_github_new`。

## 待替换的占位内容

站点目前是空白模板，以下位置还是示例文案

- `content/config.toml` 的机构名、邮箱、所在地与 Google Scholar 链接
- `content/bio.md` 与 `content_zh/bio.md` 的自我介绍
- `content/about.toml` 的研究兴趣
- `content/publications.bib` 的三条示例论文
- `content/projects.toml` `content/awards.toml` `content/cv.md`
- `public/avatar.jpg` 头像是 512 像素方图，换新照片时保持正方形且不小于 512 像素

## 许可

模板 PRISM 遵循 MIT 协议，原作者版权声明保留在 `LICENSE`。

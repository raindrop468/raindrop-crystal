# Raindrop Crystal 项目接管文档

> 最后更新：2026-06-12 | 当前版本：`5daeffa`

---

## 一、项目概况

| 项目 | 信息 |
|------|------|
| 项目名称 | Raindrop Crystal |
| 业务类型 | 天然水晶饰品海外零售 |
| GitHub 仓库 | `raindrop468/raindrop-crystal` |
| 本地路径 | `C:\Users\Administrator\Desktop\2` |
| 目标市场 | 海外用户（英文优先） |
| 支付方式 | PayPal |
| WhatsApp | +86 182 7142 5419 |

---

## 二、快查卡

```
零售站地址：https://raindropwyx.com
主站地址：  https://raindrop-crystal.netlify.app（⚠️ 额度耗尽）
代码仓库：  github.com/raindrop468/raindrop-crystal
部署方式：  git push → GitHub Actions → Cloudflare Pages
域名注册：  Cloudflare Registrar
DNS 管理：  Cloudflare (paris.ns / ridge.ns)
```

---

## 三、网站架构

### 3.1 主站（面向品牌展示）

| 文件 | 内容 |
|------|------|
| `index.html` | 品牌首页：Hero + 双系列入口 + 9条评价 + 42张买家秀 + 信任徽章 |
| `classic.html` | 经典水晶系列（9款产品） |
| `zodiac.html` | 星座守护系列（12款产品，按1-12月排列） |
| `shipping.html` | 物流政策 |
| `refund.html` | 退换政策 |
| `contact.html` | 联系方式 |
| `privacy.html` | 隐私政策 |
| `terms.html` | 服务条款 |

### 3.2 零售独立站（面向直接购买）

| 文件 | 内容 |
|------|------|
| `retail/index.html` | 零售首页：产品展示 + 买家秀实拍墙 + PayPal 购买按钮 |
| `retail/classic.html` | 经典水晶零售版 |
| `retail/zodiac.html` | 星座水晶零售版 |

### 3.3 图片资源

| 目录 | 内容 | 文件数 |
|------|------|--------|
| `images/classic/` | 经典系列 WebP（主图+缩略图） | 56 |
| `images/zodiac/` | 星座系列 WebP（主图+缩略图） | 72 |
| `images/reviews/` | 买家秀 WebP（主图+缩略图） | 84 |
| `retail/images/` | 零售站专用图片副本 | 同上 |
| `originals/` | 原始 JPG/PNG（不推送 GitHub） | — |
| `买家秀/` | 买家秀原始图（不推送 GitHub） | 42张 |

---

## 四、域名与托管

### 4.1 域名

| 域名 | 注册商 | 到期 |
|------|--------|------|
| `raindropwyx.com` | Cloudflare Registrar | 2027-06-11 |

### 4.2 托管平台

| 站点 | 平台 | 状态 |
|------|------|------|
| 零售站 | **Cloudflare Pages** | ✅ 在线 |
| 主站 | Netlify | ⚠️ 额度耗尽（300 credits/月） |

### 4.3 Cloudflare 信息

| 项目 | 值 |
|------|-----|
| 账户邮箱 | Raindrop446688@gmail.com |
| 账户 ID | `25f5926f22588cded7c5366edd1535ec` |
| Zone ID | `193699636c39d51978655e0a1f15f365` |
| Pages 项目名 | `raindrop-crystal-retail` |
| Pages 子域名 | `raindrop-crystal-retail.pages.dev` |
| DNS 服务器 | `paris.ns.cloudflare.com` / `ridge.ns.cloudflare.com` |
| API Token (全权限) | 存于 GitHub Secrets `CLOUDFLARE_API_TOKEN` |

### 4.4 Netlify 信息（⚠️ 额度耗尽，暂时不可用）

| 项目 | 值 |
|------|-----|
| 主站 Site ID | `713cf611-8356-4e72-ad33-52dc075fd439` |
| 零售站 Site ID | `8ae45537-3c0d-4d1d-815e-683ab8ef84ea` |
| Token | `nfp_m9oR4hmRDdUzxtHx8sRS2uT5n41uxR3a456a`（存 GitHub Secrets `NETLIFY_AUTH_TOKEN`）|

---

## 五、部署流水线

### 5.1 正常流程

```
本地修改 → git add + commit + push → GitHub Actions → Cloudflare Pages 部署
                                         └→ 零售站 https://raindropwyx.com
```

### 5.2 Workflow 文件

| 文件 | 目标 | 状态 |
|------|------|------|
| `.github/workflows/cloudflare-pages-deploy.yml` | 零售站 → Cloudflare Pages | ✅ 活跃 |
| `.github/workflows/netlify-deploy.yml` | 主站 → Netlify | ⚠️ 额度耗尽 |
| `.github/workflows/netlify-deploy-retail.yml` | 零售站 → Netlify | ⚠️ 已废弃 |

### 5.3 Cloudflare Pages 部署详解

**触发方式**：
- `push` 到 `main` 分支 → 自动触发
- 手动 `workflow_dispatch` → 从 GitHub Actions 面板触发

**部署内容**：`retail/` 目录下的所有文件

**部署工具**：`wrangler pages deploy retail/`（无需构建步骤，纯静态文件）

**重要特性**：
- 每月 500 次免费构建（远超需求）
- 带宽无硬性上限
- 全球 330+ CDN 节点
- 自动 SSL

### 5.4 GitHub Secrets 清单

| Secret 名 | 用途 | 对应平台 |
|-----------|------|----------|
| `CLOUDFLARE_API_TOKEN` | Cloudflare Pages 部署 | Cloudflare |
| `NETLIFY_AUTH_TOKEN` | Netlify 部署（当前不可用） | Netlify |

---

## 六、图片处理规范

### 6.1 铁律

> ⚠️ **任何新图片加入网站前，必须先用脚本压缩为 WebP！禁止直接将原始 JPG/PNG 用于页面！**

### 6.2 压缩标准

| 类型 | 尺寸 | 质量 | 后缀 |
|------|------|------|------|
| 主图 | 1200px 宽 | 80% | `{name}.webp` |
| 缩略图 | 400px 宽 | 75% | `{name}_thumb.webp` |

### 6.3 买家秀处理

```bash
# 原图位置：买家秀/（不推 GitHub）
# 处理脚本：python process_reviews.py
# 步骤：裁剪底部8%去水印 → 转 WebP 主图+缩略图
# 输出：images/reviews/
```

### 6.4 文件名冲突

同一产品若有同名不同后缀的原图（如 `3-.jpg` 和 `3-.png`），压缩后 WebP 同名会覆盖。
解决：重命名 `.png` 原图加 `--` 后缀（如 `3--.png`）再压缩，并同步更新 HTML 中的 `photos` 数组。

### 6.5 原图备份

- `originals/` — 产品原图备份（.gitignore）
- `买家秀/` — 买家秀原图（.gitignore）
- 两个目录均不推送到 GitHub

---

## 七、PayPal 合规红线

写入任何产品描述时必须遵守：

| 禁止词 (English) | 禁止词 (中文) | 替代词 |
|------------------|---------------|--------|
| Healing / Cure / Medical / Health | 治疗 / 治愈 / 功效 / 保健 / 健康 | — |
| Anxiety / Disease / Remedy / Wellness | 辟邪 / 转运 / 改运 | — |
| Energy / Crystal Energy | 能量 / 水晶能量 | 光彩(radiance) / 魅力(charm) / 之美(beauty) |
| — | 水晶能量 | 水晶种类 / Crystal Type |

| 允许词 |
|--------|
| Decorative / Handmade / Memorial Gift |
| Spiritual Meaning / 天然水晶 / 手工制作 |

---

## 八、关键凭证位置

> ⚠️ 以下信息仅供项目维护使用，请勿公开分享

| 凭证 | 存储位置 |
|------|----------|
| GitHub Token | git remote URL（已写入）；值见本地 `git remote -v` |
| Netlify Token | GitHub Secrets `NETLIFY_AUTH_TOKEN`；值见本地记忆文档 |
| Cloudflare Token | GitHub Secrets `CLOUDFLARE_API_TOKEN`；值见本地记忆文档 |
| Cloudflare 账户 | Raindrop446688@gmail.com / Cloudflare 面板 |

---

## 九、目录结构完整地图

```
C:\Users\Administrator\Desktop\2/
├── index.html                     # 品牌首页
├── classic.html                   # 经典系列
├── zodiac.html                    # 星座系列
├── shipping.html / refund.html    # 物流/退换政策
├── contact.html / privacy.html    # 联系/隐私政策
├── terms.html                     # 服务条款
├── process_reviews.py             # 买家秀处理脚本
├── .gitignore                     # 排除 originals/ 买家秀/ 等
├── .github/workflows/
│   ├── cloudflare-pages-deploy.yml   # → 零售站 Cloudflare
│   ├── netlify-deploy.yml            # → 主站 Netlify（暂不可用）
│   └── netlify-deploy-retail.yml     # → 零售站 Netlify（已废弃）
├── images/
│   ├── classic/       # 经典系列 WebP（56个）
│   ├── zodiac/        # 星座系列 WebP（72个）
│   └── reviews/       # 买家秀 WebP（84个）
├── retail/
│   ├── index.html     # 零售首页
│   ├── classic.html   # 零售经典系列
│   ├── zodiac.html    # 零售星座系列
│   └── images/        # 零售站图片副本（镜像 images/）
├── originals/         # 产品原图备份（.gitignore）
├── 买家秀/            # 买家秀原图（.gitignore）
└── .workbuddy/
    └── memory/        # 项目工作日志
```

---

## 十、常用操作指南

### 10.1 日常修改并部署

```bash
# 1. 修改代码
# 2. 提交并推送
cd "C:\Users\Administrator\Desktop\2"
git add .
git commit -m "描述你的改动"
git push

# 3. 等待 GitHub Actions 自动部署（约 1-2 分钟）
# 4. 验证：https://raindropwyx.com
```

### 10.2 添加新产品图片

```bash
# 1. 将原图放入 originals/
# 2. 运行压缩脚本（生成 WebP 到 images/）
# 3. 复制到 retail/images/（零售站需要独立副本）
# 4. 更新 HTML 中的产品数据和图片引用
# 5. git add + commit + push
```

### 10.3 更新买家秀

```bash
# 1. 原图放入 买家秀/
# 2. python process_reviews.py
# 3. 复制 images/reviews/ 到 retail/images/reviews/
# 4. 更新 HTML 中 PHOTO_IDS 数组
# 5. git add + commit + push
```

### 10.4 Cloudflare 相关操作

| 需求 | 操作 |
|------|------|
| 查看部署状态 | `https://dash.cloudflare.com` → Workers & Pages → raindrop-crystal-retail |
| 管理 DNS | Cloudflare 面板 → raindropwyx.com → DNS |
| 续费域名 | Cloudflare 面板 → Domain Registration |
| 创建新 Token | Cloudflare 面板 → My Profile → API Tokens |

### 10.5 手动重新部署

从 GitHub Actions 面板：
1. 打开 https://github.com/raindrop468/raindrop-crystal/actions
2. 点击 **Deploy Retail to Cloudflare Pages**
3. 点击 **Run workflow** → **Run workflow**

---

## 十一、已知问题与注意事项

| 问题 | 状态 | 备注 |
|------|------|------|
| Netlify 主站额度耗尽 | ⚠️ 待解决 | 300 credits/月用完，主站无法部署新版本 |
| Netlify 零售站 | ✅ 已迁移 | 已切换至 Cloudflare Pages，Netlify workflow 可禁用 |
| 零售站图片路径 | ✅ 已修复 | `../images/` → `./images/`，线上已生效 |
| Cloudflare Token 权限 | ✅ 已补齐 | Zone DNS/Zone + Account Pages/Workers + User Details |

### 后续建议

1. **主站迁移**：将主站 (`index.html`, `classic.html`, `zodiac.html` 及政策页面) 也迁移到 Cloudflare Pages，彻底摆脱 Netlify 额度限制
2. **统一图片目录**：目前 `images/` 和 `retail/images/` 重复存放，可考虑用软链接或构建脚本统一
3. **Cloudflare Email Routing**：可配置 `@raindropwyx.com` 邮箱转发，提升品牌专业度

---

## 十二、紧急联系

| 服务 | 控制台地址 |
|------|-----------|
| GitHub | https://github.com/raindrop468/raindrop-crystal |
| Cloudflare | https://dash.cloudflare.com |
| Netlify | https://app.netlify.com |
| PayPal | https://www.paypal.com/businessmanage/ |
| 域名 Whois | raindropwyx.com 注册邮箱: Raindrop446688@gmail.com |

---

> 文档维护：每次重大架构变更后请更新此文档。当前版本对应 commit `5daeffa`。

# Raindrop Crystal — 项目部署文档

> 最后更新：2026-06-27 | 当前 commit：`4213206`

---

## 一、快查卡

```
零售站地址：  https://raindropwyx.com
备用地址：    https://raindrop-crystal-retail.pages.dev
代码仓库：    https://github.com/raindrop468/raindrop-crystal
部署方式：    git push → GitHub Actions → Cloudflare Pages（全自动）
WhatsApp：   +86 182 7142 5419
联系邮箱：   Raindrop446688@gmail.com
```

---

## 二、网站产品页一览

### 零售站产品页（retail/）

| 文件 | 产品名 | 价格 |
|------|--------|------|
| `retail/index.html` | 零售首页（热销轮播 + 买家秀 + 搜索） | — |
| `retail/classic.html` | 经典水晶项圈系列 | $41 |
| `retail/zodiac.html` | 星座守护项圈系列（⚠️ 已售罄） | $41 |
| `retail/pet-urn.html` | 宠物骨灰盒 | $22 |
| `retail/pet-keychain.html` | 亚克力宠物钥匙扣 | $4.90 |
| `retail/pet-leather.html` | 皮革宠物毛发钥匙扣 | $4.90–$9.80 |
| `retail/pet-fridge.html` | 3D 宠物冰箱贴/立体头像/车载香薰 | $19.80–$36.80 |
| `retail/pet-plush.html` | 狗狗毛绒发声玩具 | $9.80 |
| `retail/pet-ring.html` | 甜美合金可调节戒指 | $8.80 |
| `retail/pet-patches.html` | 狗狗刺绣布贴套装 | $8.80 |
| `retail/pet-portrait.html` | 宠物手绘定制肖像 | $19.80–$29.80 |
| `retail/pet-necklace.html` | 宠物珍珠小香风项圈 | $9.90 |
| `retail/pet-bib.html` | 猫猫狗狗口水巾围兜领结 | $13.80 |
| `retail/pet-hairclip.html` | 宠物手工 BB 夹发卡 | $9.90–$32.80 |
| `retail/pet-rug.html` | 来图定制宠物地毯 | $23.80–$48.80 |
| `retail/pet-bed.html` | 防水防撕咬宠物窝 | $16.80–$32.80 |
| `retail/pet-wool-felt.html` | 尼泊尔手工羊毛毡女王兔 | $26.80 |
| `retail/pet-crystal-lamp.html` | 水晶 3D 激光雕刻 LED 台灯 | $26.80–$29.80 |
| `retail/pet-puzzle.html` | 来图定制宠物照片拼图 | $32.80–$46.80 |
| `retail/pet-rope-toys.html` | 狗咬绳结磨牙玩具套装 | $12.80–$16.80 |
| `retail/pet-bracelet.html` | 定制合金手链项链可调节 | $19.80–$22.80 |
| `retail/pet-bolster.html` | 来图定制宠物短毛绒抱枕 | $18.80–$24.80 |
| `retail/shipping.html` | 配送政策页 | — |
| `retail/refund.html` | 退款政策页 | — |
| `retail/about-us.html` | 关于我们 | — |
| `retail/sitemap.xml` | SEO 站点地图 | — |
| `retail/robots.txt` | 搜索引擎爬取规则 | — |

### 主站（根目录，品牌展示用）

| 文件 | 内容 |
|------|------|
| `index.html` | 品牌首页（水晶项圈） |
| `classic.html` | 经典水晶系列 |
| `zodiac.html` | 星座守护系列 |
| `shipping.html` / `refund.html` / `contact.html` / `privacy.html` / `terms.html` | 品牌政策页 |

---

## 三、托管与域名

| 项目 | 值 |
|------|----|
| 域名 | `raindropwyx.com` |
| 注册商 | Cloudflare Registrar |
| 到期时间 | 2027-06-11 |
| DNS 服务器 | `paris.ns.cloudflare.com` / `ridge.ns.cloudflare.com` |
| 托管平台 | **Cloudflare Pages** |
| Pages 项目名 | `raindrop-crystal-retail` |
| Pages 子域名 | `raindrop-crystal-retail.pages.dev` |
| Cloudflare 账户 | `Raindrop446688@gmail.com` |
| Cloudflare 账户 ID | `25f5926f22588cded7c5366edd1535ec` |
| Zone ID | `193699636c39d51978655e0a1f15f365` |

---

## 四、部署流程

### 4.1 标准部署（日常改动）

```bash
# 在本地修改文件后：
cd "C:\Users\Administrator\Desktop\2"
git add .
git commit -m "改动说明"
git push
# 等待约 1-2 分钟，Cloudflare Pages 自动部署完成
# 验证：https://raindropwyx.com
```

### 4.2 部署流水线

```
本地修改
  → git push main
    → GitHub Actions 触发 (.github/workflows/cloudflare-pages-deploy.yml)
      → npm install -g wrangler
        → wrangler pages deploy retail/
          → Cloudflare Pages 更新
            → https://raindropwyx.com 上线
```

### 4.3 Workflow 文件

| 文件 | 作用 | 状态 |
|------|------|------|
| `.github/workflows/cloudflare-pages-deploy.yml` | 零售站 → Cloudflare Pages | ✅ 活跃 |
| `.github/workflows/netlify-deploy.yml` | 主站 → Netlify | ⚠️ 额度耗尽，暂停 |
| `.github/workflows/netlify-deploy-retail.yml` | 零售站 → Netlify（旧） | ⚠️ 已废弃 |

### 4.4 GitHub Secrets

| Secret 名 | 用途 |
|-----------|------|
| `CLOUDFLARE_API_TOKEN` | wrangler 部署到 Cloudflare Pages |
| `NETLIFY_AUTH_TOKEN` | Netlify 部署（当前不可用） |

### 4.5 手动触发部署（不 push 代码）

1. 打开 https://github.com/raindrop468/raindrop-crystal/actions
2. 点击左侧 **Deploy to Cloudflare Pages**
3. 点击右上角 **Run workflow** → **Run workflow**

---

## 五、图片处理规范

### 5.1 铁律

> ⚠️ **任何新图片上线前，必须先压缩为 WebP。禁止直接使用原始 JPG/PNG！**

### 5.2 压缩标准

| 类型 | 最大宽度 | 质量 | 文件名规则 |
|------|---------|------|-----------|
| 主图 | 1200px | 80% | `{name}.webp` |
| 缩略图 | 400px | 75% | `{name}_thumb.webp` |

### 5.3 各系列图片目录

| 目录 | 系列 |
|------|------|
| `retail/images/classic/` | 经典水晶项圈 |
| `retail/images/zodiac/` | 星座项圈 |
| `retail/images/urns/` | 骨灰盒 |
| `retail/images/keychains/` | 亚克力钥匙扣 |
| `retail/images/leather/` | 皮革钥匙扣 |
| `retail/images/fridge/` | 3D 冰箱贴 |
| `retail/images/plush/` | 毛绒玩具 |
| `retail/images/rings/` | 戒指 |
| `retail/images/patches/` | 刺绣布贴 |
| `retail/images/portrait/` | 手绘肖像 |
| `retail/images/necklace/` | 珍珠项圈 |
| `retail/images/bib/` | 口水巾 |
| `retail/images/hairclip/` | 发卡 |
| `retail/images/rug/` | 地毯 |
| `retail/images/petbed/` | 宠物窝 |
| `retail/images/wool-felt/` | 羊毛毡 |
| `retail/images/crystal-lamp/` | 水晶台灯 |
| `retail/images/puzzle/` | 拼图 |
| `retail/images/rope-toys/` | 绳结玩具 |
| `retail/images/bracelet/` | 手链项链 |
| `retail/images/bolster/` | 抱枕 |
| `retail/images/reviews/` | 买家秀实拍 |

### 5.4 压缩脚本

项目根目录下有各系列专用压缩脚本：

```
process_bolster.py       # 抱枕
process_bracelet.py      # 手链
process_crystal_lamp.py  # 台灯
process_hairclip.py      # 发卡
process_necklace.py      # 项链
process_portrait.py      # 肖像
process_reviews.py       # 买家秀（含底部裁剪去水印）
process_bib.py           # 口水巾
process_petbed.py        # 宠物窝
... 等
```

运行方式（以抱枕为例）：
```bash
"C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe" process_bolster.py
```

### 5.5 原图存放（不推送 GitHub）

以下目录已加入 `.gitignore`，原图只在本地保留：

```
originals/    买家秀/    抱枕/    手链/    羊毛、/    玩具/
刺绣/    戒指/    发卡/    口水巾/    地毯/    头像/    宠物垫/    项链/
激光台灯/    拼图/    毛绒娃娃/    皮革钥匙扣/    骨灰盒宠物/    冰箱贴/
主页图片/    ...（所有中文名源图文件夹）
```

---

## 六、添加新产品系列（操作步骤）

```
1. 将原图放入本地中文名文件夹（如 新系列/）
2. 新建压缩脚本 process_xxx.py，参考现有脚本
3. 运行压缩脚本 → 生成 retail/images/xxx/ 中的 WebP 文件
4. 新建产品页 retail/pet-xxx.html，参考现有产品页模板
5. 更新 retail/index.html：
   - Best Sellers 轮播新增卡片
   - 搜索关键词数组新增关键词
6. 更新所有现有产品页的 <nav> 和 <footer>，加入新产品链接
7. 将新文件夹加入 .gitignore（原图不上传）
8. git add . && git commit -m "feat: add xxx series" && git push
```

---

## 七、PayPal 合规红线

产品标题和描述中**绝对禁止**使用以下词汇：

| 禁止（英文） | 禁止（中文） | 可用替代词 |
|-------------|-------------|-----------|
| Healing / Cure / Medical / Health | 治疗 / 治愈 / 功效 / 保健 | — |
| Anxiety / Disease / Remedy / Wellness | 辟邪 / 转运 / 改运 | — |
| Energy / Crystal Energy | 能量 / 水晶能量 | radiance / charm / beauty |

✅ 可用：`Decorative` / `Handmade` / `Memorial Gift` / `Spiritual Meaning` / `天然水晶` / `手工制作`

**PayPal Client ID（全站统一）：**
```
AbuhPoOeEsNEvryLw7bTOeG2ry6AseOqhH7c7DOvP9F2SX8tuz6VNHL0cS3J1BTae9z9XWRBs8jS2hJa
```

---

## 八、库存状态

| 系列 | 库存状态 |
|------|----------|
| 星座守护项圈 (`zodiac.html`) | 🔴 **已售罄（Out of Stock）** |
| 其他所有产品页 | 🟢 **有货（In Stock: 1000+）** |

---

## 九、常用控制台链接

| 服务 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/raindrop468/raindrop-crystal |
| GitHub Actions 部署记录 | https://github.com/raindrop468/raindrop-crystal/actions |
| Cloudflare 面板 | https://dash.cloudflare.com |
| Cloudflare Pages 项目 | https://dash.cloudflare.com → Workers & Pages → raindrop-crystal-retail |
| DNS 管理 | https://dash.cloudflare.com → raindropwyx.com → DNS |
| PayPal 商户后台 | https://www.paypal.com/businessmanage/ |

---

## 十、社交账号与联系方式

| 平台 | 账号 / 链接 |
|------|------------|
| WhatsApp | +86 182 7142 5419 |
| TikTok | https://www.tiktok.com/@raindrop446688 |
| Instagram | https://www.instagram.com/raindrop_6688 |
| 邮箱 | raindrop446688@gmali.com（注意：gmali，非 gmail） |

---

> 每次添加新产品系列或重大改动后，请更新此文档的「产品页一览」和「最后更新」日期。

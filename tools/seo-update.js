const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..", "retail");
const site = "https://raindropwyx.com";

const pages = {
  "index.html": {
    title: "Raindrop Pet | Custom Pet Gifts & Handmade Pet Accessories",
    description:
      "Shop custom pet gifts, personalized pet accessories, handmade crystal pet collars, pet memorial keepsakes, custom portraits, photo keychains, rugs, pillows and more.",
    type: "website",
    image: "/images/hero.webp"
  },
  "classic.html": {
    title: "Handmade Crystal Pet Collars | Natural Stone Dog & Cat Jewelry | Raindrop Pet",
    description:
      "Handmade natural crystal pet collars for dogs and cats. A meaningful personalized pet accessory and gift for pet lovers.",
    price: "16.80",
    image: "/images/classic/1.webp"
  },
  "zodiac.html": {
    title: "Zodiac Crystal Pet Collars | Personalized Dog & Cat Jewelry | Raindrop Pet",
    description:
      "12-zodiac handmade crystal pet collars designed for dogs and cats. Personalized pet jewelry with natural stone style.",
    price: "18.80",
    image: "/images/zodiac/1.webp"
  },
  "pet-portrait.html": {
    title: "Custom Pet Portrait from Photo | Personalized Dog & Cat Art Gift | Raindrop Pet",
    description:
      "Turn a dog or cat photo into a custom hand-drawn digital pet portrait. A personalized pet gift and keepsake for pet parents.",
    price: "19.80",
    image: "/images/portrait/1.webp"
  },
  "pet-keychain.html": {
    title: "Custom Pet Photo Keychain | Personalized Dog Cat Acrylic Charm | Raindrop Pet",
    description:
      "Custom acrylic pet photo keychain made from your dog or cat picture. Personalized bag charm and cute gift for pet lovers.",
    price: "9.90",
    image: "/images/keychains/1.webp"
  },
  "pet-leather.html": {
    title: "Pet Fur Keepsake Keychain | Dog Hair Memorial Charm | Raindrop Pet",
    description:
      "Leather pet fur keepsake keychain for dog or cat hair memorials. A thoughtful pet memorial gift and remembrance charm.",
    price: "12.90",
    image: "/images/leather/1.webp"
  },
  "pet-urn.html": {
    title: "Pet Memorial Urn | Wooden Dog & Cat Keepsake Box | Raindrop Pet",
    description:
      "Handcrafted wooden pet memorial urn and keepsake box for beloved dogs and cats. A gentle remembrance gift for pet loss.",
    price: "29.80",
    image: "/images/urns/1.webp"
  },
  "pet-fridge.html": {
    title: "3D Custom Pet Fridge Magnet | Personalized Dog Cat Portrait Gift | Raindrop Pet",
    description:
      "Custom 3D pet fridge magnet and car air freshener made from your dog or cat photo. A personalized pet memorial gift.",
    price: "14.90",
    image: "/images/fridge/1.webp"
  },
  "pet-crystal-lamp.html": {
    title: "Custom Photo Crystal LED Lamp | Pet Memorial Gift | Raindrop Pet",
    description:
      "Custom engraved crystal LED lamp from a pet photo. A personalized dog, cat or pet memorial gift with warm light.",
    price: "24.80",
    image: "/images/crystal-lamp/1.webp"
  },
  "pet-puzzle.html": {
    title: "Custom Pet Portrait Puzzle | Personalized Dog & Cat Jigsaw Gift | Raindrop Pet",
    description:
      "Personalized wooden jigsaw puzzle made from your pet portrait. A custom dog or cat gift for pet lovers and families.",
    price: "18.80",
    image: "/images/puzzle/1.webp"
  },
  "pet-rug.html": {
    title: "Custom Pet Rug from Photo | Personalized Dog Cat Floor Mat | Raindrop Pet",
    description:
      "Custom pet rug and floor mat inspired by your dog or cat. A personalized pet decor gift for bedrooms, studios and pet corners.",
    price: "19.80",
    image: "/images/rug/1.webp"
  },
  "pet-bolster.html": {
    title: "Custom Pet Photo Pillow | Personalized Dog Cat Plush Cushion | Raindrop Pet",
    description:
      "Personalized pet photo pillow and plush cushion made from your dog or cat picture. A soft custom gift for pet lovers.",
    price: "16.80",
    image: "/images/bolster/1.webp"
  },
  "pet-bed.html": {
    title: "Waterproof Dog & Cat Pet Bed | Cozy Pet Nest | Raindrop Pet",
    description:
      "Waterproof anti-bite pet bed for dogs and cats. A cozy all-season pet nest with practical washable comfort.",
    price: "22.80",
    image: "/images/petbed/1.webp"
  },
  "pet-bib.html": {
    title: "Cute Pet Bib Scarf | Dog Cat Bowtie Drool Bib | Raindrop Pet",
    description:
      "Cute pet bib scarf with bowtie for dogs and cats. A handmade pet accessory for photos, parties and everyday style.",
    price: "13.80",
    image: "/images/bib/1.webp"
  },
  "pet-hairclip.html": {
    title: "Pet Hair Clip | Handmade Dog Cat BB Hair Accessory | Raindrop Pet",
    description:
      "Handmade pet hair clips for dogs and cats. Cute BB hair accessories for grooming, photos and pet outfits.",
    price: "9.80",
    image: "/images/hairclip/1.webp"
  },
  "pet-necklace.html": {
    title: "Pearl Pet Collar Necklace | Dog Cat Jewelry Accessory | Raindrop Pet",
    description:
      "Original pearl pet collar necklace for cats and dogs. A stylish handmade pet jewelry accessory and pet lover gift.",
    price: "9.90",
    image: "/images/necklace/1.webp"
  },
  "pet-bracelet.html": {
    title: "Custom Pet Bracelet & Necklace | Adjustable Dog Cat Jewelry | Raindrop Pet",
    description:
      "Adjustable pet bracelet and necklace for dogs and cats. Cute personalized pet jewelry for photos and everyday style.",
    price: "8.80",
    image: "/images/bracelet/1.webp"
  },
  "pet-ring.html": {
    title: "Pet Lover Adjustable Ring | Cute Dog Cat Jewelry Gift | Raindrop Pet",
    description:
      "Sweet adjustable pet lover ring with dog and cat designs. A small jewelry gift for dog moms, cat moms and pet lovers.",
    price: "8.80",
    image: "/images/rings/1.webp"
  },
  "pet-patches.html": {
    title: "Dog Embroidery Patch Set | Cute Iron-On Pet Patches | Raindrop Pet",
    description:
      "Cute dog embroidery iron-on patch set for clothes, bags and accessories. A playful gift for pet lovers.",
    price: "7.90",
    image: "/images/patches/1.webp"
  },
  "pet-plush.html": {
    title: "Dog Squeaky Plush Chew Toy | Interactive Pet Toy | Raindrop Pet",
    description:
      "Durable squeaky plush chew toy for dogs. Interactive pet toy for teething, boredom relief and everyday play.",
    price: "12.80",
    image: "/images/plush/1.webp"
  },
  "pet-rope-toys.html": {
    title: "Dog Rope Chew Toy Set | Cotton Knot Toys for Dogs | Raindrop Pet",
    description:
      "Dog rope chew toy set with cotton knot toys for teething, tug play and boredom relief.",
    price: "10.80",
    image: "/images/rope-toys/1.webp"
  },
  "pet-wool-felt.html": {
    title: "Handmade Wool Felt Pet Charm | Cute Bag Keychain Gift | Raindrop Pet",
    description:
      "Handmade wool felt charm and keychain for bags, cars and pet lover gifts. Cute artisan accessory with playful detail.",
    price: "11.80",
    image: "/images/wool-felt/1.webp"
  },
  "shipping.html": {
    title: "Shipping Policy | Raindrop Pet",
    description: "Shipping policy for Raindrop Pet custom pet gifts, handmade accessories and personalized pet keepsakes.",
    type: "website"
  },
  "refund.html": {
    title: "Refund & Return Policy | Raindrop Pet",
    description: "Refund and return policy for Raindrop Pet handmade and custom pet products.",
    type: "website"
  }
};

const articles = {
  "best-custom-pet-memorial-gifts.html": {
    title: "Best Custom Pet Memorial Gifts for Dogs and Cats | Raindrop Pet",
    description:
      "A gentle guide to custom pet memorial gifts, including fur keepsake keychains, pet urns, portraits, crystal lamps and photo keepsakes.",
    heading: "Best Custom Pet Memorial Gifts for Dogs and Cats",
    intro:
      "Losing a beloved pet is deeply personal. A custom memorial gift can preserve a small, tangible part of that bond in a way that feels warm rather than formal.",
    sections: [
      ["Pet fur keepsake keychains", "A fur keepsake keychain is one of the most intimate choices because it keeps a real part of your pet close in daily life."],
      ["Pet memorial urns", "A handcrafted urn or keepsake box gives families a dedicated place for ashes, a collar tag, a small photo, or a handwritten note."],
      ["Custom pet portraits", "A portrait from a favorite photo can turn a familiar expression into artwork for a desk, hallway, or remembrance corner."],
      ["Photo crystal lamps", "A crystal LED lamp adds soft light to a pet memorial space and works well for customers who want something decorative and comforting."],
      ["How to choose", "Choose by the feeling you want to keep: closeness, display, daily carry, or a warm memory at home."]
    ]
  },
  "how-to-choose-custom-pet-portrait.html": {
    title: "How to Choose a Custom Pet Portrait from Photo | Raindrop Pet",
    description:
      "Learn how to choose the best photo, portrait style and gift format for a custom dog or cat portrait.",
    heading: "How to Choose a Custom Pet Portrait from Photo",
    intro:
      "A custom pet portrait works best when the photo, pose and style all support your pet's personality. The right starting photo makes the final artwork feel much more alive.",
    sections: [
      ["Pick a clear favorite photo", "Choose a photo where the eyes, face shape and markings are easy to see. Natural light usually works better than heavy filters."],
      ["Head portrait or full body", "A head portrait is ideal for expressive faces. A full-body portrait works better when the pose, tail, outfit or body shape is part of the charm."],
      ["Think about the final use", "For framed art, choose a vertical or square image. For gifts, choose a photo that the recipient already loves."],
      ["Include extra references", "Sending two or three extra photos helps the artist understand markings, fur color and small details."],
      ["Keep the emotion simple", "The best portrait usually captures one strong feeling: playful, gentle, proud, sleepy, or funny."]
    ]
  },
  "pet-memorial-keychain-vs-urn.html": {
    title: "Pet Memorial Keychain vs Pet Urn: Which Keepsake Is Right? | Raindrop Pet",
    description:
      "Compare pet memorial keychains and pet urns to choose the right keepsake for remembering a beloved dog or cat.",
    heading: "Pet Memorial Keychain vs Pet Urn: Which Keepsake Is Right?",
    intro:
      "Pet memorial keepsakes are not one-size-fits-all. Some families want something they can carry every day, while others want a quiet memorial place at home.",
    sections: [
      ["Choose a keychain for closeness", "A pet fur keepsake keychain is best when you want a small remembrance that can travel with you."],
      ["Choose an urn for a dedicated space", "A pet memorial urn is better when you want a respectful home for ashes or keepsakes in one place."],
      ["Consider gifting", "For a grieving friend, a portrait or crystal lamp may feel easier to receive than an urn unless you know their wishes."],
      ["Many families combine both", "It is common to keep an urn at home and use a keychain for a small daily connection."],
      ["The right choice is personal", "The best keepsake is the one that matches how someone naturally remembers and feels comfort."]
    ]
  },
  "custom-pet-gifts-for-dog-moms-cat-lovers.html": {
    title: "Custom Pet Gifts for Dog Moms and Cat Lovers | Raindrop Pet",
    description:
      "Personalized gift ideas for dog moms, cat lovers and pet parents, from custom portraits to pet photo keychains and handmade accessories.",
    heading: "Custom Pet Gifts for Dog Moms and Cat Lovers",
    intro:
      "The best pet lover gifts feel personal. Instead of a generic pet-themed item, custom gifts use the real pet's face, name, colors, or story.",
    sections: [
      ["Custom pet photo keychains", "Photo keychains are easy everyday gifts because they are small, affordable and personal."],
      ["Custom pet portraits", "Portraits are strong gifts for birthdays, holidays, new pet parents and memorial moments."],
      ["Pet rugs and pillows", "A custom rug or pillow is playful and works well for customers who love home decor with personality."],
      ["Handmade pet accessories", "Crystal collars, pearl necklaces, bib scarves and hair clips make pets photo-ready for special days."],
      ["Gift by personality", "For sentimental owners choose portraits or keepsakes. For playful owners choose rugs, pillows, clips or accessories."]
    ]
  },
  "personalized-pet-accessories-guide.html": {
    title: "Personalized Pet Accessories Guide | Custom Dog & Cat Gifts | Raindrop Pet",
    description:
      "A guide to personalized pet accessories, including handmade collars, bib scarves, hair clips, rugs, pillows and photo gifts.",
    heading: "Personalized Pet Accessories Guide",
    intro:
      "Personalized pet accessories help a dog or cat's personality show up in daily life, photos and family memories.",
    sections: [
      ["Start with comfort", "For wearable accessories, choose lightweight pieces that suit your pet's size, coat and activity level."],
      ["Match the occasion", "Crystal collars and pearl necklaces suit photos and celebrations. Bib scarves and hair clips are lighter everyday styling pieces."],
      ["Use custom photo gifts for memories", "Portraits, keychains, pillows and rugs are better when you want the pet's actual face or character included."],
      ["Think about care", "Choose washable or easy-care items for daily use, and reserve delicate handmade pieces for supervised wear."],
      ["Build a small collection", "Many pet parents like one daily accessory, one photo accessory and one personalized keepsake."]
    ]
  }
};

function esc(s) {
  return String(s).replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function stripTags(s) {
  return String(s).replace(/<[^>]*>/g, "").replace(/\s+/g, " ").trim();
}

function headTags(file, meta) {
  const url = `${site}/${file === "index.html" ? "" : file}`;
  const image = meta.image ? `${site}${meta.image}` : `${site}/images/hero.webp`;
  const base = [
    `<title>${esc(meta.title)}</title>`,
    `<meta name="description" content="${esc(meta.description)}">`,
    `<link rel="canonical" href="${url}">`,
    `<meta property="og:site_name" content="Raindrop Pet">`,
    `<meta property="og:type" content="${meta.type || "product"}">`,
    `<meta property="og:title" content="${esc(meta.title)}">`,
    `<meta property="og:description" content="${esc(meta.description)}">`,
    `<meta property="og:url" content="${url}">`,
    `<meta property="og:image" content="${image}">`,
    `<meta name="twitter:card" content="summary_large_image">`,
    `<meta name="twitter:title" content="${esc(meta.title)}">`,
    `<meta name="twitter:description" content="${esc(meta.description)}">`,
    `<meta name="twitter:image" content="${image}">`
  ];
  const schema =
    meta.type === "website"
      ? {
          "@context": "https://schema.org",
          "@type": "WebSite",
          name: "Raindrop Pet",
          url: site,
          description: meta.description,
          potentialAction: {
            "@type": "SearchAction",
            target: `${site}/?q={search_term_string}`,
            "query-input": "required name=search_term_string"
          }
        }
      : {
          "@context": "https://schema.org",
          "@type": "Product",
          name: stripTags(meta.title.replace(/\s*\|\s*Raindrop Pet.*/, "")),
          brand: { "@type": "Brand", name: "Raindrop Pet" },
          description: meta.description,
          image,
          url,
          offers: {
            "@type": "Offer",
            priceCurrency: "USD",
            price: meta.price || "9.90",
            availability: "https://schema.org/InStock",
            url
          },
          aggregateRating: {
            "@type": "AggregateRating",
            ratingValue: "4.9",
            reviewCount: "42"
          }
        };
  base.push(`<script type="application/ld+json">${JSON.stringify(schema)}</script>`);
  return base.join("\n");
}

function replaceHead(file, meta) {
  const p = path.join(root, file);
  let html = fs.readFileSync(p, "utf8");
  html = html
    .replace(/<title>[\s\S]*?<\/title>\s*/i, "")
    .replace(/<meta\s+name=["']description["'][\s\S]*?>\s*/i, "")
    .replace(/<link\s+rel=["']canonical["'][\s\S]*?>\s*/gi, "")
    .replace(/<meta\s+(?:property|name)=["'](?:og:[^"']+|twitter:[^"']+)["'][\s\S]*?>\s*/gi, "")
    .replace(/<script\s+type=["']application\/ld\+json["'][\s\S]*?<\/script>\s*/gi, "");
  html = html.replace(/(<meta name="viewport"[^>]*>\s*)/i, `$1\n${headTags(file, meta)}\n`);
  fs.writeFileSync(p, html);
}

function articleHtml(file, meta) {
  const url = `${site}/${file}`;
  const json = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: meta.heading,
    description: meta.description,
    author: { "@type": "Organization", name: "Raindrop Pet" },
    publisher: { "@type": "Organization", name: "Raindrop Pet" },
    mainEntityOfPage: url
  };
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(meta.title)}</title>
<meta name="description" content="${esc(meta.description)}">
<link rel="canonical" href="${url}">
<meta property="og:site_name" content="Raindrop Pet">
<meta property="og:type" content="article">
<meta property="og:title" content="${esc(meta.title)}">
<meta property="og:description" content="${esc(meta.description)}">
<meta property="og:url" content="${url}">
<meta property="og:image" content="${site}/images/hero.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${esc(meta.title)}">
<meta name="twitter:description" content="${esc(meta.description)}">
<meta name="twitter:image" content="${site}/images/hero.webp">
<script type="application/ld+json">${JSON.stringify(json)}</script>
<style>
*,*::before,*::after{box-sizing:border-box}body{margin:0;font-family:Segoe UI,system-ui,-apple-system,sans-serif;color:#2d2924;background:#fffdf8;line-height:1.75}a{color:inherit}.nav{border-bottom:1px solid #e8dfd3;background:#fffdf8}.nav-inner{max-width:1080px;margin:0 auto;padding:18px 24px;display:flex;justify-content:space-between;gap:20px;align-items:center}.logo{font-family:Georgia,serif;font-weight:700;font-size:22px;text-decoration:none}.logo span{color:#c4956a}.nav-links{display:flex;gap:16px;flex-wrap:wrap;font-size:14px;color:#776d61}.hero{background:#f5f0ea;padding:56px 24px 42px}.hero-inner{max-width:880px;margin:0 auto}.eyebrow{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#a4774f;font-weight:700;margin-bottom:12px}h1{font-family:Georgia,serif;font-size:clamp(32px,5vw,52px);line-height:1.15;margin:0 0 18px}main{max-width:880px;margin:0 auto;padding:42px 24px 72px}.lead{font-size:19px;color:#5f574f;margin-bottom:34px}.article-section{padding:26px 0;border-top:1px solid #eadfce}.article-section h2{font-size:22px;margin:0 0 10px}.article-section p{margin:0;color:#5f574f}.cta{margin-top:42px;padding:24px;border:1px solid #e8dfd3;background:#faf6ef;border-radius:8px}.cta a{display:inline-block;margin-top:12px;background:#25d366;color:#fff;text-decoration:none;padding:11px 18px;border-radius:6px;font-weight:700}footer{padding:30px 24px;background:#2d2924;color:#c4beb4;text-align:center;font-size:13px}
</style>
</head>
<body>
<nav class="nav"><div class="nav-inner"><a class="logo" href="index.html">Raindrop <span>Pet</span></a><div class="nav-links"><a href="index.html">Shop</a><a href="pet-portrait.html">Portraits</a><a href="pet-keychain.html">Keychains</a><a href="pet-urn.html">Memorial</a></div></div></nav>
<section class="hero"><div class="hero-inner"><div class="eyebrow">Raindrop Pet Guide</div><h1>${esc(meta.heading)}</h1></div></section>
<main>
<p class="lead">${esc(meta.intro)}</p>
${meta.sections.map(([h, p]) => `<section class="article-section"><h2>${esc(h)}</h2><p>${esc(p)}</p></section>`).join("\n")}
<div class="cta"><strong>Looking for a custom pet gift?</strong><br>Explore personalized pet portraits, photo keychains, memorial keepsakes and handmade accessories from Raindrop Pet.<br><a href="index.html">Shop Custom Pet Gifts</a></div>
</main>
<footer>&copy; 2026 Raindrop Pet. Custom pet gifts and handmade pet accessories.</footer>
</body>
</html>
`;
}

Object.entries(pages).forEach(([file, meta]) => replaceHead(file, meta));
Object.entries(articles).forEach(([file, meta]) => fs.writeFileSync(path.join(root, file), articleHtml(file, meta)));

let index = fs.readFileSync(path.join(root, "index.html"), "utf8");
index = index.replace(/Raindrop\s*<span class="brand-accent">Pet<\/span>/g, 'Raindrop <span class="brand-accent">Pet</span>');
index = index.replace(
  /<p class="lead">[\s\S]*?<\/p>/,
  '<p class="lead">Raindrop Pet creates custom pet gifts, personalized pet accessories, handmade crystal pet collars and pet memorial keepsakes for dogs, cats and the people who love them.</p>'
);
if (!index.includes('class="seo-guides"')) {
  const css = `
/* ===== SEO GUIDES ===== */
.seo-guides{padding:64px 32px;background:#fff}.seo-guides-inner{max-width:1100px;margin:0 auto}.seo-guides h2{font-family:Georgia,"Times New Roman",serif;font-size:clamp(24px,4vw,34px);color:#2d2924;text-align:center;margin-bottom:10px}.seo-guides .intro{text-align:center;color:#888;font-size:14px;margin-bottom:28px}.guide-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.guide-card{border:1px solid #f0ebe3;border-radius:8px;padding:22px;background:#fff;transition:box-shadow .25s,transform .25s}.guide-card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,.07)}.guide-card h3{font-size:16px;line-height:1.35;color:#2d2924;margin-bottom:8px}.guide-card p{font-size:13px;color:#776d61;line-height:1.6}@media(max-width:768px){.guide-grid{grid-template-columns:1fr}.seo-guides{padding:48px 20px}}
`;
  index = index.replace("</style>", `${css}\n</style>`);
  const guides = `
<!-- SEO Guides -->
<section class="seo-guides">
  <div class="seo-guides-inner">
    <h2>Custom Pet Gift Guides</h2>
    <p class="intro">Helpful guides for choosing personalized pet gifts, memorial keepsakes and handmade accessories.</p>
    <div class="guide-grid">
      <a class="guide-card" href="best-custom-pet-memorial-gifts.html"><h3>Best Custom Pet Memorial Gifts</h3><p>Fur keepsakes, urns, portraits and crystal lamps for remembering a beloved dog or cat.</p></a>
      <a class="guide-card" href="how-to-choose-custom-pet-portrait.html"><h3>How to Choose a Custom Pet Portrait</h3><p>Pick the best photo, portrait style and gift format for a dog or cat portrait.</p></a>
      <a class="guide-card" href="pet-memorial-keychain-vs-urn.html"><h3>Pet Memorial Keychain vs Urn</h3><p>Compare daily-carry keepsakes and home memorial boxes before choosing.</p></a>
      <a class="guide-card" href="custom-pet-gifts-for-dog-moms-cat-lovers.html"><h3>Custom Pet Gifts for Dog Moms and Cat Lovers</h3><p>Personalized gift ideas for birthdays, holidays and pet parents.</p></a>
      <a class="guide-card" href="personalized-pet-accessories-guide.html"><h3>Personalized Pet Accessories Guide</h3><p>Handmade collars, bib scarves, clips, rugs, pillows and custom photo gifts.</p></a>
    </div>
  </div>
</section>
`;
  index = index.replace("<!-- Trust -->", `${guides}\n<!-- Trust -->`);
}
fs.writeFileSync(path.join(root, "index.html"), index);

const sitemapFiles = [...Object.keys(pages), ...Object.keys(articles)];
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapFiles
  .map((file) => {
    const loc = `${site}/${file === "index.html" ? "" : file}`;
    return `  <url><loc>${loc}</loc><changefreq>${file === "index.html" ? "weekly" : "monthly"}</changefreq><priority>${file === "index.html" ? "1.0" : file.startsWith("pet-") || file === "classic.html" || file === "zodiac.html" ? "0.8" : "0.6"}</priority></url>`;
  })
  .join("\n")}
</urlset>
`;
fs.writeFileSync(path.join(root, "sitemap.xml"), sitemap);
fs.writeFileSync(
  path.join(root, "robots.txt"),
  `User-agent: *
Allow: /

Sitemap: ${site}/sitemap.xml
`
);

console.log(`Updated SEO tags for ${Object.keys(pages).length} pages.`);
console.log(`Created ${Object.keys(articles).length} SEO guide pages.`);
console.log("Created retail/robots.txt and retail/sitemap.xml.");

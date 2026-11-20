# 2026-11-25（三）18:00｜勤美草悟聖誕村 v3 完整 6 張（實景照片 AI 編修）

完整版輸出：out_v3_full/（01、02 與 out_v3 逐位元相同；03–05 由 work/build_v3_full.py 產生；06 為固定結尾卡，與 11/23 步道篇 06_cta.jpg 同一檔案）。以下先記第 1–2 張（已核准的 v3 樣張），第 3–6 張在後段。

製作日期：2026-11-20（台北時間）。文案：/workspace/posts/20261125_勤美聖誕村_caption.txt（定稿，未改）。
康特修正（經你的全能小小助手轉達）：不要全新生成畫面，改用 v1 的 Commons 實景照片做 AI 編修。v1 紀錄見 sources_v1.md，v2（全 AI 生成）見 sources_v2.md。
程式：work/build_v3.py（沿用 work/build.py 版型與文字；封面標題下移 50px 到 y=1050，避開新增聖誕樹的樹腳）。輸出：out_v3/01_cover.jpg、out_v3/02_tree_lane.jpg。

## ⚠️ 排程時務必勾選 isAiGenerated
兩張底圖都是以真實照片為底、經 AI（GenerateImage 圖片編修，2026-11-20）**修改過**的圖片，非原始照片、非活動實景。
每張右下角兩個小標籤（16px 深色小框，與 v1 授權字同大小）：「AI 示意畫面」＋原作者授權。

## 底圖、授權與修改內容
| 張 | 原始照片 | 作者 | 原授權 | 本衍生圖授權 | 修改內容 |
|---|---|---|---|---|---|
| 01 封面 | File:勤美_誠品綠園道_201905.jpg https://commons.wikimedia.org/wiki/File:%E5%8B%A4%E7%BE%8E_%E8%AA%A0%E5%93%81%E7%B6%A0%E5%9C%92%E9%81%93_201905.jpg（本機 refs/parklane_night_2019_wpcpey.jpg） | Wpcpey | CC BY 4.0 https://creativecommons.org/licenses/by/4.0 | CC BY 4.0 要求標示作者與授權、註明有修改（已標「授權：Wpcpey・CC BY 4.0」＋「AI 示意畫面」，本檔記錄修改） | 先裁 4:5（x 510–1969，work/edit/base_cover_4x5.jpg），AI 編修：在草坪遠端、建築前加一棵一般圓錐形聖誕樹（暖白燈＋星星；非 NOIZ 主樹造型），沿草坪邊的行道樹加暖白串燈。建築、街景、構圖、夜色保留。結果 work/edit/cover_edit_v3.jpg（864×1152），再裁 y 72–1152 放大到 1080×1350，加深藍漸層與標題 |
| 02 流光之森＋光之道 | File:柳原教會鄧基鴻紀念禮拜堂.jpg https://commons.wikimedia.org/wiki/File:%E6%9F%B3%E5%8E%9F%E6%95%99%E6%9C%83%E9%84%A7%E5%9F%BA%E9%B4%BB%E7%B4%80%E5%BF%B5%E7%A6%AE%E6%8B%9C%E5%A0%82.jpg（本機 refs/liuyuan_church_2026_adao.jpg，2026-01-28 白天） | 阿道 | CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0 | **衍生作品，依相同方式分享條款同樣以 CC BY-SA 4.0 釋出**（第 2 張成品圖 02_tree_lane.jpg 整張以 CC BY-SA 4.0 授權） | 先裁 1382×778（y 310–1088，work/edit/base_church_16x9.jpg），AI 編修：白天改成藍調傍晚／入夜、禮拜堂玻璃透出暖光、背景大樓窗燈亮；兩側樹木纏上**銀白色**燈泡串燈（對應官方光之道銀白燈泡）；教堂本體不加燈。建築與構圖保留。結果 work/edit/church_edit_v3.jpg（1280×720），裁 1000×543 放入金框照片卡，地點 pill「柳原教會」 |

建築變形檢查：編修圖與原圖並排比對，封面百貨大樓（銅框窗格、綠牆陽台、圓形水塔、LED 下層立面）、兩側高樓與樹線一致；第 2 張禮拜堂 A 字形輪廓、木條外牆、淺色邊框、十字窗框與背景大樓一致，未見明顯變形。AI 另在禮拜堂玻璃內補出模糊的室內光與人影，屬示意。

## AI 編修 prompt（GenerateImage，reference_image_paths＝上表裁切底圖）
### 01 封面（aspect 3:4）
> Photo edit of the reference photo. Keep the photo exactly as it is: same camera position, framing and composition, same buildings (the white department-store building with copper-framed lit windows, green vertical garden balconies, the round rooftop tank, the dotted LED lower facade, the dark towers at the sides), same tree line and the same dark green lawn in the foreground. Do not change, redraw, straighten or restyle any architecture. Only ADD Christmas decorations: (1) one simple generic cone-shaped Christmas tree, about two storeys tall, standing at the far edge of the lawn slightly right of centre in front of the building, covered in warm white fairy lights with a small star on top (a classic fir tree shape, not geometric, not prisms, not mirrors); (2) strings of small warm white lights wrapped through the canopy of the trees along the lawn edge. Keep the night-time look and the sky as in the original. Keep the bottom third of the image (the lawn) calm and dark with no new objects. Photorealistic, natural lighting consistent with the photo. No text, no letters, no logos, no signage, no watermark.

### 02 第 2 張（aspect 16:9）
> Photo edit of the reference photo. Keep the photo exactly as it is: same camera position, framing and composition, the same church building (the tall pointed A-frame chapel with wooden slat cladding, the narrow light-coloured frame along its edges, the dark glass window with a cross-shaped mullion), the same high-rise buildings behind and the same trees on both sides. Do not change, redraw, straighten or restyle any architecture. Change the time to blue-hour dusk / early night: deep blue sky, warm interior light glowing softly through the chapel glass, lit windows in the background towers. ADD Christmas light-path decorations: countless small SILVER-WHITE (cool white, not gold, not yellow) bulb string lights wrapped along the trunks and branches of the trees on both sides and draped through their canopies, sparkling, giving a festive light-walkway atmosphere. Do not put lights or anything on the church building itself. Photorealistic, consistent with the original photo. No text, no letters, no logos, no signage, no watermark.

## 圖上文字（與 v1 相同，皆對應定稿文案）與來源
- 期間 2026/11/13（五）–2027/1/4（一）；流光之森在勤美術館好淺（噴水池廣場）前，亮燈 17:00–22:30，聲光秀 17:00–21:30 每 10 分鐘；光之道亮燈 17:00–22:30，沿線含柳原教會鄧基鴻紀念禮拜堂 — 官方「聖誕裝置」頁 https://event.parklanebycmp.com/event/2026parklanechristmas_design（2026-11-20 讀取）
- 8 公尺、40 萬顆銀白燈泡、約 250 公尺 — 自由時報 2026/11/17 https://news.ltn.com.tw/news/life/breakingnews/5643762（2026-11-20 讀取）
- 公車 27、81 至草悟道(市民廣場) — 勤美誠品綠園道「如何抵達」https://parklane.com.tw/service/transportation/


---

# 第 3–6 張（2026-11-20 台北時間製作；方法同第 1–2 張：Commons 可商用實景 → GenerateImage 圖片編修只加燈，構圖不變）

燈色：全部戶外樹燈都要求**銀白色燈泡**（勤美之森、PARK2 都在官方光之道沿線；市民廣場也統一用銀白，避免跟光之道混淆）。沒有任何一張加聖誕樹、NOIZ 主樹或官方裝置／地標的樣子。
每張照片右下（第 4 張為右上）兩個 16px 小標籤：「AI 示意畫面」＋「授權：作者・授權條款」。授權已於 2026-11-20 用 Commons API（extmetadata）重新確認。

| 張 | 原始照片（Commons） | 作者 | 原授權 | 衍生圖授權 | 修改內容／裁切 | 地點 pill |
|---|---|---|---|---|---|---|
| 03 左 | File:CMP_Midtown_勤美之森_20230228.jpg https://commons.wikimedia.org/wiki/File:CMP_Midtown_%E5%8B%A4%E7%BE%8E%E4%B9%8B%E6%A3%AE_20230228.jpg （refs/cmp_midtown_2023_brian25.jpg，2023-02-28 白天） | brian25_tw | CC BY-SA 2.0 https://creativecommons.org/licenses/by-sa/2.0 | **衍生作品，依 CC BY-SA 2.0 釋出**（標示「授權：brian25_tw・CC BY-SA 2.0」） | 裁 3:4（x 600–4196）→ work/edit/base_midtown_3x4.jpg；AI 改藍調傍晚、窗燈亮、樓下綠地樹木加銀白串燈 → work/edit/midtown_edit_v3.jpg（864×1152）；卡片 490×510 | 勤美之森 |
| 03 右 | File:勤美_誠品綠園道_B2_View_2019.jpg https://commons.wikimedia.org/wiki/File:%E5%8B%A4%E7%BE%8E_%E8%AA%A0%E5%93%81%E7%B6%A0%E5%9C%92%E9%81%93_B2_View_2019.jpg （refs/parklane_b2_2019_wpcpey.jpg，2019-05） | Wpcpey | CC BY 4.0 https://creativecommons.org/licenses/by/4.0 | CC BY 4.0（標示作者＋授權，並註明已修改：本檔） | 裁 3:4（x 500–1868）→ base_b2_3x4.jpg；AI 只在天花板與木作天花加銀白串燈（室內光線不變）→ b2_edit_v3.jpg（768×1024）；卡片 490×510 | 勤美誠品 B2 |
| 04 背景帶 | File:Calligraphy_Greenway_Square.jpg https://commons.wikimedia.org/wiki/File:Calligraphy_Greenway_Square.jpg （refs/caowu_square_night_2022_taichunggov.jpg，2022-09-02 空拍） | 臺中市政府 | 政府網站資料開放宣告（{{GWOIA}}，可商用、須標示出處）https://www.taichung.gov.tw/13599/post | 同條件，標示「授權：臺中市政府・政府網站資料開放宣告」並註明已修改 | 裁 16:9（y 230–3042）→ base_park2_16x9.jpg；AI 改藍調傍晚、建築下方暖光、廣場與屋頂花園樹木加銀白串燈 → park2_edit_v3.jpg（1280×720）；1080×420 頂部背景帶＋深藍漸層。原圖右下角的市府浮水印 logo 在 AI 編修時被移除，且不在裁切範圍內 | PARK2 草悟廣場 |
| 05 | File:2022_Taichung_Civic_Square.jpg https://commons.wikimedia.org/wiki/File:2022_Taichung_Civic_Square.jpg （refs/civic_square_2022_ssjf01.jpg，2022） | SSJF01 | CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0 | **衍生作品，依 CC BY-SA 4.0 釋出** | 裁 16:9（y 300–3684）→ base_civic_16x9.jpg；AI 改藍調傍晚、窗燈亮、草坪對面整排樹加銀白串燈 → civic_edit_v3.jpg（1280×720）；卡片 1000×397 | 臺中市民廣場 |
| 06 | 固定結尾卡 /workspace/ig-assets/templates/cta_card.png（與 posts/2026-11-23_1800_trails_v1/06_cta.jpg 同檔，md5 bb075e98…） | — | 自家設計 | — | 無照片、無 AI | — |

改選說明（照規劃換點）：
- 第 3 張原規劃用 PARK2 草悟廣場（Wpcpey）小圖；因第 4 張已用 PARK2，第 3 張改用同在路線上的「勤美之森」（PARKLANE CHRISTMAS 地標所在），pill 標實際照片地點。B2 照片是 2019 年 B2 走道，不一定是挑空區本身 → pill 只寫「勤美誠品 B2」。
- 第 5 張原規劃首選 Dquai 的草悟道街景，但畫面有大型 Starbucks／FamilyMart 招牌 → 改用規劃中的備案「臺中市民廣場」（SSJF01）。

建築變形檢查（原圖與編修圖並排比對，work/preview_v3/cmp_midtown.jpg、cmp_park2.jpg）：勤美之森兩棟住宅塔樓、勤美洲際大樓（原圖就有的頂部招牌）、禮拜堂木構量體一致；PARK2 弧形量體、屋頂花園、藍色招牌一致；B2 走道、地磚、店面一致；市民廣場百貨大樓、看板、樹線、人物一致。未見明顯變形，無需重做。

## AI 編修 prompt（GenerateImage，reference_image_paths＝上表裁切底圖）
### 03 左 勤美之森（3:4）
> Photo edit of the reference photo (residential skyscrapers with a low office building and a green tree-filled park at their base). Keep the photo exactly as it is: same camera position, framing and composition, same towers, facades, windows, glass office block, low buildings and tree canopy. Do not change, redraw, straighten or restyle any architecture. Change the time to blue-hour dusk: deep blue sky, warm lit windows in the towers and office block. ADD Christmas lights only: countless small SILVER-WHITE (cool white, not gold) bulb string lights wrapped through the trees of the green park at the bottom of the image, sparkling. Do not add a Christmas tree, giant letters, signs or any new structures. Photorealistic, consistent with the photo. No text, no letters, no logos, no watermark.

### 03 右 勤美誠品 B2（3:4）
> Photo edit of the reference photo (an indoor shopping-mall basement corridor). Keep the photo exactly as it is: same camera position, framing and composition, same corridor, floor tiles, ceiling, wooden ceiling panel, shop fronts, counters, people and signage. Do not change, redraw, straighten or restyle any architecture or shops. Only ADD festive Christmas lights: strands of small silver-white (cool white) bulb string lights draped along the ceiling edges and the wooden ceiling panel, softly glowing, with a gentle sparkle. Do not add any Christmas tree, snowman, characters, decorations with text, or new objects. Photorealistic, consistent with the original lighting. No new text, no new logos, no watermark.

### 04 PARK2 草悟廣場（16:9）
> Photo edit of the reference aerial photo (a low curving white mesh-clad commercial building with a green roof garden and a paved plaza with trees, surrounded by city buildings). Keep the photo exactly as it is: same aerial camera position, framing and composition, same curving building shape, roof garden, plaza paving, trees and surrounding buildings. Do not change, redraw, straighten or restyle any architecture. Change the time to blue-hour dusk: deep blue sky, warm lit windows in the surrounding buildings, soft warm light from under the curving building. ADD Christmas lights only: small SILVER-WHITE (cool white, not gold) bulb string lights wrapped through the trees on the plaza and roof garden, sparkling. Do not add a Christmas tree, stalls, signs or any new structures. Photorealistic, consistent with the photo. No text, no letters, no logos, no watermark (remove nothing that is part of the buildings).

### 05 臺中市民廣場（16:9）
> Photo edit of the reference photo (a large city park lawn with people and dogs, a white department-store building with a billboard and towers behind, a row of trees across the lawn). Keep the photo exactly as it is: same camera position, framing and composition, same buildings, billboards, tree line, lawn and people. Do not change, redraw, straighten or restyle any architecture or people. Change the time to blue-hour dusk: deep blue sky with a little sunset glow, warm lit windows in the buildings. ADD Christmas lights only: small SILVER-WHITE (cool white, not gold) bulb string lights wrapped through the row of trees across the lawn, sparkling. Do not add a Christmas tree, signs or any new structures. Photorealistic, consistent with the photo. No new text, no new logos, no watermark.

## 第 3–5 張圖上文字 ↔ 定稿文案（2026-11-20 重新讀官方頁確認）
- 03 其他必拍：四項名稱與地點 = 文案「📸 其他必拍」；官方聖誕裝置頁 https://event.parklanebycmp.com/event/2026parklanechristmas_design （地標＝勤美之森璞真大門前廣場；DISCO SNOWMAN＝勤美誠品綠園道 B2F 挑空區；森林片語＝勤美誠品西側平台；森林迴響＝PARK2 主、次入口）
- 04 活動＆市集：文案「🎁 活動＆市集」7 項＋「🫧 冬季展」；官方活動體驗頁 https://event.parklanebycmp.com/event/2026parklanechristmas_activities （DJ 派對官方另有 11/21，發文時已過，依文案只列 12/5、12/26；GROOVE 日期 12/4、11、18 五＋12/5、12、19、26 六 一致）。各場細節（時段、免費）見上方「已查證事實」與各活動詳細頁。
- 05 交通＆停車：文案「🚌」「🚗」；官方如何抵達頁 https://event.parklanebycmp.com/event/2025parklanechristmas_transportation （300–308 科博館、159 廣三SOGO 步行約 4 分鐘、水安宮站 27/81/107/107 延、市政府站 300–308、人潮眾多鼓勵搭大眾運輸）；勤美誠品如何抵達 https://parklane.com.tw/service/transportation/ （停車 07:00–24:00、1000 位、4F–14F、平日 50／假日 70 元每小時、消費折抵）。

精簡／一次性說明：
- 公車 27、81 → 草悟道(市民廣場) 已在第 2 張，第 5 張不重複（捷運水安宮站那行仍寫轉乘 27／81，是不同資訊）。
- 03：「緞帶字地標」「鏡球雪人工廠」保留；04：收藏行動寫「加 LINE 六站集章，勤美誠品 B1 換貼紙禮包」（略「會員中心」「限定」）；PEEK-A-BOO 略「插畫家 Minghan H.」「微型展免費看」；HO'clock 寫「馬戲巡遊到主樹」（略「從勤美誠品走光之道」）；冬季展略「Studio Swine × A.A. Murakami」「泡泡樹」。完整內容都在文案。
- 05：YouBike 寫「臺中市民廣場、草悟道站／都在公益路155巷」；停車折抵細節（500 元折 1 小時、最高 6 小時）不放圖上。

事實衝突（未寫進圖）：勤美誠品官網寫高鐵 159 下車「步行約 5 分鐘」，聖誕村官方交通頁寫「約 4 分鐘」→ 依文案與活動官方頁用 4 分鐘。官方交通頁另有台中客運 72 號，與商場頁不同 → 不寫（同文案）。

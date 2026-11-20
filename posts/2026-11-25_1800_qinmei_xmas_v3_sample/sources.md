# 2026-11-25（三）18:00｜勤美草悟聖誕村 v3 樣張（封面＋第 2 張：v1 實景照片 AI 編修）

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

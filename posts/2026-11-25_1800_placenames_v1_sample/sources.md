# 2026-11-25（三）18:00｜中部地名由來 v1 樣張（封面＋第 2 張）

查證／製作日期：2026-11-19（台北時間）。文案定稿：/workspace/posts/20261125_caption.txt（未改動）。
產生程式：work/build.py（沿用 packing v3b 設計系統：/workspace/posts/20261117_1000_packing/work_v3_final/build_final.py 的字型、色票、masthead/footer 與排版 helper）。
字型：jf open 粉圓 2.1（SIL Open Font License 1.1）。

## 地圖資料（第 1 張）
- 縣市界線：內政部〈直轄市、縣市界線(TWD97經緯度)〉https://data.gov.tw/dataset/7442
  授權：政府資料開放授權條款－第1版（需標示出處）。畫面右下角標示「授權：內政部・政府資料開放授權條款」。
- 取用的 TopoJSON 轉檔：dkaoster/taiwan-atlas 2021.9.20（MIT），counties-10t.json；鄉鎮界 towns-10t.json（源自內政部〈鄉鎮市區界線(TWD97經緯度)〉https://data.gov.tw/dataset/7441，同授權）只用來核對圖針位置，未畫在圖上。
  https://cdn.jsdelivr.net/npm/taiwan-atlas/counties-10t.json ・ https://github.com/dkaoster/taiwan-atlas
- 投影：等距圓柱，經度乘 cos 24°，1 度≈1100 px。海岸線、縣市界都是真實資料，只做柔和配色。
- 圖針：放在今日區／鎮公所附近的經緯度（大約位置，誤差約 1 km 內）；每一點都以程式核對落在該鄉鎮市區的界線內。
  | 舊名 | 今名 | 經度 | 緯度 |
  |---|---|---|---|
  | 葫蘆墩 | 豐原區 | 120.7186 | 24.2525 |
  | 牛罵頭 | 清水區 | 120.5595 | 24.2675 |
  | 五汊港 | 梧棲區 | 120.5317 | 24.2553 |
  | 沙轆 | 沙鹿區 | 120.5664 | 24.2335 |
  | 大里杙 | 大里區 | 120.6779 | 24.0993 |
  | 阿罩霧 | 霧峰區 | 120.7003 | 24.0621 |
  | 半線 | 彰化市 | 120.5427 | 24.0805 |
  | 鹿仔港 | 鹿港鎮 | 120.4347 | 24.0560 |
  | 埔里社 | 埔里鎮 | 120.9680 | 23.9652 |
  | 林圮埔 | 竹山鎮 | 120.6869 | 23.7579 |
- 標籤以程式檢查：膠囊彼此、膠囊與圖針、膠囊與地圖邊框皆無重疊；膠囊文字以字形實際墨跡置中。

## AI 生成元素（排程時請勾 isAiGenerated）
以 GenerateImage 生成於白底，再用 packing 同一套去白底程式（work/cutout.py）去背。原圖在 work/ai/，去背在 work/cutouts/。
- 第 1 張：南投山區的可愛小山（mountains_sheet_02.png），純裝飾、示意中央山脈。地圖本身不是 AI。
- 第 2 張：大里「木樁繫竹筏」（dali_stake_raft）、豐原「葫蘆」（fengyuan_gourd，對應「三座小丘形狀像葫蘆」一說）、「松柏林」小樹（fengyuan_pines，對應「泰耶爾墩＝松柏林」一說）。
- 其餘（地圖、圖針、卡片、文字）為程式繪製。
- 未採用：work/ai/_rejected_gourd_hills.jpg（看不出葫蘆與三座小丘）。

## 第 2 張文字來源（皆取自定稿文案，精簡後上圖）
- 大里：臺中市大里區公所〈歷史沿革〉https://www.dali.taichung.gov.tw/982726/982748/982754/982757/1210435
- 豐原：臺中市豐原區公所〈歷史沿革〉https://www.fengyuan.taichung.gov.tw/982171/1514378/982195/1114352

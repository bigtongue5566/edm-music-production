# 電子音樂的開放式製作路由

先找本案的聲音語法，再選工具。以下是便於製作的家族路由，非完整歷史樹，也不主張子流派互斥。使用者明確指定的參考與地方場景優先於表格。「支援」表示可依此研究並製作；內建九個 preset 的能力另列，不以分類表冒充引擎功能。

## 從可聽特徵選方向

| 家族／方向 | 要決定的節奏與聲音關係 | 可採製作策略 |
| --- | --- | --- |
| House：classic、deep、progressive、tech、future、tropical、melodic | 四拍基礎如何 swing；bass、和弦、hook 誰主導 | 先建立 groove，再按分支選 organ、短句或主題發展；不要把所有 House 等同大鋪陳 |
| Techno：Detroit、minimal、dub、acid、industrial | 循環中的重音、音色與空間如何演化 | 小節級微變、調變周期、dub send、acid 式濾波或失真；非每首都要旋律與 rumble |
| Trance：progressive、uplifting、psy | riff、低音脈動、期待與釋放的關係 | Uplifting 可分層展開旋律；Psy 需設計短低音序列及節奏化音色，不把 supersaw 當通則 |
| Dubstep：deep、UK、brostep、melodic、riddim | half-time 重心、sub、留白、bass 問答 | 依分支選克制低頻或激烈中頻，不一律「怪獸咆哮」；常以約 140 或半速 70 記拍 |
| Electronic Trap／Future Bass／Wave | half-time／double-time、808 或和弦調變、hat 細分 | 分清嘻哈 Trap 與電子舞曲 Trap；808 音高、roll、呼應或調變和弦按方向設計 |
| Drum & Bass／Jungle：liquid、neuro、jump-up、drumfunk | 快速破拍、ghost notes、sub／mid-bass 分工 | Jungle 可重切 break，liquid 可強調流動樂句，neuro 可主導音色演化；D&B 是舞曲家族 |
| UK Garage／2-step／Speed Garage／Bassline | 四拍或 2-step、shuffle、低音與短句的空隙 | 實作微時值及力度；普通 breakbeat 改 BPM 不會自動變 UKG |
| Breakbeat／Breaks／Big Beat／Electro | 切分 kick、backbeat、funk 或機械感 | 自製或合法 break 重切；Electro 的機器 funk 不等同 Electro House |
| Hardstyle／Hardcore／Gabber | kick 音高、失真、bass 與主題的分工 | 選合適失真與取樣管線，控制低頻與瞬態；不是把 House 加速與 clipping |
| Synthwave／Retrowave／Synthpop／Electropop | 復古音色、歌曲／器樂 hook、drum-machine 節奏 | 以音色與曲式實作；風格不必依賴人聲，要求無人聲時保留器樂版本 |
| Ambient／Drone／Soundscape | 可無固定拍、前後景、音色持續與慢變 | 用秒數／事件而非必需小節；不要求鼓、hook、drop 或舒適冥想用途 |
| Downtempo／Chillout／Trip-hop／Lounge | 慢 groove、空間、取樣與人性時值 | 決定有鼓／稀疏鼓／無鼓；Chillout 是重疊的用途／美學詞，不是固定 BPM 類別 |
| IDM／Glitch／Experimental | 不規則事件、重切、機率、非線性或音色結構 | 控制亂數、保存 automation／seed／音訊，必要時採複拍號或自由時間 |
| Electroacoustic／Musique concrète／Acousmatic | 實錄素材的形態、空間、剪輯與轉化 | 來源與授權先清楚；可用原創錄音、granular、spectral、resampling，無需硬套調性 |
| Cinematic／Industrial／Hybrid electronic score | 服務敘事與 cue 的聲音關係 | 從上述語法組合，分清節奏、質地與管弦配器；「緊張」不自動等於高速舞曲 |

## 速度是參考，不是分類器

House 約 120–128、Techno 約 125–140、Trance 約 130–145、Dubstep 約 140、電子 Trap 約 140–160、DnB 約 170–175 可作常見教學起點，但不是邊界。慢速或快速分支、歷史時期、半／倍速記拍皆會超出。Ambient 可能沒有可用的單一 BPM；Downtempo 也不限於 100 以下。不要把使用者的速度要求改成表格值。

## 開放擴充與實作選擇

1. 把指定風格拆成節奏／微時值、低音角色、和聲／音高、音色／處理、曲式／空間；混合案記錄各元素來自哪個方向。
2. 讀相關原始製作教學、作者訪談或技術文件。未有聽音能力時不捏造參考曲的實際音訊分析。
3. 選能實現這些特徵的現有 DAW／音源。採本機 starter 時檢查它真正支援的音符、拍號與音色。
4. 先完成一段具有所選語法的材料，再展開全曲。若工具不足，實作必要功能或換工具，不暗中退回某個 House preset。

## 內建配方與限制

| CLI 起點 | 真正不同之處 |
| --- | --- |
| melodic-house | 四拍、反拍 bass、鍵盤與 pluck 樂句 |
| breakbeat | 切分鼓、swing、tine keys 與 organ |
| drum-and-bass | 快速 broken beat、ghost snare、Reese bass |
| techno | 單一和聲中心、短脈衝序列、分樂句明暗變化 |
| trance | 四拍、反拍短低音、十六分 arp 與 saw 層 |
| dubstep | 第三拍 snare、不同調變速度的 bass 問答 |
| trap | 第三拍 snare、三連音 hat roll、定音的 808 式低音 |
| ambient | 無鼓／無 kick ducking，按秒數換和聲的慢變 drone 與噪聲質地 |
| downtempo | 延後的 backbeat、鬆散 hat、稀疏 tine 回應與較長 bass |

大小調三和弦和簡化合成器仍是 starter 的限制。Deep House、Future Bass、Hardstyle、IDM 等可用本 Skill 製作，但需要對應的實際編曲／DAW 管線，不能聲稱 CLI 已內建。

## 資料與閱讀範圍

製作路由是本 Skill 的綜合建議。舞曲的直接教學來源見 [genre-production.md](genre-production.md)；Ambient／自由時間見 [ambient-and-experimental.md](ambient-and-experimental.md)。新增檢閱日期：2026-10-24。分支例子用來定位需求，不主張存在固定「五大」或「八大」的唯一分類。

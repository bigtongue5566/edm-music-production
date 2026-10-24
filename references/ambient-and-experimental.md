# 氛圍、低速與實驗電子的製作

用於 Ambient、Drone、Soundscape、Downtempo／Trip-hop、IDM／Glitch、Electroacoustic 及混合案。以下是製作決策，非所有作品的通則；指引範圍大於附帶的 Ambient／Downtempo 合成草稿。

## 沒有鼓也需要結構

先指定前景與背景如何隨時間改變：來源靠近或遠離、頻譜由窄到寬、乾聲轉成聲景、密度聚集再稀釋。用事件、音色和空間構成樂句，不為「有起伏」強插 riser、snare roll 或 drop。Ambient 可以溫和、黑暗或不安，不一律等同睡眠音樂。

**直接來源：** [Ableton：KMRU: Spaces](https://www.ableton.com/en/blog/kmru-spaces/)，檢閱 2026-10-24。KMRU 訪談談到使用質地、field recording 後離開 grid／metronome，更直覺地決定何時疊入材料。這支持自由時間作為可行的創作方法，不表示 Ambient 都必須無拍。

**本案實作：** 可在時間線寫「0–18 秒揭露來源、18–42 秒增加頻譜／層次、42–60 秒退去」，再用 automation 和交疊形成轉變。曲長是限制，內部不必等分小節。Drone 先選持續音高／泛音關係；無調性案則記錄質地與頻域意圖，不用三和弦音符 checker 阻止整個方向。

## 質地與空間

混響只是材料之一。改變聲源、起音、拉伸、剪輯、濾波、聲像與調變，使變化可在實際音訊中辨識。低頻持續音與寬頻噪聲分工；檢查回授、累積能量、突變 click 和單聲道。

**方法來源：** [Native Instruments：7 quick tips for ambient, atmospheric music](https://www.native-instruments.com/blogs/blog/7-ways-to-amp-up-the-atmosphere)，檢閱 2026-10-24。官方教學包含空間、質地及弱化的節奏殘影；此處採用的製作建議是讓 rhythmic shadow 可作低強度層，而不是必需的前景鼓。

想做 granular／spectral 時優先使用成熟工具，例如 [Robert Henke 的 Granulator III](https://roberthenke.com/technology/granulator3.html) 或可用 DAW 的既有設備。這是工具路線；本套簡化 additive drone 不應標示成完整 granular 引擎。需要 field recording 時使用原創或合法授權素材，保存來源，避免把取樣素材宣稱為自製錄音。

## Downtempo、Trip-hop 與 Chillout

先決定 groove 是規律、破拍、laid-back 還是稀疏。hat 的微時值、snare 的重心、低音延音和取樣／和弦的空隙，比「BPM 小於 100」更有製作意義。可有人聲，也可依 brief 完全器樂；可有鼓或接近無鼓。不要把所有案都加爵士和弦、黑膠噪聲與海灘音效。

本機 downtempo 是一個延後 backbeat、稀疏電鍵盤與 organ 的配方，不是 Trip-hop 的完整定義。需要 break chop、錄音質感或特殊 swing 時使用相應素材與工具。

## IDM、Glitch 與電聲實驗

先設計規則與可感知的變化，之後才加入受控不規則性。例如不同長度 pattern 的交錯、少量機率觸發、resampling 後重切，或原始聲源逐漸失去辨識度。固定 seed 可重現隨機選擇；保存產生的 audio、automation 或 session。不是所有 Glitch 都要亂數，也不是所有實驗電子都要高密度。

不強迫主旋律、4/4、小節換和弦或緊張音程解決；保留使用者對音量與刺耳程度的要求。失真、噪聲和不協和可以是材料，但數位 clipping、破檔、失控 feedback 仍應分開查明。需要複拍號／非音高事件時用對應 DAW／引擎，不把 GM MIDI 當完整聲音來源。

## 檢查要符合意圖

留白、極低音量與漸進變化可能是構成，不因 RMS 低於舞曲門檻就加鼓或 Pad。記錄預期休止與低能量區間；本機 `music.intentional_silence` 只對完成音檔的近靜音告警作語境判讀，不會自動靜音混音。循環測接點，長尾測 truncation，自由時間測事件落點。固定 sample count、無錯誤解碼與音符無衝突都不能代替聽音評審。

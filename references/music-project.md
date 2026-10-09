# 音樂專案設定

project.json 只包含音樂資料。沒有畫面、LOGO、字型或影片尺寸欄位。

| 欄位 | 意義 |
| --- | --- |
| name / slug | 顯示名稱與成品檔名；slug 使用英數、底線或連字號 |
| duration | 秒數，精確到 48kHz 整數樣本；至少 1 秒 |
| music.bpm | 範本支援 30–240 BPM，Melodic House 常以約 120 BPM 開始 |
| music.style | melodic-house、breakbeat、drum-and-bass，控制實際編曲、音色與混音分支；舊專案未填時沿用 melodic-house |
| music.key | 調性，例如 G major、D major、A minor、F# minor；大小調皆可移調 |
| music.progression | 循環的和弦級數；每小節一個和弦，高潮重新從第一個開始，outro 與最後小節回到主和弦 |
| music.seed | 鼓與噪聲合成的固定種子，讓相同設定可重現 |
| music.lufs / true_peak | 母帶目標；預設 −16 LUFS、−2 dBTP |
| music.continuity | 可選物件，tie_pad 預設 false、room_wet 預設 0（0–0.5）；替換持續 Pad 或加入濾波 room，需符合本曲編曲意圖 |
| music.export_stems | 是否輸出 Float32 WAV 分軌，預設 false |
| music.soundfont / fluidsynth | 可選本機 SoundFont 與相容的 FluidSynth 執行檔 |
| music.soundfont_source / license | 使用音色庫的來源 URL 與本機授權檔路徑 |
| sections | 連續的音樂段落，涵蓋 0 到 duration，包含 start、end、role、label |

大調支援 I、ii、iii、IV、V、vi；預設 I–V–vi–IV。
小調支援 i、III、iv、v、V、VI、VII；預設 i–VI–III–VII。小調 V 為升高導音的大三和弦。擴充更多和弦與旋律張力時，同時調整 composer 與檢查的允許音符。

sections.role 可用 intro、groove、build、drop、break、outro。label 供人閱讀。段落切換在指定時間做效果與鼓密度的提示；主和弦／鍵盤／主旋律以小節為單位切換。若要所有聲部在特定時刻一起切換，優先把該時刻設在小節邊界，或改寫局部編曲。

4/4 拍的一拍 = 60 / bpm 秒，一小節 = 240 / bpm 秒。
片長不是整小節時最後小節裁切、主和弦解決並淡出。改成其他拍號或 DJ 延伸結構時，需要調整範本節奏。

MIDI 的 GM 音色是編輯建議，不會精確重現自製合成器。分軌共用增益與淡入淡出，含原始混音的 EQ／ducking；相加重現 premaster，沒有逐軌獨立響度正規化。WAV 母帶經另一階段響度處理，音量可能不同。

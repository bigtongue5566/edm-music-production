---
name: electronic-music-production
description: "Compose, arrange, design sounds, mix, master, and revise electronic music across dance, ambient, downtempo, experimental, and hybrid styles. Deliver playable audio and appropriate editable sources; use for original tracks, electronic scores/BGM, or repairs to their rhythm, harmony, timbre, arrangement, and mix."
---

# 電子音樂製作

製作可播放的 Electronic Music，交付音訊與適合本案的可編輯來源。電子舞曲是其中一部分；無鼓、自由時間、聲景、實驗電子及混合流派也在範圍內。影片與品牌素材不是必要條件。

## 先決定音樂語法

沿用使用者的片長、風格、情緒、用途與偏好。先定義脈動（四拍、破拍、half-time、自由時間）、聲音主體（旋律、低音、鼓、質地）、和聲語法與段落演變。BPM 是編曲座標，不能單獨決定曲風；同一首歌也可能採半速／倍速計拍。

讀 [references/electronic-styles.md](references/electronic-styles.md) 選擇相關家族，舞曲細節再讀 [references/genre-production.md](references/genre-production.md)，氛圍與實驗方向讀 [references/ambient-and-experimental.md](references/ambient-and-experimental.md)。這些是開放的製作路由，不是完整且互斥的分類表。未列出的子流派、地方場景與混合風格仍可處理：研究該方向的原始製作資料，從節奏、音色、和聲、空間與曲式建立實作，記錄採用的來源。

已有明確方向就直接製作；方向差異會實際影響成品而資訊不足時，可做短片段比較。參考曲分析、不同作品的聲音身份見 [references/style-and-identity.md](references/style-and-identity.md)。不能把每個要求轉成相同鋼琴開場、四拍鼓、反拍 bass 與 pluck，也不能只換 BPM、調性、曲名或 seed 冒充另一曲風。

## 依風格作曲與設計聲音

先完成本曲需要的核心材料：可能是鼓／低音互動、riff、和聲樂句，也可能是聲景、非週期質地或音色變形。讓 swing、切分、重拍、音符長短、包絡、調變與聲部進出在實際音訊及可編輯來源中發生。

和聲依 brief 選擇。未指定且需要舒適、旋律型 BGM 時，可從低張力三和弦開始；明確的爵士延伸、調式、Drone、無調性或實驗方向使用相應語法，不套用一律禁七度／九度的規則。使用者要求協和或不喜歡張力時優先保留。和弦音、經過音、聲部尾音與音色粗糙感分開判斷；方法與保守檢查的邊界見 [references/harmonic-comfort.md](references/harmonic-comfort.md)。

曲式也依用途選擇：DJ 段落、build／drop、歌曲式、緩慢演化、非線性段落或循環都可以。Ambient 不強塞鼓和高潮；Techno 可用微小音色與節奏變化推進；Dubstep 不一律等同 Brostep；Chillout 不一律等同無鼓或特定 BPM。從參考與本案選擇，不把家族特徵當作每個子流派的硬規則。

精確保留指定秒數。先設計最後一次有效起音、尾音空間及最終狀態；以編曲完成終止，不只在未結束的 loop 上淡出。漸快／變速作品共用 beat-to-time map；自由時間用秒數與事件標記，不虛構固定拍點。可循環、硬切及長尾結尾按實際需求驗證。

優先沿用現有 DAW、樂器與成熟套件。合成、取樣、FM、wavetable、granular、resampling 或 field recording 按所需聲音選擇。真實樂器、合成近似與取樣來源如實標示；不把簡單振盪器包裝成專業音色庫。頻段分工、ducking、動態與空間服務本曲，不能每種風格都套同一個強側鏈或響度。混音細節見 [references/composition-and-mix.md](references/composition-and-mix.md)。

## 修改既有音樂

反覆被指出單調、配器不對或要求研究知名配樂時，讀 [references/score-development.md](references/score-development.md)，把研究轉成主題、音色與聲部的實際改寫。刺耳、主擊／回聲不清或「每拍斷掉」時，讀 [references/continuity-and-articulation.md](references/continuity-and-articulation.md)，solo 被指出的聲部與時間段，分辨 gate、release、尾音重疊、ducking 及刻意留白。用同段、相近響度的音檔比較；影片配樂另核對畫面 cue。

## 可用管線與能力邊界

音樂製作範圍不受內建 preset 限制。已有合適 DAW／專案時直接使用；需要本機可重現草稿時，讀 [references/local-workflow.md](references/local-workflow.md) 與 [references/music-project.md](references/music-project.md)。內建九個實際編曲起點：`melodic-house`、`breakbeat`、`drum-and-bass`、`techno`、`trance`、`dubstep`、`trap`、`ambient`、`downtempo`。

```text
uv run --no-project python <skill>/scripts/init_project.py --project <music-directory> --duration 90 --style ambient
uv sync --project <music-directory>/work
uv run --project <music-directory>/work python <music-directory>/work/compose_music.py --project <music-directory>
uv run --project <music-directory>/work python <music-directory>/work/finish_music.py --project <music-directory>
```

這些是有限的合成研究，不是「所有流派的一鍵專業製作」。其他方向需實作所需鼓型、聲音、和聲表示與 automation，或改用適合的現有工具；不可把相近 preset 改名交付。範本仍以大小調三和弦、4/4／自由時間與固定 MIDI 參考速度為限；複拍號、延伸和弦、無調性、完整 granular／wavetable 與 tempo map 需要對應管線。舊 `compose_edm.py` 保留相容，新專案使用 `compose_music.py`。

## 檢查、來源與交付

有聽音能力才宣稱試聽；檢查完整曲目、段落銜接、關鍵音色、高潮或質地轉變、片尾、小音量與單聲道。沒有聽音能力時，提供可播放音檔並說明已做的客觀檢查。訊號、MIDI 與符號和聲檢查不能證明曲風成立、悅耳或商業完成度。

依用途交付 WAV 母帶、方便播放的格式，以及需要的 MIDI、stems、automation／DAW 或程式來源。純音訊質地不必強行轉成 MIDI；MIDI 無法保存的音色與空間另附可重建來源。記錄樂曲、音色／取樣及第三方錄音的來源、授權與必要雜湊，分清原創音符與外部素材。

對完成檔直接檢查片長、解碼、取樣率、聲道、響度、真峰值與結尾；必要時檢查短時間窗、相位與循環接點。Ambient 的低能量與實驗音樂的休止不自動當成故障；標記預期休止後判讀。範本預設 −16 LUFS、−2 dBTP 是 BGM 起點，不是所有風格的要求。工作檔放 work/、成品放 outputs/，交付可直接播放的結果與實際限制。

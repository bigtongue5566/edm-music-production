---
name: edm-music-production
description: "Compose, arrange, synthesize, mix, master, and revise original instrumental EDM with playable audio, editable MIDI, optional stems, provenance, and direct audio QC. Use for EDM songs, Melodic House tracks, electronic background music, or requests to fix their harmony, sound design, arrangement, and mix; video production is optional and outside this skill's core scope."
---

# EDM 音樂製作

製作可播放的 EDM，交付完成版音訊與需要的可編輯來源。可單獨作曲、製作 BGM 或修改現有配樂；不需要影片、品牌素材或其他 Skill。

## 明確的音樂目標

沿用對話中的片長、曲風、情緒、用途、速度與調性。缺少次要設定時可選合理起點並繼續；Melodic House 是附帶範本的方向，不是所有 EDM 的唯一選擇。指定長度要精確保留，非整小節長度以末段編曲收束，不擅自延長。需要口白空間、無人聲、可循環或不同力度時，讓編曲與輸出符合要求；可循環版本需另做銜接，不套用範本的淡出。

## 作曲、編曲與音色

先建立調性、和弦、主旋律輪廓與段落時間表。讓長音與重拍考慮當下和弦；經過音、懸留、延伸音等張力需有意安排及解決。固定旋律不應任意疊在所有和弦上。檢查跨和弦的延音、延遲與混響是否衝突。

讓主旋律、低音、鼓、和弦、琶音與效果各有角色；用疏密、音域、濾波與起伏組成開場、build、drop、break、outro 等段落。依用途調整曲式，不必照範本的固定樂句。讓主旋律可辨識，副旋律和效果支援它。

選擇合適的取樣樂器或可控制泛音的合成器，處理過亮音色、不合適的失諧、非整數泛音與尾音。為大鼓與低音留出空間，使用節拍錯開、EQ、側鏈或音量 ducking；減少頻段重疊的聲部。詳細方法與不和諧排查見 [references/composition-and-mix.md](references/composition-and-mix.md)。

## 本機音樂範本

有現成 DAW、專案或音源時優先沿用；沒有管線時可用獨立 Python 範本。開始前閱讀 [references/local-workflow.md](references/local-workflow.md) 與 [references/music-project.md](references/music-project.md)。

```text
python <skill>/scripts/init_project.py --project <music-directory> --duration 90 --bpm 120 --key "G major"
python <music-directory>/work/compose_edm.py --project <music-directory>
python <music-directory>/work/finish_music.py --project <music-directory>
```

修改 project.json 的片長、BPM、大小調、和弦級數與段落；範本輸出原創合成鍵盤與電子音色，亦支援外部 SoundFont／FluidSynth 鋼琴。可開啟分軌輸出，供重新混音。依本案重寫樂句或音色，不把範本的同一旋律當成每次成品。

## 檢查、來源與交付

有聽音能力時檢查完整曲目，以及和弦轉換、高潮、間奏、片尾、小音量及單聲道聽感。量測與音符檢查不能證明好聽；沒有實際聽音能力時，清楚說明客觀檢查，提供可播放結果，不宣稱已試聽。使用者指出不和諧時，分析和聲、旋律、音色、聲部及尾音，再交付修改版本。

交付 24-bit WAV 母帶、AAC 或使用者指定格式，及需要的 MIDI／分軌；直接檢查完成版的片長、取樣率、聲道、解碼、響度、真峰值、淡出與意外靜音。母帶目標依用途選擇，範本預設 −16 LUFS、−2 dBTP，並驗證 AAC 編碼後的峰值。

分別記錄樂曲、音色庫／取樣、第三方歌曲的來源。真實鋼琴、合成鍵盤與取樣庫如實標示；保存實際使用音色庫的來源、雜湊與授權。若使用現成歌曲，確認使用範圍並標示，不能宣稱是原創。

工作檔放在 work/、成品放在 outputs/。在聊天中提供可直接播放的音訊與成品連結，將實際測量及尚需主觀判斷的事項說清楚。

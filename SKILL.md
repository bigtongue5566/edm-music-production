---
name: edm-music-production
description: "Compose, arrange, synthesize, mix, master, and revise original instrumental EDM with playable audio, editable MIDI, optional stems, provenance, and direct audio QC. Use for electronic dance music, electronic background music, or requests to fix their harmony, sound design, arrangement, and mix; video production is optional and outside this skill's core scope."
---

# EDM 音樂製作

製作可播放的 EDM，交付完成版音訊與需要的可編輯來源。可單獨作曲、製作 BGM 或修改現有配樂；不需要影片、品牌素材或其他 Skill。

## 明確的音樂目標

沿用對話中的片長、曲風、情緒、用途、速度與調性。先寫下本曲的聲音方向：鼓的律動、主導音色、低音性格、旋律節奏與段落起伏。從用途和參考聽感選擇，科技／企業影片也能使用不同的電子音樂方向。方向差異會影響成品而使用者尚未指定時，可先提供短片段比較；不要自動把所有需求轉成 120 BPM 的 Melodic House。

選定曲風後，閱讀 [references/genre-production.md](references/genre-production.md) 中對應的製作方向。它整理官方教學及製作人訪談，涵蓋 Melodic House、Deep House、Tech House、Dub Techno、Trance、UK Garage、Drum & Bass、Dubstep 與 Future Bass；將方法轉成實際鼓型、音色調變與編曲，按本案改寫。使用者有參考曲時依 [references/style-and-identity.md](references/style-and-identity.md) 分析它；需要補充其他流派時查找該流派的原始製作教學，保存實際採用的來源。

連續製作多首或使用者指出「都很像」時，閱讀 [references/style-and-identity.md](references/style-and-identity.md)，比較已完成作品的鼓型、音色、低音、樂句與曲式。換曲名、BPM、調性或 seed 不足以建立新身份；依需求實際改寫這些聲部。使用者希望系列一致時可保留共同元素。

指定長度要精確保留，非整小節長度以末段編曲收束，不擅自延長。需要口白空間、無人聲、可循環或不同力度時，讓編曲與輸出符合要求；可循環版本需另做銜接，不套用範本的淡出。

## 作曲、編曲與音色

依聲部角色建立調性、和聲或低音素材與段落時間表；旋律型作品再發展主旋律輪廓。讓有音高的長音與重拍考慮當下和聲；經過音、懸留、延伸音等張力需有意安排及解決。固定旋律不應任意疊在所有和弦上。檢查跨和弦的延音、延遲與混響是否衝突。

讓需要的主旋律、低音、鼓、和弦、琶音與效果各有角色；用疏密、音域、濾波與起伏組成開場、build、drop、break、outro 等段落。依用途調整曲式，不必照範本的固定樂句。旋律型作品讓主題可辨識，副旋律和效果支援它。

先做能成立的核心樂句：鼓與低音的互動，加上本曲需要的 hook 或和弦。依曲風決定 swing、切分、half-time、音符長短與呼應；再用音色包絡、濾波／振幅調變、效果 send 與聲部進出展開完整曲目。變化要能在音訊、MIDI 或可編輯 automation 中找到，不能只寫在風格標籤。低音主導或質地演化的作品可省略前景主旋律，不強塞相同的鋼琴／pluck。

選擇合適的取樣樂器或可控制泛音的合成器，依聲音方向調整泛音、濾波、失諧、包絡與尾音，排除意外刺耳及遮蔽。使用者指出特定秒數、刺耳或拍點模糊時，solo 該段的問題聲部，核對實際音源、音域、力度、泛音／失諧及 primary／echo onset；方法見 [references/continuity-and-articulation.md](references/continuity-and-articulation.md)。為大鼓與低音留出空間，使用節拍錯開、EQ、側鏈或音量 ducking；減少頻段重疊的聲部。詳細方法與不和諧排查見 [references/composition-and-mix.md](references/composition-and-mix.md)。

使用者指出「每拍斷掉、沒有連貫性」時，先閱讀 [references/continuity-and-articulation.md](references/continuity-and-articulation.md)。區分 MIDI gate 與實際 release，檢查共同音是否被逐小節重啟、音量 gate／ducking 是否同時抽空所有聲部，以及樂句是否只有短音而缺少延續。以同段、相近響度的短片段比較修正；依曲風保留刻意的切分與留白，不用加混響代替編曲修正。

## 本機音樂範本

有現成 DAW、專案或音源時優先沿用；沒有管線時可用獨立 Python 範本。開始前閱讀 [references/local-workflow.md](references/local-workflow.md) 與 [references/music-project.md](references/music-project.md)。範本提供 melodic-house、breakbeat、drum-and-bass 三個實際不同的起點；依聲音方向選擇 `--style`。九種製作指引不等於九個可執行 preset；未支援的曲風需實作相應編曲／音色或使用適合的 DAW 管線，保留使用者選擇，不把現有 preset 改名充當另一曲風。

```text
python <skill>/scripts/init_project.py --project <music-directory> --duration 90 --style breakbeat
python <music-directory>/work/compose_edm.py --project <music-directory>
python <music-directory>/work/finish_music.py --project <music-directory>
```

修改 project.json 的片長、曲風、BPM、大小調、和弦級數與段落；preset 是可執行的草稿，不代表本案已完成創作。依本案重寫樂句、律動、音色及段落。範本輸出原創電子合成；含鍵盤聲部的編曲亦支援外部 SoundFont／FluidSynth 鋼琴。可開啟分軌輸出，供重新混音。

## 檢查、來源與交付

有聽音能力時檢查完整曲目，以及和弦轉換、高潮、間奏、片尾、小音量及單聲道聽感。量測與音符檢查不能證明好聽；沒有實際聽音能力時，清楚說明客觀檢查，提供可播放結果，不宣稱已試聽。使用者指出不和諧時，分析和聲、旋律、音色、聲部及尾音，再交付修改版本。保留使用者偏好的疏密與方向；不要因 RMS 更平坦而強制加 Pad 或 legato bass。影片配樂用含畫面的片段比較具體 cue，核對主擊與重要動作。

交付 24-bit WAV 母帶、AAC 或使用者指定格式，及需要的 MIDI／分軌；直接檢查完成版的片長、取樣率、聲道、解碼、響度、真峰值、淡出與意外靜音。母帶目標依用途選擇，範本預設 −16 LUFS、−2 dBTP，並驗證 AAC 編碼後的峰值。

連續性問題另用短時間窗檢查完成版及有音高的聲部；一秒平均 RMS 會漏掉拍間空隙。範本提供 10ms 能量診斷，結果須和樂句、刻意休止一起判讀，不能把「無長靜音、音符符合和弦」當作連貫或悅耳的證明。

分別記錄樂曲、音色庫／取樣、第三方歌曲的來源。真實鋼琴、合成鍵盤與取樣庫如實標示；保存實際使用音色庫的來源、雜湊與授權。若使用現成歌曲，確認使用範圍並標示，不能宣稱是原創。

工作檔放在 work/、成品放在 outputs/。在聊天中提供可直接播放的音訊與成品連結，將實際測量及尚需主觀判斷的事項說清楚。

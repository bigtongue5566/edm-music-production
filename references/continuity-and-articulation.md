# 音符銜接與拍間斷續排查

用於「每一拍像分開貼上」「尾音被切掉」或要求流暢的配樂。刻意的短音、切分、gate 和休止也能構成完整樂句；先辨識問題聲部，不把所有 EDM 改成持續長音。

## 本次失敗的具體原因

公開 Demo 的舊渲染器用 `sound[:gate_samples]` 裁聲音，把 MIDI note-off 當成音訊結束。部分音源的 fade-out 也在 gate 內提前開始；這是短音包絡，不能代替 note-off 後的 release。和弦與 Pad 在小節／和弦邊界重啟，低音也逐音重置振盪器。Future Bass 的和弦 gate 最低僅剩 5% 振幅。短聲部加上共同的 ducking，可能強化聲部一起收掉的感覺；稀疏 UKG／Dub 的休止本身不是錯誤。

原來的一秒 RMS 與音符 pitch-class 檢查仍可能通過：它們檢查平均能量與音高，沒有檢查 articulation、拍間空隙與樂句延續。

## 修正順序

1. 分別保留 `duration`（MIDI gate）與 `sounding_duration`（乾聲實際長度）。音源產生 gate 加 release 的波形；渲染器保留那段 release。`soften` 適合邊緣防爆音，不能把整段 release 提前挪到 note-off 以前。
2. 檢查相鄰和弦的共同音與聲部移動。共同音可合併為長音，避免全和弦一起重觸發包絡。需移動的聲部安排相近的轉位；稠密的低音區與相鄰半音會增加粗糙感，是否保留由和聲意圖決定。
3. 新和弦仍容納的尾音可繼續；不相容的音適當縮短、淡出或改寫。不要為了符號檢查，無條件在每個小節切掉所有尾音；效果回授另作聽感與頻段檢查。
4. 需要 legato 低音時，音符接到下一個 onset，振盪器保持相位，包絡不逐音降到零。需要 pluck／短低音時保留其休止；由樂句判斷是否需要其他聲部或效果承接，不把每個空隙填滿。
5. 先修 gate、包絡和聲部，再減輕會把所有層一起抽空的側鏈。決定哪個聲部讓位給大鼓，哪個聲部保留穩定底層。避免高通過度削掉 Pad 或旋律基音。
6. 最後加入適量、經高通的 room／tempo delay。低音與大鼓保留清楚的乾聲，避免用大量混響掩蓋短音、衝突或沒有發展的樂句。

## 範本中的可重用實作

`instruments.release_shape` 在 note-off 後執行 release。`Score.note` 保留音源長度，以 `continuity.tail_end` 控制跨和弦的乾聲尾音；裁切時另作短淡出。MIDI 不把 release 誤寫成按鍵持續時間。

`continuity.sustained_pad` 對共同音作 tie，保存實際 Pad 轉位；其避免相鄰半音的排列是範本選擇，可依需求替換。`connected_bass` 是可選的 legato／持續相位實作，用於這次需要流暢的 Demo；它不是所有預設的強制低音律動。`room` 提供小音量的濾波反射，不使用第三方錄音。

標準 composer 預設只修正 gate／release 的處理，保留既有聲部密度與混音方向。需要持續和聲時才設定 `music.continuity: {"tie_pad": true, "room_wet": 0.08}`：tie_pad 會替換 Pad 並增加持續底層，room_wet 可獨立選用，範圍 0–0.5。`connected_bass` 需在本案 composer 中明確呼叫；它會改寫 articulation，不能用較平坦的 RMS 作為採用理由。修改後重新產生音符、MIDI、automation 和完成版檢查。

SoundFont 鍵盤保留音源自己的 release，MIDI 不在每個和弦發送 CC120（All Sound Off），不在每個和弦邊界對整條 bus 加淡入淡出。其真實尾音與效果仍需在渲染音訊中檢查；MIDI gate 的符號檢查不涵蓋取樣尾音。

## 刺耳音色與拍點辨識

音符符合和弦不等於音色舒服。使用者指到特定秒數時，先切出該段並分別 solo 鼓、低音、和弦／鍵盤、效果。記錄實際音源與音域；高八度和弦、密集延伸音、失諧的相近泛音、偏亮 attack、filter resonance 和重複回聲，可能造成刺耳或拍點模糊。不要用「鋼琴」稱呼未使用鋼琴取樣的振盪器。

先在原聲部中降低不合適的音域、力度／velocity、失諧或回授，刪減互相遮蔽的音，必要時更換實際音源。先比較 dry tone 和效果版本，再決定 EQ／動態 EQ；固定削掉整段高頻不能替代音色選擇。約 2–5kHz 的頻帶能量與窄峰只能提示檢查位置，不是通用刺耳門檻。取樣鋼琴也需比較較輕力度的 attack，並保存音源來源與授權。

把 primary onset、echo onset 和 intentional swing 分別列到拍格。附點延遲與切分可以完全在拍格上，仍可能讓主拍難辨識；讓主擊有清楚層級，降低／減少回聲，或依用途改寫節奏。只有 BPM 一樣、音符可整除或音高符號通過，不能證明聽感有律動。

作為影片配樂時，用實際畫面的入場／組裝完成／數字定格建立 cue map，核對音訊 onset 與最終影格；只讓章節時間相同或讓圖形隨音量跳動不足以對點。音樂單獨成立也要檢查含畫面的短片段。

## 驗證與聽感

`micro_dynamics` 以 10ms 視窗，記錄活動段落的 p10/p95 能量差及深谷最長時間。深谷門檻是相對 p95 的 −34dB 診斷值，並非所有曲風的及格線。它避免只靠一秒平均值漏掉短空隙；它也不證明音色協調或旋律好聽。

使用者偏好先前版本時，保留那版的疏密與音色方向，針對被指出的問題做可比較的局部修正。客觀能量更平坦不能推翻聽感回饋；未被接受的實驗版本不作為「已改善」的示範。

另看 harmonic bed（keys／chords／Pad／lead 合計）的能量包絡，分別檢查鼓與音高層。用相同起點、相近響度做 A/B，至少涵蓋完整樂句、和弦銜接及段落切換。可實際聽音時檢查完整曲目、低音量與單聲道；無聽音能力時交付可播放比較並說明限制。

回歸測試覆蓋 note-off 後仍有聲音、相容／不相容和聲尾音、跨小節共同音、低音的能量與相位連續，以及一秒 RMS 隱藏的 200ms 空隙。

## 採用的方法來源

2026-10-10 查閱以下原始資料，方法用於原創合成；未複製教學的歌曲或音色錄音。

- [Ableton Live Instrument Reference](https://www.ableton.com/en/manual/live-instrument-reference/)：ADSR 的 sustain、note-off 後 release，及 legato 時的包絡行為。
- [Native Instruments：How to make a deep house track](https://blog.native-instruments.com/how-to-make-a-deep-house-track/)：持續 Pad、legato 低音、節奏化 organ 與附點延遲的分工。本次借用聲部銜接方法，未將四首作品改成 Deep House。

# 獨立音樂製作流程

## 建立

```text
uv run --no-project python <skill>/scripts/init_project.py --project <music-directory> --duration 90 --style breakbeat
uv sync --project <music-directory>/work --python 3.12
```

在其他平台使用 venv/bin/python。initializer 只需要 Python 標準庫，先驗證設定，再複製專案；有同名檔案即拒絕覆寫。--name、--slug、--stems 可設定標題、檔名及分軌。--duration 按比例縮放預設段落，可在 project.json 再修改。

範本音訊依賴只有 NumPy、SciPy、Mido、imageio-ffmpeg。FFmpeg 由 imageio_ffmpeg.get_ffmpeg_exe() 尋找；不依賴影片、字型、Skia 或原本的 motion-graphics-video Skill。套件快取已有依賴時可用 uv offline；無權限寫全域快取時指定 work/uv-cache。

## 作曲與混音

用 `uv run --no-project python <skill>/scripts/init_project.py --help` 查看九個可執行草稿；完整差異見 [electronic-styles.md](electronic-styles.md)。省略 style 保留舊版 melodic-house 相容路徑，新案先選風格。未列入 CLI 的風格使用 DAW 或實作相應語法，不改 preset 名稱冒充支援。

```text
uv run --project <music-directory>/work python <music-directory>/work/compose_music.py --project <music-directory>
uv run --project <music-directory>/work python <music-directory>/work/finish_music.py --project <music-directory>
```

`compose_edm.py` 是相容入口，舊案不用改名。新案的 pyproject.toml 位於 work/，由 uv sync 管理依賴；不要直接使用系統 Python 或手動 pip 安裝。

compose 依共同段落時間表寫音符與合成聲部、做頻段整理與大鼓 ducking，產生工作混音、MIDI、音符紀錄與來源 metadata。音符檢查只驗證這個簡單三和弦範本；不把所有和弦外音一律當作不和諧。

渲染器分別保留 MIDI gate 與 sounding release，跨和弦尾音按相容性處理；Pad 連接與 room 是選用的編曲變更：設定 `music.continuity` 的 `tie_pad`、`room_wet` 才啟用，預設保留聲部密度。`continuity.py` 提供這些實作及可選 legato bass、低量 room 與 10ms 診斷。使用方法與邊界見 [continuity-and-articulation.md](continuity-and-articulation.md)。

finish 用雙階段響度處理輸出 48kHz／24-bit 立體聲 WAV 與 256kbps AAC，再解碼實際成品檢查。WAV 母帶有精確樣本數；AAC 的解碼長度可能有不足一個 codec frame 的尾端補樣本，檢查會容許 1024 / 48000 秒的差異並記錄。

完成版 QC 另外記錄 `micro_dynamics`；它提示拍間深谷，需依段落的休止意圖判讀，不用固定門檻取代實際試聽。

## 可選自然鋼琴

下載相容音色庫後，設定 music.soundfont、music.fluidsynth、soundfont_source、license。套件沒有隱藏下載，也不包含取樣音源。作者現行授權與播放器相容性需依實際來源確認；GeneralUser GS 搭配 FluidSynth 是本案已驗證的選擇。SoundFont 必須下載完整，RIFF 宣告長度與檔案相同。

沒有指定 SoundFont 時使用合成鍵盤，如實寫入來源紀錄；不把簡單合成稱為真實鋼琴。

## 交付與重新混音

outputs/ 包含 <slug>-master.wav、<slug>.m4a、<slug>-music.mid、<slug>-qc.json、<slug>-provenance.json、<slug>-production.md；開啟 export_stems 時另有 stems/，八個立體聲分軌時間對齊。

work/ 包含浮點混音、音符與和弦資訊、響度紀錄、選用的取樣鍵盤中間檔。來源套件可以附設定與腳本；若包含外部音色庫，附它的授權。不打包虛擬環境、快取、秘密資料或個人絕對路徑。

修改 project.json 或樂句後重新 compose、finish；檢查新的完成版，不能沿用先前的測量作為本次成功證據。


Ambient 預設 `pulse: free`，`harmony_seconds: 12`，沒有鼓、四拍 ducking 或必需的 build／drop。`bpm: 60` 是 MIDI 參考，不是聲景聽感的固定拍。大／小調三和弦仍是此草稿的限制。需要無調性、複拍號、tempo map 或 granular 時使用對應管線。`intentional_silence: [[start,end], ...]` 標記預期休止，只調整近靜音檢查，不自動修改聲音。

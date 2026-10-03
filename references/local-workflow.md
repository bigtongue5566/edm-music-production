# 獨立音樂製作流程

## 建立

```text
python <skill>/scripts/init_project.py --project <music-directory> --duration 90 --bpm 120 --key "G major"
uv venv <music-directory>/work/.venv --python 3.12
uv pip install --python <music-directory>/work/.venv/Scripts/python.exe -r <music-directory>/work/requirements.txt
```

在其他平台使用 venv/bin/python。initializer 只需要 Python 標準庫，先驗證設定，再複製專案；有同名檔案即拒絕覆寫。--name、--slug、--stems 可設定標題、檔名及分軌。--duration 按比例縮放預設段落，可在 project.json 再修改。

範本音訊依賴只有 NumPy、SciPy、Mido、imageio-ffmpeg。FFmpeg 由 imageio_ffmpeg.get_ffmpeg_exe() 尋找；不依賴影片、字型、Skia 或原本的 motion-graphics-video Skill。套件快取已有依賴時可用 uv offline；無權限寫全域快取時指定 work/uv-cache。

## 作曲與混音

```text
python work/compose_edm.py --project .
python work/finish_music.py --project .
```

compose 依共同段落時間表寫音符與合成聲部、做頻段整理與大鼓 ducking，產生工作混音、MIDI、音符紀錄與來源 metadata。音符檢查只驗證這個簡單三和弦範本；不把所有和弦外音一律當作不和諧。

finish 用雙階段響度處理輸出 48kHz／24-bit 立體聲 WAV 與 256kbps AAC，再解碼實際成品檢查。WAV 母帶有精確樣本數；AAC 的解碼長度可能有不足一個 codec frame 的尾端補樣本，檢查會容許 1024 / 48000 秒的差異並記錄。

## 可選自然鋼琴

下載相容音色庫後，設定 music.soundfont、music.fluidsynth、soundfont_source、license。套件沒有隱藏下載，也不包含取樣音源。作者現行授權與播放器相容性需依實際來源確認；GeneralUser GS 搭配 FluidSynth 是本案已驗證的選擇。SoundFont 必須下載完整，RIFF 宣告長度與檔案相同。

沒有指定 SoundFont 時使用合成鍵盤，如實寫入來源紀錄；不把簡單合成稱為真實鋼琴。

## 交付與重新混音

outputs/ 包含 <slug>-master.wav、<slug>.m4a、<slug>-music.mid、<slug>-qc.json、<slug>-provenance.json、<slug>-production.md；開啟 export_stems 時另有 stems/，八個立體聲分軌時間對齊。

work/ 包含浮點混音、音符與和弦資訊、響度紀錄、選用的取樣鍵盤中間檔。來源套件可以附設定與腳本；若包含外部音色庫，附它的授權。不打包虛擬環境、快取、秘密資料或個人絕對路徑。

修改 project.json 或樂句後重新 compose、finish；檢查新的完成版，不能沿用先前的測量作為本次成功證據。

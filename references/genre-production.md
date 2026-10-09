# 不同電子舞曲的製作方法

依已選曲風讀對應段落，再實作本案的鼓、低音、音色與曲式。這是對官方教學文字及製作人訪談的整理，查閱日期為 **2026-10-10**；「本案實作」是本 Skill 依那些方法提出的製作建議，不是製作人的原話，也不是所有子流派的定義。

教學中的 BPM、調性、音量及效果數值屬於該示範。先依參考曲、用途和實際樂器選擇，再調整參數；不把某個數值、特定品牌音源或固定和弦當作曲風的必要條件。可用現有 DAW 的合成器、濾波、延遲、調變及合法音源實作。

## 選擇製作方向

| 方向 | 優先建立的聲音特徵 | 詳細指引 |
| --- | --- | --- |
| Melodic House | 四拍脈動、主題樂句、lead／bass 的動態演化 | [旋律與自動化](#melodic-house) |
| Deep House | 有 swing 的四拍、organ／pad、低音與和弦的呼應 | [律動與空間](#deep-house) |
| Tech House | 鼓與低音主導、精簡 hook、推進的節奏 | [精簡聲部](#tech-house) |
| Dub Techno | 和弦 stab、濾波、多重調變、處理過的 echo | [質地演化](#dub-techno) |
| Trance | 四拍、短反拍低音、分層 synth riff、期待與釋放 | [riff 與曲式](#trance) |
| UK Garage／2-step | 切分 kick、shuffle hat、與低音交錯的短句 | [切分與 swing](#uk-garage) |
| Drum & Bass | 快速破拍、鼓層次、獨立 sub 與中頻低音 | [鼓與低音分工](#drum-and-bass) |
| Dubstep | half-time 重心、低音問答、留白與音色動態 | [低音設計](#dubstep) |
| Future Bass | half-time／trap 律動、延伸和弦、節奏化振幅調變 | [和弦與調變](#future-bass) |

上表的九個方向是製作指引。本機 initializer 仍只有 `melodic-house`、`breakbeat`、`drum-and-bass` 三個合成草稿；其他方向要選擇現有 DAW 或改寫引擎，再交付實際音訊。Breakbeat 是現有破拍草稿，不能直接等同 UK Garage；DnB 草稿也不代表所有 liquid、jungle 或 neurofunk 的聲音。

<a id="melodic-house"></a>
## Melodic House

**方法來源：** [Ableton／LNA：Make a Melodic House Track](https://www.ableton.com/en/blog/make-a-melodic-house-track-in-10-minutes-on-ableton-move/)，2024-12-12。官方教學介紹從簡單鼓組出發，錄製 lead、bass 的即時 automation，使聲部動態變化。

**本案實作：** 寫一個可呼應的原創主題，再讓音色的明暗、尾音和效果量隨樂句變化。展開段落時選擇揭露哪些聲部；保留主題，避免每次只是相同 pluck 換調。

**檢查：** lead／bass 的變化能在 automation 或音訊中找到，和弦切換時長尾仍合理；高潮與間奏有聲部或音色的對比。

<a id="deep-house"></a>
## Deep House

**方法來源：** [Native Instruments／Tim Cant：How to make a deep house track](https://blog.native-instruments.com/how-to-make-a-deep-house-track/)，2023-01-24。示範 swung shakers、柔和 pad、legato 低音、節奏化 organ 與附點延遲；以濾波讓前景聲部保有位置。

**本案實作：** 先讓 kick、hat／shaker 和低音構成完整 groove，再用 organ 或和弦短句回答它。依和弦排列決定低音，不自動複製四個反拍根音；用較少的前景聲部保留空間。

**檢查：** 靜音 lead 後 groove 仍成立；swing 來自可辨識的時值關係，延遲不淹沒下一句。

<a id="tech-house"></a>
## Tech House

**方法來源：** [Native Instruments／Tim Cant：How to produce a tech house track](https://blog.native-instruments.com/tech-house/)，2024-10-03。先建立 house beat、簡潔 lead 與推進的低音，再發展氣氛、和聲與 intro／breakdown／drop。

**本案實作：** 以鼓和短而有節奏的低音作前景，hook 保持精簡；用 percussion 變化、靜音和回歸推動段落。DJ 版可保留接歌空間，短片 BGM 則按片長安排進入點。

**檢查：** 低音的節奏和聲部進出產生推進感；沒有為了「豐富」把 pad、arp 和主旋律全部常駐。

<a id="dub-techno"></a>
## Dub Techno

**方法來源：** [Ableton／El Choop，Joseph Joyce 訪談：Designing Dub Chords](https://www.ableton.com/en/blog/designing-dub-chords-in-ableton-live-with-el-chooppizza-hotline/)，2024-03-26。El Choop 以和弦取樣或合成、濾波、不同周期的調變，以及經處理的 reverb／delay sends 建立變化；echo 的質地與乾聲分開。

**本案實作：** 可先錄下自己的和弦 stab，再重觸發並調變濾波、send、延遲回授。選擇互相作用的調變周期，讓重複片段的質地逐步演化。這是 Dub Techno 路線，不把所有 Techno 都定義成 rumble kick 或同一種 chord。

**檢查：** 重複樂句之間有可辨識的調變；效果回授不失控，低頻與單聲道仍清楚。

<a id="trance"></a>
## Trance

**方法來源：** [Native Instruments／Arthur Kody：How to make an uplifting trance track](https://blog.native-instruments.com/trance-music/)，2023-03-30。採先寫 riff 再編曲的流程；四拍 kick 配帶留白的短反拍低音，以不同明暗、寬窄、乾濕的 synth 層和 Modwheel automation 展開。

**本案實作：** 先做能循環並發展的原創 riff，再安排和聲、低音、build 與釋放；不同層各負責起音、持續或空間。固定秒數的配樂可縮短曲式，保留期待與釋放的關係。

**檢查：** 回歸主題時有實際的層次或音色展開；多層不是同頻段、同包絡的重複疊加。

<a id="uk-garage"></a>
## UK Garage／2-step

**方法來源：** [Native Instruments／Tim Cant：How to make UK garage](https://blog.native-instruments.com/uk-garage-music/)，2023-08-28。示範 2-step 的 kick／snare、刻意延後的 hat 與 shuffle，之後加入低音、短 synth 和 vocal 元素；UKG 也包含四拍路線。

**本案實作：** 先選 2-step 或四拍語法，將 hat／細 percussion 的時值與力度和主拍分開調整。低音和短句填入 drum groove 的空隙。無人聲案用原創 synth／organ 短句呼應，不為曲風擅自加入 vocal。

**檢查：** kick、snare、hat 與低音的交錯能在事件時值中找到；swing 不靠全聲部隨機抖動。

<a id="drum-and-bass"></a>
## Drum & Bass

**方法來源：** [Native Instruments／Tim Cant：How to produce a drum and bass track](https://blog.native-instruments.com/drum-and-bass/)，2023-08-23。示範 break 與 one-shot 鼓的互補，並把中頻低音與 sine sub 分工，透過 fills、效果與編曲展開。

**本案實作：** 選本案的鼓語法與低音角色，再調速度。用自己編寫的鼓或已取得授權的 break；讓 ghost notes／fills 支援主 snare。可把移動的中頻層和穩定 sub 分開設計，避免低頻重複堆疊。

**檢查：** 低音和快速鼓型都清楚；有樂句層級的鼓變化，並驗證 sub 和中頻層的單聲道關係。

Reese 音色可參考 [Tim Cant：How to create the signature Reese bass sound](https://blog.native-instruments.com/reese-bass/)，2025-04-25：從失諧 saw 的拍頻、低通與 mono voice 起步，再用失真及 notch 濾波演化。失諧量決定移動速度；這個音色跨多種流派使用，不是 DnB 的唯一選擇。

<a id="dubstep"></a>
## Dubstep

**方法來源：** [Native Instruments／Tim Cant：How to make a dubstep track](https://blog.native-instruments.com/how-to-make-dubstep/)，2023-02-17。這篇採 classic 路線：half-time 重心、sub、氣氛與受調變的中頻低音；用 phase modulation 及 LFO 濾波設計低音動態。

**本案實作：** 先決定偏空間／sub 或偏激烈音色的路線，再寫帶停頓的低音問答。保留清楚的重拍；音色調變與回應句的節奏一起設計，不把四拍 House 單純加失真稱作 Dubstep。

**檢查：** 低音句與停頓構成可辨識的呼應；濾波、FM／phase modulation 的變化沒有掩蓋鼓或需要保留的口白。

[Modestep 訪談](https://blog.native-instruments.com/modestep/)，2025-07-21，提供另一個工作方法：先在獨立 sound-design session 建立個人 patch 與 macros；編曲時選擇強烈音色各自出現的時機，再處理同時出現聲部的頻段／mid-side 分工。本案可沿用既有音色庫，但仍要為本曲編寫樂句與 automation。

<a id="future-bass"></a>
## Future Bass

**方法來源：** [Native Instruments／Tim Cant：How to make future bass](https://blog.native-instruments.com/how-to-make-future-bass/)，2022-12-16。示範 half-time／trap 鼓、hat rolls、延伸和弦、節奏化振幅調變、和弦分層與呼應旋律；整理各層的效果避免混濁。

**本案實作：** 先選有聲部連接的和弦排列，再共同設計鼓、和弦起音與 gate／振幅節奏。低音負責需要的根音，和弦層可重新配音以留空間；亮度、寬度、持續層各有用途，不用堆音量代替層次。

**檢查：** 改編為七／九等延伸和弦時，同步修改和聲表示及音符檢查；舊版三和弦 audit 不能判定所有延伸音。保留可編輯的調變與真正的和弦層次。

## 跨曲風的製作人方法

[Karizma 訪談，Brian Mitchell／Native Instruments](https://blog.native-instruments.com/how-karizma-found-his-swing/)，2018-01-08：他依低音的 sub 角色決定 kick 的音色位置，分組整理聲部，也保留草稿供之後重聽。本案先一起處理 kick 和 bass；找靈感後重寫自己的音符和音色，保留有用的草稿。

[Ableton Live 12 手冊：Using Grooves](https://www.ableton.com/en/manual/using-grooves/) 說明 timing、velocity 與 random 是不同控制，也能對單一聲部處理 groove。本案在適合的 hat／shaker／snare 上調整時值與重音；維持需要的主拍與低音關係。若以程式輸出，將偏移寫入 MIDI 事件，而非只在報告中聲稱有 swing。

記錄實際採用的教學來源與本案修改，並分開記錄真正使用的錄音／音源及其授權。教學可供研究，不代表其中的歌曲、示範音檔或專案素材已取得再利用授權。

# emotext: Emotions in Chinese Texts

中文文本情感分析

使用大连理工大学情感本体库：

- 徐琳宏,林鸿飞,潘宇,等.情感词汇本体的构造[J]. 情报学报, 2008, 27(2): 180-185.
- 词典来源： http://ir.dlut.edu.cn/info/1013/1142.htm
- `[emotext/dict.csv]` 由上述词典转换成的 csv 格式。如使用本资源，请按照原作者要求，请引用上述论文。

参考实现：

- https://github.com/hiDaDeng/cnsenti

## Getting Started

Poetry (recommended):

```sh
git clone <this-repo>

pyenv local 3.10.10
poetry install
poetry run python emotext/httpapi.py --port 9003
```

or, install dependencies by PIP (no one tested yet):

```
pip install --requirement requirements.txt
```

## Usage

请求：

```sh
curl -X POST -d '我今天很开心' http://localhost:9003
```

响应：

```json
{
   "emotions" : {
      "NN" : 12.19853498427,
      "PA" : 20.33089164045
   },
   "polarity" : {
      "negative" : 4.06617832809,
      "positive" : 4.06617832809
   },
   "va" : {
      "arousal" : 0.65125,
      "valence" : 0.59875
   }
}
```

## Details for dev

### DLUT 中文情感词典

大连理工情感词典（以下简称 DLUT）把情感分成了 7 大类，21 小类（忽略英文描述那一栏，那个系之前瞎写的。）。


|             |                                   | DLUT |     | Emotic |
|-----------|-----------------------------------------------|-----------|----|-----------|
| 编号    | 情感大类   | 情感类             | 例词              | emotion categories with definitions |
| 1      | 乐         | 快乐(PA) | 喜悦、欢喜、笑眯眯、欢天喜地  | **17. Happiness**: feeling delighted; feeling enjoyment or amusement<br />**20. Pleasure**: feeling of delight in the senses |
| 2      |            | 安心(PE) | 踏实、宽心、定心丸、问心无愧  | **6. Confidence**: feeling of being certain; conviction that an outcome will be favorable; encouraged; proud<br />**19. Peace**: well being and relaxed; no worry; having positive thoughts or sensations; satisfied |
| 3      | 好         | 尊敬(PD) | 恭敬、敬爱、毕恭毕敬、肃然起敬 | **13. Esteem**: feelings of favourable opinion or judgement; respect; admiration; gratefulness |
| 4       |           | 赞扬(PH) | 英俊、优秀、通情达理、实事求是 | **14. Excitement**: feeling enthusiasm; stimulated; energetic |
| 5       |           | 相信(PG) | 信任、信赖、可靠、毋庸置疑   | **4. Anticipation**: state of looking forward; hoping on or getting prepared for possible future events<br />**12. Engagement**: paying attention to something; absorbed into something; curious; intereste |
| 6       |           | 喜爱(PB) | 倾慕、宝贝、一见钟情、爱不释手 | **1. Affection**: fond feelings; love; tenderness |
| 7       |           | 祝愿(PK) | 渴望、保佑、福寿绵长、万寿无疆 | **4. Anticipation**: state of looking forward; hoping on or getting prepared for possible future events |
| 8      | 怒        | 愤怒(NA) | 气愤、恼火、大发雷霆、七窍生烟 | **2. Anger**: intense displeasure or rage; furious; resentful |
| 9      | 哀        | 悲伤(NB) | 忧伤、悲苦、心如刀割、悲痛欲绝 | **21. Sadness**: feeling unhappy, sorrow, disappointed, or discouraged<br />**23. Suffering**: psychological or emotional pain; distressed; an- guished<br />**22. Sensitivity**: feeling of being physically or emotionally wounded; feeling delicate or vulnerable |
| 10      |           | 失望(NJ) | 憾事、绝望、灰心丧气、心灰意冷 | **5. Aversion**: feeling disgust, dislike, repulsion; feeling hate<br />**21. Sadness**: feeling unhappy, sorrow, disappointed, or discouraged |
| 11      |           | 疚(NH)  | 内疚、忏悔、过意不去、问心有愧 | **25. Sympathy**: state of sharing others emotions, goals or troubles; supportive; compassionate |
| 12      |           | 思(PF)  | 思念、相思、牵肠挂肚、朝思暮想 | **15. Fatigue**: weariness; tiredness; sleepy                |
| 13     | 惧        | 慌(NI)  | 慌张、心慌、不知所措、手忙脚乱 | **18. Pain**: physical suffering<br />**3. Annoyance**: bothered by something or someone; irritated; impa- tient; frustrated |
| 14      |           | 恐惧(NC)  | 胆怯、害怕、担惊受怕、胆颤心惊 | **16. Fear**: feeling suspicious or afraid of danger, threat, evil or pain; horror |
| 15      |           | 羞(NG)    | 害羞、害臊、面红耳赤、无地自容 | **11. Embarrassment**: feeling ashamed or guilty |
| 16     | 恶        | 烦闷(NE)   | 憋闷、烦躁、心烦意乱、自寻烦恼 | **9. Disquietment**: nervous; worried; upset; anxious; tense; pres- sured; alarmed<br />**8. Disconnection**: feeling not interested in the main event of the surrounding; indifferent; bored; distracted |
| 17     |            | 憎恶(ND)  | 反感、可耻、恨之入骨、深恶痛绝 | **5. Aversion**: feeling disgust, dislike, repulsion; feeling hate<br />**7. Disapproval**: feeling that something is wrong or reprehensible; contempt; hostile |
| 18     |            | 贬责(NN)  | 呆板、虚荣、杂乱无章、心狠手辣 | **3. Annoyance**: bothered by something or someone; irritated; impa- tient; frustrated<br /> |
| 19     |            | 妒忌(NK)  | 眼红、吃醋、醋坛子、嫉贤妒能  | **26. Yearning**: strong desire to have something; jealous; envious; lust |
| 20      |           | 怀疑(NL)  | 多心、生疑、将信将疑、疑神疑鬼 | **10. Doubt/Confusion**: difficulty to understand or decide; thinking about different options |
| 21     | 惊        | 惊奇(PC)  | 奇怪、奇迹、大吃一惊、瞠目结舌 | **24. Surprise**: sudden discovery of something unexpected |

### 工作原理

在 `emotext` 中，实现了利用大连理工大学情感本体库进行中文文本情感分析。

从 DLUT 的网站下载到情感词典：http://ir.dlut.edu.cn/info/1013/1142.htm

它给的是 Excel 表格，为了方便，我们将其重新导出为 CSV 格式，得到的文件形如：

```csv
词语,词性种类,词义数,词义序号,情感分类,强度,极性,辅助情感分类,强度,极性
脏乱,adj,1,1,NN,7,2,,,
糟报,adj,1,1,NN,5,2,,,
战祸,noun,1,1,ND,5,2,NC,5,2
招灾,adj,1,1,NN,5,2,,,
```

接下来，要把这个大表读到程序里。我们把「词语 + 情感」视为一个 Word 对象，如果一个词有「辅助情感分类」则把它看成两个 Word：

```python
class Word:
    word: str
    emotion: str
    intensity: int  # 情感强度: 分为 1, 3, 5, 7, 9 五档，9 表示强度最大，1 为强度最小。
    polarity: Polarity
```

再写一个 Emotions 类来放所有的这些 Word 即对应情感。用一个 `self.words` dict，把每种情感的 Word 分开放。

```python
class Emotions:
    def __init__(self):
        self.words = {emo: [] for emo in emotions}  # {"emotion": [words...]}
        with open('/path/to/dict.csv') as f:
            self._read_dict(f)
```

现在给定一个词汇，只需在表中查找，若存在，就到的了情感与对应强度（Word 对象）；若不存在，就认为这个词没有感情，直接忽略。

```python
def _find_word(self, w: str) -> List[Word]:
    result = []
    for emotion, words_of_emotion in self.words.items():
        ws = list(map(lambda x: x.word, words_of_emotion))
        if w in ws:
            result.append(words_of_emotion[ws.index(w)])
    return result
```

而给定一个句子，则先进行分词，取出句子中的前 20 个关键词，做前面的查表分析，将所有得到的关键词情感累加，就得到了句子的情感：

```python
def emotion_count(self, text) -> Emotions:
    emotions = empty_emotions()

    keywords = jieba.analyse.extract_tags(text, withWeight=True)

    for word, weight in keywords:
        for w in self._find_word(word):
            emotions[w.emotion] += w.intensity * weight

    return emotions
```

如果你不喜欢看文字叙述，也不爱阅读代码，那么可以数学一下。这里我们使用 TF-IDF 算法抽取关键词：

- TF（term frequency, 词频）：字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降：${\displaystyle \mathrm {tf} (t,d)={\frac {f_{t,d}}{\sum _{t'\in d}{f_{t',d}}}}}$
- IDF（inverse document frequency, 逆向文件频率）：由总文件数目除以包含该词语之文件的数目，再将得到的商取对数：$ \mathrm{idf}(t, D) = \log \frac{N}{|\{d \in D: t \in d\}|}$，这里 $D$ 使用默认的常见词典。
- TF-IDF 权重就是把两个乘起来，达到过滤掉常见的词语，保留重要的词语的目的：${\displaystyle \mathrm {tfidf} (t,d,D)=\mathrm {tf} (t,d)\cdot \mathrm {idf} (t,D)}$
- 将词语按照得到的 tfidf 权重从大到小排序，取前 20 个作为关键词。
- 我们认为关键词最终的情感 $E_t$ 为由该词语的情感强度 $I_t$ （查字典得到）以及它的 TF-IDF 权共同决定：$\mathrm{E}_t=I_t \cdot \mathrm {tfidf} (t,d,D)$
- 那么文本 $d$ 最终的总情感为所有关键词情感的叠加：

$$
E(d)=\sum_{t \in \mathrm{key}(d, D)}I_t\cdot \mathrm {tfidf} (t,d,D)
$$

这里我们并没有分析句子的连续特征，只是简单的用关键词分析，但对于分析常见的，不是藏的非常深的句子已经可以用了。

```python
>>> t = '后悔也都没有用 还不如一切没有发生过 不过就是又少一个诗人 换一个人沉迷你的笑'
>>> r = Emotext.emotion_count(t)
>>> r.emotions = softmax(r.emotions)
>>> e = Emotion(**r.emotions)
Emotion(PA=0.0, PE=0.0, PD=0.0, PH=0.0, PG=0.2428551306285703, PB=0.0, PK=0.0, NA=0.0, NB=0.0, NJ=0.41260819965515805, NH=0.175202571704109, PF=0.0, NI=0.0, NC=0.0, NG=0.0, NE=0.1693340980121628, ND=0.0, NN=0.0, NK=0.0, NL=0.0, PC=0.0)
```

这里我们获取到了 NJ、PG、NH、NE 的情感，即：失望，相信，内疚，和烦闷。差不多，至于文字下埋藏的也许是喜爱的情感？我们目前这种方式并不能让计算机理解，这是个缺陷。



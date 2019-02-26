# Viterbi Algorithm
Implement my Viterbi Algorithm with Python3.

## Description of Viterbi Algorithm (小筆記)
- 維特比演算法（英語：Viterbi algorithm）是一種動態規劃演算法
- 例如在統計句法分析中DP算法可以被用於發現最可能的上下文無關的衍生（解析）的字串，有時被稱為「維特比分析」。


#### HMM vs. Viterbi Algorithm
與HMM(Hidden Markov Model)相比，HMM是暴力列舉法，而Viterbi是比較Greedy(?)

- HMM: 超級沒效率，但較精準

每個 state 都會因為前面有 N 種不同的 states , 而增加 N 種不同的序列, 這樣一直增加, 序列的數量呈指數函數成長, 最後再一起比誰的機率比較大。


- Viterbi: 比較有效率，精準度雖不高，但CP值高

用 Dynamic Programming 的概念, 在計算每個 state 的機率時, 就直接比較序列的機率大小, 只保留機率最大的一條序列。


## Examples
如圖，假設在理想狀態下，醫生幫病人診斷，透過病人序列性的狀態下，醫生可以利用Viterbi Algorithm診斷病人最終狀態。
其中，醫生診斷病人只有2種結果(states)，醫生從病人口中可以得知其徵狀(observations)，其他變數如下：

![example_of_hmm](https://upload.wikimedia.org/wikipedia/commons/0/0c/An_example_of_HMM.png)

Figure 1. Graphical representation of the given HMM by Wikipedia

透過輸入病人每天的徵狀(Observation)，得出最後結果(state)。

#### 參數設定
```
states = ('health', 'fever')
start_probabilities = {'health': 0.6, 'fever': 0.4}
transition_probabilities = {
                    'health' : {'health': 0.7, 'fever': 0.3},
                    'fever' : {'health': 0.4, 'fever': 0.6}
                    }
emission_probabilities = {
                    'health' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
                    'fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
                    }
```

#### 建立一個Viterbi模型 (a doctor)
```
myViterbi = Viterbi(states, start_probabilities,
                    transition_probabilities, emission_probabilities)
```

#### 開始看診
```
obs_1 = ('normal', 'cold', 'dizzy')   # features that
dignosis = myViterbi.run(obs_1)
```

#### 列印診斷報告
```
print_report(patient_no, observations, process_results)
```


## References
- [維特比演算法 by Wikipedia](https://zh.wikipedia.org/wiki/%E7%BB%B4%E7%89%B9%E6%AF%94%E7%AE%97%E6%B3%95)
- [自然語言處理 -- Viterbi Algorithm By Mark Chang](http://cpmarkchang.logdown.com/posts/192522-natural-language-processing-viterbi-algorithm)

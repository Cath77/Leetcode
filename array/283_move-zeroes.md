# 283. 移动零
[Leetcode](https://leetcode.cn/problems/move-zeroes/)

## 题目


提示:  
* 

解法:  
* 


## C++
```

```

## Python
```

```


We modified the prompt again and have a functional parameter set now. It's `temperature = 0.6, frequency_penalty = 10.0, and presence_penalty = 1.0`. The BLEU scores are reduced to `5.2813154577367` for entailment and `3.3839253585342903` for contradiction.
The scores: https://app.box.com/file/1262241808578?s=d77jhteymea57a2x0302i2qzme6tp1bv
The outputs: https://app.box.com/folder/219522681159?s=27qua8bubiytio8qxmh6h3hp0vxvuqde

A few problems remains:
1. Patterns
Only two patterns are seen for contradiction: 'In contrast to the claim that {rephrase of the original claim}' and 'The claim that {rephrase of the original claim} {phrases showing negative sentiment}.' As for entailment, no patterns have occurred so far.
2. Incomplete sentences
One problem is that ChatGPT tends to generate responses that are too long, resulting in responses that contain too much useless information. In order to control the length of the responses, we first add a constraint in the prompt, asking Chatgpt to generate the answer of no more than 50 words, and this constraint seems to be ignored by ChatGPT.
Then we use the parameter `max_token` of API, set it to 100, so that ideally the generated response would contain at most 100 tokens. However, this works very differently than we thought it would. It seems like ChatGPT still first tries to generate a long response, then stop at the 100th tokens. This leaves us with many incomplete responses.

We've tried many ways to address these problems, but unfortunately minor improvements have been achieved so far. Therefore, I would like to ask if it's allowed to conduct manual postprocessing. Since the current responses usually contain several sentences, and since the patterns are usually the prefix of the first sentence and the incomplete sentences occurs only at the end of the response, we can simply manually remove those unwanted parts. This should still give us responses with enough details.

We'd appreciate any feedback from you. And we'll keep finding better parameter sets before Aniket send us the candidate sentences.



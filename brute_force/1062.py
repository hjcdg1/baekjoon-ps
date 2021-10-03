from sys import stdin


def alphabet_to_idx(alphabet):
	return ord(alphabet) - ord('a')

def dfs(start_idx, learn_cnt):
	# K개 단어 학습 완료
	if learn_cnt == K:
		word_cnt = 0
		for word in words:
			is_readable = True
			for alphabet in word:
				if not is_learnerd[alphabet_to_idx(alphabet)]:
					is_readable = False
					break
			if is_readable:
				word_cnt += 1
		return word_cnt

	# (K - learn_cnt)개 단어 학습 필요
	max_word_cnt = 0
	for idx in range(start_idx, required_alphabets_len - (K - learn_cnt) + 1):
		is_learnerd[alphabet_to_idx(required_alphabets[idx])] = True
		max_word_cnt = max(max_word_cnt, dfs(idx + 1, learn_cnt + 1))
		is_learnerd[alphabet_to_idx(required_alphabets[idx])] = False
	return max_word_cnt

N, K = list(map(int, stdin.readline().split()))
words = [stdin.readline().rstrip() for _ in range(N)]

if K < 5:
	print(0)

else:
	# 각 알파벳의 학습 여부
	is_learnerd = [False for _ in range(26)]

	# 'a', 'n', 't', 'i', 'c' 학습
	for alphabet in ['a', 'n', 't', 'i', 'c']:
		is_learnerd[alphabet_to_idx(alphabet)] = True
	K -= 5
	words = [word[4:-4] for word in words]

	# 추가로 학습해야하는 모든 알파벳 수집
	required_alphabets = set()
	for word in words:
		required_alphabets |= set(word)
	required_alphabets = list(required_alphabets - {'a', 'n', 't', 'i', 'c'})
	required_alphabets_len = len(required_alphabets)
	K = min(K, required_alphabets_len)  # K가 학습 필요 알파벳 개수보다 큰 경우 처리

	# DFS
	print(dfs(0, 0))

"""
<Another Solution>

from sys import stdin
from itertools import combinations
from copy import copy


N, K = list(map(int, stdin.readline().split()))
words = [stdin.readline().rstrip() for _ in range(N)]

if K < 5:
	print(0)

else:
	ALPHABETS = {
		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
	}
	ALPHABETS_FIXED = {'a', 'n', 't', 'i', 'c'}
	K -= 5

	words_cnt = [0 for _ in range(N)]
	alphabet_to_words = {
		alphabet: [] for alphabet in ALPHABETS - ALPHABETS_FIXED
	}

	alphabets_required_total = set()
	for idx, word in enumerate(words):	
		alphabets_required = set(word[4:-4]) - ALPHABETS_FIXED
		if len(alphabets_required) > K:
			words_cnt[idx] = float('inf')
			continue

		words_cnt[idx] = len(alphabets_required)
		for alphabet in alphabets_required:
			alphabet_to_words[alphabet].append(idx)
		alphabets_required_total |= alphabets_required
	K = min(K, len(alphabets_required_total))

	answer = 0
	for combination in combinations(alphabets_required_total, K):
		words_cnt_copy = copy(words_cnt)
		for alphabet in combination:
			for word_idx in alphabet_to_words[alphabet]:
				words_cnt_copy[word_idx] -= 1
		cnt = len(list(filter(lambda word_cnt: word_cnt == 0, words_cnt_copy)))
		answer = max(answer, cnt)

	print(answer)
"""

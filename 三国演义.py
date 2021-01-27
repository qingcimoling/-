import jieba
# 打开并读取“三国演义.txt”
txt = open(r"C:\Users\墨翎\Desktop\上机课3\三国演义.TXT", "rb").read()
# 构建排除词库
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此",
              "如何", "商议","主公", "军士", "左右", "军马", "次日",
              "大喜", "天下", "于是", "今日", "一人", "人马", "汉中",
              "大军", "上马", "大叫", "太守", "何不", "夫人", "背后",
              "城中", "天子", "一面", "引兵"}
# 使用jieba分词
words = jieba.lcut(txt)
# 对划分的单词计数
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "刘皇叔" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
# 删除无意义的词语
for word in excludes:
    del counts[word]
# 按词语出现的次数排序
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
# 采用固定的格式进行输出
for i in range(9):
    word, count = items[i]
    print("{0:<5}{1:>5}次".format(word, count))
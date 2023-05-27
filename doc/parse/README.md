# 解析类教程 | Parsing class tutorials
**在Natural中，有一个专门解析xml以及json的类，这个类的名字是`parse`,如果您想使用它，应该通过该语句`import NaturalAPI.parse`来引用它或者通过如下语句引用它：**
> **In Natural, there is a class dedicated to parsing xml and json, the name of this class is `parse`, if you want to use it, you should refer to it by the statement `import NaturalAPI.parse` or by the following statement:**
```
from Natrual import parse
```

# 使用它 | Use it
> 假设我们有一个这样的文件结构： | Suppose we have a file structure like this:
```
|_ exp
  |_config
    |_ main.json
  |_main.py
```
> 假设main.json里有如下内容： | Suppose main.json has the following:
```json
{
  "ver":"0.0.2",
  "author":["Buelie","WindAF"]
}
```
> 接着，我们在main.py文件内输入如下内容：
```python
import NaturalAPI.parse #或者from Natrual import parse | or `from Natrual import parse`

ini = NaturalAPI.parse.json('config/main.json').start()
print(ini['ver']+","+ini['author'])
```
> 它的输出结果应该是这样的： | Its output should look like this:
```js
0.0.2,['Buelie','WindAF']
```

# 为什么没有XML解析？ |  Why is there no XML parsing?
***因为python中类的环境比较特殊，类内无法调用文档模型对象的相关方法导致该功能尚未开发完成，但是您依旧能够看到hxml这个方法，目前我们也在想尽办法开发这个功能****
> **Because the environment of the class in Python is special, the relevant methods of the document model object cannot be called in the class, so the function has not yet been developed, but you can still see the method of hxml, and we are currently trying our best to develop this function**

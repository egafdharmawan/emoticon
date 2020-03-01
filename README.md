## Emoticon

Emoticon is a Python package to transform or translate emoticon into text or its meaning. Based on list of emotion in wikipedia, i created a library for text mining. This package contain western and eastern emoticon with over 300 emoticon. This package can also translate emoticon into desired language by adding optional argument.

# How to install

Simply run this code on your cmd.

```
pip install emoticon
```

# Usage

Following code will show you example how to use this package

```
from emoticon import emoticon

text = "good morning :)"
emoticon(text)
```

You can also specify the desired language by adding optional argument, for example if you want to return indonesian language, use 'id' as optional parameter.

```
from emoticon import emoticon

text = "good morning :)"
emoticon(text, 'id')
```

if you don't specify, it will return english by default.
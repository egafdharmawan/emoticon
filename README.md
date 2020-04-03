## Emoticon

Emoticon is a Python package to transform or translate emoticon into text or its meaning. Based on list of emotion in wikipedia, i created a library for text mining. This package contain western and eastern emoticon with over 300 emoticon. This package can also translate emoticon into desired language by adding optional argument.

# How to install

```
pip install emoticon
```

# Usage

Following code will show you example how to use this package

From text to emoticon :
```
from emoticon import emoticon

text = ":) :("
emoticon(text)
```

Output : "Smile Sad"

You can also specify the desired language by adding optional argument, for example if you want to return indonesian language, use 'id' as optional parameter.

```
from emoticon import emoticon

text = ":) :("
emoticon(text, 'id')
```

Output : "Senyum Sedih"

if you don't specify, it will return english by default.

From emoticon to text :

```
from emoticon import demoticon

text = "Smile Sad"
demoticon(text)
```

Output : ":) :("
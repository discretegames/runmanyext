# [RunMany Support for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=discretegames.runmany)

[RunMany](https://pypi.org/project/runmany/) is a tool that lets you write and run programs in multiple languages
from one file. This VSCode extension provides syntax highlighting for RunMany files (file extension `.many`)
and 34 embeddable languages:

> Ada,
> C,
> C#,
> Clojure,
> COBOL,
> C++,
> Dart,
> Fortran,
> F#,
> Go,
> Groovy,
> Haskell,
> Java,
> JavaScript,
> Julia,
> Kotlin,
> Lisp,
> Lua,
> Objective-C,
> Pascal,
> Perl,
> PHP,
> Python,
> Python 2,
> R,
> Racket,
> Ruby,
> Rust,
> Scala,
> Scheme,
> Swift,
> TypeScript,
> VBScript,
> and Visual Basic

Languages not [built into VSCode](https://github.com/microsoft/vscode/tree/main/extensions) such as Ada and Pascal
require their own respective VSCode extensions to be installed for their syntax highlighting to work in RunMany files.

RunMany syntax highlighting in action for [sample file](https://github.com/discretegames/runmanyext/blob/main/sample.many):

![syntax highlighting sample](https://raw.githubusercontent.com/discretegames/runmanyext/main/images/sample.png)

For the exact same RunMany syntax colors as the image, copy the `"editor.tokenColorCustomizations"` setting in this
[settings.json](https://github.com/discretegames/runmanyext/blob/main/.vscode/settings.json)
into your own settings.json.

## Requirements

This extension only really makes sense if you are using it with the
[RunMany Python package](https://pypi.org/project/runmany/), which is the tool that actually runs `.many` files.

Install it on Python 3.6 and above with:

```text
pip install runmany
```

Then run a file with:

```text
runmany myfile.many
```

See more about how to use the RunMany Python package on [PyPI](https://pypi.org/project/runmany/)
or [GitHub](https://github.com/discretegames/runmany) or try some
[example files](https://github.com/discretegames/runmany/tree/main/examples).

## Resources

- [Change Log](https://marketplace.visualstudio.com/items/discretegames.runmany/changelog)

- [GitHub Repo](https://github.com/discretegames/runmanyext)

- [Marketplace Page](https://marketplace.visualstudio.com/items?itemName=discretegames.runmany)

- [RunMany Python Package on PyPI](https://pypi.org/project/runmany/)

- [RunMany Python Package on GitHub](https://github.com/discretegames/runmany)

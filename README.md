# [RunMany Syntax Highlighting](https://marketplace.visualstudio.com/items?itemName=discretegames.runmany)

[RunMany](https://pypi.org/project/runmany/) is a tool that lets you write and run programs in multiple languages
from one file. This VSCode extension provides syntax highlighting for RunMany files
(file extension `.many` or `.runmany`)
and 34 [embeddable languages](https://github.com/discretegames/runmanyext/blob/main/supported-languages.csv):

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
Use the [Better C Syntax](https://marketplace.visualstudio.com/items?itemName=jeff-hykin.better-c-syntax)
extension for proper C highlighting.

RunMany syntax highlighting in action for a [sample file](https://github.com/discretegames/runmanyext/blob/main/sample.many):

![syntax highlighting sample](https://raw.githubusercontent.com/discretegames/runmanyext/main/images/sample.png)

For the exact same RunMany syntax colors as the image, copy
[this settings.json](https://github.com/discretegames/runmanyext/blob/main/exampleWorkspace/.vscode/settings.json)
to the .vscode folder of your workspace, or combine it with your existing settings.json.

## Requirements

This extension is intended to be used alongside the [RunMany Python package](https://pypi.org/project/runmany/), which is the tool that actually runs `.many` files.

Install it on [Python 3.6 and above](https://www.python.org/downloads/) with:

```text
pip install runmany
```

TODO talk about launch configurations.

Then run a file with:

```text
runmany myfile.many
```

See more about how to use the RunMany Python package on [PyPI](https://pypi.org/project/runmany/)
or [GitHub](https://github.com/discretegames/runmany) or try some
[example files](https://github.com/discretegames/runmany/tree/main/examples).

## Limitations

Until [LSP 3.17](https://microsoft.github.io/language-server-protocol/specifications/specification-3-17/)
is released there is unfortunately
[no reasonable way](https://code.visualstudio.com/api/language-extensions/embedded-languages#conclusion)
to have underlined errors and warnings (knows as diagnostics) show up in embedded code in VSCode.

So for for now, this extension only provides syntax highlighting, no autocompletion or diagnostics.

## Resources

- [Change Log](https://marketplace.visualstudio.com/items/discretegames.runmany/changelog)

- [GitHub Repo](https://github.com/discretegames/runmanyext)

- [Marketplace Page](https://marketplace.visualstudio.com/items?itemName=discretegames.runmany)

- [RunMany Python Package on PyPI](https://pypi.org/project/runmany/)

- [RunMany Python Package on GitHub](https://github.com/discretegames/runmany)

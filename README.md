
# RunMany Support for Visual Studio Code

[RunMany](https://pypi.org/project/runmany/) is a Python package that lets you write and run programs in
multiple languages from one file, primarily for educational purposes when learning new programming languages.

This VSCode extension provides syntax highlighting for RunMany files (file extension `.many`),
plus syntax highlighting for 34 other languages when embedded in a RunMany file:

1. Ada
2. C
3. C#
4. Clojure
5. COBOL
6. C++
7. Dart
8. Fortran
9. F#
10. Go
11. Groovy
12. Haskell
13. Java
14. JavaScript
15. Julia
16. Kotlin
17. Lisp
18. Lua
19. Objective-C
20. Pascal
21. Perl
22. PHP
23. Python
24. Python 2
25. R
26. Racket
27. Ruby
28. Rust
29. Scala
30. Scheme
31. Swift
32. TypeScript
33. VBScript
34. Visual Basic

Some of these languages may need their own respective VSCode extensions installed for their syntax highlighting to work
properly. This is because support for uncommon languages is not built into the
[extensions VSCode comes with](https://github.com/microsoft/vscode/tree/main/extensions).

The [RunMany Python package](https://pypi.org/project/runmany/) can in fact support any language you set up commands
for, but only those listed above can be syntax highlighted in a RunMany file with this VSCode extension.

## Requirements

This extension only really makes sense if you are using it with the
[RunMany Python package](https://pypi.org/project/runmany/), which is the tool that actually runs `.many` files.

Run

```text
pip install runmany
```

to install it. Python versions 3.6 and beyond are supported.

See the RunMany [Python Package Index page](https://pypi.org/project/runmany/)
or [GitHub repo](https://github.com/discretegames/runmany) for more info on how to write and run `.many` files..

# C Syntax Highlighting Issue

```c
#include <stdio.h>
int main() {
    printf("Hello, World!\n" );
    return 0;
}
```


```cpp
using namespace std;
#include <iostream>

int main(int argc, char *argv[]) {
    cout << argv[1] << endl;
    return 0;
}
```

Documented in all these issues, nor sure I can do much about it other than not mark as invalid
https://github.com/microsoft/vscode/issues/34525
https://github.com/microsoft/vscode/issues/36069
https://github.com/textmate/textmate/pull/1276
https://github.com/atom/language-c/issues/146 - core

https://github.com/atom/language-c/issues/146#issuecomment-485647740

https://github.com/jeff-hykin/better-cpp-syntax - fix?
still not sure how to use those grammars instead of others though

https://github.com/atom/language-c/issues/146#issuecomment-498438151 says the extension should fix it but it doesn't

# Ruby Example

```ruby
x = 5 + 6
puts "Hello World! #{x}"
```

# C Example

```c
int main() {
  int y = SOME_MACRO_REFERENCE;
  int x = 5 + 6;
  cout << "Hello World! " << x << std::endl();
}
```

# C++ Example

```cpp
int main() {
  int y = SOME_MACRO_REFERENCE;
  int x = 5 + 6;
  cout << "Hello World! " << x << std::endl();
}
```
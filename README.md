jetbrains-mono
===

JetBrains Mono – the free and open-source typeface for developers

[![npm][jetbrains-npm-badge]][jetbrains-npm-url]
[![no dependencies][jetbrains-dependencies-badge]][jetbrains-dependencies-url]

---

This is a convenience package to self host the [JetBrains Mono][jetbrains-site] font for use in web apps.

I don't claim any rights to the font itself, I just wrote the CSS file.

This package is based on the version 2.221 of the font.

Installation
---

```sh
npm install jetbrains-mono
```

Usage (CSS)
---

The default export of this package is a CSS file. Load it as follows:

```js
import 'jetbrains-mono'
```

Alternatively, you can just include it in HTML like this:

```html
<link rel="stylesheet" href="./node_modules/jetbrains-mono/css/jetbrains-mono.css">
```

Usage (SCSS)
---

Set the `$font-dir` variable to the correct path, as shown here:

```scss
$font-dir: './node_modules/jetbrains-mono/fonts/webfonts';

@import '~jetbrains-mono/scss/jetbrains-mono';
```

License
---

The files I authored are licensed under the [MIT License][license].

JetBrains Mono typeface is available under the [OFL-1.1 License][font-license] and can be used free of charge, for both commercial and non-commercial purposes.

[jetbrains-npm-badge]: https://img.shields.io/npm/v/jetbrains-mono.svg?style=flat
[jetbrains-npm-url]: https://www.npmjs.com/package/jetbrains-mono
[jetbrains-dependencies-badge]: https://img.shields.io/librariesio/release/npm/jetbrains-mono?style=flat
[jetbrains-dependencies-url]: https://www.npmjs.com/package/jetbrains-mono?activeTab=dependencies
[jetbrains-site]: https://jetbrains.com/mono
[license]: https://github.com/mvasilkov/jetbrains-mono/blob/master/LICENSE
[font-license]: https://github.com/JetBrains/JetBrainsMono/blob/master/LICENSE

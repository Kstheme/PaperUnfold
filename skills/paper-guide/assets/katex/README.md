# KaTeX 0.19.0

Vendored from the published KaTeX package:
https://registry.npmjs.org/katex/-/katex-0.19.0.tgz

The downloaded archive was checked against its npm SHA-512 integrity:
`sha512-v6Tznz3zJ7u3niRCoDTsumM2+HA2XXcCu+WAacCeHD2z3p9A9Ks987o5FzfTGBN0e8A0vjEgIDvLbICrXpdw/Q==`.

`katex.min.js` and `auto-render.min.js` are unmodified distribution files.
`katex.min.css` retains the distribution styles; each font-face source was
replaced with that distribution's WOFF2 font encoded as a data URL (20 fonts).
WOFF and TTF alternatives were omitted. The adjacent MIT LICENSE covers these
assets and is also embedded in generated HTML pages containing mathematics.

The Python renderer embeds these assets only when explanatory text contains
math delimiters. No download, npm installation, or CDN is needed at runtime.

Documentation: https://katex.org/docs/autorender and https://katex.org/docs/options

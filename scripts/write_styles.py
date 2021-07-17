#!/usr/bin/env python3

from pathlib import Path

fonts = {
    'Thin': {
        'Italic': 'ThinItalic',
        'Weight': 100,
    },
    'ExtraLight': {
        'Italic': 'ExtraLightItalic',
        'Weight': 200,
    },
    'Light': {
        'Italic': 'LightItalic',
        'Weight': 300,
    },
    'Regular': {
        'Italic': 'Italic',
        'Weight': 400,
    },
    'Medium': {
        'Italic': 'MediumItalic',
        'Weight': 500,
    },
    'Bold': {
        'Italic': 'BoldItalic',
        'Weight': 700,
    },
    'ExtraBold': {
        'Italic': 'ExtraBoldItalic',
        'Weight': 800,
    },
}

scss = '''
@font-face {{
  font-family: 'JetBrains Mono{nl_space}';
  font-style: {normal_italic};
  font-weight: {weight};
  src: local('JetBrains Mono{nl_space}{suffix_space}'),
    local('JetBrainsMono{nl}-{suffix}'),
    url('{font_dir}/JetBrainsMono{nl}-{suffix}.woff2') format('woff2');
  font-display: swap;
}}
'''

font_dir = '#{$font-dir}'
font_dir_init = "$font-dir: '../fonts/webfonts' !default;"

test_html = '''
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>JetBrains Mono{nl_space} test</title>
        <link rel="stylesheet" href="../css/{css_file}">
    </head>
    <body>
{test_cases}
    </body>
</html>
'''

test_case = '''
<p style="font-family: 'JetBrains Mono{nl_space}'; font-style: {normal_italic}; font-weight: {weight};">
    JetBrains Mono{nl_space} test string =&gt; (style={normal_italic} weight={weight})
</p>
'''


def get_suffix_space(font):
    return '' if font == 'Regular' else ' ' + font


def run(is_nl=False):
    nl = 'NL' if is_nl else ''
    nl_space = ' NL' if is_nl else ''

    result = font_dir_init
    tests = ''

    for font, props in fonts.items():
        # font: normal
        result += scss.format(
            font_dir=font_dir,
            normal_italic='normal',
            weight=props['Weight'],
            nl=nl,
            nl_space=nl_space,
            suffix=font,
            suffix_space=' ' + font,  # get_suffix_space(font)
        )
        # font: italic
        result += scss.format(
            font_dir=font_dir,
            normal_italic='italic',
            weight=props['Weight'],
            nl=nl,
            nl_space=nl_space,
            suffix=props['Italic'],
            suffix_space=get_suffix_space(font) + ' Italic',
        )

        # test: normal
        tests += test_case.format(normal_italic='normal', weight=props['Weight'], nl_space=nl_space)
        # test: italic
        tests += test_case.format(normal_italic='italic', weight=props['Weight'], nl_space=nl_space)

    project_root = Path(__file__).parents[1]

    out_file = project_root / 'scss' / ('jetbrains-mono-nl.scss' if is_nl else 'jetbrains-mono.scss')
    out_file.write_text(result, encoding='utf-8')

    css_file = 'jetbrains-mono-nl.css' if is_nl else 'jetbrains-mono.css'
    test_result = test_html.format(css_file=css_file, nl_space=nl_space, test_cases=tests).lstrip()

    test_file = project_root / 'test' / ('nl.html' if is_nl else 'index.html')
    test_file.write_text(test_result, encoding='utf-8')


if __name__ == '__main__':
    run()
    run(is_nl=True)

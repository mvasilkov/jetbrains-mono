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
  font-family: 'JetBrains Mono';
  font-style: {normal_italic};
  font-weight: {weight};
  src: local('JetBrains Mono{suffix_space}'),
    local('JetBrainsMono-{suffix}'),
    url('{font_dir}/JetBrainsMono-{suffix}.woff2') format('woff2'),
    url('{font_dir}/JetBrainsMono-{suffix}.woff') format('woff');
  font-display: swap;
}}
'''

font_dir = '#{$font-dir}'
font_dir_init = "$font-dir: '../fonts/web' !default;"


def get_suffix_space(font):
    return '' if font == 'Regular' else ' ' + font


def run():
    result = font_dir_init

    for font, props in fonts.items():
        # normal
        result += scss.format(
            font_dir=font_dir,
            normal_italic='normal',
            weight=props['Weight'],
            suffix=font,
            suffix_space=get_suffix_space(font)
        )
        # italic
        result += scss.format(
            font_dir=font_dir,
            normal_italic='italic',
            weight=props['Weight'],
            suffix=props['Italic'],
            suffix_space=get_suffix_space(font) + ' Italic'
        )

    out_file = Path(__file__).parents[1] / 'scss' / 'jetbrains-mono.scss'
    out_file.write_text(result, encoding='utf-8')


if __name__ == '__main__':
    run()

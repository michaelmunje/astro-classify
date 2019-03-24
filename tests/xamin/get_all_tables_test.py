import pytest
import galana as ga


def test_get_all_tables():
    ga.xamin.install()
    expected = ['a2pic', 'abell', 'abellzcat', 'acceptcat', 'agnsdssxm2', 'agnsdssxmm', 'allwiseagn',
                'arxa', 'ascaegclus', 'asiagosn', 'baxgalclus', 'cbatpicagn', 'ccosrssfag', 'cfa2s',
                'cgmw', 'cosmosvlba', 'cosxfirmwc', 'denisigal', 'eingalcat', 'eingalclus', 'esouppsala',
                'etgalxray', 'exgalemobj', 'fricat', 'friicat', 'fsvsclustr', 'gcscat', 'glxsdssqs2', 'hcg',
                'hcggalaxy', 'intibisag2', 'iraspscz', 'kuehr', 'lbqs', 'lcrscat', 'lorcat', 'lowzvlqvla',
                'lqac', 'markarian', 'markarian2', 'mcg', 'mcxc', 'milliquas', 'neargalcat', 'noras',
                'osqsonvss', 'osrilqxray', 'pgc2003', 'qorgcat', 'qso', 'rass6dfgs', 'rassbscpgc', 'rasscals',
                'rassdssagn', 'rassebcs', 'rasssdssgc', 'rc3', 'reflex', 'romabzcat', 'rosatrlq', 'rosatrqq',
                'rosgalclus', 'rosnepagn', 'roxa', 'saisncat', 'sbsggencat', 'sdssbalqs2', 'sdssbalqso',
                'sdsscxoqso', 'sdsslasqso', 'sdssnbckde', 'sdssnbcqsc', 'sdssquasar', 'sdssunuqsr', 'sdsswhlgc',
                'sdssxmmqso', 'shk', 'shkgalaxy', 'sixdfgs', 'sptszgalcl', 'swsdssqso', 'swxcscat', 'swxcsoxid',
                'tartarus', 'twodfqsoz', 'twomassrsc', 'ugc', 'ulxrbcat', 'uvqs', 'uzc', 'veroncat', 'w2ragncat',
                'warps', 'warps2', 'wbl', 'wblgalaxy', 'wisehspcat', 'xmmcty2agn', 'xrayselbll', 'xshzagncxo',
                'zcat', 'zwclusters']
    assert(ga.xamin.get_all_names() == expected)


if __name__ == '__main__':
    pytest.main([__file__])

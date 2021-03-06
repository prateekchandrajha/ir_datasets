import unittest
from ir_datasets.formats import GenericDoc, GenericQuery, TrecQrel, GenericDocPair, GenericScoredDoc
from .base import DatasetIntegrationTest


class TestMsMarcoPassage(DatasetIntegrationTest):
    def test_msmarco_passage_docs(self):
        # Include some situations that were tricky to handle correctly with the encoding fix
        self._test_docs('msmarco-passage', count=8_841_823, items={
            0: GenericDoc(doc_id='0', text='The presence of communication amid scientific minds was equally important to the success of the Manhattan Project as scientific intellect was. The only cloud hanging over the impressive achievement of the atomic researchers and engineers is what their success truly meant; hundreds of thousands of innocent lives obliterated.'),
            9: GenericDoc(doc_id='9', text="One of the main reasons Hanford was selected as a site for the Manhattan Project's B Reactor was its proximity to the Columbia River, the largest river flowing into the Pacific Ocean from the North American coast."),
            99: GenericDoc(doc_id='99', text="(1841 - 1904) Contrary to legend, Antonín Dvořák (September 8, 1841 - May 1, 1904) was not born in poverty. His father was an innkeeper and butcher, as well as an amateur musician. The father not only put no obstacles in the way of his son's pursuit of a musical career, he and his wife positively encouraged the boy."),
            243: GenericDoc(doc_id='243', text="John Maynard Keynes, 1st Baron Keynes, CB, FBA (/ˈkeɪnz/ KAYNZ; 5 June 1883 – 21 April 1946), was a British economist whose ideas fundamentally changed the theory and practice of modern macroeconomics and the economic policies of governments."),
            8841822: GenericDoc(doc_id='8841822', text='View full size image. Behind the scenes of the dazzling light shows that spectators ooh and ahh at on the Fourth of July, are carefully crafted fireworks. Whether red, white and blue fountains or purple sparklers, each firework is packed with just the right mix of chemicals to create these colorful lights. Inside each handmade firework are small packets filled with special chemicals, mainly metal salts and metal oxides, which react to produce an array of colors.')
        })

    def test_msmarco_passage_queries(self):
        self._test_queries('msmarco-passage/train', count=808731, items={
            0: GenericQuery(query_id='121352', text='define extreme'),
            9: GenericQuery(query_id='492875', text='sanitizer temperature'),
            808730: GenericQuery(query_id='50393', text='benefits of boiling lemons and drinking juice.')
        })
        self._test_queries('msmarco-passage/train/judged', count=502939, items={
            0: GenericQuery(query_id='121352', text='define extreme'),
            9: GenericQuery(query_id='54528', text='blood clots in urine after menopause'),
            502938: GenericQuery(query_id='50393', text='benefits of boiling lemons and drinking juice.')
        })
        self._test_queries('msmarco-passage/train/split200-train', count=808531, items={
            0: GenericQuery(query_id='121352', text='define extreme'),
            9: GenericQuery(query_id='492875', text='sanitizer temperature'),
            808530: GenericQuery(query_id='50393', text='benefits of boiling lemons and drinking juice.')
        })
        self._test_queries('msmarco-passage/train/split200-valid', count=200, items={
            0: GenericQuery(query_id='93927', text='coastal processes are located on what vertebrae'),
            9: GenericQuery(query_id='503706', text='steroid prednisone possible risks'),
            199: GenericQuery(query_id='44209', text='average spousal ss benefit')
        })
        self._test_queries('msmarco-passage/train/medical', count=78895, items={
            0: GenericQuery(query_id='54528', text='blood clots in urine after menopause'),
            9: GenericQuery(query_id='445408', text='marijuana for weight loss'),
            78894: GenericQuery(query_id='945443', text='when do you start going to the doctor every other week during pregnancy')
        })
        self._test_queries('msmarco-passage/dev', count=101093, items={
            0: GenericQuery(query_id='1048578', text='cost of endless pools/swim spa'),
            9: GenericQuery(query_id='1048587', text='what is patron'),
            101092: GenericQuery(query_id='524285', text='treadmill incline meaning')
        })
        self._test_queries('msmarco-passage/dev/small', count=6980, items={
            0: GenericQuery('1048585', "what is paula deen's brother"),
            9: GenericQuery('524699', 'tricare service number'),
            6979: GenericQuery('1048565', 'who plays sebastian michaelis'),
        })
        self._test_queries('msmarco-passage/dev/judged', count=55578, items={
            0: GenericQuery(query_id='1048578', text='cost of endless pools/swim spa'),
            9: GenericQuery(query_id='1048601', text='what is pastoral medicine'),
            55577: GenericQuery(query_id='1048570', text='what is pearls before swine?')
        })
        self._test_queries('msmarco-passage/eval', count=101092, items={
            0: GenericQuery(query_id='786436', text='what is prescribed to treat thyroid storm'),
            9: GenericQuery(query_id='1048619', text='who plays stitch'),
            101091: GenericQuery(query_id='786430', text='what is prescribed for pelvic inflammatory disease?')
        })
        self._test_queries('msmarco-passage/eval/small', count=6837, items={
            0: GenericQuery('57', ' term service agreement definition'),
            9: GenericQuery('262636', 'how long is a moment'),
            6836: GenericQuery('567976', 'what are the causes of unemployment'),
        })
        self._test_queries('msmarco-passage/trec-dl-2019', count=200, items={
            0: GenericQuery(query_id='1108939', text='what slows down the flow of blood'),
            9: GenericQuery(query_id='885490', text='what party is paul ryan in'),
            199: GenericQuery(query_id='532603', text='university of dubuque enrollment')
        })
        self._test_queries('msmarco-passage/trec-dl-2019/judged', count=43, items={
            0: GenericQuery(query_id='156493', text='do goldfish grow'),
            9: GenericQuery(query_id='1037798', text='who is robert gray'),
            42: GenericQuery(query_id='146187', text='difference between a mcdouble and a double cheeseburger')
        })
        self._test_queries('msmarco-passage/trec-dl-2020', count=200, items={
            0: GenericQuery(query_id='1030303', text='who is aziz hashim'),
            9: GenericQuery(query_id='1071750', text='why is pete rose banned from hall of fame'),
            199: GenericQuery(query_id='132622', text='definition of attempted arson')
        })

    def test_msmarco_passage_qrels(self):
        self._test_qrels('msmarco-passage/train', count=532761, items={
            0: TrecQrel(query_id='1185869', doc_id='0', relevance=1, iteration='0'),
            9: TrecQrel(query_id='186154', doc_id='1160', relevance=1, iteration='0'),
            532760: TrecQrel(query_id='405466', doc_id='8841735', relevance=1, iteration='0')
        })
        self._test_qrels('msmarco-passage/train/judged', count=532761, items={
            0: TrecQrel(query_id='1185869', doc_id='0', relevance=1, iteration='0'),
            9: TrecQrel(query_id='186154', doc_id='1160', relevance=1, iteration='0'),
            532760: TrecQrel(query_id='405466', doc_id='8841735', relevance=1, iteration='0')
        })
        self._test_qrels('msmarco-passage/train/medical', count=54627, items={
            0: TrecQrel(query_id='403613', doc_id='60', relevance=1, iteration='0'),
            9: TrecQrel(query_id='685235', doc_id='12191', relevance=1, iteration='0'),
            54626: TrecQrel(query_id='496447', doc_id='8839368', relevance=1, iteration='0')
        })
        self._test_qrels('msmarco-passage/dev', count=59273, items={
            0: TrecQrel(query_id='1102432', doc_id='2026790', relevance=1, iteration='0'),
            9: TrecQrel(query_id='300674', doc_id='7067032', relevance=1, iteration='0'),
            59272: TrecQrel(query_id='371455', doc_id='8009476', relevance=1, iteration='0')
        })
        self._test_qrels('msmarco-passage/dev/small', count=7437, items={
            0: TrecQrel('300674', '7067032', 1, '0'),
            9: TrecQrel('54544', '7068203', 1, '0'),
            7436: TrecQrel('195199', '8009377', 1, '0'),
        })
        self._test_qrels('msmarco-passage/dev/judged', count=59273, items={
            0: TrecQrel(query_id='1102432', doc_id='2026790', relevance=1, iteration='0'),
            9: TrecQrel(query_id='300674', doc_id='7067032', relevance=1, iteration='0'),
            59272: TrecQrel(query_id='371455', doc_id='8009476', relevance=1, iteration='0')
        })
        self._test_qrels('msmarco-passage/trec-dl-2019', count=9260, items={
            0: TrecQrel(query_id='19335', doc_id='1017759', relevance=0, iteration='Q0'),
            9: TrecQrel(query_id='19335', doc_id='1274615', relevance=0, iteration='Q0'),
            9259: TrecQrel(query_id='1133167', doc_id='977421', relevance=0, iteration='Q0')
        })
        self._test_qrels('msmarco-passage/trec-dl-2019/judged', count=9260, items={
            0: TrecQrel(query_id='19335', doc_id='1017759', relevance=0, iteration='Q0'),
            9: TrecQrel(query_id='19335', doc_id='1274615', relevance=0, iteration='Q0'),
            9259: TrecQrel(query_id='1133167', doc_id='977421', relevance=0, iteration='Q0')
        })
        self._test_qrels('msmarco-passage/train/split200-train', count=532630, items={
            0: TrecQrel(query_id='1185869', doc_id='0', relevance=1, iteration='0'),
            9: TrecQrel(query_id='186154', doc_id='1160', relevance=1, iteration='0'),
            532629: TrecQrel(query_id='405466', doc_id='8841735', relevance=1, iteration='0')
        })
        self._test_qrels('msmarco-passage/train/split200-valid', count=131, items={
            0: TrecQrel(query_id='318166', doc_id='179254', relevance=1, iteration='0'),
            9: TrecQrel(query_id='1158250', doc_id='791721', relevance=1, iteration='0'),
            130: TrecQrel(query_id='302427', doc_id='512871', relevance=1, iteration='0')
        })

    def test_msmarco_passage_docpairs(self):
        with self.subTest(subset='msmarco-passage/train'):
            self._test_docpairs('msmarco-passage/train', count=269919004, items={
                0: GenericDocPair(query_id='662731', doc_id_a='193249', doc_id_b='2975302'),
                9: GenericDocPair(query_id='411362', doc_id_a='31018', doc_id_b='4238671'),
                269919003: GenericDocPair(query_id='88228', doc_id_a='5117891', doc_id_b='7075853')
            })
        with self.subTest(subset='msmarco-passage/train/judged'):
            self._test_docpairs('msmarco-passage/train/judged', count=269919004, items={
                0: GenericDocPair(query_id='662731', doc_id_a='193249', doc_id_b='2975302'),
                9: GenericDocPair(query_id='411362', doc_id_a='31018', doc_id_b='4238671'),
                269919003: GenericDocPair(query_id='88228', doc_id_a='5117891', doc_id_b='7075853')
            })

    def test_msmarco_passage_scoreddocs(self):
        self._test_scoreddocs('msmarco-passage/train', count=478002393, items={
            0: GenericScoredDoc(query_id='965162', doc_id='1000930', score=0.0),
            9: GenericScoredDoc(query_id='817636', doc_id='1000930', score=0.0),
            478002392: GenericScoredDoc(query_id='824165', doc_id='999540', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/train/judged', count=478002393, items={
            0: GenericScoredDoc(query_id='965162', doc_id='1000930', score=0.0),
            9: GenericScoredDoc(query_id='817636', doc_id='1000930', score=0.0),
            478002392: GenericScoredDoc(query_id='824165', doc_id='999540', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/train/medical', count=48852277, items={
            0: GenericScoredDoc(query_id='15613', doc_id='1000930', score=0.0),
            9: GenericScoredDoc(query_id='85825', doc_id='1008454', score=0.0),
            48852276: GenericScoredDoc(query_id='466728', doc_id='993343', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/train/split200-train', count=477883382, items={
            0: GenericScoredDoc(query_id='965162', doc_id='1000930', score=0.0),
            9: GenericScoredDoc(query_id='817636', doc_id='1000930', score=0.0),
            477883381: GenericScoredDoc(query_id='824165', doc_id='999540', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/train/split200-valid', count=119011, items={
            0: GenericScoredDoc(query_id='867810', doc_id='1158056', score=0.0),
            9: GenericScoredDoc(query_id='540814', doc_id='1609172', score=0.0),
            119010: GenericScoredDoc(query_id='908661', doc_id='8839164', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/dev', count=6668967, items={
            0: GenericScoredDoc(query_id='188714', doc_id='1000052', score=0.0),
            9: GenericScoredDoc(query_id='345453', doc_id='1000327', score=0.0),
            6668966: GenericScoredDoc(query_id='36473', doc_id='999956', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/dev/judged', count=6668967, items={
            0: GenericScoredDoc(query_id='188714', doc_id='1000052', score=0.0),
            9: GenericScoredDoc(query_id='345453', doc_id='1000327', score=0.0),
            6668966: GenericScoredDoc(query_id='36473', doc_id='999956', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/eval', count=6515736, items={
            0: GenericScoredDoc(query_id='992904', doc_id='1000038', score=0.0),
            9: GenericScoredDoc(query_id='1114402', doc_id='1000236', score=0.0),
            6515735: GenericScoredDoc(query_id='30677', doc_id='999956', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/trec-dl-2019', count=189877, items={
            0: GenericScoredDoc(query_id='494835', doc_id='7130104', score=0.0),
            9: GenericScoredDoc(query_id='1014126', doc_id='8001869', score=0.0),
            189876: GenericScoredDoc(query_id='1124145', doc_id='7998901', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/trec-dl-2019/judged', count=41042, items={
            0: GenericScoredDoc(query_id='131843', doc_id='7130104', score=0.0),
            9: GenericScoredDoc(query_id='1117099', doc_id='7135553', score=0.0),
            41041: GenericScoredDoc(query_id='1115776', doc_id='7997171', score=0.0)
        })
        self._test_scoreddocs('msmarco-passage/trec-dl-2020', count=190699, items={
            0: GenericScoredDoc(query_id='1104501', doc_id='5138533', score=0.0),
            9: GenericScoredDoc(query_id='1129081', doc_id='5140109', score=0.0),
            190698: GenericScoredDoc(query_id='197312', doc_id='8001747', score=0.0)
        })


if __name__ == '__main__':
    unittest.main()

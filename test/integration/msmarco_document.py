import re
import unittest
from ir_datasets.datasets.msmarco_document import MsMarcoDocument
from ir_datasets.formats import GenericQuery, TrecQrel, GenericScoredDoc
from .base import DatasetIntegrationTest


class TestMsMarcoDocument(DatasetIntegrationTest):
    def test_msmarco_document_docs(self):
        self._test_docs('msmarco-document', count=3213835, items={
            0: MsMarcoDocument('D1555982', 'https://answers.yahoo.com/question/index?qid=20071007114826AAwCFvR', 'The hot glowing surfaces of stars emit energy in the form of electromagnetic radiation.?', re.compile('^Science \\& Mathematics Physics\nThe hot glowing surfaces of stars emit energy in the form of electroma.{1451}free website\\?\nInterested in dating sites\\?\nNeed a Home Security Safe\\?\nHow to order contacts online\\?\n\n$', flags=48)),
            9: MsMarcoDocument('D3048094', 'https://answers.yahoo.com/question/index?qid=20080718121858AAmfk0V', 'I have trouble swallowing due to MS, can I crush valium & other meds to be easier to swallowll?', re.compile('^Health Other \\- Health\nI have trouble swallowing due to MS, can I crush valium \\& other meds to be eas.{1335}ring Devices Considering an online college\\?\nNeed migraine treatment\\?\nVPN options for your computer\n\n$', flags=48)),
            3213834: MsMarcoDocument('D1551606', 'https://www.sciencedaily.com/releases/2014/01/140107102634.htm', 'Cancer Statistics 2014: Death rates continue to drop', re.compile('^Science News from research organizations\nCancer Statistics 2014: Death rates continue to drop\nDate: .{6213} you\\.\nScience\nDaily shares links and proceeds with scholarly publications in the Trend\nMD network\\.\n\n$', flags=48)),
        })

    def test_msmarco_document_queries(self):
        self._test_queries('msmarco-document/dev', count=5193, items={
            0: GenericQuery(query_id='174249', text='does xpress bet charge to deposit money in your account'),
            9: GenericQuery(query_id='68095', text='can hives be a sign of pregnancy'),
            5192: GenericQuery(query_id='195199', text='glioma meaning')
        })
        self._test_queries('msmarco-document/eval', count=5793, items={
            0: GenericQuery(query_id='355339', text='how to display how.close you are to.cell.tower'),
            9: GenericQuery(query_id='920435', text='what was the first mammal cloned?'),
            5792: GenericQuery(query_id='132622', text='definition of attempted arson')
        })
        self._test_queries('msmarco-document/train', count=367013, items={
            0: GenericQuery(query_id='1185869', text=')what was the immediate impact of the success of the manhattan project?'),
            9: GenericQuery(query_id='666321', text='what happens in a wrist sprain'),
            367012: GenericQuery(query_id='405466', text='is carbonic acid soluble')
        })
        self._test_queries('msmarco-document/orcas', count=10405342, items={
            0: GenericQuery(query_id='9265503', text='github'),
            9: GenericQuery(query_id='3262423', text='! in c'),
            10405341: GenericQuery(query_id='10460090', text='ð§¡')
        })
        self._test_queries('msmarco-document/trec-dl-2019', count=200, items={
            0: GenericQuery(query_id='1108939', text='what slows down the flow of blood'),
            9: GenericQuery(query_id='885490', text='what party is paul ryan in'),
            199: GenericQuery(query_id='532603', text='university of dubuque enrollment')
        })
        self._test_queries('msmarco-document/trec-dl-2019/judged', count=43, items={
            0: GenericQuery(query_id='156493', text='do goldfish grow'),
            9: GenericQuery(query_id='915593', text='what types of food can you cook sous vide'),
            42: GenericQuery(query_id='146187', text='difference between a mcdouble and a double cheeseburger')
        })
        self._test_queries('msmarco-document/trec-dl-2020', count=200, items={
            0: GenericQuery(query_id='1030303', text='who is aziz hashim'),
            9: GenericQuery(query_id='1071750', text='why is pete rose banned from hall of fame'),
            199: GenericQuery(query_id='132622', text='definition of attempted arson')
        })

    def test_msmarco_document_qrels(self):
        self._test_qrels('msmarco-document/dev', count=5193, items={
            0: TrecQrel(query_id='2', doc_id='D1650436', relevance=1, iteration='0'),
            9: TrecQrel(query_id='6217', doc_id='D1361055', relevance=1, iteration='0'),
            5192: TrecQrel(query_id='1102400', doc_id='D677570', relevance=1, iteration='0')
        })
        self._test_qrels('msmarco-document/train', count=367013, items={
            0: TrecQrel(query_id='3', doc_id='D312959', relevance=1, iteration='0'),
            9: TrecQrel(query_id='42', doc_id='D1439360', relevance=1, iteration='0'),
            367012: TrecQrel(query_id='1185869', doc_id='D59219', relevance=1, iteration='0')
        })
        self._test_qrels('msmarco-document/orcas', count=18823602, items={
            0: TrecQrel(query_id='9265503', doc_id='D1265400', relevance=1, iteration='0'),
            9: TrecQrel(query_id='9571352', doc_id='D372245', relevance=1, iteration='0'),
            18823601: TrecQrel(query_id='10460090', doc_id='D536071', relevance=1, iteration='0')
        })
        self._test_qrels('msmarco-document/trec-dl-2019', count=16258, items={
            0: TrecQrel(query_id='19335', doc_id='D1035833', relevance=0, iteration='Q0'),
            9: TrecQrel(query_id='19335', doc_id='D114440', relevance=0, iteration='Q0'),
            16257: TrecQrel(query_id='1133167', doc_id='D984590', relevance=0, iteration='Q0')
        })
        self._test_qrels('msmarco-document/trec-dl-2019/judged', count=16258, items={
            0: TrecQrel(query_id='19335', doc_id='D1035833', relevance=0, iteration='Q0'),
            9: TrecQrel(query_id='19335', doc_id='D114440', relevance=0, iteration='Q0'),
            16257: TrecQrel(query_id='1133167', doc_id='D984590', relevance=0, iteration='Q0')
        })

    def test_msmarco_document_scoreddocs(self):
        self._test_scoreddocs('msmarco-document/dev', count=519300, items={
            0: GenericScoredDoc(query_id='174249', doc_id='D3126539', score=-5.99003),
            9: GenericScoredDoc(query_id='174249', doc_id='D531991', score=-6.34283),
            519299: GenericScoredDoc(query_id='195199', doc_id='D2834135', score=-7.73695)
        })
        self._test_scoreddocs('msmarco-document/eval', count=579300, items={
            0: GenericScoredDoc(query_id='355339', doc_id='D2612180', score=-5.21639),
            9: GenericScoredDoc(query_id='355339', doc_id='D2956497', score=-5.5352),
            579299: GenericScoredDoc(query_id='808400', doc_id='D1316047', score=-5.55934)
        })
        # self._build_test_scoreddocs('msmarco-document/orcas')
        self._test_scoreddocs('msmarco-document/train', count=36701116, items={
            0: GenericScoredDoc(query_id='1185869', doc_id='D59221', score=-4.80433),
            9: GenericScoredDoc(query_id='1185869', doc_id='D1379540', score=-5.21803),
            36701115: GenericScoredDoc(query_id='748176', doc_id='D3083754', score=-6.28339)
        })
        self._test_scoreddocs('msmarco-document/trec-dl-2019', count=20000, items={
            0: GenericScoredDoc(query_id='1108939', doc_id='D388799', score=-4.80563),
            9: GenericScoredDoc(query_id='1108939', doc_id='D290854', score=-5.1522),
            19999: GenericScoredDoc(query_id='532603', doc_id='D903913', score=-6.73873)
        })
        self._test_scoreddocs('msmarco-document/trec-dl-2019/judged', count=4300, items={
            0: GenericScoredDoc(query_id='156493', doc_id='D683584', score=-4.692),
            9: GenericScoredDoc(query_id='156493', doc_id='D47015', score=-5.28076),
            4299: GenericScoredDoc(query_id='146187', doc_id='D3476417', score=-7.41072)
        })
        self._test_scoreddocs('msmarco-document/trec-dl-2020', count=20000, items={
            0: GenericScoredDoc(query_id='1049519', doc_id='D3466', score=-5.57078),
            9: GenericScoredDoc(query_id='1049519', doc_id='D1497292', score=-6.00984),
            19999: GenericScoredDoc(query_id='808400', doc_id='D1316047', score=-5.55934)
        })


if __name__ == '__main__':
    unittest.main()

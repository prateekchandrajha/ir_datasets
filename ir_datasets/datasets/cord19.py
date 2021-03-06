import io
import json
import csv
import contextlib
import os
import shutil
import tarfile
from collections import defaultdict
from typing import NamedTuple
from pathlib import Path
import ir_datasets
from ir_datasets.util import Lazy, DownloadConfig
from ir_datasets.datasets.base import Dataset, FilteredQueries, FilteredQrels, YamlDocumentation
from ir_datasets.formats import BaseDocs, TrecXmlQueries, TrecQrels, GenericQuery, GenericQrel
from ir_datasets.indices import PickleLz4FullStore


NAME = 'cord19'

_logger = ir_datasets.log.easy()


class Cord19Doc(NamedTuple):
    doc_id: str
    title: str
    doi: str
    date: str
    abstract: str
    text: str


QRELS_DEFS = {
    2: 'Relevant: the article is fully responsive to the information need as expressed by the topic, i.e. answers the Question in the topic. The article need not contain all information on the topic, but must, on its own, provide an answer to the question.',
    1: 'Partially Relevant: the article answers part of the question but would need to be combined with other information to get a complete answer.',
    0: 'Not Relevant: everything else.',
}


class Cord19Docs(BaseDocs):
    def __init__(self, streamer, extr_path, date):
        self._streamer = streamer
        self._extr_path = Path(extr_path)
        self._date = date

    def docs_path(self):
        return self._streamer.path()

    def docs_cls(self):
        return Cord19Doc

    def docs_iter(self):
        return iter(self.docs_store())

    def _docs_iter(self):
        if not os.path.exists(self._extr_path):
            try:
                with self._streamer.stream() as stream:
                    with _logger.duration('extracting tarfile'):
                        with tarfile.open(fileobj=stream, mode='r|gz') as tarf:
                            tarf.extractall(self._extr_path)
            except:
                shutil.rmtree(self._extr_path)
                raise

        with contextlib.ExitStack() as ctxt:
            # Sometiems the document parses are in a single big file, sometimes in separate.
            bigfile = self._extr_path/self._date/'document_parses.tar.gz'
            if bigfile.exists():
                fulltexts = tarfile.open(fileobj=ctxt.push(bigfile.open('rb')))
            else:
                fulltexts = {
                    'biorxiv_medrxiv': tarfile.open(fileobj=ctxt.push((self._extr_path/self._date/'biorxiv_medrxiv.tar.gz').open('rb'))),
                    'comm_use_subset': tarfile.open(fileobj=ctxt.push((self._extr_path/self._date/'comm_use_subset.tar.gz').open('rb'))),
                    'noncomm_use_subset': tarfile.open(fileobj=ctxt.push((self._extr_path/self._date/'noncomm_use_subset.tar.gz').open('rb'))),
                    'custom_license': tarfile.open(fileobj=ctxt.push((self._extr_path/self._date/'custom_license.tar.gz').open('rb'))),
                }
            csv_reader = ctxt.push((self._extr_path/self._date/'metadata.csv').open('rt'))
            csv_reader = csv.DictReader(csv_reader)
            for record in csv_reader:
                did = record['cord_uid']
                title = record['title']
                doi = record['doi']
                abstract = record['abstract']
                date = record['publish_time']
                body = ''
                data = None
                # Sometiems the document parses are in a single big file, sometimes in separate.
                # The metadata format is also different in these cases.
                if isinstance(fulltexts, dict):
                    if record['has_pmc_xml_parse']:
                        path = os.path.join(record['full_text_file'], 'pmc_json', record['pmcid'] + '.xml.json')
                        data = json.load(fulltexts[record['full_text_file']].extractfile(path))
                    elif record['has_pdf_parse']:
                        path = os.path.join(record['full_text_file'], 'pdf_json', record['sha'].split(';')[0].strip() + '.json')
                        data = json.load(fulltexts[record['full_text_file']].extractfile(path))
                else:
                    if record['pmc_json_files']:
                        data = json.load(fulltexts.extractfile(record['pmc_json_files'].split(';')[0]))
                    elif record['pdf_json_files']:
                        data = json.load(fulltexts.extractfile(record['pdf_json_files'].split(';')[0]))
                if data is not None:
                    if 'body_text' in data:
                        body = '\n\n'.join(b['section'] + '\n' + b['text'] for b in data['body_text'])
                text = f'{title}\n\n{abstract}\n\n{body}'
                yield Cord19Doc(did, title, doi, date, abstract, text)

    def docs_store(self, field='doc_id'):
        return PickleLz4FullStore(
            path=f'{self.docs_path()}.pklz4',
            init_iter_fn=self._docs_iter,
            data_cls=self.docs_cls(),
            lookup_field=field,
            index_fields=['doc_id'],
        )

    def docs_count(self):
        return self.docs_store().count()

    def docs_namespace(self):
        return NAME


def _init():
    subsets = {}
    base_path = ir_datasets.util.home_path()/NAME
    dlc = DownloadConfig.context(NAME, base_path)
    documentation = YamlDocumentation(f'docs/{NAME}.yaml')
    collection = Cord19Docs(dlc['docs/2020-07-16'], base_path/'2020-07-16', '2020-07-16')

    base = Dataset(collection, documentation('_'))

    subsets['trec-covid'] = Dataset(
        TrecXmlQueries(dlc['trec-covid/queries'], qtype_map={'query': 'title', 'question': 'description', 'narrative': 'narrative'}, namespace=NAME),
        TrecQrels(dlc['trec-covid/qrels'], QRELS_DEFS),
        collection,
        documentation('trec-covid'))

    ir_datasets.registry.register(NAME, base)
    for s in sorted(subsets):
        ir_datasets.registry.register(f'{NAME}/{s}', subsets[s])

    return base, subsets

base, subsets = _init()

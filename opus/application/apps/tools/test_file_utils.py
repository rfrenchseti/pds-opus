# tools/test_file_utils.py

from collections import OrderedDict
import logging
import sys
from unittest import TestCase

from django.core.cache import cache
from tools.file_utils import get_pds_products

import settings

class fileUtilsTests(TestCase):

    def setUp(self):
        self.maxDiff = None
        logging.disable(logging.ERROR)
        cache.clear()

    def tearDown(self):
        logging.disable(logging.NOTSET)


            ###############################################
            ######### get_pds_products UNIT TESTS #########
            ###############################################

    def test__get_pds_products_ib4v21gc_opusid_url(self):
        "[test_file_utils.py] get_pds_products: no versions opusid hst-11559-wfc3-ib4v21gc url"
        opus_id = 'hst-11559-wfc3-ib4v21gc'
        ret = get_pds_products(opus_id)
        expected = OrderedDict([('hst-11559-wfc3-ib4v21gc', OrderedDict([('Current', OrderedDict([(('browse', 10, 'browse-thumb', 'Browse Image (thumbnail)'), ['https://pds-rings.seti.org/holdings/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_thumb.jpg']), (('browse', 20, 'browse-small', 'Browse Image (small)'), ['https://pds-rings.seti.org/holdings/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_small.jpg']), (('browse', 30, 'browse-medium', 'Browse Image (medium)'), ['https://pds-rings.seti.org/holdings/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_med.jpg']), (('browse', 40, 'browse-full', 'Browse Image (full-size)'), ['https://pds-rings.seti.org/holdings/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_full.jpg']), (('HST', 10, 'hst-text', 'FITS Header Text'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.ASC', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL']), (('HST', 20, 'hst-tiff', 'Raw Data Preview (lossless)'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_RAW.TIF', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL']), (('HST', 30, 'hst-raw', 'Raw Data Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_RAW.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL']), (('HST', 40, 'hst-calib', 'Calibrated Data Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_FLT.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL']), (('HST', 70, 'hst-drizzled', 'Calibrated Geometrically Corrected Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_DRZ.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL'])]))]))])
        print('Got:')
        print(ret)
        print('Expected:')
        print(expected)
        self.assertEqual(dict(ret), dict(expected))

    def test__get_pds_products_ib4v19r3_opusid_url(self):
        "[test_file_utils.py] get_pds_products: versions opusid hst-11559-wfc3-ib4v19r3 url"
        opus_id = 'hst-11559-wfc3-ib4v19r3'
        ret = get_pds_products(opus_id)
        expected = OrderedDict([('hst-11559-wfc3-ib4v19r3', OrderedDict([('Current', OrderedDict([(('browse', 10, 'browse-thumb', 'Browse Image (thumbnail)'), ['https://pds-rings.seti.org/holdings/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_thumb.jpg']), (('browse', 20, 'browse-small', 'Browse Image (small)'), ['https://pds-rings.seti.org/holdings/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_small.jpg']), (('browse', 30, 'browse-medium', 'Browse Image (medium)'), ['https://pds-rings.seti.org/holdings/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_med.jpg']), (('browse', 40, 'browse-full', 'Browse Image (full-size)'), ['https://pds-rings.seti.org/holdings/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_full.jpg']), (('HST', 10, 'hst-text', 'FITS Header Text'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.ASC', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 20, 'hst-tiff', 'Raw Data Preview (lossless)'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.TIF', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 30, 'hst-raw', 'Raw Data Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 40, 'hst-calib', 'Calibrated Data Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_FLT.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 70, 'hst-drizzled', 'Calibrated Geometrically Corrected Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_DRZ.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL'])])), ('1.1', OrderedDict([(('HST', 10, 'hst-text', 'FITS Header Text'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.ASC', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 20, 'hst-tiff', 'Raw Data Preview (lossless)'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.TIF', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 30, 'hst-raw', 'Raw Data Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 40, 'hst-calib', 'Calibrated Data Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_FLT.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 70, 'hst-drizzled', 'Calibrated Geometrically Corrected Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_DRZ.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL'])])), ('1.0', OrderedDict([(('HST', 10, 'hst-text', 'FITS Header Text'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.ASC', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 20, 'hst-tiff', 'Raw Data Preview (lossless)'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.TIF', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 30, 'hst-raw', 'Raw Data Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 40, 'hst-calib', 'Calibrated Data Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_FLT.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 70, 'hst-drizzled', 'Calibrated Geometrically Corrected Preview'), ['https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_DRZ.JPG', 'https://pds-rings.seti.org/holdings/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL'])]))]))])
        print('Got:')
        print(ret)
        print('Expected:')
        print(expected)
        self.assertEqual(dict(ret), dict(expected))

    def test__get_pds_products_ib4v21gc_opusid_path(self):
        "[test_file_utils.py] get_pds_products: no versions opusid hst-11559-wfc3-ib4v21gc path"
        opus_id = 'hst-11559-wfc3-ib4v21gc'
        ret = get_pds_products(opus_id, loc_type='path')
        expected = OrderedDict([('hst-11559-wfc3-ib4v21gc', OrderedDict([('Current', OrderedDict([(('browse', 10, 'browse-thumb', 'Browse Image (thumbnail)'), [settings.PDS_DATA_DIR+'/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_thumb.jpg']), (('browse', 20, 'browse-small', 'Browse Image (small)'), [settings.PDS_DATA_DIR+'/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_small.jpg']), (('browse', 30, 'browse-medium', 'Browse Image (medium)'), [settings.PDS_DATA_DIR+'/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_med.jpg']), (('browse', 40, 'browse-full', 'Browse Image (full-size)'), [settings.PDS_DATA_DIR+'/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_full.jpg']), (('HST', 10, 'hst-text', 'FITS Header Text'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.ASC', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL']), (('HST', 20, 'hst-tiff', 'Raw Data Preview (lossless)'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_RAW.TIF', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL']), (('HST', 30, 'hst-raw', 'Raw Data Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_RAW.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL']), (('HST', 40, 'hst-calib', 'Calibrated Data Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_FLT.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL']), (('HST', 70, 'hst-drizzled', 'Calibrated Geometrically Corrected Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ_DRZ.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_21/IB4V21GCQ.LBL'])]))]))])
        print('Got:')
        print(ret)
        print('Expected:')
        print(expected)
        self.assertEqual(dict(ret), dict(expected))

    def test__get_pds_products_ib4v19r3_opusid_path(self):
        "[test_file_utils.py] get_pds_products: versions opusid hst-11559-wfc3-ib4v19r3 path"
        opus_id = 'hst-11559-wfc3-ib4v19r3'
        ret = get_pds_products(opus_id, loc_type='path')
        expected = OrderedDict([('hst-11559-wfc3-ib4v19r3', OrderedDict([('Current', OrderedDict([(('browse', 10, 'browse-thumb', 'Browse Image (thumbnail)'), [settings.PDS_DATA_DIR+'/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_thumb.jpg']), (('browse', 20, 'browse-small', 'Browse Image (small)'), [settings.PDS_DATA_DIR+'/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_small.jpg']), (('browse', 30, 'browse-medium', 'Browse Image (medium)'), [settings.PDS_DATA_DIR+'/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_med.jpg']), (('browse', 40, 'browse-full', 'Browse Image (full-size)'), [settings.PDS_DATA_DIR+'/previews/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_full.jpg']), (('HST', 10, 'hst-text', 'FITS Header Text'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.ASC', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 20, 'hst-tiff', 'Raw Data Preview (lossless)'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.TIF', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 30, 'hst-raw', 'Raw Data Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 40, 'hst-calib', 'Calibrated Data Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_FLT.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 70, 'hst-drizzled', 'Calibrated Geometrically Corrected Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_DRZ.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL'])])), ('1.1', OrderedDict([(('HST', 10, 'hst-text', 'FITS Header Text'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.ASC', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 20, 'hst-tiff', 'Raw Data Preview (lossless)'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.TIF', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 30, 'hst-raw', 'Raw Data Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 40, 'hst-calib', 'Calibrated Data Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_FLT.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 70, 'hst-drizzled', 'Calibrated Geometrically Corrected Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_DRZ.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.1/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL'])])), ('1.0', OrderedDict([(('HST', 10, 'hst-text', 'FITS Header Text'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.ASC', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 20, 'hst-tiff', 'Raw Data Preview (lossless)'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.TIF', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 30, 'hst-raw', 'Raw Data Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_RAW.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 40, 'hst-calib', 'Calibrated Data Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_FLT.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL']), (('HST', 70, 'hst-drizzled', 'Calibrated Geometrically Corrected Preview'), [settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q_DRZ.JPG', settings.PDS_DATA_DIR+'/volumes/HSTIx_xxxx_v1.0/HSTI1_1559/DATA/VISIT_19/IB4V19R3Q.LBL'])]))]))])
        print('Got:')
        print(ret)
        print('Expected:')
        print(expected)
        self.assertEqual(dict(ret), dict(expected))

    def test__get_pds_products_multiple_opusid(self):
        "[test_file_utils.py] get_pds_products: no versions multiple opusids path"
        opus_id_list = ['co-iss-n1460960868',
                        'co-uvis-euv2001_001_02_12',
                        'co-vims-v1484504505_ir',
                        'vg-iss-2-s-c4360048']
        ret = get_pds_products(opus_id_list, loc_type='path')
        expected = OrderedDict([('co-iss-n1460960868', OrderedDict([('Current', OrderedDict([(('metadata', 10, 'inventory', 'Target Body Inventory'), [settings.PDS_DATA_DIR+'/metadata/COISS_2xxx/COISS_2002/COISS_2002_inventory.tab', settings.PDS_DATA_DIR+'/metadata/COISS_2xxx/COISS_2002/COISS_2002_inventory.lbl']), (('metadata', 20, 'planet-geometry', 'Planet Geometry Index'), [settings.PDS_DATA_DIR+'/metadata/COISS_2xxx/COISS_2002/COISS_2002_saturn_summary.tab', settings.PDS_DATA_DIR+'/metadata/COISS_2xxx/COISS_2002/COISS_2002_saturn_summary.lbl']), (('metadata', 30, 'moon-geometry', 'Moon Geometry Index'), [settings.PDS_DATA_DIR+'/metadata/COISS_2xxx/COISS_2002/COISS_2002_moon_summary.tab', settings.PDS_DATA_DIR+'/metadata/COISS_2xxx/COISS_2002/COISS_2002_moon_summary.lbl']), (('metadata', 40, 'ring-geometry', 'Ring Geometry Index'), [settings.PDS_DATA_DIR+'/metadata/COISS_2xxx/COISS_2002/COISS_2002_ring_summary.tab', settings.PDS_DATA_DIR+'/metadata/COISS_2xxx/COISS_2002/COISS_2002_ring_summary.lbl']), (('browse', 10, 'browse-thumb', 'Browse Image (thumbnail)'), [settings.PDS_DATA_DIR+'/previews/COISS_2xxx/COISS_2002/data/1460960653_1461048959/N1460960868_1_thumb.jpg']), (('browse', 20, 'browse-small', 'Browse Image (small)'), [settings.PDS_DATA_DIR+'/previews/COISS_2xxx/COISS_2002/data/1460960653_1461048959/N1460960868_1_small.jpg']), (('browse', 30, 'browse-medium', 'Browse Image (medium)'), [settings.PDS_DATA_DIR+'/previews/COISS_2xxx/COISS_2002/data/1460960653_1461048959/N1460960868_1_med.jpg']), (('browse', 40, 'browse-full', 'Browse Image (full-size)'), [settings.PDS_DATA_DIR+'/previews/COISS_2xxx/COISS_2002/data/1460960653_1461048959/N1460960868_1_full.png']), (('Cassini ISS', 0, 'coiss-raw', 'Raw image'), [settings.PDS_DATA_DIR+'/volumes/COISS_2xxx/COISS_2002/data/1460960653_1461048959/N1460960868_1.IMG', settings.PDS_DATA_DIR+'/volumes/COISS_2xxx/COISS_2002/data/1460960653_1461048959/N1460960868_1.LBL', settings.PDS_DATA_DIR+'/volumes/COISS_2xxx/COISS_2002/label/prefix2.fmt', settings.PDS_DATA_DIR+'/volumes/COISS_2xxx/COISS_2002/label/tlmtab.fmt']), (('Cassini ISS', 10, 'coiss-calib', 'Calibrated image'), [settings.PDS_DATA_DIR+'/calibrated/COISS_2xxx/COISS_2002/data/1460960653_1461048959/N1460960868_1_CALIB.IMG', settings.PDS_DATA_DIR+'/calibrated/COISS_2xxx/COISS_2002/data/1460960653_1461048959/N1460960868_1_CALIB.LBL']), (('Cassini ISS', 110, 'coiss-thumb', 'Extra preview (thumbnail)'), [settings.PDS_DATA_DIR+'/volumes/COISS_2xxx/COISS_2002/extras/thumbnail/1460960653_1461048959/N1460960868_1.IMG.jpeg_small']), (('Cassini ISS', 120, 'coiss-medium', 'Extra preview (medium)'), [settings.PDS_DATA_DIR+'/volumes/COISS_2xxx/COISS_2002/extras/browse/1460960653_1461048959/N1460960868_1.IMG.jpeg']), (('Cassini ISS', 130, 'coiss-full', 'Extra preview (full)'), [settings.PDS_DATA_DIR+'/volumes/COISS_2xxx/COISS_2002/extras/full/1460960653_1461048959/N1460960868_1.IMG.png'])])), ('1.0', OrderedDict([(('Cassini ISS', 10, 'coiss-calib', 'Calibrated image'), [settings.PDS_DATA_DIR+'/calibrated/COISS_2xxx_v1.0/COISS_2002/data/1460960653_1461048959/N1460960868_1_CALIB.IMG', settings.PDS_DATA_DIR+'/calibrated/COISS_2xxx_v1.0/COISS_2002/data/1460960653_1461048959/N1460960868_1_CALIB.LBL'])]))])), ('co-uvis-euv2001_001_02_12', OrderedDict([('Current', OrderedDict([(('browse', 10, 'browse-thumb', 'Browse Image (thumbnail)'), [settings.PDS_DATA_DIR+'/previews/COUVIS_0xxx/COUVIS_0002/DATA/D2001_001/EUV2001_001_02_12_thumb.png']), (('browse', 20, 'browse-small', 'Browse Image (small)'), [settings.PDS_DATA_DIR+'/previews/COUVIS_0xxx/COUVIS_0002/DATA/D2001_001/EUV2001_001_02_12_small.png']), (('browse', 30, 'browse-medium', 'Browse Image (medium)'), [settings.PDS_DATA_DIR+'/previews/COUVIS_0xxx/COUVIS_0002/DATA/D2001_001/EUV2001_001_02_12_med.png']), (('browse', 40, 'browse-full', 'Browse Image (full-size)'), [settings.PDS_DATA_DIR+'/previews/COUVIS_0xxx/COUVIS_0002/DATA/D2001_001/EUV2001_001_02_12_full.png']), (('Cassini UVIS', 10, 'couvis-raw', 'Raw Data'), [settings.PDS_DATA_DIR+'/volumes/COUVIS_0xxx/COUVIS_0002/DATA/D2001_001/EUV2001_001_02_12.DAT', settings.PDS_DATA_DIR+'/volumes/COUVIS_0xxx/COUVIS_0002/DATA/D2001_001/EUV2001_001_02_12.LBL'])]))])), ('co-vims-v1484504505_ir', OrderedDict([('Current', OrderedDict([(('metadata', 10, 'inventory', 'Target Body Inventory'), [settings.PDS_DATA_DIR+'/metadata/COVIMS_0xxx/COVIMS_0006/COVIMS_0006_inventory.tab', settings.PDS_DATA_DIR+'/metadata/COVIMS_0xxx/COVIMS_0006/COVIMS_0006_inventory.lbl']), (('metadata', 20, 'planet-geometry', 'Planet Geometry Index'), [settings.PDS_DATA_DIR+'/metadata/COVIMS_0xxx/COVIMS_0006/COVIMS_0006_saturn_summary.tab', settings.PDS_DATA_DIR+'/metadata/COVIMS_0xxx/COVIMS_0006/COVIMS_0006_saturn_summary.lbl']), (('metadata', 30, 'moon-geometry', 'Moon Geometry Index'), [settings.PDS_DATA_DIR+'/metadata/COVIMS_0xxx/COVIMS_0006/COVIMS_0006_moon_summary.tab', settings.PDS_DATA_DIR+'/metadata/COVIMS_0xxx/COVIMS_0006/COVIMS_0006_moon_summary.lbl']), (('metadata', 40, 'ring-geometry', 'Ring Geometry Index'), [settings.PDS_DATA_DIR+'/metadata/COVIMS_0xxx/COVIMS_0006/COVIMS_0006_ring_summary.tab', settings.PDS_DATA_DIR+'/metadata/COVIMS_0xxx/COVIMS_0006/COVIMS_0006_ring_summary.lbl']), (('browse', 10, 'browse-thumb', 'Browse Image (thumbnail)'), [settings.PDS_DATA_DIR+'/previews/COVIMS_0xxx/COVIMS_0006/data/2005015T175855_2005016T184233/v1484504505_4_thumb.png']), (('browse', 20, 'browse-small', 'Browse Image (small)'), [settings.PDS_DATA_DIR+'/previews/COVIMS_0xxx/COVIMS_0006/data/2005015T175855_2005016T184233/v1484504505_4_small.png']), (('browse', 30, 'browse-medium', 'Browse Image (medium)'), [settings.PDS_DATA_DIR+'/previews/COVIMS_0xxx/COVIMS_0006/data/2005015T175855_2005016T184233/v1484504505_4_med.png']), (('browse', 40, 'browse-full', 'Browse Image (full-size)'), [settings.PDS_DATA_DIR+'/previews/COVIMS_0xxx/COVIMS_0006/data/2005015T175855_2005016T184233/v1484504505_4_full.png']), (('Cassini VIMS', 0, 'covims-raw', 'Raw cube'), [settings.PDS_DATA_DIR+'/volumes/COVIMS_0xxx/COVIMS_0006/data/2005015T175855_2005016T184233/v1484504505_4.qub', settings.PDS_DATA_DIR+'/volumes/COVIMS_0xxx/COVIMS_0006/data/2005015T175855_2005016T184233/v1484504505_4.lbl', settings.PDS_DATA_DIR+'/volumes/COVIMS_0xxx/COVIMS_0006/label/band_bin_center.fmt', settings.PDS_DATA_DIR+'/volumes/COVIMS_0xxx/COVIMS_0006/label/core_description.fmt', settings.PDS_DATA_DIR+'/volumes/COVIMS_0xxx/COVIMS_0006/label/suffix_description.fmt']), (('Cassini VIMS', 110, 'covims-thumb', 'Extra preview (thumbnail)'), [settings.PDS_DATA_DIR+'/volumes/COVIMS_0xxx/COVIMS_0006/extras/thumbnail/2005015T175855_2005016T184233/v1484504505_4.qub.jpeg_small']), (('Cassini VIMS', 120, 'covims-medium', 'Extra preview (medium)'), [settings.PDS_DATA_DIR+'/volumes/COVIMS_0xxx/COVIMS_0006/extras/browse/2005015T175855_2005016T184233/v1484504505_4.qub.jpeg']), (('Cassini VIMS', 130, 'covims-full', 'Extra preview (full)'), [settings.PDS_DATA_DIR+'/volumes/COVIMS_0xxx/COVIMS_0006/extras/tiff/2005015T175855_2005016T184233/v1484504505_4.qub.tiff'])]))])), ('vg-iss-2-s-c4360048', OrderedDict([('Current', OrderedDict([(('metadata', 10, 'inventory', 'Target Body Inventory'), [settings.PDS_DATA_DIR+'/metadata/VGISS_6xxx/VGISS_6210/VGISS_6210_inventory.tab', settings.PDS_DATA_DIR+'/metadata/VGISS_6xxx/VGISS_6210/VGISS_6210_inventory.lbl']), (('metadata', 20, 'planet-geometry', 'Planet Geometry Index'), [settings.PDS_DATA_DIR+'/metadata/VGISS_6xxx/VGISS_6210/VGISS_6210_saturn_summary.tab', settings.PDS_DATA_DIR+'/metadata/VGISS_6xxx/VGISS_6210/VGISS_6210_saturn_summary.lbl']), (('metadata', 30, 'moon-geometry', 'Moon Geometry Index'), [settings.PDS_DATA_DIR+'/metadata/VGISS_6xxx/VGISS_6210/VGISS_6210_moon_summary.tab', settings.PDS_DATA_DIR+'/metadata/VGISS_6xxx/VGISS_6210/VGISS_6210_moon_summary.lbl']), (('metadata', 40, 'ring-geometry', 'Ring Geometry Index'), [settings.PDS_DATA_DIR+'/metadata/VGISS_6xxx/VGISS_6210/VGISS_6210_ring_summary.tab', settings.PDS_DATA_DIR+'/metadata/VGISS_6xxx/VGISS_6210/VGISS_6210_ring_summary.lbl']), (('browse', 10, 'browse-thumb', 'Browse Image (thumbnail)'), [settings.PDS_DATA_DIR+'/previews/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_thumb.jpg']), (('browse', 20, 'browse-small', 'Browse Image (small)'), [settings.PDS_DATA_DIR+'/previews/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_small.jpg']), (('browse', 30, 'browse-medium', 'Browse Image (medium)'), [settings.PDS_DATA_DIR+'/previews/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_med.jpg']), (('browse', 40, 'browse-full', 'Browse Image (full-size)'), [settings.PDS_DATA_DIR+'/previews/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_full.jpg']), (('Voyager ISS', 0, 'vgiss-raw', 'Raw Image'), [settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_RAW.IMG', settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_RAW.LBL']), (('Voyager ISS', 10, 'vgiss-cleaned', 'Cleaned Image'), [settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_CLEANED.IMG', settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_CLEANED.LBL']), (('Voyager ISS', 20, 'vgiss-calib', 'Calibrated Image'), [settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_CALIB.IMG', settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_CALIB.LBL']), (('Voyager ISS', 30, 'vgiss-geomed', 'Geometrically Corrected Image'), [settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_GEOMED.IMG', settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_GEOMED.LBL']), (('Voyager ISS', 40, 'vgiss-resloc', 'Reseau Table'), [settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_RESLOC.TAB', settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_RESLOC.DAT', settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_RESLOC.LBL']), (('Voyager ISS', 50, 'vgiss-geoma', 'Geometric Tiepoint Table'), [settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_GEOMA.TAB', settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_GEOMA.DAT', settings.PDS_DATA_DIR+'/volumes/VGISS_6xxx/VGISS_6210/DATA/C43600XX/C4360048_GEOMA.LBL'])]))]))])
        print('Got:')
        print(ret)
        print('Expected:')
        print(expected)
        self.assertEqual(dict(ret), dict(expected))

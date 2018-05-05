################################################################################
# populate_obs_mission_hubble_hubble.py
#
# Routines to populate fields specific to HST. It may change fields in
# obs_general or obs_mission_hubble_hubble.
################################################################################

import julian

from config_data import *
import impglobals
import import_util


################################################################################
# THESE NEED TO BE IMPLEMENTED FOR EVERY MISSION
################################################################################

def _helper_hubble_planet_id(**kwargs):
    metadata = kwargs['metadata']
    index_row_num = metadata['index_row_num']
    index_row = metadata['index_row']
    planet_name = index_row['PLANET_NAME']

    if planet_name == 'N/A':
        return None

    if planet_name not in ['VENUS', 'EARTH', 'MARS', 'JUPITER', 'SATURN',
                           'URANUS', 'NEPTUNE', 'PLUTO']:
        return None
    return planet_name[:3]

def populate_obs_general_HST_planet_id(**kwargs):
    planet = _helper_hubble_planet_id(**kwargs)
    if planet is None:
        return 'OTH'
    return planet


################################################################################
# THESE NEED TO BE IMPLEMENTED FOR EVERY INSTRUMENT
################################################################################

### OBS_GENERAL TABLE ###

def populate_obs_general_HSTx_rms_obs_id(**kwargs):
    metadata = kwargs['metadata']
    instrument = kwargs['instrument_name']
    index_row = metadata['index_row']
    start_time = import_util.safe_column(index_row, 'START_TIME')
    product_id = index_row['PRODUCT_ID']
    planet_id = _helper_hubble_planet_id(**kwargs)
    ret = 'X'
    if planet_id is not None:
        ret = planet_id[0]
    return ret+'_IMG_HSTx_'+instrument[3:]+'_'+start_time[:10]+'_'+product_id

populate_obs_general_HSTACS_rms_obs_id = populate_obs_general_HSTx_rms_obs_id
populate_obs_general_HSTNICMOS_rms_obs_id = populate_obs_general_HSTx_rms_obs_id
populate_obs_general_HSTSTIS_rms_obs_id = populate_obs_general_HSTx_rms_obs_id
populate_obs_general_HSTWFC3_rms_obs_id = populate_obs_general_HSTx_rms_obs_id
populate_obs_general_HSTWFPC2_rms_obs_id = populate_obs_general_HSTx_rms_obs_id

def populate_obs_general_HSTx_inst_host_id(**kwargs):
    return 'HST'

populate_obs_general_HSTACS_inst_host_id = populate_obs_general_HSTx_inst_host_id
populate_obs_general_HSTNICMOS_inst_host_id = populate_obs_general_HSTx_inst_host_id
populate_obs_general_HSTSTIS_inst_host_id = populate_obs_general_HSTx_inst_host_id
populate_obs_general_HSTWFC3_inst_host_id = populate_obs_general_HSTx_inst_host_id
populate_obs_general_HSTWFPC2_inst_host_id = populate_obs_general_HSTx_inst_host_id

def populate_obs_general_HSTx_data_type(**kwargs):
    return 'IMG'

populate_obs_general_HSTACS_data_type = populate_obs_general_HSTx_data_type
populate_obs_general_HSTNICMOS_data_type = populate_obs_general_HSTx_data_type
populate_obs_general_HSTSTIS_data_type = populate_obs_general_HSTx_data_type
populate_obs_general_HSTWFC3_data_type = populate_obs_general_HSTx_data_type
populate_obs_general_HSTWFPC2_data_type = populate_obs_general_HSTx_data_type

def populate_obs_general_HSTx_time1(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    start_time = import_util.safe_column(index_row, 'START_TIME')
    return start_time

populate_obs_general_HSTACS_time1 = populate_obs_general_HSTx_time1
populate_obs_general_HSTNICMOS_time1 = populate_obs_general_HSTx_time1
populate_obs_general_HSTSTIS_time1 = populate_obs_general_HSTx_time1
populate_obs_general_HSTWFC3_time1 = populate_obs_general_HSTx_time1
populate_obs_general_HSTWFPC2_time1 = populate_obs_general_HSTx_time1

def populate_obs_general_HSTx_time2(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    stop_time = import_util.safe_column(index_row, 'STOP_TIME')
    return stop_time

populate_obs_general_HSTACS_time2 = populate_obs_general_HSTx_time2
populate_obs_general_HSTNICMOS_time2 = populate_obs_general_HSTx_time2
populate_obs_general_HSTSTIS_time2 = populate_obs_general_HSTx_time2
populate_obs_general_HSTWFC3_time2 = populate_obs_general_HSTx_time2
populate_obs_general_HSTWFPC2_time2 = populate_obs_general_HSTx_time2

def populate_obs_general_HSTx_time_sec1(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    start_time = import_util.safe_column(index_row, 'START_TIME')
    return julian.tai_from_iso(start_time)

populate_obs_general_HSTACS_time_sec1 = populate_obs_general_HSTx_time_sec1
populate_obs_general_HSTNICMOS_time_sec1 = populate_obs_general_HSTx_time_sec1
populate_obs_general_HSTSTIS_time_sec1 = populate_obs_general_HSTx_time_sec1
populate_obs_general_HSTWFC3_time_sec1 = populate_obs_general_HSTx_time_sec1
populate_obs_general_HSTWFPC2_time_sec1 = populate_obs_general_HSTx_time_sec1

def populate_obs_general_HSTx_time_sec2(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    stop_time = import_util.safe_column(index_row, 'STOP_TIME')
    obs_general_row = metadata['obs_general_row']

    time2 = julian.tai_from_iso(stop_time)

    if time2 < obs_general_row['time_sec1']:
        start_time = import_util.safe_column(index_row, 'START_TIME')
        index_row_num = metadata['index_row_num']
        impglobals.LOGGER.log('error',
            f'time_sec1 ({start_time}) and time_sec2 ({stop_time}) are '+
            f'in the wrong order [line {index_row_num}]')
        impglobals.IMPORT_HAS_BAD_DATA = True

    return time2

populate_obs_general_HSTACS_time_sec2 = populate_obs_general_HSTx_time_sec2
populate_obs_general_HSTNICMOS_time_sec2 = populate_obs_general_HSTx_time_sec2
populate_obs_general_HSTSTIS_time_sec2 = populate_obs_general_HSTx_time_sec2
populate_obs_general_HSTWFC3_time_sec2 = populate_obs_general_HSTx_time_sec2
populate_obs_general_HSTWFPC2_time_sec2 = populate_obs_general_HSTx_time_sec2

def populate_obs_general_HSTx_target_name(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']

    target_name = index_row['TARGET_NAME'].upper()
    if target_name in TARGET_NAME_MAPPING:
        target_name = TARGET_NAME_MAPPING[target_name]

    return (target_name, target_name.title())

populate_obs_general_HSTACS_target_name = populate_obs_general_HSTx_target_name
populate_obs_general_HSTNICMOS_target_name = populate_obs_general_HSTx_target_name
populate_obs_general_HSTSTIS_target_name = populate_obs_general_HSTx_target_name
populate_obs_general_HSTWFC3_target_name = populate_obs_general_HSTx_target_name
populate_obs_general_HSTWFPC2_target_name = populate_obs_general_HSTx_target_name

def populate_obs_general_HSTx_observation_duration(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    exposure = import_util.safe_column(index_row, 'EXPOSURE_DURATION')

    if exposure is None:
        return None

    return exposure / 1000

populate_obs_general_HSTACS_observation_duration = populate_obs_general_HSTx_observation_duration
populate_obs_general_HSTNICMOS_observation_duration = populate_obs_general_HSTx_observation_duration
populate_obs_general_HSTSTIS_observation_duration = populate_obs_general_HSTx_observation_duration
populate_obs_general_HSTWFC3_observation_duration = populate_obs_general_HSTx_observation_duration
populate_obs_general_HSTWFPC2_observation_duration = populate_obs_general_HSTx_observation_duration

def populate_obs_general_HSTx_quantity(**kwargs):
    return 'REFLECT'

populate_obs_general_HSTACS_quantity = populate_obs_general_HSTx_quantity
populate_obs_general_HSTNICMOS_quantity = populate_obs_general_HSTx_quantity
populate_obs_general_HSTSTIS_quantity = populate_obs_general_HSTx_quantity
populate_obs_general_HSTWFC3_quantity = populate_obs_general_HSTx_quantity
populate_obs_general_HSTWFPC2_quantity = populate_obs_general_HSTx_quantity

def populate_obs_general_HSTx_note(**kwargs):
    return None

populate_obs_general_HSTACS_note = populate_obs_general_HSTx_note
populate_obs_general_HSTNICMOS_note = populate_obs_general_HSTx_note
populate_obs_general_HSTSTIS_note = populate_obs_general_HSTx_note
populate_obs_general_HSTWFC3_note = populate_obs_general_HSTx_note
populate_obs_general_HSTWFPC2_note = populate_obs_general_HSTx_note

def populate_obs_general_HSTx_primary_file_spec(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    return index_row['FILE_SPECIFICATION_NAME']

populate_obs_general_HSTACS_primary_file_spec = populate_obs_general_HSTx_primary_file_spec
populate_obs_general_HSTNICMOS_primary_file_spec = populate_obs_general_HSTx_primary_file_spec
populate_obs_general_HSTSTIS_primary_file_spec = populate_obs_general_HSTx_primary_file_spec
populate_obs_general_HSTWFC3_primary_file_spec = populate_obs_general_HSTx_primary_file_spec
populate_obs_general_HSTWFPC2_primary_file_spec = populate_obs_general_HSTx_primary_file_spec

def populate_obs_general_HSTx_data_set_id(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    dsi = index_row['DATA_SET_ID']
    return (dsi, dsi)

populate_obs_general_HSTACS_data_set_id = populate_obs_general_HSTx_data_set_id
populate_obs_general_HSTNICMOS_data_set_id = populate_obs_general_HSTx_data_set_id
populate_obs_general_HSTSTIS_data_set_id = populate_obs_general_HSTx_data_set_id
populate_obs_general_HSTWFC3_data_set_id = populate_obs_general_HSTx_data_set_id
populate_obs_general_HSTWFPC2_data_set_id = populate_obs_general_HSTx_data_set_id

def populate_obs_general_HSTx_product_id(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    product_id = index_row['PRODUCT_ID']

    return product_id

populate_obs_general_HSTACS_product_id = populate_obs_general_HSTx_product_id
populate_obs_general_HSTNICMOS_product_id = populate_obs_general_HSTx_product_id
populate_obs_general_HSTSTIS_product_id = populate_obs_general_HSTx_product_id
populate_obs_general_HSTWFC3_product_id = populate_obs_general_HSTx_product_id
populate_obs_general_HSTWFPC2_product_id = populate_obs_general_HSTx_product_id

def populate_obs_general_HSTx_right_asc1(**kwargs):
    return None

populate_obs_general_HSTACS_right_asc1 = populate_obs_general_HSTx_right_asc1
populate_obs_general_HSTNICMOS_right_asc1 = populate_obs_general_HSTx_right_asc1
populate_obs_general_HSTSTIS_right_asc1 = populate_obs_general_HSTx_right_asc1
populate_obs_general_HSTWFC3_right_asc1 = populate_obs_general_HSTx_right_asc1
populate_obs_general_HSTWFPC2_right_asc1 = populate_obs_general_HSTx_right_asc1

def populate_obs_general_HSTx_right_asc2(**kwargs):
    return None

populate_obs_general_HSTACS_right_asc2 = populate_obs_general_HSTx_right_asc2
populate_obs_general_HSTNICMOS_right_asc2 = populate_obs_general_HSTx_right_asc2
populate_obs_general_HSTSTIS_right_asc2 = populate_obs_general_HSTx_right_asc2
populate_obs_general_HSTWFC3_right_asc2 = populate_obs_general_HSTx_right_asc2
populate_obs_general_HSTWFPC2_right_asc2 = populate_obs_general_HSTx_right_asc2

def populate_obs_general_HSTx_declination1(**kwargs):
    return None

populate_obs_general_HSTACS_declination1 = populate_obs_general_HSTx_declination1
populate_obs_general_HSTNICMOS_declination1 = populate_obs_general_HSTx_declination1
populate_obs_general_HSTSTIS_declination1 = populate_obs_general_HSTx_declination1
populate_obs_general_HSTWFC3_declination1 = populate_obs_general_HSTx_declination1
populate_obs_general_HSTWFPC2_declination1 = populate_obs_general_HSTx_declination1

def populate_obs_general_HSTx_declination2(**kwargs):
    return None

populate_obs_general_HSTACS_declination2 = populate_obs_general_HSTx_declination2
populate_obs_general_HSTNICMOS_declination2 = populate_obs_general_HSTx_declination2
populate_obs_general_HSTSTIS_declination2 = populate_obs_general_HSTx_declination2
populate_obs_general_HSTWFC3_declination2 = populate_obs_general_HSTx_declination2
populate_obs_general_HSTWFPC2_declination2 = populate_obs_general_HSTx_declination2


### OBS_TYPE_IMAGE TABLE ###

def populate_obs_type_image_HSTx_image_type_id(**kwargs):
    return 'FRAM'

populate_obs_type_image_HSTACS_image_type_id = populate_obs_type_image_HSTx_image_type_id
populate_obs_type_image_HSTNICMOS_image_type_id = populate_obs_type_image_HSTx_image_type_id
populate_obs_type_image_HSTSTIS_image_type_id = populate_obs_type_image_HSTx_image_type_id
populate_obs_type_image_HSTWFC3_image_type_id = populate_obs_type_image_HSTx_image_type_id
populate_obs_type_image_HSTWFPC2_image_type_id = populate_obs_type_image_HSTx_image_type_id

def populate_obs_type_image_HSTx_duration(**kwargs):
    metadata = kwargs['metadata']
    obs_general_row = metadata['obs_general_row']
    return obs_general_row['observation_duration']

populate_obs_type_image_HSTACS_duration = populate_obs_type_image_HSTx_duration
populate_obs_type_image_HSTNICMOS_duration = populate_obs_type_image_HSTx_duration
populate_obs_type_image_HSTSTIS_duration = populate_obs_type_image_HSTx_duration
populate_obs_type_image_HSTWFC3_duration = populate_obs_type_image_HSTx_duration
populate_obs_type_image_HSTWFPC2_duration = populate_obs_type_image_HSTx_duration

def populate_obs_type_image_HSTACS_levels(**kwargs):
    return None # XXX

def populate_obs_type_image_HSTNICMOS_levels(**kwargs):
    return None

def populate_obs_type_image_HSTSTIS_levels(**kwargs):
    return None # XXX

def populate_obs_type_image_HSTWFC3_levels(**kwargs):
    return None # XXX

def populate_obs_type_image_HSTWFPC2_levels(**kwargs):
    return None # XXX

def populate_obs_type_image_HSTx_lesser_pixel_size(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    lines = import_util.safe_column(index_row, 'LINES')
    samples = import_util.safe_column(index_row, 'LINE_SAMPLES')
    if lines is None or samples is None:
        return None
    return min(lines, samples)

populate_obs_type_image_HSTACS_lesser_pixel_size = populate_obs_type_image_HSTx_lesser_pixel_size
populate_obs_type_image_HSTNICMOS_lesser_pixel_size = populate_obs_type_image_HSTx_lesser_pixel_size
populate_obs_type_image_HSTSTIS_lesser_pixel_size = populate_obs_type_image_HSTx_lesser_pixel_size
populate_obs_type_image_HSTWFC3_lesser_pixel_size = populate_obs_type_image_HSTx_lesser_pixel_size
populate_obs_type_image_HSTWFPC2_lesser_pixel_size = populate_obs_type_image_HSTx_lesser_pixel_size

def populate_obs_type_image_HSTx_greater_pixel_size(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    lines = import_util.safe_column(index_row, 'LINES')
    samples = import_util.safe_column(index_row, 'LINE_SAMPLES')
    if lines is None or samples is None:
        return None
    return max(lines, samples)

populate_obs_type_image_HSTACS_greater_pixel_size = populate_obs_type_image_HSTx_greater_pixel_size
populate_obs_type_image_HSTNICMOS_greater_pixel_size = populate_obs_type_image_HSTx_greater_pixel_size
populate_obs_type_image_HSTSTIS_greater_pixel_size = populate_obs_type_image_HSTx_greater_pixel_size
populate_obs_type_image_HSTWFC3_greater_pixel_size = populate_obs_type_image_HSTx_greater_pixel_size
populate_obs_type_image_HSTWFPC2_greater_pixel_size = populate_obs_type_image_HSTx_greater_pixel_size


### OBS_WAVELENGTH TABLE ###

def populate_obs_wavelength_HSTx_wavelength1(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    wl1 = import_util.safe_column(index_row, 'MINIMUM_WAVELENGTH')

    return wl1

populate_obs_wavelength_HSTACS_wavelength1 = populate_obs_wavelength_HSTx_wavelength1
populate_obs_wavelength_HSTNICMOS_wavelength1 = populate_obs_wavelength_HSTx_wavelength1
populate_obs_wavelength_HSTSTIS_wavelength1 = populate_obs_wavelength_HSTx_wavelength1
populate_obs_wavelength_HSTWFC3_wavelength1 = populate_obs_wavelength_HSTx_wavelength1
populate_obs_wavelength_HSTWFPC2_wavelength1 = populate_obs_wavelength_HSTx_wavelength1

def populate_obs_wavelength_HSTx_wavelength2(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    wl2 = import_util.safe_column(index_row, 'MINIMUM_WAVELENGTH')

    return wl2

populate_obs_wavelength_HSTACS_wavelength2 = populate_obs_wavelength_HSTx_wavelength2
populate_obs_wavelength_HSTNICMOS_wavelength2 = populate_obs_wavelength_HSTx_wavelength2
populate_obs_wavelength_HSTSTIS_wavelength2 = populate_obs_wavelength_HSTx_wavelength2
populate_obs_wavelength_HSTWFC3_wavelength2 = populate_obs_wavelength_HSTx_wavelength2
populate_obs_wavelength_HSTWFPC2_wavelength2 = populate_obs_wavelength_HSTx_wavelength2

def populate_obs_wavelength_HSTx_wave_res1(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    wr = import_util.safe_column(index_row, 'WAVELENGTH_RESOLUTION')

    return wr

populate_obs_wavelength_HSTACS_wave_res1 = populate_obs_wavelength_HSTx_wave_res1
populate_obs_wavelength_HSTNICMOS_wave_res1 = populate_obs_wavelength_HSTx_wave_res1
populate_obs_wavelength_HSTWFC3_wave_res1 = populate_obs_wavelength_HSTx_wave_res1
populate_obs_wavelength_HSTWFPC2_wave_res1 = populate_obs_wavelength_HSTx_wave_res1

def populate_obs_wavelength_HSTx_wave_res2(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    wr = import_util.safe_column(index_row, 'WAVELENGTH_RESOLUTION')

    return wr

populate_obs_wavelength_HSTACS_wave_res2 = populate_obs_wavelength_HSTx_wave_res2
populate_obs_wavelength_HSTNICMOS_wave_res2 = populate_obs_wavelength_HSTx_wave_res2
populate_obs_wavelength_HSTWFC3_wave_res2 = populate_obs_wavelength_HSTx_wave_res2
populate_obs_wavelength_HSTWFPC2_wave_res2 = populate_obs_wavelength_HSTx_wave_res2

def populate_obs_wavelength_HSTSTIS_wave_res1(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    wr1 = import_util.safe_column(index_row, 'MINIMUM_WAVELENGTH_RESOLUTION')

    return wr1

def populate_obs_wavelength_HSTSTIS_wave_res2(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    wr2 = import_util.safe_column(index_row, 'MAXIMUM_WAVELENGTH_RESOLUTION')

    return wr2

def populate_obs_wavelength_HSTx_wave_no1(**kwargs):
    metadata = kwargs['metadata']
    wavelength_row = metadata['obs_wavelength_row']
    wl2 = wavelength_row['wavelength2']
    if wl2 is None:
        return None
    return 10000 / wl2 # cm^-1

populate_obs_wavelength_HSTACS_wave_no1 = populate_obs_wavelength_HSTx_wave_no1
populate_obs_wavelength_HSTNICMOS_wave_no1 = populate_obs_wavelength_HSTx_wave_no1
populate_obs_wavelength_HSTSTIS_wave_no1 = populate_obs_wavelength_HSTx_wave_no1
populate_obs_wavelength_HSTWFC3_wave_no1 = populate_obs_wavelength_HSTx_wave_no1
populate_obs_wavelength_HSTWFPC2_wave_no1 = populate_obs_wavelength_HSTx_wave_no1

def populate_obs_wavelength_HSTx_wave_no2(**kwargs):
    metadata = kwargs['metadata']
    wavelength_row = metadata['obs_wavelength_row']
    wl1 = wavelength_row['wavelength1']
    if wl1 is None:
        return None
    return 10000 / wl1 # cm^-1

populate_obs_wavelength_HSTACS_wave_no2 = populate_obs_wavelength_HSTx_wave_no2
populate_obs_wavelength_HSTNICMOS_wave_no2 = populate_obs_wavelength_HSTx_wave_no2
populate_obs_wavelength_HSTSTIS_wave_no2 = populate_obs_wavelength_HSTx_wave_no2
populate_obs_wavelength_HSTWFC3_wave_no2 = populate_obs_wavelength_HSTx_wave_no2
populate_obs_wavelength_HSTWFPC2_wave_no2 = populate_obs_wavelength_HSTx_wave_no2

def populate_obs_wavelength_HSTx_wave_no_res1(**kwargs):
    metadata = kwargs['metadata']
    wl_row = metadata['obs_wavelength_row']
    wno1 = wl_row['wave_no1']
    wno2 = wl_row['wave_no2']
    if wno1 is None or wno2 is None:
        return None
    return wno2 - wno1

populate_obs_wavelength_HSTACS_wave_no_res1 = populate_obs_wavelength_HSTx_wave_no_res1
populate_obs_wavelength_HSTNICMOS_wave_no_res1 = populate_obs_wavelength_HSTx_wave_no_res1
populate_obs_wavelength_HSTWFC3_wave_no_res1 = populate_obs_wavelength_HSTx_wave_no_res1
populate_obs_wavelength_HSTWFPC2_wave_no_res1 = populate_obs_wavelength_HSTx_wave_no_res1

def populate_obs_wavelength_HSTx_wave_no_res2(**kwargs):
    metadata = kwargs['metadata']
    wl_row = metadata['obs_wavelength_row']
    wno1 = wl_row['wave_no1']
    wno2 = wl_row['wave_no2']
    if wno1 is None or wno2 is None:
        return None
    return wno2 - wno1

populate_obs_wavelength_HSTACS_wave_no_res2 = populate_obs_wavelength_HSTx_wave_no_res2
populate_obs_wavelength_HSTNICMOS_wave_no_res2 = populate_obs_wavelength_HSTx_wave_no_res2
populate_obs_wavelength_HSTWFC3_wave_no_res2 = populate_obs_wavelength_HSTx_wave_no_res2
populate_obs_wavelength_HSTWFPC2_wave_no_res2 = populate_obs_wavelength_HSTx_wave_no_res2

def populate_obs_wavelength_HSTSTIS_wave_no_res1(**kwargs):
    metadata = kwargs['metadata']
    wl_row = metadata['obs_wavelength_row']
    wave_res2 = wl_row['wave_res2']
    wl2 = wl_row['wavelength2']

    if wave_res2 is None or wl2 is None:
        return None

    return wave_res2 * 10000. / (wl2*wl2)

def populate_obs_wavelength_HSTSTIS_wave_no_res2(**kwargs):
    metadata = kwargs['metadata']
    wl_row = metadata['obs_wavelength_row']
    wave_res1 = wl_row['wave_res1']
    wl1 = wl_row['wavelength1']

    if wave_res1 is None or wl1 is None:
        return None

    return wave_res1 * 10000. / (wl1*wl1)

def populate_obs_wavelength_HSTx_spec_flag(**kwargs):
    return 'N'

populate_obs_wavelength_HSTACS_spec_flag = populate_obs_wavelength_HSTx_spec_flag
populate_obs_wavelength_HSTNICMOS_spec_flag = populate_obs_wavelength_HSTx_spec_flag
populate_obs_wavelength_HSTWFC3_spec_flag = populate_obs_wavelength_HSTx_spec_flag
populate_obs_wavelength_HSTWFPC2_spec_flag = populate_obs_wavelength_HSTx_spec_flag

def populate_obs_wavelength_HSTSTIS_spec_flag(**kwargs):
    return 'N' # XXX

def populate_obs_wavelength_HSTx_spec_size(**kwargs):
    return None

populate_obs_wavelength_HSTACS_spec_size = populate_obs_wavelength_HSTx_spec_size
populate_obs_wavelength_HSTNICMOS_spec_size = populate_obs_wavelength_HSTx_spec_size
populate_obs_wavelength_HSTWFC3_spec_size = populate_obs_wavelength_HSTx_spec_size
populate_obs_wavelength_HSTWFPC2_spec_size = populate_obs_wavelength_HSTx_spec_size

def populate_obs_wavelength_HSTSTIS_spec_size(**kwargs):
    return None

def populate_obs_wavelength_HSTACS_polarization_type(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    filter_name = index_row['FILTER_NAME']

    if filter_name.find('POL') == -1:
        return 'NONE'
    return 'LINEAR'

def populate_obs_wavelength_HSTNICMOS_polarization_type(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    filter_name = index_row['FILTER_NAME']

    if filter_name.find('POL') == -1:
        return 'NONE'
    return 'LINEAR'

def populate_obs_wavelength_HSTSTIS_polarization_type(**kwargs):
    return 'NONE'

def populate_obs_wavelength_HSTWFC3_polarization_type(**kwargs):
    return 'NONE'

def populate_obs_wavelength_HSTWFPC2_polarization_type(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    filter_name = index_row['FILTER_NAME']

    if filter_name.find('POL') == -1:
        return 'NONE'
    return 'LINEAR'


################################################################################
# THESE ARE SPECIFIC TO OBS_MISSION_HUBBLE
################################################################################

def populate_obs_mission_hubble_detector_id(**kwargs):
    metadata = kwargs['metadata']
    instrument = kwargs['instrument_name']
    index_row = metadata['index_row']
    detector_id = index_row['DETECTOR_ID']
    if detector_id == '':
        return None
    ret = instrument[3:] + '-' + detector_id
    return (ret, ret)

def populate_obs_mission_hubble_instrument_mode_id(**kwargs):
    metadata = kwargs['metadata']
    instrument = kwargs['instrument_name']
    index_row = metadata['index_row']
    instrument_mode_id = index_row['INSTRUMENT_MODE_ID']
    ret = instrument[3:] + '-' + instrument_mode_id
    return (ret, ret)

def populate_obs_mission_hubble_filter_name(**kwargs):
    metadata = kwargs['metadata']
    instrument = kwargs['instrument_name']
    index_row = metadata['index_row']
    filter_name = index_row['FILTER_NAME']
    filter_name = filter_name.replace('_', ' ')
    ret = instrument[3:] + '-' + filter_name
    return (ret, ret)

def populate_obs_mission_hubble_filter_width(**kwargs):
    metadata = kwargs['metadata']
    instrument = kwargs['instrument_name']
    index_row = metadata['index_row']
    filter_name = index_row['FILTER_NAME']
    return ('XXX', 'XXX')

def populate_obs_mission_hubble_aperture_type(**kwargs):
    metadata = kwargs['metadata']
    instrument = kwargs['instrument_name']
    index_row = metadata['index_row']
    aperture = index_row['APERTURE_TYPE']
    ret = instrument[3:] + '-' + aperture
    return (ret, ret)

def populate_obs_mission_hubble_HSTACS_targeted_detector_id(**kwargs):
    return None

def populate_obs_mission_hubble_HSTNICMOS_targeted_detector_id(**kwargs):
    return None

def populate_obs_mission_hubble_HSTSTIS_targeted_detector_id(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFC3_targeted_detector_id(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFPC2_targeted_detector_id(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    targeted_detector_id = index_row['TARGETED_DETECTOR_ID']
    if targeted_detector_id == '':
        return 'NONE'
    return targeted_detector_id

def populate_obs_mission_hubble_HSTACS_pc1_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTNICMOS_pc1_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTSTIS_pc1_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFC3_pc1_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFPC2_pc1_flag(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    pc1_flag = index_row['PC1_FLAG']
    return pc1_flag

def populate_obs_mission_hubble_HSTACS_wf2_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTNICMOS_wf2_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTSTIS_wf2_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFC3_wf2_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFPC2_wf2_flag(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    wf2_flag = index_row['WF2_FLAG']
    return wf2_flag

def populate_obs_mission_hubble_HSTACS_wf3_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTNICMOS_wf3_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTSTIS_wf3_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFC3_wf3_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFPC2_wf3_flag(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    wf3_flag = index_row['WF3_FLAG']
    return wf3_flag

def populate_obs_mission_hubble_HSTACS_wf4_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTNICMOS_wf4_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTSTIS_wf4_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFC3_wf4_flag(**kwargs):
    return None

def populate_obs_mission_hubble_HSTWFPC2_wf4_flag(**kwargs):
    metadata = kwargs['metadata']
    index_row = metadata['index_row']
    wf4_flag = index_row['WF4_FLAG']
    return wf4_flag
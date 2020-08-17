import re

NOISES = {'-', '.', ';', ':', ',', ' ', ''}

CLAIM_TOTAL_CONSTANTS = [r'[tflI][otali]{3,}[L]?[.;,:!\- ]+.{2,4}[.;,:!\- ]+[cg\(]([lhftakoimnre!v]{3,6}|im|la)[s]?']

MEMBER_ID_CONSTANTS = [r"[MNIE]{1,2}[ioe][mbeorn]{3,5}[\s.,:;\-]*[1IC][D0n][.;,:!\- ]*.{0,3}([.;,:!\- ]+|$)"]

MEMBER_NAME_CONSTANTS = [r"[MNIE]{1,2}[ioe][mbeorn]{3,5}[\s.,:;\-]*Nam[eo]([.;,:!\- ]+|$)",
                         r"[oe][mbeor][-.]Nam[eo]([.;,:!\- ]+|$)"]

DATE_LINES_CONSTANTS = [
    r"(\d{1,2}[.;:,\'_]?[/1][.;:,\'_]?\d{1,2}[.;:,\'_]?/[.;:,\'_]?\d{1,2}[-\s\.\:_\S]*\d{1,2}[.;:,\'_]?[/1][.;:,\'_]?\d{1,2}[.;:,\'_]?/[.;:,\'_]?\d{1,2}[.;:,\'_]?)",
    r"(\d{1,2}[.;:,\'_]?/[.;:,\'_]?\d{1,2}[.;:,\'_]?[/1][.;:,\'_]?\d{1,2}[-\s\.\:_\S]*\d{1,2}[.;:,\'_]?/[.;:,\'_]?\d{1,2}[.;:,\'_]?[/1][.;:,\'_]?\d{1,2}[.;:,\'_]?)"]

CLAIM_NAME_CONSTANTS = [r"[mcenum]{3}[i!lbpcer]{3,4}[\s:;,.\-]?[Nmw]{1}[aod]{1}[nmwec]{2,4}[s]?([.;,:!\- ]+|$)"]

CLAIM_INTEREST_CONSTANTS = [r"[i!lnarm]{2,3}[tfernc]{3}[es$tf:]{3,5}([.;,:!\- ]+|$)"]

ALAMEDA_CONSTANTS = [r'[A][LIAMEDOC]{5,7}']

PAY_CONSTANTS = [r'p[ayv]{1,2}[,.:\-\s]*']

VOID_AFTER = [r"^[vw][o0][i!lrnd0]{1,3}[.;,:\-\s]*A[ftl][tlfe0r]{2,3}"]

CHECK_ORDER_CONSTANTS = [r'o[rdieurlz]{3,5}[.;,:!\- ]*']

TO_THE_CONSTANTS = [r"[Tf][O0C][.;,:\-\s]*[TF]H[.]?E"]


def get_data(dict_data, data_string):
    result = {'claim_name': get_from_regex(CLAIM_NAME_CONSTANTS, data_string),
              'claim_interest': get_from_regex(CLAIM_INTEREST_CONSTANTS, data_string),
              'alameda': get_from_regex(ALAMEDA_CONSTANTS, data_string),
              'claim_total': get_from_regex(CLAIM_TOTAL_CONSTANTS, data_string),
              'member_id': get_from_regex(MEMBER_ID_CONSTANTS, data_string),
              'member_name': get_from_regex(MEMBER_NAME_CONSTANTS, data_string),
              'data_lines': get_from_regex(DATE_LINES_CONSTANTS, data_string),
              'pay': get_from_regex(PAY_CONSTANTS, data_string),
              'void_after': get_from_regex(VOID_AFTER, data_string),
              'check_order': get_from_regex(CHECK_ORDER_CONSTANTS, data_string),
              'to_the': get_from_regex(TO_THE_CONSTANTS, data_string)}

    return result


def get_from_regex(regex_arr, data_string):
    result = []
    for pattern in regex_arr:
        res = re.findall(pattern, data_string)
        res = [i.strip() for i in res]

        result += res

    result = filter(lambda i: i not in NOISES, result)
    return list(result)

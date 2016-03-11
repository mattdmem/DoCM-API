from RestExecuter import WS

__author__ = 'mparker'

class Variants(WS):
    """
    This class contains methods for variants
    """

    def variant_detail(self,hgvs):
        """
        gets detail on a single variant

        e.g ENST00000078429:c.626A>C

        :param hgvs: hgvs of the variant of interest
        :return: result of the query
        """
        return self.general_method("variants", "json", hgvs)

    def variant_list(self,format,**options):
        """
        gets a list of variants

        :param format: format of output; tsv,csv,json
        :param options:
        :return: result of the query
        """
        options_string = "&".join([option_name + "=" + str(options[option_name]) for option_name in options])
        return self.general_method("list", format, options_string)
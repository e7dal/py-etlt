"""
ETLT

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
import abc

from etlt.writer.Writer import Writer


class SqlLoaderWriter(Writer):
    """
    Abstract parent class for writing rows to a destination.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def get_bulk_load_sql(self):
        """
        Returns a SQL statement for bulk loading the data into the database.

        :rtype: str
        """
        raise NotImplementedError()

# ----------------------------------------------------------------------------------------------------------------------
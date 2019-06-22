# coding: utf-8

"""
    PyBloods

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class NewSample(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'source_id': 'int',
        'taken_at': 'datetime'
    }

    attribute_map = {
        'source_id': 'source_id',
        'taken_at': 'taken_at'
    }

    def __init__(self, source_id=None, taken_at=None):  # noqa: E501
        """NewSample - a model defined in OpenAPI"""  # noqa: E501

        self._source_id = None
        self._taken_at = None
        self.discriminator = None

        self.source_id = source_id
        self.taken_at = taken_at

    @property
    def source_id(self):
        """Gets the source_id of this NewSample.  # noqa: E501


        :return: The source_id of this NewSample.  # noqa: E501
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this NewSample.


        :param source_id: The source_id of this NewSample.  # noqa: E501
        :type: int
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def taken_at(self):
        """Gets the taken_at of this NewSample.  # noqa: E501


        :return: The taken_at of this NewSample.  # noqa: E501
        :rtype: datetime
        """
        return self._taken_at

    @taken_at.setter
    def taken_at(self, taken_at):
        """Sets the taken_at of this NewSample.


        :param taken_at: The taken_at of this NewSample.  # noqa: E501
        :type: datetime
        """
        if taken_at is None:
            raise ValueError("Invalid value for `taken_at`, must not be `None`")  # noqa: E501

        self._taken_at = taken_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

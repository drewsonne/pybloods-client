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


class Source(object):
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
        'lab_id': 'int',
        'provider_id': 'int',
        'source_id': 'int'
    }

    attribute_map = {
        'lab_id': 'lab_id',
        'provider_id': 'provider_id',
        'source_id': 'source_id'
    }

    def __init__(self, lab_id=None, provider_id=None, source_id=None):  # noqa: E501
        """Source - a model defined in OpenAPI"""  # noqa: E501

        self._lab_id = None
        self._provider_id = None
        self._source_id = None
        self.discriminator = None

        self.lab_id = lab_id
        self.provider_id = provider_id
        self.source_id = source_id

    @property
    def lab_id(self):
        """Gets the lab_id of this Source.  # noqa: E501


        :return: The lab_id of this Source.  # noqa: E501
        :rtype: int
        """
        return self._lab_id

    @lab_id.setter
    def lab_id(self, lab_id):
        """Sets the lab_id of this Source.


        :param lab_id: The lab_id of this Source.  # noqa: E501
        :type: int
        """
        if lab_id is None:
            raise ValueError("Invalid value for `lab_id`, must not be `None`")  # noqa: E501

        self._lab_id = lab_id

    @property
    def provider_id(self):
        """Gets the provider_id of this Source.  # noqa: E501


        :return: The provider_id of this Source.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this Source.


        :param provider_id: The provider_id of this Source.  # noqa: E501
        :type: int
        """
        if provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def source_id(self):
        """Gets the source_id of this Source.  # noqa: E501


        :return: The source_id of this Source.  # noqa: E501
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this Source.


        :param source_id: The source_id of this Source.  # noqa: E501
        :type: int
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

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
        if not isinstance(other, Source):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

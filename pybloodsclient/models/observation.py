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


class Observation(object):
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
        'extracted_at': 'datetime',
        'processed_at': 'datetime',
        'unit_id': 'int',
        'value': 'float',
        'observation_id': 'int'
    }

    attribute_map = {
        'extracted_at': 'extracted_at',
        'processed_at': 'processed_at',
        'unit_id': 'unit_id',
        'value': 'value',
        'observation_id': 'observation_id'
    }

    def __init__(self, extracted_at=None, processed_at=None, unit_id=None, value=None, observation_id=None):  # noqa: E501
        """Observation - a model defined in OpenAPI"""  # noqa: E501

        self._extracted_at = None
        self._processed_at = None
        self._unit_id = None
        self._value = None
        self._observation_id = None
        self.discriminator = None

        self.extracted_at = extracted_at
        if processed_at is not None:
            self.processed_at = processed_at
        self.unit_id = unit_id
        self.value = value
        self.observation_id = observation_id

    @property
    def extracted_at(self):
        """Gets the extracted_at of this Observation.  # noqa: E501


        :return: The extracted_at of this Observation.  # noqa: E501
        :rtype: datetime
        """
        return self._extracted_at

    @extracted_at.setter
    def extracted_at(self, extracted_at):
        """Sets the extracted_at of this Observation.


        :param extracted_at: The extracted_at of this Observation.  # noqa: E501
        :type: datetime
        """
        if extracted_at is None:
            raise ValueError("Invalid value for `extracted_at`, must not be `None`")  # noqa: E501

        self._extracted_at = extracted_at

    @property
    def processed_at(self):
        """Gets the processed_at of this Observation.  # noqa: E501


        :return: The processed_at of this Observation.  # noqa: E501
        :rtype: datetime
        """
        return self._processed_at

    @processed_at.setter
    def processed_at(self, processed_at):
        """Sets the processed_at of this Observation.


        :param processed_at: The processed_at of this Observation.  # noqa: E501
        :type: datetime
        """

        self._processed_at = processed_at

    @property
    def unit_id(self):
        """Gets the unit_id of this Observation.  # noqa: E501


        :return: The unit_id of this Observation.  # noqa: E501
        :rtype: int
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this Observation.


        :param unit_id: The unit_id of this Observation.  # noqa: E501
        :type: int
        """
        if unit_id is None:
            raise ValueError("Invalid value for `unit_id`, must not be `None`")  # noqa: E501

        self._unit_id = unit_id

    @property
    def value(self):
        """Gets the value of this Observation.  # noqa: E501


        :return: The value of this Observation.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Observation.


        :param value: The value of this Observation.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def observation_id(self):
        """Gets the observation_id of this Observation.  # noqa: E501


        :return: The observation_id of this Observation.  # noqa: E501
        :rtype: int
        """
        return self._observation_id

    @observation_id.setter
    def observation_id(self, observation_id):
        """Sets the observation_id of this Observation.


        :param observation_id: The observation_id of this Observation.  # noqa: E501
        :type: int
        """
        if observation_id is None:
            raise ValueError("Invalid value for `observation_id`, must not be `None`")  # noqa: E501

        self._observation_id = observation_id

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
        if not isinstance(other, Observation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

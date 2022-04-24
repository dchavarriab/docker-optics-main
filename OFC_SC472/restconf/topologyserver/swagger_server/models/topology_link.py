# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TopologyLink(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, target_port: str=None, source_port: str=None, target_node: str=None, link_id: str=None, source_node: str=None):  # noqa: E501
        """TopologyLink - a model defined in Swagger

        :param target_port: The target_port of this TopologyLink.  # noqa: E501
        :type target_port: str
        :param source_port: The source_port of this TopologyLink.  # noqa: E501
        :type source_port: str
        :param target_node: The target_node of this TopologyLink.  # noqa: E501
        :type target_node: str
        :param link_id: The link_id of this TopologyLink.  # noqa: E501
        :type link_id: str
        :param source_node: The source_node of this TopologyLink.  # noqa: E501
        :type source_node: str
        """
        self.swagger_types = {
            'target_port': str,
            'source_port': str,
            'target_node': str,
            'link_id': str,
            'source_node': str
        }

        self.attribute_map = {
            'target_port': 'target-port',
            'source_port': 'source-port',
            'target_node': 'target-node',
            'link_id': 'link-id',
            'source_node': 'source-node'
        }
        self._target_port = target_port
        self._source_port = source_port
        self._target_node = target_node
        self._link_id = link_id
        self._source_node = source_node

    @classmethod
    def from_dict(cls, dikt) -> 'TopologyLink':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The topology.Link of this TopologyLink.  # noqa: E501
        :rtype: TopologyLink
        """
        return util.deserialize_model(dikt, cls)

    @property
    def target_port(self) -> str:
        """Gets the target_port of this TopologyLink.


        :return: The target_port of this TopologyLink.
        :rtype: str
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port: str):
        """Sets the target_port of this TopologyLink.


        :param target_port: The target_port of this TopologyLink.
        :type target_port: str
        """

        self._target_port = target_port

    @property
    def source_port(self) -> str:
        """Gets the source_port of this TopologyLink.


        :return: The source_port of this TopologyLink.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port: str):
        """Sets the source_port of this TopologyLink.


        :param source_port: The source_port of this TopologyLink.
        :type source_port: str
        """

        self._source_port = source_port

    @property
    def target_node(self) -> str:
        """Gets the target_node of this TopologyLink.


        :return: The target_node of this TopologyLink.
        :rtype: str
        """
        return self._target_node

    @target_node.setter
    def target_node(self, target_node: str):
        """Sets the target_node of this TopologyLink.


        :param target_node: The target_node of this TopologyLink.
        :type target_node: str
        """

        self._target_node = target_node

    @property
    def link_id(self) -> str:
        """Gets the link_id of this TopologyLink.


        :return: The link_id of this TopologyLink.
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id: str):
        """Sets the link_id of this TopologyLink.


        :param link_id: The link_id of this TopologyLink.
        :type link_id: str
        """

        self._link_id = link_id

    @property
    def source_node(self) -> str:
        """Gets the source_node of this TopologyLink.


        :return: The source_node of this TopologyLink.
        :rtype: str
        """
        return self._source_node

    @source_node.setter
    def source_node(self, source_node: str):
        """Sets the source_node of this TopologyLink.


        :param source_node: The source_node of this TopologyLink.
        :type source_node: str
        """

        self._source_node = source_node